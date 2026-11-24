import datetime as dt
import json
import os
import sqlite3
import uuid
from .core import Invalid, cutoff, ident, now, parse_time, private_dir, score_assessment, text, COHORTS, ROUTES

SCHEMA = '''
PRAGMA foreign_keys=ON;
CREATE TABLE IF NOT EXISTS meta(key TEXT PRIMARY KEY,value TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS candidates(id TEXT PRIMARY KEY, dataset TEXT NOT NULL, source_id TEXT NOT NULL, created_at TEXT NOT NULL, UNIQUE(dataset,source_id));
CREATE TABLE IF NOT EXISTS observations(id TEXT PRIMARY KEY,candidate_id TEXT NOT NULL REFERENCES candidates(id) ON DELETE CASCADE, observed_at TEXT NOT NULL, payload TEXT NOT NULL, UNIQUE(candidate_id,observed_at));
CREATE TABLE IF NOT EXISTS notes(id TEXT PRIMARY KEY,candidate_id TEXT NOT NULL REFERENCES candidates(id) ON DELETE CASCADE, created_at TEXT NOT NULL, payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS analyses(id TEXT PRIMARY KEY,candidate_id TEXT NOT NULL REFERENCES candidates(id) ON DELETE CASCADE, created_at TEXT NOT NULL, payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS decisions(id TEXT PRIMARY KEY,candidate_id TEXT NOT NULL REFERENCES candidates(id) ON DELETE CASCADE, created_at TEXT NOT NULL,payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS briefs(id TEXT PRIMARY KEY,dataset TEXT NOT NULL,kind TEXT NOT NULL,period TEXT NOT NULL,created_at TEXT NOT NULL, UNIQUE(dataset,kind,period));
CREATE TABLE IF NOT EXISTS brief_items(brief_id TEXT NOT NULL REFERENCES briefs(id) ON DELETE CASCADE,candidate_id TEXT NOT NULL REFERENCES candidates(id) ON DELETE CASCADE,position INTEGER NOT NULL,decision_id TEXT NOT NULL REFERENCES decisions(id) ON DELETE CASCADE, PRIMARY KEY(brief_id,candidate_id));
CREATE TABLE IF NOT EXISTS runs(id TEXT PRIMARY KEY,dataset TEXT NOT NULL,started_at TEXT NOT NULL,finished_at TEXT,status TEXT NOT NULL,counts TEXT NOT NULL,errors TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS budgets(day TEXT NOT NULL,bucket TEXT NOT NULL,used INTEGER NOT NULL,PRIMARY KEY(day,bucket));
CREATE TABLE IF NOT EXISTS slots(day TEXT PRIMARY KEY,run_id TEXT NOT NULL);
'''

class Store:
    def __init__(self, data_dir, clock=now):
        self.dir = private_dir(data_dir)
        self.path = self.dir / 'intelligence.sqlite3'
        self.clock = clock
        self.db = sqlite3.connect(str(self.path), timeout=20)
        self.db.row_factory = sqlite3.Row
        self.db.executescript(SCHEMA)
        self.db.execute('PRAGMA secure_delete=ON')
        self.db.execute("INSERT OR IGNORE INTO meta VALUES ('schema_version','1')")
        if self.db.execute("SELECT value FROM meta WHERE key='schema_version'").fetchone()[0] != '1':
            raise Invalid('Unsupported database schema version.')
        self.db.commit()
        os.chmod(self.path, 0o600)

    def close(self):
        self.db.close()

    def consume(self, bucket, limit):
        day = self.clock()[:10]
        with self.db:
            self.db.execute('BEGIN IMMEDIATE')
            row = self.db.execute('SELECT used FROM budgets WHERE day=? AND bucket=?', (day, bucket)).fetchone()
            used = row[0] if row else 0
            if used >= limit:
                raise Invalid('Daily %s limit reached.' % bucket)
            self.db.execute('INSERT INTO budgets VALUES (?,?,?) ON CONFLICT(day,bucket) DO UPDATE SET used=excluded.used', (day, bucket, used + 1))

    def start_run(self, dataset):
        rid = uuid.uuid4().hex
        with self.db:
            self.db.execute('INSERT INTO runs VALUES (?,?,?,NULL,?,?,?)', (rid, dataset, self.clock(), 'RUNNING', '{}', '[]'))
        return rid

    def finish_run(self, rid, status, counts, errors):
        with self.db:
            self.db.execute('UPDATE runs SET finished_at=?,status=?,counts=?,errors=? WHERE id=?', (self.clock(), status, json.dumps(counts), json.dumps(errors), rid))

    def recover_runs(self):
        # Only called while holding the process lock.
        with self.db:
            self.db.execute("UPDATE runs SET finished_at=?,status='INTERRUPTED',errors=? WHERE status='RUNNING'", (self.clock(), '["Worker interrupted. Inspect before retrying."]'))

    def ingest(self, dataset, item):
        if dataset not in ['demo', 'live']:
            raise Invalid('Invalid dataset.')
        text(item.get('source_id'), 'source ID', 100)
        observed = item['observed_at']
        parse_time(observed)
        if item.get('published_at') is not None:parse_time(item['published_at'])
        if parse_time(observed) > parse_time(self.clock()) + dt.timedelta(minutes=5):
            raise Invalid('Observation time cannot be in the future.')
        if dataset == 'live' and item.get('origin') not in ('youtube_api','firecrawl','catalog_title'):
            raise Invalid('Live collector accepts only supported connector records.')
        if dataset == 'demo' and item.get('origin') != 'synthetic':
            raise Invalid('Demo must contain synthetic fixtures only.')
        cid = ident(dataset, item['source_id'])
        oid = ident(cid, observed)
        with self.db:
            self.db.execute('INSERT OR IGNORE INTO candidates VALUES (?,?,?,?)', (cid, dataset, item['source_id'], self.clock()))
            self.db.execute('INSERT OR IGNORE INTO observations VALUES (?,?,?,?)', (oid, cid, observed, json.dumps(item)))
        return cid

    def purge(self):
        if self.db.execute("SELECT 1 FROM sqlite_master WHERE name='collection_previews'").fetchone():
            from .web_collection import initialize
            initialize(self)
        boundary = (parse_time(self.clock()) - dt.timedelta(days=29)).isoformat().replace('+00:00','Z')
        with self.db:
            self.db.execute("DELETE FROM observations WHERE observed_at<? AND candidate_id IN (SELECT id FROM candidates WHERE dataset='live')", (boundary,))
            if self.db.execute("SELECT 1 FROM sqlite_master WHERE name='finding_versions'").fetchone():
                self.db.execute("DELETE FROM finding_versions WHERE created_at<? AND candidate_id IN (SELECT id FROM candidates WHERE dataset='live')",(boundary,))
            # Purge annotations too: they could reference expired API material.
            for table in ['notes', 'analyses', 'decisions']:
                self.db.execute('DELETE FROM '+table+" WHERE created_at<? AND candidate_id IN (SELECT id FROM candidates WHERE dataset='live')", (boundary,))
            self.db.execute('DELETE FROM candidates WHERE NOT EXISTS (SELECT 1 FROM observations o WHERE o.candidate_id=candidates.id)')

    def require(self, cid):
        row = self.db.execute('SELECT * FROM candidates WHERE id=?', (cid,)).fetchone()
        if not row:
            raise Invalid('Candidate not found or expired.')
        return row

    def get(self, cid):
        row = dict(self.require(cid))
        observations = [json.loads(x[0]) for x in self.db.execute('SELECT payload FROM observations WHERE candidate_id=? ORDER BY observed_at DESC', (cid,))]
        row['latest'] = observations[0]
        row['observations'] = observations
        for table in ['notes', 'analyses', 'decisions']:
            row[table] = [dict(id=x['id'], created_at=x['created_at'], **json.loads(x['payload'])) for x in self.db.execute('SELECT * FROM '+table+' WHERE candidate_id=? ORDER BY created_at DESC,rowid DESC', (cid,))]
        row['decision'] = row['decisions'][0] if row['decisions'] else None
        row['analysis'] = row['analyses'][0] if row['analyses'] else None
        row['review_state'] = 'REVIEWED' if row['decision'] else 'NEEDS_REVIEW'
        row['derived_metrics'] = None
        if row['latest'].get('origin')=='catalog_title':
            row['measurement_note']='Title listing evidence. Displayed source figures are not audience demographics or independently verified growth.'
            return row
        if row['latest'].get('origin')=='firecrawl':
            row['measurement_note']='Website text capture. No audience metrics or audiovisual inspection.'
            return row
        row['measurement_note'] = 'YouTube source counters only. Custom derived metrics are disabled.' if row['dataset']=='live' else 'Synthetic fixtures. Not audience or market evidence.'
        return row

    def list(self, dataset):
        return [self.get(x[0]) for x in self.db.execute('SELECT id FROM candidates WHERE dataset=? ORDER BY created_at DESC,id', (dataset,))]

    def add_note(self, cid, value):
        self.require(cid)
        body = {'author': text(value.get('author'), 'author', 100), 'text': text(value.get('text'), 'note', 10000),
                'coverage': text(value.get('coverage'), 'inspection coverage', 500), 'evidence_type': value.get('evidence_type'),
                'analysis_allowed': value.get('analysis_allowed') is True, 'access_basis': text(value.get('access_basis'), 'access basis', 500)}
        if body['evidence_type'] not in ['D', 'O', 'I', 'FP']:
            raise Invalid('Evidence type must be D, O, I or FP.')
        # No external source content or credentials are automatically transmitted.
        nid = uuid.uuid4().hex
        with self.db:
            self.db.execute('INSERT INTO notes VALUES (?,?,?,?)', (nid, cid, self.clock(), json.dumps(body)))
        return nid

    def decide(self, cid, value):
        candidate = self.get(cid)
        route = value.get('route')
        if route not in ROUTES:
            raise Invalid('Invalid editorial route.')
        cohort = value.get('primary_cohort')
        if cohort is not None and cohort not in COHORTS:
            raise Invalid('Unknown primary cohort.')
        if route in ['TEST', 'DEVELOP_PILOT'] and not cohort:
            raise Invalid('This recommendation requires one primary cohort.')
        allowed = {n['id'] for n in candidate['notes'] if n['analysis_allowed']}
        body = {'route': route, 'primary_cohort': cohort, 'author': text(value.get('author'), 'reviewer', 100),
                'rationale': text(value.get('rationale'), 'decision rationale'),
                'confidence': text(value.get('confidence'), 'confidence', 100),
                'sample_size_note': text(value.get('sample_size_note'), 'sample size / availability', 500),
                'rights_status': value.get('rights_status'), 'execution_authorized': False,
                'assessment': score_assessment(value.get('assessment'), allowed)}
        if body['rights_status'] not in ['UNREVIEWED', 'ORIGINAL_PROPOSAL', 'REQUIRES_LICENSE', 'REVIEWED']:
            raise Invalid('Invalid rights status.')
        did = uuid.uuid4().hex
        with self.db:
            self.db.execute('INSERT INTO decisions VALUES (?,?,?,?)', (did, cid, self.clock(), json.dumps(body)))
        return did

    def save_analysis(self, cid, body):
        self.require(cid)
        aid = uuid.uuid4().hex
        with self.db:
            self.db.execute('INSERT INTO analyses VALUES (?,?,?,?)', (aid, cid, self.clock(), json.dumps(body)))
        return aid

    def delete(self, cid):
        self.require(cid)
        with self.db:
            self.db.execute('DELETE FROM candidates WHERE id=?', (cid,))

    def brief(self, dataset, kind='daily'):
        if kind not in ['daily','weekly']:
            raise Invalid('Invalid brief type.')
        clock = parse_time(self.clock())
        period = clock.date().isoformat() if kind=='daily' else '%04d-W%02d' % clock.isocalendar()[:2]
        bid = ident(dataset, kind, period)
        existing = self.db.execute('SELECT id FROM briefs WHERE id=?', (bid,)).fetchone()
        if existing:
            return self.brief_view(bid)
        eligible = []
        for item in self.list(dataset):
            if not item['decision'] or item['decision']['route']=='REJECT':
                continue
            if kind=='weekly' and item['decision']['route'] not in ['TEST','DEVELOP_PILOT','RIGHTS_REVIEW']:
                continue
            if self.db.execute('SELECT 1 FROM brief_items bi JOIN briefs b ON b.id=bi.brief_id WHERE bi.candidate_id=? AND b.kind=?', (item['id'],kind)).fetchone():
                continue
            eligible.append(item)
        eligible.sort(key=lambda x: (x['decision']['created_at'], x['id']), reverse=True)
        with self.db:
            self.db.execute('INSERT INTO briefs VALUES (?,?,?,?,?)', (bid,dataset,kind,period,self.clock()))
            for i,item in enumerate(eligible[:5 if kind=='daily' else 3]):
                self.db.execute('INSERT INTO brief_items VALUES (?,?,?,?)', (bid,item['id'],i,item['decision']['id']))
        return self.brief_view(bid)

    def brief_view(self, bid):
        row = self.db.execute('SELECT * FROM briefs WHERE id=?',(bid,)).fetchone()
        if not row:
            raise Invalid('Brief not found.')
        result = dict(row)
        result['items'] = []
        for member in self.db.execute('SELECT candidate_id,decision_id FROM brief_items WHERE brief_id=? ORDER BY position', (bid,)):
            item = self.get(member['candidate_id'])
            decision = next((d for d in item['decisions'] if d['id']==member['decision_id']), None)
            if decision is not None:
                item['decision'] = decision
                result['items'].append(item)
        result['note'] = 'Reviewed candidates; not a measured breakout ranking. Current source metadata; expired/deleted evidence is omitted. No scores are combined.'
        return result
