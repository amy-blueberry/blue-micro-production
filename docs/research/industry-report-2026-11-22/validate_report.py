#!/usr/bin/env python3
"""Validate the handoff's structure and arithmetic, not external claim truth."""
import hashlib
import json
import math
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def validate():
    sources = json.loads((ROOT / 'sources.json').read_text())
    source_ids = {s['id'] for s in sources}
    assert len(source_ids) == len(sources)
    assert all(s['url'].startswith('https://') for s in sources)
    for s in sources:
        assert all(s[k] for k in ('title', 'publication_date', 'evidence_type', 'limitations'))
    data = json.loads((ROOT / 'chart_data.json').read_text())
    datasets = {d['id']: d for d in data['datasets']}
    assert len(datasets) == len(data['datasets']) == 16
    record_count = 0
    for d in datasets.values():
        assert all(d[k] for k in ('title', 'unit', 'period', 'geography', 'evidence_type', 'interpretation_limits'))
        assert set(d['source_ids']) <= source_ids
        assert d['source_ids'] or d['evidence_type'] == 'synthetic illustration'
        for row in d['records']:
            record_count += 1
            if 'source_id' in row:
                assert row['source_id'] in source_ids
            if 'company_source_ids' in row:
                assert set(row['company_source_ids']) <= source_ids
    ranked = datasets['D08']['records']
    assert [r['rank'] for r in ranked] == list(range(1, 11))
    assert [r['app'] for r in ranked] == [
        'DramaBox', 'ReelShort', 'NetShort', 'DramaWave', 'GoodShort',
        'ShortMax', 'FlickReels', 'MyDrama', 'Stardust TV', 'FlareFlow']
    assert sum(r['value'] for r in datasets['D02']['records']) == 14
    assert sum(r['value'] for r in datasets['D05']['records']) == 100
    assert all(r['male'] + r['female'] == 100 for r in datasets['D06']['records'])
    assert datasets['D10']['records'][0]['bound'] == 'at least'
    assert datasets['D10']['records'][1]['bound'] == 'greater than'
    inputs = datasets['D15']['inputs']
    n = inputs['acquired_users']
    for dataset_id in ('D15', 'D16'):
        for row in datasets[dataset_id]['records']:
            expected = n * (row['payer_conversion'] * inputs['gross_receipts_per_payer'] * inputs['net_collection_factor']
                            + inputs['net_ad_receipts_per_acquired_user'] - inputs['variable_service_cost_per_acquired_user']
                            - row['cost_per_acquired_user']) - row['content_allocation']
            assert math.isclose(expected, row['contribution_after_content'], abs_tol=0.001)
    assert [r['contribution_after_content'] for r in datasets['D15']['records']] == [-60000, -30000]
    for key, allocation in [('conventional', 50000), ('hypothetical_ai', 20000)]:
        expected = (inputs['cost_per_acquired_user'] + inputs['variable_service_cost_per_acquired_user']
                    + allocation / n - inputs['net_ad_receipts_per_acquired_user']) / (30 * .8)
        assert math.isclose(expected, datasets['D15']['breakeven_payer_conversion'][key])
    report = (ROOT / 'INDUSTRY_REPORT.md').read_text()
    brief = (ROOT / 'CLAUDE_DESIGN_BRIEF.md').read_text()
    assert len(re.findall(r'^### 5\.\d+ ', report, re.M)) == 10
    assert len(re.findall(r'^### \d\d\. ', brief, re.M)) == 36
    assert len(re.findall(r'^- \*\*A\d+\.', brief, re.M)) == 10
    assert not re.search(r'\{\{S\d+\}\}', report + brief)
    assert 'SYNTHETIC 90-DAY EXAMPLE' in brief
    for path in ROOT.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if not target.startswith(('https://', 'http://', '#')):
                assert (path.parent / target.split('#')[0]).exists(), (path.name, target)
        for source_id in re.findall(r'\bS\d{2}\b', path.read_text()):
            assert source_id in source_ids, (path.name, source_id)
        for dataset_id in re.findall(r'\bD\d{2}\b', path.read_text()):
            assert dataset_id in datasets, (path.name, dataset_id)
    result = {'status': 'PASS', 'research_cut': '2026-11-22', 'company_profiles': 10,
              'sources': len(sources), 'datasets': len(datasets), 'dataset_records': record_count,
              'main_slides': 36, 'appendix_topics': 10, 'report_words_whitespace': len(report.split()),
              'checks': ['source and dataset identifiers', 'source fields', 'fixed ten-app order',
                         'geographic and demographic sums', 'AI bound qualifiers', 'synthetic model arithmetic',
                         'profile and slide counts', 'local Markdown links'],
              'limit': 'Checks establish internal consistency, not external truth, audited finances or audience validation.'}
    (ROOT / 'VALIDATION.json').write_text(json.dumps(result, indent=2) + '\n')
    hashes = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted(ROOT.iterdir()) if p.is_file() and p.name != 'manifest.json'}
    (ROOT / 'manifest.json').write_text(json.dumps(hashes, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    validate()
