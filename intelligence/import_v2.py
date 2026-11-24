"""Transactional, repeatable import of supplied research specifications.
Raw attachments and reports stay in private runtime storage, never the repository.
"""
import hashlib
import json
import re
import sqlite3
import unicodedata
import urllib.parse
import uuid
from pathlib import Path
from .core import Invalid, text
from . import feeds, sources, frameworks

FEED_MAP={'feed_name':'name','what_should_this_feed_discover':'universe','what_should_it_include_or_exclude':'relevance_filter','desired_review_frequency':'cadence_proposed','starting_links':'entry_points','discovery_searches_hashtags':'seed_queries','communities_to_review':'candidate_community_allowlist'}

from .registry_utils import norm, canonical

def framework_text(content):
    # Keep explicit framework/lens passages; never promote a live signal to a lens.
    matches=re.findall(r'(?:\*\*Framework[^*]*\*\*|\*\*Persistent lens:\*\*|Framework contribution:)(.*?)(?=\*\*(?:Live pull|Why/use)|Live pull:|$)',content,re.S)
    return '\n\n'.join(dict.fromkeys(m.strip() for m in matches if m.strip()))

def prepare(store):
    feeds.initialize(store);sources.initialize(store);frameworks.initialize(store)

def apply_document(store,document,digest):
    old=store.db.execute('SELECT report FROM registry_imports WHERE digest=?',(digest,)).fetchone()
    if old:return dict(json.loads(old[0]),already_applied=True)
    if document.get('import_mode')!='upsert_preserve_existing':raise Invalid('Expected an upsert-preserve-existing specification.')
    if not isinstance(document.get('feeds'),list) or not isinstance(document.get('sources'),list):raise Invalid('Missing feed or source records.')
    report={'digest':digest,'feeds_updated':0,'feeds_added':0,'sources_updated':0,'sources_added':0,'framework_drafts':0,'issues':[],
        'mappings':['External research → external','F10 Internal analytics → preserve existing internal kind','Reference → Creative reference for new records; preserve type of matched sources','Lobby → The Lobby; Crossover → The Crossover (existing cohort labels)'],
        'monitoring_activated':False,'already_applied':False}
    seen=set()
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        for raw in document['feeds']:
            fid=raw.get('feed_id')
            if not isinstance(fid,str) or not re.fullmatch(r'F\d{2,}',fid) or fid in seen:raise Invalid('Invalid or duplicate feed ID.')
            seen.add(fid)
            row=store.db.execute('SELECT payload FROM feed_definitions WHERE id=?',(fid,)).fetchone()
            old=json.loads(row[0]) if row else None
            if fid=='F11' and old and norm(old['name'])!=norm(raw['feed_name']):raise Invalid('F11 is already assigned to a different feed. Resolve this conflict before importing.')
            kind={'External research':'external','Internal analytics':'internal'}.get(raw.get('kind'))
            if kind is None:raise Invalid('Unresolved feed kind: '+str(raw.get('kind')))
            if raw.get('priority') not in ['P0','P1','P2']:raise Invalid('Invalid priority.')
            record=dict(old or {'id':fid,'active':True,'version':0,'activation_state':'NOT_CONNECTED','access_validation':'REQUIRED','last_run_at':None})
            for source,target in FEED_MAP.items():
                value=raw.get(source)
                record[target]=feeds.lines(value,source,source=='starting_links') if isinstance(value,list) else text(value,source,30000 if target=='universe' else 2000)
            record.update(kind=old['kind'] if fid=='F10' and old else kind,priority=raw['priority'],version=record['version']+1,updated_at=store.clock(),import_digest=digest,
                intelligence_class='first_party_performance' if fid=='F10' else 'live_cultural',imported_kind=raw['kind'],connector_requirement='Authorized connector and account/source verification required; saving does not connect.',
                query_templates=[q for q in record['seed_queries'] if re.search(r'\{[^}]+\}',q)])
            issues=['Connector access and permissions require validation.']
            if record['query_templates']:issues.append('Braced searches are templates; no resolver is configured and they must not run literally.')
            if fid in ['F02','F04','F07']:issues.append('Requested YouTube-derived metrics remain disabled under the current standard API implementation.')
            if fid=='F10':issues.append('Exact owned accounts and internal endpoints remain unresolved. Public discovery fields intentionally empty.')
            if fid=='F11':issues.append('A24 catalog routes and property roles require verification; no live ranking connector configured.')
            record['import_issues']=issues
            frameworks.archive_record(store,'feed',fid,old)
            store.db.execute('INSERT INTO feed_definitions VALUES (?,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload',(fid,json.dumps(record)))
            report['feeds_updated' if old else 'feeds_added']+=1
            content=framework_text(record['universe'])
            if content:
                frameworks.propose(store,fid,content,'Supplied V2 research specification '+digest+'. Proposed editorial framework; supporting research and approval required.')
                report['framework_drafts']+=1
            else:report['issues'].append({'entity':fid,'issue':'No explicit framework section extracted; manual review required.'})
            report['issues'].extend({'entity':fid,'issue':issue} for issue in issues)
        for raw in document['sources']:
            fid=text(raw.get('feed'),'Feed reference',300).split()[0]
            if not store.db.execute('SELECT 1 FROM feed_definitions WHERE id=?',(fid,)).fetchone():raise Invalid('Unresolved source feed '+fid)
            name=text(raw.get('name'),'Source name',200);supplied_url=raw.get('source_link') or '';canonical(supplied_url)
            objective=text(raw.get('learning_objective'),'Learning objective',30000)
            if type(raw.get('active')) is not bool or type(raw.get('verification_required')) is not bool:raise Invalid('Invalid source flags.')
            mapped_type={'Reference':'Creative reference','Creator / channel':'Creator / channel'}.get(raw.get('source_type'))
            if not mapped_type:raise Invalid('Unresolved source type '+str(raw.get('source_type')))
            candidates=[dict(id=r['id'],**json.loads(r['payload'])) for r in store.db.execute('SELECT * FROM sources')]
            candidates=[s for s in candidates if s['feed_id']==fid and (norm(s['name'])==norm(name) or supplied_url and canonical(s.get('url'))==canonical(supplied_url) or supplied_url and canonical(s.get('supplied_url'))==canonical(supplied_url))]
            if len(candidates)>1:
                report['issues'].append({'entity':name,'issue':'Ambiguous name/URL match; source left unchanged for manual resolution.'});continue
            old=candidates[0] if candidates else None
            sid=old['id'] if old else uuid.uuid4().hex
            record=dict(old or {'created_at':store.clock(),'origin':'Supplied V2 research specification','monitoring':False})
            issues=[]
            url=supplied_url
            if old and old.get('url') and canonical(old['url'])!=canonical(supplied_url):
                url=old['url'];issues.append('Existing URL retained; differing supplied URL saved separately for review.')
            if old and old.get('active') is False and raw['active']:issues.append('Existing explicit archive preserved.')
            verified=bool(old and (old.get('verified_at') or old.get('verification_status')=='VERIFIED'))
            search_link=bool(url and urllib.parse.urlsplit(url).path=='/results')
            if search_link:issues.append('Discovery search URL only; resolve an official account before collection.')
            if not url:issues.append('Exact internal endpoint / account is not supplied.')
            if fid=='F10':issues.append('Authorized owned-account connector required; a generic Studio URL is not an account connection.')
            if fid=='F11':issues.append('Catalog routes / source access have not been independently verified.')
            record.update(name=name,url=url,kind=old['kind'] if old else mapped_type,feed_id=fid,notes=objective,
                active=False if old and old.get('active') is False else raw['active'],
                role=old.get('role','Creative reference') if old else 'Authority panel' if fid=='F07' else 'Supporting research' if 'corroboration' in name or name=='Google Trends' else 'Discovery',
                status='SAVED' if url else 'NEEDS_LINK',updated_at=store.clock(),import_digest=digest,
                supplied_url=supplied_url,imported_source_type=raw['source_type'],verification_required=raw['verification_required'] if not verified else False,
                verification_status='VERIFIED' if verified else 'UNVERIFIED',link_kind='DISCOVERY_SEARCH' if search_link else 'REFERENCE' if url else 'UNRESOLVED',
                import_issues=issues,connector_requirement='Not connected by this import; access and account configuration required.')
            frameworks.archive_record(store,'source',sid,old)
            key=fid+'|'+canonical(url) if url else 'unlinked:'+sid
            store.db.execute('INSERT INTO sources VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET url=excluded.url,payload=excluded.payload',(sid,key,json.dumps({k:v for k,v in record.items() if k!='id'})))
            report['sources_updated' if old else 'sources_added']+=1
            report['issues'].extend({'entity':name,'issue':issue} for issue in issues)
        report['total_feeds']=store.db.execute('SELECT count(*) FROM feed_definitions').fetchone()[0]
        report['total_sources']=store.db.execute('SELECT count(*) FROM sources').fetchone()[0]
        store.db.execute('INSERT INTO registry_imports VALUES (?,?,?)',(digest,store.clock(),json.dumps(report)))
    return report

def run(store,path,apply=False):
    raw=Path(path).read_bytes();document=json.loads(raw);digest=hashlib.sha256(raw).hexdigest()
    prepare(store)
    if not apply:
        # Clone the initialized registry and all history; validate without changing records.
        clone=sqlite3.connect(':memory:');clone.row_factory=sqlite3.Row;store.db.backup(clone)
        class Preview:pass
        preview=Preview();preview.db=clone;preview.clock=store.clock
        try:return dict(apply_document(preview,document,digest),mode='PREVIEW')
        finally:clone.close()
    if not store.db.execute('SELECT 1 FROM registry_imports WHERE digest=?',(digest,)).fetchone():
        target=store.dir/('before-v2-'+digest[:12]+'.sqlite3')
        if not target.exists():
            backup=sqlite3.connect(str(target));store.db.backup(backup);backup.close();target.chmod(0o600)
    result=apply_document(store,document,digest)
    report=store.dir/('import-v2-'+digest[:12]+'.json');report.write_text(json.dumps(result,indent=2));report.chmod(0o600)
    return dict(result,mode='APPLIED',report_path=str(report))
