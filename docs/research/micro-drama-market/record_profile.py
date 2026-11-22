#!/usr/bin/env python3
"""Persist a researched draft and an explicit analyst judgment; does not research or fabricate evidence."""
import json,re,sys,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
HEADINGS=['Company & Ownership','Core Strategy & Positioning','Monetization & Unit Economics','Traction & Financial Data Points','Notable Titles & IP','Competitive Moat & Risks']
def save(d):
 q=json.loads((ROOT/'queue.json').read_text())
 active=next((x for x in q if x['status']=='PENDING'),None)
 assert active and active['company']==d['company'],'Strict sequential queue violation'
 slug=re.sub(r'[^A-Za-z0-9]+','_',d['company']).strip('_')
 text='# '+d['company']+'\n\nResearch date: 2026-11-21. Entity level: '+d['entity_level']+'.\n\n'
 for heading in HEADINGS:
  assert d['sections'].get(heading)
  text+='## '+heading+'\n\n'+d['sections'][heading]+'\n\n'
 checks=d['judge']['criteria']
 assert set(checks)=={'ownership_hq','two_dated_metrics','no_placeholders','specific_strategy'}
 placeholder=bool(re.search(r'\bTBD\b|\bunknown\b|no data found',text,re.I))
 checks['no_placeholders']=not placeholder
 validmetrics=[m for m in d['metrics'] if m.get('period') and m.get('source_url') and m.get('value') is not None and m.get('qualifies') is True]
 checks['two_dated_metrics']=checks['two_dated_metrics'] and len(validmetrics)>=2
 passed=all(checks.values())
 judgment='PASS' if passed else ('EXCEPTION_AFTER_TWO_RETRIES' if active['attempts']>=2 else 'NEEDS_FOLLOWUP')
 text+='Evidence gate: **'+judgment+'**. '+d['judge']['rationale']+'\n'
 (ROOT/'profiles'/f'{slug}.md').write_text(text)
 d['judge']['result']=judgment
 d['judge']['attempts']=active['attempts']
 d['judge']['profile_sha256']=hashlib.sha256(text.encode()).hexdigest()
 (ROOT/'evidence'/f'{slug}.json').write_text(json.dumps(d,indent=2)+'\n')
 (ROOT/'judgments'/f'{slug}.json').write_text(json.dumps(d['judge'],indent=2)+'\n')
 active.update({'judge_status':judgment,'profile':f'profiles/{slug}.md'})
 if passed or active['attempts']>=2:active['status']='DONE'
 tmp=ROOT/'queue.json.tmp';tmp.write_text(json.dumps(q,indent=2)+'\n');tmp.replace(ROOT/'queue.json')
 state=json.loads((ROOT/'run_state.json').read_text())
 pending=[x for x in q if x['status']=='PENDING']
 state.update({'active_company':pending[0]['company'] if pending else None,'done':len(q)-len(pending),'pending':len(pending),'phase':'WORKER_JUDGE' if pending else 'FINAL_PACKAGING'})
 (ROOT/'run_state.json').write_text(json.dumps(state,indent=2)+'\n')
 with (ROOT/'events.jsonl').open('a') as f:f.write(json.dumps({'company':d['company'],'event':'JUDGED','attempts':active['attempts'],'result':judgment})+'\n')
 print(json.dumps({'company':d['company'],'judge':judgment,'done':state['done'],'pending':state['pending'],'next':state['active_company']}))
if __name__=='__main__':save(json.loads(Path(sys.argv[1]).read_text()))
