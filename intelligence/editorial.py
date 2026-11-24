"""Version-bound feedback and separately retained, explicitly approved editorial memory."""
import json
import uuid
from .core import Invalid, text

SECTIONS=('general','observed','meaning','rationale','gaps','next_step')
KINDS=('CORRECTION','PREFERENCE','HYPOTHESIS')

def initialize(store):
    store.db.executescript('''
    CREATE TABLE IF NOT EXISTS finding_comments(id TEXT PRIMARY KEY,finding_id TEXT NOT NULL REFERENCES finding_versions(id) ON DELETE CASCADE,created_at TEXT NOT NULL,payload TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS editorial_lessons(id TEXT PRIMARY KEY,created_at TEXT NOT NULL,payload TEXT NOT NULL);
    CREATE TABLE IF NOT EXISTS editorial_lesson_events(id TEXT PRIMARY KEY,lesson_id TEXT NOT NULL REFERENCES editorial_lessons(id),created_at TEXT NOT NULL,payload TEXT NOT NULL);
    ''')

def listing(store):
    initialize(store)
    comments=[dict(id=r['id'],finding_id=r['finding_id'],created_at=r['created_at'],**json.loads(r['payload'])) for r in store.db.execute('SELECT * FROM finding_comments ORDER BY rowid')]
    lessons=[]
    for r in store.db.execute('SELECT * FROM editorial_lessons ORDER BY rowid DESC'):
        events=[dict(created_at=e['created_at'],**json.loads(e['payload'])) for e in store.db.execute('SELECT * FROM editorial_lesson_events WHERE lesson_id=? ORDER BY rowid',(r['id'],))]
        lessons.append(dict(id=r['id'],created_at=r['created_at'],**json.loads(r['payload']),status=events[-1]['status'] if events else 'DRAFT',events=events))
    return {'comments':comments,'lessons':lessons}

def comment(store,value):
    initialize(store)
    row=store.db.execute('SELECT * FROM finding_versions WHERE id=?',(value.get('finding_id'),)).fetchone()
    if not row:raise Invalid('Brief no longer exists. Refresh first.')
    if value.get('section') not in SECTIONS or value.get('kind') not in KINDS:raise Invalid('Choose a section and feedback type.')
    body={k:text(value.get(k),k,n) for k,n in [('author',100),('text',2000)]}
    body.update(section=value['section'],kind=value['kind'])
    cid=uuid.uuid4().hex
    with store.db:store.db.execute('INSERT INTO finding_comments VALUES (?,?,?,?)',(cid,row['id'],store.clock(),json.dumps(body)))
    return cid

def propose(store,value):
    initialize(store)
    # Durable memory contains editorial principles, never copied source passages.
    if value.get('kind') not in ('PREFERENCE','HYPOTHESIS'):raise Invalid('Factual corrections stay with their source; only preferences or hypotheses become lasting lessons.')
    if value.get('retention_confirmed') is not True:raise Invalid('Confirm this is an original editorial lesson, not copied source text or personal data.')
    feed=value.get('feed_id')
    if not store.db.execute('SELECT 1 FROM feed_definitions WHERE id=?',(feed,)).fetchone():raise Invalid('Choose an existing feed.')
    body={k:text(value.get(k),k,n) for k,n in [('author',100),('text',1500)]}
    body.update(kind=value['kind'],feed_id=feed)
    lid=uuid.uuid4().hex
    with store.db:store.db.execute('INSERT INTO editorial_lessons VALUES (?,?,?)',(lid,store.clock(),json.dumps(body)))
    return lid

def decide(store,value):
    initialize(store)
    if value.get('status') not in ('APPROVED','RETIRED'):raise Invalid('Choose approve or retire.')
    author=text(value.get('author'),'reviewer',100)
    if not store.db.execute('SELECT 1 FROM editorial_lessons WHERE id=?',(value.get('id'),)).fetchone():raise Invalid('Lesson not found.')
    with store.db:store.db.execute('INSERT INTO editorial_lesson_events VALUES (?,?,?,?)',(uuid.uuid4().hex,value['id'],store.clock(),json.dumps({'status':value['status'],'author':author})))

def context(store,feed_ids):
    eligible=[x for x in listing(store)['lessons'] if x['status']=='APPROVED' and x['feed_id'] in feed_ids]
    # Explicitly bounded context, newest matching lessons first.
    return [dict(id=x['id'],kind=x['kind'],text=x['text']) for x in eligible[:8]]
