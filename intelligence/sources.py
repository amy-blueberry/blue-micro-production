"""User-curated reference registry. Saving never starts network collection."""
import json
import urllib.parse
import uuid
from .core import Invalid, REPO, text

KINDS = ['Creator / channel', 'Show / series', 'Episode / scene', 'Creative reference', 'Trend / topic']

def initialize(store):
    store.db.execute('CREATE TABLE IF NOT EXISTS sources(id TEXT PRIMARY KEY,url TEXT UNIQUE NOT NULL,payload TEXT NOT NULL)')
    if store.db.execute("SELECT 1 FROM meta WHERE key='source_seeds_v1'").fetchone():return
    seed=json.loads((REPO/'docs/production-engine/agent_watchlist.json').read_text())
    with store.db:
        for row in seed['creator_watchlist']+seed['additional_references']:
            save(store,{'name':row['reference'],'url':row['url'],'kind':'Creator / channel' if 'creator' in row else 'Episode / scene',
                'feed_id':'F02' if 'youtube.com' in row['url'] else 'F03','notes':'Amy / user-supplied reference. Audience fit and performance are not independently verified.', 'active':True},seed=True)
        store.db.execute("INSERT INTO meta VALUES ('source_seeds_v1','1')")

def save(store,value,seed=False):
    url=text(value.get('url'),'Source URL',2000)
    try: parsed=urllib.parse.urlsplit(url)
    except ValueError:raise Invalid('Enter a valid public https:// source link.')
    if parsed.scheme!='https' or not parsed.hostname or parsed.username or parsed.password or parsed.hostname in ['localhost','127.0.0.1','::1']:
        raise Invalid('Enter a public https:// link without credentials.')
    url=urllib.parse.urlunsplit(('https',parsed.netloc.lower(),parsed.path.rstrip('/'),parsed.query,''))
    kind=value.get('kind');feed=value.get('feed_id')
    if kind not in KINDS or feed not in ['F%02d'%i for i in range(1,11)]:raise Invalid('Choose a source type and feed.')
    sid=value.get('id');existing=None
    if sid:
        existing=store.db.execute('SELECT * FROM sources WHERE id=?',(sid,)).fetchone()
        if not existing:raise Invalid('Source not found.')
    duplicate=store.db.execute('SELECT id FROM sources WHERE url=?',(url,)).fetchone()
    if duplicate and duplicate[0]!=sid:
        if seed:return duplicate[0]
        raise Invalid('This link is already saved. Edit the existing source instead.')
    body={'name':text(value.get('name'),'Name',200),'url':url,'kind':kind,'feed_id':feed,
        'notes':text(value.get('notes',''),'Notes',2000,optional=True),'active':value.get('active',True) is True,
        'created_at':json.loads(existing['payload'])['created_at'] if existing else store.clock(),
        'updated_at':store.clock(),'origin':json.loads(existing['payload'])['origin'] if existing else 'Amy / supplied references' if seed else 'Added in admin',
        'status':'SAVED','monitoring':False}
    sid=sid or uuid.uuid4().hex
    with store.db:store.db.execute('INSERT INTO sources VALUES (?,?,?) ON CONFLICT(id) DO UPDATE SET url=excluded.url,payload=excluded.payload',(sid,url,json.dumps(body)))
    return sid

def listing(store):
    initialize(store)
    return [dict(id=r['id'],**json.loads(r['payload'])) for r in store.db.execute('SELECT * FROM sources ORDER BY rowid')]
