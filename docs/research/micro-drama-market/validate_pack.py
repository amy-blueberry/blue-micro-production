#!/usr/bin/env python3
"""Check package structure and provenance completeness, not external claim truth."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HEADINGS = [
    'Company & Ownership', 'Core Strategy & Positioning',
    'Monetization & Unit Economics', 'Traction & Financial Data Points',
    'Notable Titles & IP', 'Competitive Moat & Risks',
]

def validate():
    queue = json.loads((ROOT / 'queue.json').read_text())
    assert len(queue) == 10
    assert sorted(x['rank_q1_2026_iap'] for x in queue) == list(range(1, 11))
    assert len(list((ROOT / 'profiles').glob('*.md'))) == 10
    assert len({x['company'] for x in queue}) == 10
    metric_count = 0
    for item in queue:
        assert item['status'] == 'DONE'
        profile = ROOT / item['profile']
        text = profile.read_text()
        assert re.findall(r'^## (.+)$', text, re.M) == HEADINGS
        assert not re.search(r'\bTBD\b|\bunknown\b|no data found', text, re.I)
        data = json.loads((ROOT / 'evidence' / profile.with_suffix('.json').name).read_text())
        judge = json.loads((ROOT / 'judgments' / profile.with_suffix('.json').name).read_text())
        assert data['company'] == item['company']
        assert data['parent'] and data['headquarters']
        assert judge == data['judge']
        assert judge['result'] == item['judge_status'] == 'PASS'
        assert all(judge['criteria'].values())
        assert judge['profile_sha256'] == hashlib.sha256(profile.read_bytes()).hexdigest()
        assert len([m for m in data['metrics'] if m['qualifies']]) >= 2
        for metric in data['metrics']:
            assert isinstance(metric['value'], (int, float))
            assert all(metric[k] for k in ['name', 'unit', 'period', 'scope', 'source_url'])
            assert metric['source_url'].startswith('https://')
        metric_count += len(data['metrics'])
    for path in ROOT.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if not target.startswith(('http://', 'https://', '#')):
                assert (path.parent / target.split('#')[0]).exists(), (path, target)
    with (ROOT / 'MASTER_COMPARISON.csv').open(newline='') as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == 10
    assert [int(r['rank_q1_2026_iap']) for r in rows] == list(range(1, 11))
    assert {r['company_app'] for r in rows} == {x['company'] for x in queue}
    with (ROOT / 'METRICS.csv').open(newline='') as f:
        assert len(list(csv.DictReader(f))) == metric_count
    state = json.loads((ROOT / 'run_state.json').read_text())
    assert state['pending'] == 0 and state['done'] == state['total'] == 10
    result = {
        'result': 'PASS', 'research_date': '2026-11-21',
        'profiles': 10, 'metrics': metric_count, 'pending': 0,
        'checks': ['unique ranked entities', 'six required sections',
                   'no prohibited placeholders', 'two qualifying dated metrics',
                   'source URL fields', 'judgment/profile hashes',
                   'local Markdown links', 'CSV row counts and rank order',
                   'queue/run-state agreement'],
        'limitation': 'Structural checks do not independently audit external claims.'
    }
    (ROOT / 'VALIDATION.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))

if __name__ == '__main__':
    validate()
