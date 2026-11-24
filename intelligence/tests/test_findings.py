import tempfile
import unittest
from intelligence.store import Store
from intelligence.findings import save,listing
from intelligence.core import Invalid

class FindingsTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.clock='2026-11-23T12:00:00Z';self.s=Store(self.tmp.name,clock=lambda:self.clock)
  self.cid=self.s.ingest('live',dict(source_id='test',origin='catalog_title',observed_at=self.clock,published_at=None))
  self.body=dict(candidate_id=self.cid,author='Test researcher',headline='Synthetic observation',source_url='https://example.com/story',coverage='Synopsis only',observed='Synthetic observed detail',meaning='Unvalidated relevance hypothesis',action='INVESTIGATE',rationale='Need fuller inspection',confidence='Low',gaps='Audience fit unmeasured',next_step='Inspect first scene',owner='Research lead',inspection_confirmed=True)
 def tearDown(self):self.s.close();self.tmp.cleanup()
 def test_versions_preserve_evidence_and_stale_edits_rejected(self):
  save(self.s,self.body)
  with self.assertRaises(Invalid):save(self.s,self.body)
  save(self.s,dict(self.body,base_version=1,headline='Revised finding'))
  rows=listing(self.s,'live');self.assertEqual(len(rows),2);self.assertEqual(rows[0]['version'],2)
  self.assertEqual(rows[1]['observed'],'Synthetic observed detail');self.assertEqual(rows[0]['status'],'EDITORIAL_DRAFT')
  self.assertEqual(listing(self.s,'demo'),[])
 def test_evidence_and_test_requirements(self):
  for update in [dict(observed=''),dict(inspection_confirmed=False),dict(source_url='javascript:alert(1)'),dict(action='DEVELOP_PILOT'),dict(action='PROPOSE_TEST')]:
   with self.assertRaises(Invalid):save(self.s,dict(self.body,**update))
  self.assertEqual(listing(self.s,'live'),[])
  save(self.s,dict(self.body,action='PROPOSE_TEST',test='Synthetic concept test',success_measure='Predeclared threshold',disconfirming_result='No preference over control'))
  self.assertEqual(len(listing(self.s,'live')),1)
 def test_candidate_deletion_cascades(self):
  save(self.s,self.body);self.s.delete(self.cid);self.assertEqual(listing(self.s,'live'),[])
