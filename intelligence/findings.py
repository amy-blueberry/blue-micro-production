"""Versioned, researcher-authored decision briefs with explicit inspected evidence."""
import json
import uuid
import urllib.parse
from .core import Invalid, text

def initialize(store):
    store.db.execute('''CREATE TABLE IF NOT EXISTS finding_versions(
        id TEXT PRIMARY KEY,candidate_id TEXT NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,
        version INTEGER NOT NULL,created_at TEXT NOT NULL,payload TEXT NOT NULL,
        UNIQUE(candidate_id,version))''')
    store.db.commit()

def listing(store,dataset):
    initialize(store)
    return [dict(id=r['id'],candidate_id=r['candidate_id'],version=r['version'],created_at=r['created_at'],**json.loads(r['payload']))
        for r in store.db.execute('SELECT f.* FROM finding_versions f JOIN candidates c ON c.id=f.candidate_id WHERE c.dataset=? ORDER BY f.created_at DESC,f.version DESC',(dataset,))]

def save(store,value,agent=None):
    initialize(store);cid=value.get('candidate_id');store.require(cid)
    body={k:text(value.get(k),k.replace('_',' '),n) for k,n in [('author',100),('headline',200),('observed',6000),('coverage',1000),('meaning',3000),('rationale',3000),('gaps',3000),('next_step',2000),('owner',100)]}
    if agent is None and value.get('inspection_confirmed') is not True:raise Invalid('Confirm what material you actually inspected before saving a finding.')
    body['source_url']=text(value.get('source_url'),'evidence source URL',2000)
    try:u=urllib.parse.urlsplit(body['source_url'])
    except ValueError:raise Invalid('Use a public HTTPS evidence link.')
    if u.scheme!='https' or not u.hostname or u.username or u.password or u.hostname in ('localhost','127.0.0.1','::1'):raise Invalid('Use a public HTTPS evidence link.')
    body['action']=value.get('action')
    if body['action'] not in ('INVESTIGATE','WATCH','REJECT','PROPOSE_TEST'):raise Invalid('Choose a supported next action.')
    body['confidence']=value.get('confidence')
    if body['confidence'] not in ('Low','Medium','High'):raise Invalid('Choose confidence in the recommendation.')
    body['test']=text(value.get('test',''),'proposed test',2000,optional=body['action']!='PROPOSE_TEST')
    body['success_measure']=text(value.get('success_measure',''),'success measure',1000,optional=body['action']!='PROPOSE_TEST')
    body['disconfirming_result']=text(value.get('disconfirming_result',''),'disconfirming result',1000,optional=body['action']!='PROPOSE_TEST')
    body['status']='AI_DRAFT' if agent else 'EDITORIAL_DRAFT';body['inspection_confirmed']=agent is None
    if agent:body['agent']=agent
    base=value.get('base_version',0)
    if type(base) is not int:raise Invalid('Refresh before editing this finding.')
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        latest=store.db.execute('SELECT MAX(version) FROM finding_versions WHERE candidate_id=?',(cid,)).fetchone()[0] or 0
        if base!=latest:raise Invalid('This finding changed. Refresh and edit the latest version.')
        fid=uuid.uuid4().hex
        store.db.execute('INSERT INTO finding_versions VALUES (?,?,?,?,?)',(fid,cid,latest+1,store.clock(),json.dumps(body)))
    return fid
