"""Bounded, explicit Firecrawl previews. No crawling, model calls or schedules."""
import datetime as dt
import hashlib
import json
import os
import urllib.error
import urllib.parse
import urllib.request
import uuid
from .core import Invalid, lock, parse_time
from .sources import listing

# Pilot adapters: exact public hosts only, never private analytics/account URLs.
HOSTS = {'a24films.com', 'mydramalist.com', 'webtoons.com', 'reelshort.com', 'dramabox.com'}
MAX_PAGES = 3
DAILY_PAGES = 10

def initialize(store):
    store.db.execute('CREATE TABLE IF NOT EXISTS collection_previews(id TEXT PRIMARY KEY,created_at TEXT NOT NULL,payload TEXT NOT NULL)')
    boundary=(parse_time(store.clock())-dt.timedelta(days=1)).isoformat().replace('+00:00','Z')
    with store.db:store.db.execute('DELETE FROM collection_previews WHERE created_at<?',(boundary,))

def credential(store):
    value=os.environ.get('FIRECRAWL_API_KEY','').strip()
    path=store.dir/'firecrawl-key'
    return value or (path.read_text().strip() if path.exists() else '')

def save_credential(store,key):
    if not isinstance(key,str) or not key.strip() or len(key)>500 or any(c.isspace() for c in key):
        raise Invalid('Enter a valid Firecrawl key without whitespace.')
    if os.environ.get('FIRECRAWL_API_KEY','').strip():
        raise Invalid('An environment key is active. Update or remove FIRECRAWL_API_KEY and restart the desk before saving a replacement here.')
    path=store.dir/'firecrawl-key'
    fd=os.open(str(path),os.O_WRONLY|os.O_CREAT|os.O_TRUNC,0o600)
    os.fchmod(fd,0o600)
    with os.fdopen(fd,'w') as f:f.write(key)
    return {'configured':True,'verified':False}


def eligibility(source, feeds):
    f=next((f for f in feeds if f['id']==source['feed_id']),None)
    if not source.get('active') or not f or not f.get('active'):return 'Source or feed is archived.'
    if f['kind']=='internal':return 'First-party analytics requires an owned-data connection.'
    try:
        u=urllib.parse.urlsplit(source.get('url',''));host=(u.hostname or '').removeprefix('www.')
        if u.scheme!='https' or u.username or u.password or u.port not in (None,443):return 'A public HTTPS source link is required.'
        if host not in HOSTS:return 'This platform needs a separate connector; website pilot does not support it yet.'
        if u.query or any(x in u.path.lower().split('/') for x in ('login','account','signin','settings','checkout')):return 'Choose a public content page without query parameters or account paths.'
    except ValueError:return 'Source link is invalid.'
    return ''

def readiness(store):
    from .feeds import listing as feeds
    fs=feeds(store)
    return {'connected':bool(credential(store)), 'max_pages':MAX_PAGES,'daily_pages':DAILY_PAGES,
        'sources':{s['id']:eligibility(s,fs) for s in listing(store)}}

def fetch_page(url, key):
    body=json.dumps({'url':url,'formats':['markdown'],'onlyMainContent':True,'timeout':30000}).encode()
    req=urllib.request.Request('https://api.firecrawl.dev/v2/scrape',data=body,
        headers={'Authorization':'Bearer '+key,'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(req,timeout=40) as response:raw=response.read(2_000_001)
        if len(raw)>2_000_000:raise Invalid('Response exceeded the pilot size limit.')
        result=json.loads(raw)
    except urllib.error.HTTPError as exc:
        raise Invalid('Firecrawl returned HTTP %s. Check access, credits or service status.'%exc.code) from None
    except (urllib.error.URLError,OSError,ValueError):
        raise Invalid('Firecrawl could not return a usable response. No automatic retry was made.') from None
    if not isinstance(result,dict) or result.get('success') is not True or not isinstance(result.get('data'),dict):
        raise Invalid('Firecrawl did not return a successful page capture.')
    return result['data']

def history(store):
    initialize(store)
    return [dict(id=r['id'],created_at=r['created_at'],**json.loads(r['payload'])) for r in store.db.execute('SELECT * FROM collection_previews ORDER BY created_at DESC,rowid DESC LIMIT 10')]

def run(store, ids, transport=None):
    from .feeds import listing as feeds
    initialize(store)
    if not isinstance(ids,list) or not 1<=len(ids)<=MAX_PAGES or any(not isinstance(i,str) for i in ids) or len(set(ids))!=len(ids):
        raise Invalid('Choose one to three distinct saved sources.')
    all_sources={s['id']:s for s in listing(store)};fs=feeds(store);chosen=[]
    for sid in ids:
        if sid not in all_sources:raise Invalid('Source no longer exists. Refresh the desk.')
        s=all_sources[sid];reason=eligibility(s,fs)
        if reason:raise Invalid(s['name']+': '+reason)
        chosen.append(s)
    if len({s['url'].rstrip('/') for s in chosen})!=len(chosen):raise Invalid('Choose distinct URLs for this batch.')
    key=credential(store)
    if not key:raise Invalid('Connect Firecrawl first. No pages were requested. Open Connections for private setup instructions.')
    with lock(store.dir/'worker.lock'):
        store.recover_runs();rid=store.start_run('live');results=[];errors=[];requested=0
        try:
            for s in chosen:
                entry={'source_id':s['id'],'name':s['name'],'url':s['url'],'feed_id':s['feed_id'],'saved_candidate_id':None}
                try:
                    store.consume('firecrawl_pages',DAILY_PAGES)
                    requested+=1
                    data=(transport or fetch_page)(s['url'],key)
                    meta=data.get('metadata') or {}
                    if not isinstance(meta,dict):raise Invalid('Page metadata could not be read.')
                    code=meta.get('statusCode',200)
                    if not isinstance(code,int) or code>=400:raise Invalid('The source returned an error page.')
                    body=data.get('markdown')
                    if not isinstance(body,str) or len(body.strip())<80:raise Invalid('Too little readable text was returned. Inspect the source manually.')
                    final=meta.get('url') or meta.get('sourceURL') or s['url']
                    probe=dict(s,url=final)
                    if eligibility(probe,fs):raise Invalid('Capture redirected outside the supported public-page scope.')
                    entry.update(status='CAPTURED',title=str(meta.get('title') or s['name'])[:1000],
                        text=body[:20000],truncated=len(body)>20000,observed_at=store.clock(),final_url=final,
                        warning='Page text only; inspect for consent walls or incomplete content. No video, audience or story-performance analysis.')
                except Invalid as exc:
                    entry.update(status='FAILED',error=str(exc));errors.append(s['name']+': '+str(exc))
                results.append(entry)
            captured=sum(r['status']=='CAPTURED' for r in results)
            status='COMPLETED' if captured==len(chosen) else 'PARTIAL' if captured else 'FAILED'
            payload={'run_id':rid,'status':status,'results':results,'requested':requested}
            pid=uuid.uuid4().hex
            with store.db:store.db.execute('INSERT INTO collection_previews VALUES (?,?,?)',(pid,store.clock(),json.dumps(payload)))
            store.finish_run(rid,status,{'website_pages_requested':requested,'captured_for_preview':captured,'saved_to_inbox':0},errors)
            return dict(id=pid,**payload)
        except Exception:
            store.finish_run(rid,'FAILED',{},['Preview interrupted. No automatic retry.']);raise

def save_preview(store,pid,ids):
    initialize(store)
    if not isinstance(ids,list) or not ids or any(not isinstance(i,str) for i in ids) or len(set(ids))!=len(ids):raise Invalid('Choose captured pages to save.')
    with lock(store.dir/'worker.lock'):
        row=store.db.execute('SELECT payload FROM collection_previews WHERE id=?',(pid,)).fetchone()
        if not row:raise Invalid('Preview expired or was not found. Run another test.')
        p=json.loads(row[0]);valid={x['source_id']:x for x in p['results'] if x['status']=='CAPTURED'}
        if any(i not in valid for i in ids):raise Invalid('Only successfully captured pages can be saved.')
        cids=[]
        for sid in ids:
            x=valid[sid]
            # Stable feed+URL identity: repeated saves/collections update one candidate.
            source_id='web:'+hashlib.sha256((x['feed_id']+'|'+x['url'].rstrip('/')).encode()).hexdigest()
            cid=store.ingest('live',{'source_id':source_id,'feed_ids':[x['feed_id']],'title':x['title'],
                'url':x['url'],'channel_name':x['name'],'channel_id':'','published_at':None,'observed_at':x['observed_at'],
                'metrics':{'views':None,'likes':None,'comments':None},'origin':'firecrawl',
                'inspection':'Captured webpage text only; not a viewing audit','series_status':'No series or audience claims verified.',
                'captured_text':x['text'],'truncated':x['truncated'],'registry_source_id':sid,'final_url':x['final_url']})
            x['saved_candidate_id']=cid;cids.append(cid)
        with store.db:
            store.db.execute('UPDATE collection_previews SET payload=? WHERE id=?',(json.dumps(p),pid))
            counts={'website_pages_requested':p['requested'],'captured_for_preview':len(valid),'saved_to_inbox':sum(bool(x.get('saved_candidate_id')) for x in p['results'])}
            store.db.execute('UPDATE runs SET counts=? WHERE id=?',(json.dumps(counts),p['run_id']))
        return {'candidate_ids':cids}
