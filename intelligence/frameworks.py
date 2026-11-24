"""Versioned editorial lenses, isolated from observations and performance data."""
import hashlib
import json
import uuid
from .core import Invalid, text

SCHEMA='''
CREATE TABLE IF NOT EXISTS framework_versions(id TEXT PRIMARY KEY,feed_id TEXT NOT NULL,version INTEGER NOT NULL,created_at TEXT NOT NULL,content TEXT NOT NULL,content_hash TEXT NOT NULL,provenance TEXT NOT NULL,UNIQUE(feed_id,version));
CREATE TABLE IF NOT EXISTS framework_approvals(id TEXT PRIMARY KEY,framework_id TEXT NOT NULL REFERENCES framework_versions(id),reviewer TEXT NOT NULL,rationale TEXT NOT NULL,evidence TEXT NOT NULL,approved_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS registry_history(id TEXT PRIMARY KEY,entity_type TEXT NOT NULL,entity_id TEXT NOT NULL,recorded_at TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS registry_imports(digest TEXT PRIMARY KEY,created_at TEXT NOT NULL,report TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS first_party_outcomes(id TEXT PRIMARY KEY,observed_at TEXT NOT NULL,payload TEXT NOT NULL);
'''

def initialize(store):
    store.db.executescript(SCHEMA)

def propose(store,feed_id,content,provenance):
    content=text(content,'Framework content',30000)
    digest=hashlib.sha256(content.encode()).hexdigest()
    latest=store.db.execute('SELECT * FROM framework_versions WHERE feed_id=? ORDER BY version DESC LIMIT 1',(feed_id,)).fetchone()
    if latest and latest['content_hash']==digest:return latest['id']
    fid=uuid.uuid4().hex
    store.db.execute('INSERT INTO framework_versions VALUES (?,?,?,?,?,?,?)',(fid,feed_id,latest['version']+1 if latest else 1,store.clock(),content,digest,provenance))
    return fid

def listing(store):
    return [dict(r,approvals=[dict(a) for a in store.db.execute('SELECT * FROM framework_approvals WHERE framework_id=? ORDER BY rowid DESC',(r['id'],))]) for r in store.db.execute('SELECT * FROM framework_versions ORDER BY feed_id,version DESC')]

def save(store,value):
    feed_id=value.get('feed_id')
    if not store.db.execute('SELECT 1 FROM feed_definitions WHERE id=?',(feed_id,)).fetchone():raise Invalid('Feed not found.')
    with store.db:
        store.db.execute('BEGIN IMMEDIATE')
        latest=store.db.execute('SELECT version FROM framework_versions WHERE feed_id=? ORDER BY version DESC LIMIT 1',(feed_id,)).fetchone()
        if value.get('base_version')!=(latest[0] if latest else 0):raise Invalid('Framework changed. Refresh before revising.')
        return propose(store,feed_id,value.get('content'),text(value.get('provenance'),'Evidence / provenance',6000))

def approve(store,value):
    fid=value.get('id')
    with store.db:
        row=store.db.execute('SELECT * FROM framework_versions WHERE id=?',(fid,)).fetchone()
        if not row:raise Invalid('Framework version not found.')
        latest=store.db.execute('SELECT max(version) FROM framework_versions WHERE feed_id=?',(row['feed_id'],)).fetchone()[0]
        if row['version']!=latest:raise Invalid('Review the latest proposed version.')
        aid=uuid.uuid4().hex
        store.db.execute('INSERT INTO framework_approvals VALUES (?,?,?,?,?,?)',(aid,fid,text(value.get('reviewer'),'Reviewer',100),text(value.get('rationale'),'Review rationale',6000),text(value.get('evidence'),'Supporting evidence and scope',6000),store.clock()))
    return aid

def archive_record(store,kind,id,payload):
    if payload is not None:store.db.execute('INSERT INTO registry_history VALUES (?,?,?,?,?)',(uuid.uuid4().hex,kind,id,store.clock(),json.dumps(payload)))
