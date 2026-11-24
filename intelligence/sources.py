"""User-curated reference registry. Saving never starts network collection."""
import json
import urllib.parse
import uuid
from .core import Invalid, REPO, text

KINDS = ['Creator / channel', 'Show / series', 'Episode / scene', 'Creative reference', 'Trend / topic']

def initialize(store):
    store.db.execute('CREATE TABLE IF NOT EXISTS sources(id TEXT PRIMARY KEY,url TEXT UNIQUE NOT NULL,payload TEXT NOT NULL)')
    if not store.db.execute("SELECT 1 FROM meta WHERE key='source_seeds_v1'").fetchone():
        seed=json.loads((REPO/'docs/production-engine/agent_watchlist.json').read_text())
        for row in seed['creator_watchlist']+seed['additional_references']:
            save(store,{'name':row['reference'],'url':row['url'],'kind':'Creator / channel' if 'creator' in row else 'Episode / scene',
                'feed_id':'F02' if 'youtube.com' in row['url'] else 'F03','notes':'Amy / user-supplied reference. Audience fit and performance are not independently verified.', 'active':True},seed=True)
        with store.db:store.db.execute("INSERT OR IGNORE INTO meta VALUES ('source_seeds_v1','1')")
    if not store.db.execute("SELECT 1 FROM meta WHERE key='source_seeds_v2'").fetchone():
        for name,url,notes in [('TikTok Creative Center','https://ads.tiktok.com/business/creativecenter/','Validate cultural signals found by the TikTok feed.'),('Google Trends','https://trends.google.com/trends/','Corroborate named terms discovered in any feed; not an independent popularity ranking.')]:
            save(store,{'name':name,'url':url,'kind':'Creative reference','role':'Supporting research','feed_id':'F03','notes':notes,'active':True},seed=True)
        panel=json.loads((REPO/'docs/production-engine/authority_panel.json').read_text())['panel']
        for person in panel:
            sid='panel-'+person['candidate_name'].casefold().replace(' ','-')
            if store.db.execute('SELECT 1 FROM sources WHERE id=?',(sid,)).fetchone():continue
            save(store,{'name':person['candidate_name'],'url':'','kind':'Creator / channel','role':'Authority panel','feed_id':'F07','notes':person['proposed_specialty']+'. Proposed review: '+person['cadence']+'. Official account and audience fit require verification.','active':True},seed=True,seed_id=sid)
        with store.db:store.db.execute("INSERT OR IGNORE INTO meta VALUES ('source_seeds_v2','1')")

def save(store,value,seed=False,seed_id=None):
    url=text(value.get('url',''),'Source URL',2000,optional=True)
    try: parsed=urllib.parse.urlsplit(url)
    except ValueError:raise Invalid('Enter a valid public https:// source link.')
    if url and (parsed.scheme!='https' or not parsed.hostname or parsed.username or parsed.password or parsed.hostname in ['localhost','127.0.0.1','::1']):
        raise Invalid('Enter a public https:// link without credentials.')
    url=urllib.parse.urlunsplit(('https',parsed.netloc.lower(),parsed.path.rstrip('/'),parsed.query,'')) if url else ''
    kind=value.get('kind');feed=value.get('feed_id')
    from .feeds import listing as feed_list
    chosen=next((f for f in feed_list(store) if f['id']==feed),None)
    if kind not in KINDS or chosen is None:raise Invalid('Choose a source type and feed.')
    sid=value.get('id');existing=None
    if sid:
        existing=store.db.execute('SELECT * FROM sources WHERE id=?',(sid,)).fetchone()
        if not existing:raise Invalid('Source not found.')
    if not chosen['active'] and (not existing or json.loads(existing['payload'])['feed_id']!=feed):
        raise Invalid('Choose an active feed for a new assignment.')
    role=value.get('role','Creative reference')
    if role not in ['Discovery','Creative reference','Authority panel','Supporting research']:raise Invalid('Choose a valid research role.')
    url_key=url or 'unlinked:'+(sid or seed_id or uuid.uuid4().hex)
    duplicate=store.db.execute('SELECT id FROM sources WHERE url=?',(url_key,)).fetchone()
    if duplicate and duplicate[0]!=sid:
        if seed:return duplicate[0]
        raise Invalid('This link is already saved. Edit the existing source instead.')
    body={'name':text(value.get('name'),'Name',200),'url':url,'kind':kind,'feed_id':feed,
        'role':role,'notes':text(value.get('notes',''),'Notes',2000,optional=True),'active':value.get('active',True) is True,
        'created_at':json.loads(existing['payload'])['created_at'] if existing else store.clock(),
        'updated_at':store.clock(),'origin':json.loads(existing['payload'])['origin'] if existing else 'Amy / supplied references' if seed else 'Added in admin',
        'status':'SAVED' if url else 'NEEDS_LINK','monitoring':False}
    sid=sid or seed_id or uuid.uuid4().hex
    with store.db:store.db.execute('INSERT INTO sources VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET url=excluded.url,payload=excluded.payload',(sid,url_key,json.dumps(body)))
    return sid

def listing(store):
    initialize(store)
    return [dict(id=r['id'],**json.loads(r['payload'])) for r in store.db.execute('SELECT * FROM sources ORDER BY rowid')]
