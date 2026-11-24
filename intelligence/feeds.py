"""Editable local research definitions; these do not configure collectors."""
import json
import urllib.parse
from .core import Invalid, REPO, text

def initialize(store):
    with store.db:
        store.db.execute('CREATE TABLE IF NOT EXISTS feed_definitions(id TEXT PRIMARY KEY,payload TEXT NOT NULL)')
        if store.db.execute("SELECT 1 FROM meta WHERE key='feed_seeds_v1'").fetchone():return
        for feed in json.loads((REPO/'docs/production-engine/intelligence_feeds.json').read_text())['feeds']:
            feed.update(active=True,version=1,updated_at=store.clock())
            store.db.execute('INSERT OR IGNORE INTO feed_definitions VALUES (?,?)',(feed['id'],json.dumps(feed)))
        store.db.execute("INSERT OR IGNORE INTO meta VALUES ('feed_seeds_v1','1')")

def listing(store):
    initialize(store)
    return [json.loads(r[0]) for r in store.db.execute('SELECT payload FROM feed_definitions ORDER BY rowid')]

def lines(value,name,urls=False):
    if not isinstance(value,list) or len(value)>30:raise Invalid(name+' must contain at most 30 entries.')
    result=[]
    for entry in value:
        entry=text(entry,name,2000 if urls else 200)
        if urls:
            try:p=urllib.parse.urlsplit(entry)
            except ValueError:raise Invalid('Invalid entry-point URL.')
            if p.scheme!='https' or not p.hostname or p.username or p.password:
                raise Invalid('Entry points must be HTTPS links without credentials.')
        if entry not in result:result.append(entry)
    return result

def save(store,value):
    initialize(store)
    from .frameworks import initialize as init_frameworks, archive_record
    init_frameworks(store)
    clean={k:text(value.get(k),k,n) for k,n in [('name',200),('universe',30000),('relevance_filter',2000),('cadence_proposed',200)]}
    if value.get('priority') not in ['P0','P1','P2'] or value.get('kind') not in ['external','internal']:
        raise Invalid('Choose a valid priority and feed kind.')
    if type(value.get('active')) is not bool:raise Invalid('Feed active status must be true or false.')
    clean.update(priority=value['priority'],kind=value['kind'],active=value['active'])
    for key in ['entry_points','seed_queries','candidate_community_allowlist']:
        clean[key]=lines(value.get(key,[]),key,key=='entry_points')
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        sid=value.get('id')
        if sid:
            row=store.db.execute('SELECT payload FROM feed_definitions WHERE id=?',(sid,)).fetchone()
            if not row:raise Invalid('Feed not found.')
            feed=json.loads(row[0])
            if type(value.get('version')) is not int or value['version']!=feed['version']:
                raise Invalid('This feed changed since you opened it. Close and refresh before editing.')
        else:
            number=max([int(r[0][1:]) for r in store.db.execute('SELECT id FROM feed_definitions')]+[0])+1
            sid='F%02d'%number
            feed={'id':sid,'version':0,'activation_state':'NOT_CONNECTED','access_validation':'REQUIRED','last_run_at':None}
        duplicate=store.db.execute('SELECT payload FROM feed_definitions WHERE id<>?',(sid,)).fetchall()
        if any(json.loads(r[0])['name'].casefold()==clean['name'].casefold() for r in duplicate):
            raise Invalid('A feed with this name already exists.')
        archive_record(store,'feed',sid,dict(feed) if feed['version'] else None)
        feed.update(clean);feed.update(version=feed['version']+1,updated_at=store.clock())
        store.db.execute('INSERT INTO feed_definitions VALUES (?,?) ON CONFLICT(id) DO UPDATE SET payload=excluded.payload',(sid,json.dumps(feed)))
    return sid
