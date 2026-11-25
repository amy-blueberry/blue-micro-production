import json
import os
import tempfile
import unittest
from unittest.mock import patch
from intelligence.store import Store
from intelligence import research_agent as agent, findings, feeds, frameworks, editorial
from intelligence.core import Invalid

class ResearchTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.s=Store(self.tmp.name,clock=lambda:'2026-11-23T12:00:00Z')
  feeds.listing(self.s);frameworks.initialize(self.s);agent.initialize(self.s)
  self.env=patch.dict(os.environ,{'FIRECRAWL_API_KEY':'synthetic-firecrawl','ANTHROPIC_API_KEY':'synthetic-claude'});self.env.start()
  self.ids=[]
  for i in range(2):
   self.ids.append(self.s.ingest('live',dict(source_id='title:'+str(i),origin='catalog_title',url='https://a24films.com/films/test-'+str(i),title='Synthetic title '+str(i),feed_ids=['F01'],published_at=None,observed_at='2026-11-23T12:00:00Z')))
 def tearDown(self):self.env.stop();self.s.close();self.tmp.cleanup()
 def fetch(self,url,key):return {'markdown':'A fictional protagonist struggles to belong in a new school. '+('Synthetic test evidence. '*10),'metadata':{'sourceURL':url,'statusCode':200}}
 def call(self,packet,cfg):
  e=packet['evidence'];return {'headline':'Investigate belonging','observations':[{'text':'The page describes a school belonging conflict.','evidence_id':e['id'],'quote':'A fictional protagonist struggles to belong in a new school.'}],'meaning':'Hypothesis: compare the stated belonging conflict with Roblox social play.','rationale':'Premise supports further investigation, not production.','gaps':'No episodes inspected or audience measured.','next_step':'Inspect an episode and seek counterexamples.','action':'INVESTIGATE'},{'input_tokens':100,'output_tokens':100}
 def run_agent(self,ids=None,fetch=None,call=None):
  rid=agent.begin(self.s,ids or self.ids);agent.execute(self.tmp.name,rid,fetch or self.fetch,call or self.call);return agent.state(self.s)['runs'][0]
 def test_complete_batch_saves_cited_drafts_without_human_attestation(self):
  run=self.run_agent();self.assertEqual(run['status'],'COMPLETED');rows=findings.listing(self.s,'live');self.assertEqual(len(rows),2)
  self.assertFalse(rows[0]['inspection_confirmed']);self.assertEqual(rows[0]['status'],'AI_DRAFT')
  self.assertTrue(rows[0]['agent']['citations'][0]['url'].startswith('https://a24films.com/films/'))
  self.assertEqual(rows[0]['confidence'],'Low');self.assertIn('No episodes',rows[0]['coverage'])
  agent.review(self.s,{'finding_id':rows[0]['id'],'status':'ACCEPTED','author':'Editor'})
  self.assertEqual(agent.state(self.s)['reviews'][0]['status'],'ACCEPTED')
 def test_fabricated_citation_rejected_partial_batch_preserves_other_result(self):
  def call(packet,cfg):
   result,usage=self.call(packet,cfg)
   if packet['title'].endswith('1'):result['observations'][0]['quote']='Fabricated quotation'
   return result,usage
  run=self.run_agent(call=call);self.assertEqual(run['status'],'PARTIAL');self.assertEqual(len(findings.listing(self.s,'live')),1)
  self.assertIn('Citation check failed',run['jobs'][1]['error'])
 def test_missing_credentials_no_network_and_single_active_batch(self):
  with patch.dict(os.environ,{'ANTHROPIC_API_KEY':''}):
   with self.assertRaises(Invalid):agent.begin(self.s,self.ids)
  self.assertEqual(agent.state(self.s)['runs'],[])
  agent.begin(self.s,self.ids)
  with self.assertRaises(Invalid):agent.begin(self.s,self.ids)
  agent.initialize(self.s,recover=True);self.assertEqual(agent.state(self.s)['runs'][0]['status'],'INTERRUPTED')
 def test_only_approved_framework_is_sent_and_stale_brief_not_overwritten(self):
  f=frameworks.propose(self.s,'F01','Draft lens not approved','test');self.s.db.commit()
  packets=[]
  def call(packet,cfg):packets.append(packet);return self.call(packet,cfg)
  self.run_agent([self.ids[0]],call=call);self.assertIsNone(packets[0]['approved_framework'])
  frameworks.approve(self.s,{'id':f,'reviewer':'Test','rationale':'Test approval','evidence':'Synthetic'})
  rid=agent.begin(self.s,[self.ids[0]])
  old=findings.listing(self.s,'live')[0]
  findings.save(self.s,dict(old,candidate_id=self.ids[0],base_version=1,inspection_confirmed=True))
  agent.execute(self.tmp.name,rid,self.fetch,call)
  self.assertEqual(packets[-1]['approved_framework']['id'],f)
  self.assertEqual(agent.state(self.s)['runs'][0]['status'],'FAILED')
  self.assertEqual(len(findings.listing(self.s,'live')),2)
  with self.assertRaises(Invalid):agent.review(self.s,{'finding_id':old['id'],'status':'ACCEPTED','author':'Editor'})
 def test_page_failure_and_model_budget_do_not_create_generic_briefs(self):
  def bad(url,key):return {'markdown':'Access denied','metadata':{'statusCode':403}}
  run=self.run_agent([self.ids[0]],fetch=bad);self.assertEqual(run['status'],'FAILED');self.assertEqual(findings.listing(self.s,'live'),[])
  # The worker has its own real-time clock; consume against that same day.
  other=Store(self.tmp.name)
  for _ in range(5):other.consume('research_model_calls',5)
  other.close()
  run=self.run_agent([self.ids[0]]);self.assertEqual(run['status'],'FAILED');self.assertEqual(findings.listing(self.s,'live'),[])
 def test_unapproved_lens_prose_is_not_sent_as_objective(self):
  o=agent.research_objective({'universe':'**Framework:** Secret draft lens.\n**Live pull:** Find new relevant titles.\n**Why/use:** Later explanation.','relevance_filter':'School stories'})
  self.assertNotIn('Secret draft lens',json.dumps(o));self.assertIn('Find new relevant titles',o['live_questions'])

 def test_model_action_contract_cannot_authorize_production(self):
  packet={'evidence':{'id':'x','text':'A fictional protagonist struggles to belong in a new school.'}}
  result,_=self.call(packet,{})
  result['action']='DEVELOP_PILOT'
  with self.assertRaises(Invalid):agent.validate(result,packet['evidence'])

 def test_feedback_revision_receives_comments_and_preserves_prior_version(self):
  self.run_agent([self.ids[0]])
  old=findings.listing(self.s,'live')[0]
  cid=editorial.comment(self.s,dict(finding_id=old['id'],section='meaning',kind='PREFERENCE',author='Editor',text='Explain costly character choices.'))
  rid=agent.begin(self.s,[self.ids[0]],revision=True)
  def revised(packet,cfg):
   self.assertEqual(packet['revision']['comments'][0]['id'],cid)
   result,usage=self.call(packet,cfg)
   result['meaning']='Hypothesis: investigate whether belonging requires a costly choice; the synopsis does not establish it.'
   result['feedback_response']='Added the requested question, without claiming scene evidence.'
   return result,usage
  agent.execute(self.tmp.name,rid,self.fetch,revised)
  rows=findings.listing(self.s,'live');self.assertEqual(len(rows),2)
  newest=max(rows,key=lambda x:x['version'])
  self.assertEqual(newest['agent']['revises'],old['id']);self.assertEqual(newest['agent']['feedback_ids'],[cid])
  self.assertNotEqual(newest['meaning'],old['meaning'])

 def test_memory_requires_approval_is_scoped_and_can_be_retired(self):
  lid=editorial.propose(self.s,dict(kind='PREFERENCE',feed_id='F01',author='Editor',text='Explain costly choices.',retention_confirmed=True))
  self.assertEqual(editorial.context(self.s,['F01']),[])
  editorial.decide(self.s,dict(id=lid,status='APPROVED',author='Editor'))
  self.assertEqual(editorial.context(self.s,['F02']),[])
  self.assertEqual(editorial.context(self.s,['F01'])[0]['id'],lid)
  packets=[]
  def call(packet,cfg):packets.append(packet);return self.call(packet,cfg)
  self.run_agent([self.ids[0]],call=call)
  self.assertEqual(packets[0]['editorial_lessons'][0]['id'],lid)
  editorial.decide(self.s,dict(id=lid,status='RETIRED',author='Editor'))
  self.assertEqual(editorial.context(self.s,['F01']),[])

 def test_source_corrections_cannot_be_promoted_as_enduring_truth(self):
  with self.assertRaises(Invalid):editorial.propose(self.s,dict(kind='CORRECTION',feed_id='F01',author='Editor',text='Unsupported age claim',retention_confirmed=True))
  with self.assertRaises(Invalid):editorial.propose(self.s,dict(kind='PREFERENCE',feed_id='F01',author='Editor',text='A lesson'))
  self.run_agent([self.ids[0]])
  with self.assertRaises(Invalid):agent.begin(self.s,[self.ids[0]],revision=True)

 def test_memory_survives_source_deletion_comments_do_not(self):
  self.run_agent([self.ids[0]])
  old=findings.listing(self.s,'live')[0]
  editorial.comment(self.s,dict(finding_id=old['id'],section='meaning',kind='PREFERENCE',author='Editor',text='Use character choices.'))
  lid=editorial.propose(self.s,dict(kind='PREFERENCE',feed_id='F01',author='Editor',text='Use character choices.',retention_confirmed=True))
  self.s.delete(self.ids[0])
  state=editorial.listing(self.s)
  self.assertEqual(state['comments'],[]);self.assertEqual(state['lessons'][0]['id'],lid)

 def test_revision_without_feedback_explanation_fails_without_overwrite(self):
  self.run_agent([self.ids[0]])
  old=findings.listing(self.s,'live')[0]
  editorial.comment(self.s,dict(finding_id=old['id'],section='meaning',kind='PREFERENCE',author='Editor',text='Explain character choices.'))
  rid=agent.begin(self.s,[self.ids[0]],revision=True)
  agent.execute(self.tmp.name,rid,self.fetch,self.call)
  self.assertEqual(agent.state(self.s)['runs'][0]['status'],'FAILED')
  self.assertEqual(len(findings.listing(self.s,'live')),1)

 def test_whole_feedback_atomic_idempotent_and_general_reaches_revision(self):
  self.run_agent([self.ids[0]])
  old=findings.listing(self.s,'live')[0]
  value=dict(finding_id=old['id'],author='Editor',request_id='unique-request',comments=[dict(section='general',kind='PREFERENCE',text='Less generic.'),dict(section='meaning',kind='HYPOTHESIS',text='Investigate character choices.')])
  rid=agent.begin(self.s,[self.ids[0]],revision=True,feedback=value)
  self.assertEqual(agent.begin(self.s,[self.ids[0]],revision=True,feedback=value),rid)
  self.assertEqual(len(editorial.listing(self.s)['comments']),2)
  calls=[]
  def call(packet,cfg):
   calls.append(packet)
   result,usage=self.call(packet,cfg);result['feedback_response']='Made the interpretation specific; audience appeal remains untested.';return result,usage
  agent.execute(self.tmp.name,rid,self.fetch,call)
  agent.execute(self.tmp.name,rid,self.fetch,call)
  self.assertEqual(len(calls),1)
  self.assertEqual(calls[0]['revision']['comments'][0]['section'],'general')

 def test_whole_feedback_stale_and_busy_save_nothing(self):
  self.run_agent([self.ids[0]])
  old=findings.listing(self.s,'live')[0]
  value=dict(finding_id=old['id'],author='Editor',request_id='test',comments=[dict(section='general',kind='PREFERENCE',text='Make it specific.')])
  rid=agent.begin(self.s,[self.ids[0]])
  with self.assertRaises(Invalid):agent.begin(self.s,[self.ids[0]],revision=True,feedback=value)
  self.assertEqual(editorial.listing(self.s)['comments'],[])
  agent.initialize(self.s,recover=True)
  findings.save(self.s,dict(old,base_version=old['version'],inspection_confirmed=True))
  with self.assertRaises(Invalid):agent.begin(self.s,[self.ids[0]],revision=True,feedback=value)
  self.assertEqual(editorial.listing(self.s)['comments'],[])

 def test_provider_migration_preserves_keys_and_pins_queued_run(self):
  with patch.dict(os.environ,{'ANTHROPIC_API_KEY':'','OPENAI_API_KEY':''}):
   (self.s.dir/'research-agent.json').write_text(json.dumps({'key':'old-claude-key','model':'claude-test'}))
   self.assertEqual(agent.credentials(self.s)['key'],'old-claude-key')
   rid=agent.begin(self.s,[self.ids[0]])
   agent.setup(self.s,{'provider':'openai','key':'openai-test-key','model':'gpt-4.1'})
   self.assertEqual(agent.credentials(self.s)['provider'],'openai')
   self.assertEqual(agent.credentials(self.s,'anthropic')['key'],'old-claude-key')
   seen=[]
   def call(packet,cfg):seen.append(cfg);return self.call(packet,cfg)
   agent.execute(self.tmp.name,rid,self.fetch,call)
   self.assertEqual(seen[0]['provider'],'anthropic');self.assertEqual(seen[0]['model'],'claude-test')
   agent.setup(self.s,{'provider':'anthropic','key':'','model':'claude-test'})
   self.assertEqual(agent.credentials(self.s,'openai')['key'],'openai-test-key')
   public=json.dumps(agent.state(self.s));self.assertNotIn('old-claude-key',public);self.assertNotIn('openai-test-key',public)

 def test_openai_response_adapter_and_incomplete_output(self):
  from unittest.mock import MagicMock
  cfg={'provider':'openai','key':'synthetic-secret','model':'gpt-4.1'}
  response=MagicMock();response.__enter__.return_value=response
  response.read.return_value=json.dumps({'status':'completed','output':[{'type':'message','content':[{'type':'output_text','text':'{"headline":"Synthetic"}'}]}],'usage':{'output_tokens':10}}).encode()
  with patch('urllib.request.urlopen',return_value=response) as mock:
   result,usage=agent.model_call({'evidence':{}},cfg)
   req=mock.call_args[0][0];body=json.loads(req.data)
   self.assertEqual(req.full_url,'https://api.openai.com/v1/responses');self.assertFalse(body['store']);self.assertEqual(result['headline'],'Synthetic')
   self.assertIn('json',body['input'].lower())
   self.assertEqual(json.loads(body['input'].split('\n',1)[1]),{'evidence':{}})
   response.read.return_value=b'{"status":"incomplete","output":[]}'
   with self.assertRaises(Invalid):agent.model_call({},cfg)
   response.read.return_value=b'{"status":"completed","output":[{"type":"message","content":[{"type":"refusal","refusal":"No"}]}]}'
   with self.assertRaises(Invalid):agent.model_call({},cfg)

 def test_openai_bad_request_is_not_mislabeled_as_credentials(self):
  import io,urllib.error
  err=urllib.error.HTTPError('https://api.openai.com/v1/responses',400,'Bad Request',{},io.BytesIO(b'{"error":{"message":"private input"}}'))
  with patch('urllib.request.urlopen',side_effect=err):
   with self.assertRaises(Invalid) as raised:agent.openai_call({}, {'model':'gpt-4.1','key':'synthetic-secret'})
  self.assertIn('request format',str(raised.exception))
  self.assertNotIn('private input',str(raised.exception))
  self.assertNotIn('credits',str(raised.exception))

 def test_openai_credit_error_is_actionable(self):
  import io,urllib.error
  err=urllib.error.HTTPError('https://api.openai.com/v1/responses',429,'Too Many Requests',{},io.BytesIO(b'{"error":{"code":"credit_balance_exhausted","message":"private provider text"}}'))
  with patch('urllib.request.urlopen',side_effect=err):
   with self.assertRaises(Invalid) as raised:agent.openai_call({}, {'model':'gpt-4.1','key':'synthetic-secret'})
  self.assertIn('API credits are exhausted',str(raised.exception))
  self.assertNotIn('private provider text',str(raised.exception))

 def test_new_brief_accepts_empty_optional_feedback_but_not_false_citations(self):
  value={'headline':'Test','observations':[{'text':'A stated fact','evidence_id':'source','quote':'Exact source text.'}],'meaning':'Hypothesis','rationale':'Investigate','gaps':'Missing scene evidence','next_step':'Inspect scenes','action':'WATCH','feedback_response':''}
  evidence={'id':'source','text':'Exact source text.'}
  self.assertNotIn('feedback_response',agent.validate(value,evidence))
  value['observations'][0]['quote']='Invented source text.'
  with self.assertRaises(Invalid):agent.validate(value,evidence)

 def test_exhausted_budget_rejects_before_queue_or_collection(self):
  for _ in range(agent.DAILY_CALLS):self.s.consume('research_model_calls',agent.DAILY_CALLS)
  with self.assertRaises(Invalid):agent.begin(self.s,[self.ids[0]])
  self.assertEqual(self.s.db.execute('select count(*) from research_runs').fetchone()[0],0)
  self.assertEqual(agent.allowance(self.s)['model_remaining'],0)
  self.assertEqual(agent.allowance(self.s)['pages_remaining'],agent.web_collection.DAILY_PAGES)

 def test_whole_batch_requires_enough_allowance(self):
  for _ in range(agent.DAILY_CALLS-1):self.s.consume('research_model_calls',agent.DAILY_CALLS)
  with self.assertRaises(Invalid):agent.begin(self.s,self.ids)
  self.assertEqual(self.s.db.execute('select count(*) from research_runs').fetchone()[0],0)
