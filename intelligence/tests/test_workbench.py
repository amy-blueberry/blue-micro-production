import copy
import datetime as dt
import json
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from pathlib import Path
from intelligence.core import Busy, COHORTS, Invalid, WEIGHTS, config, lock, now
from intelligence.store import Store
from intelligence.demo import seed
from intelligence.agents import analyze, validate_output
from intelligence.youtube import collect
from intelligence.server import make_server

class WorkbenchTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.time='2026-11-23T20:00:00Z'
        self.store=Store(self.tmp.name,clock=lambda:self.time)
        self.cfg=config(self.tmp.name)
    def tearDown(self):
        self.store.close();self.tmp.cleanup()
    def item(self,i=1,origin='synthetic'):
        return {'source_id':('synthetic-%02d'%i if origin=='synthetic' else 'v%010d'%i), 'feed_ids':['F02'],
            'title':'Synthetic software fixture','url':None,'channel_id':'synthetic','channel_name':'Synthetic',
            'published_at':'2026-11-20T20:00:00Z','observed_at':self.time,'metrics':{'views':100,'likes':None,'comments':0},
            'origin':origin,'inspection':'Metadata only','series_status':'Unconfirmed'}
    def decision(self,route='WATCH'):
        return {'author':'Test reviewer','route':route,'primary_cohort':None,'rationale':'Software test only',
            'confidence':'Unmeasured','sample_size_note':'No real audience','rights_status':'UNREVIEWED',
            'assessment':{k:{'components':{c:None for c in weights},'rationale':'','evidence_ids':[]} for k,weights in WEIGHTS.items()}}
    def note(self,cid):
        return self.store.add_note(cid,{'author':'Test reviewer','text':'This is a synthetic editorial observation.',
            'coverage':'Software fixture only','evidence_type':'I','access_basis':'Synthetic test','analysis_allowed':True})
    def test_demo_is_idempotent_and_cannot_pollute_live(self):
        seed(self.store);seed(self.store)
        self.assertEqual(len(self.store.list('demo')),6)
        self.assertEqual(len(self.store.list('live')),0)
        self.assertEqual(len(self.store.list('demo')[0]['observations']),3)
        with self.assertRaises(Invalid):self.store.ingest('live',self.item())
    def test_missing_counts_stay_missing_and_no_derived_metrics(self):
        cid=self.store.ingest('live',self.item(origin='youtube_api'))
        row=self.store.get(cid)
        self.assertIsNone(row['latest']['metrics']['likes'])
        self.assertIsNone(row['derived_metrics'])
    def test_missing_score_not_zero_and_separate_scores(self):
        cid=self.store.ingest('demo',self.item());nid=self.note(cid)
        value=self.decision()
        for k,w in WEIGHTS.items():
            value['assessment'][k]={'components':{c:80 for c in w},'rationale':'Synthetic assessment','evidence_ids':[nid]}
        value['assessment']['viral']['components']['momentum']=None
        self.store.decide(cid,value);saved=self.store.get(cid)['decision']
        self.assertIsNone(saved['assessment']['viral']['total'])
        self.assertEqual(saved['assessment']['story']['total'],80)
        self.assertFalse(saved['execution_authorized'])
        self.assertNotIn('combined_score',saved)
    def test_score_rejects_invalid_evidence_nan_and_values(self):
        cid=self.store.ingest('demo',self.item());nid=self.note(cid)
        for number in [101,-1,float('nan'),True]:
            value=self.decision();value['assessment']['viral']['components']['momentum']=number
            value['assessment']['viral']['evidence_ids']=[nid];value['assessment']['viral']['rationale']='test'
            with self.assertRaises(Invalid):self.store.decide(cid,value)
        value=self.decision();value['assessment']['viral']['evidence_ids']=['invented']
        with self.assertRaises(Invalid):self.store.decide(cid,value)
    def test_development_route_requires_cohort_but_never_dispatches(self):
        cid=self.store.ingest('demo',self.item());value=self.decision('DEVELOP_PILOT')
        with self.assertRaises(Invalid):self.store.decide(cid,value)
        value['primary_cohort']=COHORTS[0];self.store.decide(cid,value)
        self.assertFalse(self.store.get(cid)['decision']['execution_authorized'])
    def test_briefs_cap_freeze_decision_version_and_do_not_recycle(self):
        ids=[]
        for i in range(7):
            cid=self.store.ingest('demo',self.item(i));ids.append(cid)
            value=self.decision('TEST');value['primary_cohort']=COHORTS[0];self.store.decide(cid,value)
        daily=self.store.brief('demo');weekly=self.store.brief('demo','weekly')
        self.assertEqual(len(daily['items']),5);self.assertEqual(len(weekly['items']),3)
        chosen=daily['items'][0];new=self.decision('REJECT');self.store.decide(chosen['id'],new)
        self.assertEqual(self.store.brief_view(daily['id'])['items'][0]['decision']['route'],'TEST')
        self.assertEqual(self.store.brief('demo')['id'],daily['id'])
        self.time='2026-11-24T20:00:00Z';next_day=self.store.brief('demo')
        self.assertEqual(len(next_day['items']),2)
        self.assertFalse({x['id'] for x in daily['items']} & {x['id'] for x in next_day['items']})
    def test_purge_cascades_evidence_decisions_and_brief_membership(self):
        cid=self.store.ingest('live',self.item(origin='youtube_api'));self.note(cid);self.store.decide(cid,self.decision());brief=self.store.brief('live')
        self.time='2026-12-24T20:00:00Z';self.store.purge()
        self.assertEqual(self.store.list('live'),[]);self.assertEqual(self.store.brief_view(brief['id'])['items'],[])
        self.assertEqual(self.store.db.execute('SELECT count(*) FROM notes').fetchone()[0],0)
    def test_disabled_collector_still_purges_expired_records(self):
        self.store.ingest('live',self.item(origin='youtube_api'))
        self.time='2026-12-24T20:00:00Z'
        with self.assertRaises(Invalid):collect(self.store,self.cfg)
        self.assertEqual(self.store.list('live'),[])
    def test_budgets_are_persistent_and_roll_over(self):
        self.store.consume('test',1)
        with self.assertRaises(Invalid):self.store.consume('test',1)
        other=Store(self.tmp.name,clock=lambda:self.time)
        with self.assertRaises(Invalid):other.consume('test',1)
        other.close();self.time='2026-11-24T20:00:00Z';self.store.consume('test',1)
    def test_process_lock_prevents_overlap(self):
        with lock(Path(self.tmp.name)/'test.lock'):
            with self.assertRaises(Busy):
                with lock(Path(self.tmp.name)/'test.lock'):pass
    def test_live_off_or_missing_key_makes_no_network_call(self):
        calls=[]
        with self.assertRaises(Invalid):collect(self.store,self.cfg,transport=lambda *a:calls.append(a),key='test')
        self.assertEqual(calls,[])
    def fake_transport(self,resource,params):
        vid='v0000000001';channel='UC'+'x'*22
        if resource=='search':return {'items':[{'id':{'videoId':vid},'snippet':{'channelId':channel}}]}
        return {'items':[{'id':vid,'snippet':{'title':'Synthetic API fixture','channelId':channel,'channelTitle':'Test','publishedAt':'2026-11-20T12:00:00Z'},'statistics':{'viewCount':'100'},'contentDetails':{'duration':'PT1M'}}]}
    def test_collector_deduplicates_panel_and_preserves_missing_metrics(self):
        self.cfg.update(live_collection_enabled=True,scripted_queries=['series'],gaming_queries=['game'])
        self.cfg['authority_channels']=[{'channel_id':'UC'+'x'*22,'name':'Test','verification_note':'fixture','verified_at':self.time,'cadence':'daily'}]
        result=collect(self.store,self.cfg,self.fake_transport,key='fake',scheduled=True)
        self.assertEqual(result['status'],'COMPLETED');self.assertEqual(len(self.store.list('live')),1)
        latest=self.store.list('live')[0]['latest']
        self.assertEqual(latest['feed_ids'],['F02','F07']);self.assertIsNone(latest['metrics']['comments'])
        self.assertEqual(collect(self.store,self.cfg,self.fake_transport,key='fake',scheduled=True)['status'],'ALREADY_ATTEMPTED')
    def test_collector_marks_failure_and_does_not_repeat_scheduled_failure(self):
        self.cfg['live_collection_enabled']=True
        def fail(*args):raise Invalid('Provider unavailable')
        result=collect(self.store,self.cfg,fail,key='fake',scheduled=True)
        self.assertEqual(result['status'],'FAILED')
        self.assertEqual(collect(self.store,self.cfg,fail,key='fake',scheduled=True)['status'],'ALREADY_ATTEMPTED')
    def test_rules_mode_not_mislabeled_as_model(self):
        cid=self.store.ingest('demo',self.item());self.note(cid);analyze(self.store,cid,self.cfg)
        row=self.store.get(cid)['analysis'];self.assertEqual(row['method'],'RULES_ONLY');self.assertFalse(row['human_approved'])
    def test_model_citations_are_verified_and_paid_retry_not_automatic(self):
        cid=self.store.ingest('demo',self.item());nid=self.note(cid)
        self.cfg['model'].update(enabled=True,name='test-model',max_calls_per_day=1)
        output={'summary':'Synthetic test','primary_cohort':None,'hypotheses':[{'text':'Test','evidence_id':nid,'quote':'invented quote'}],'limitations':['Test only'],'recommended_action':'WATCH'}
        with self.assertRaises(Invalid):analyze(self.store,cid,self.cfg,caller=lambda *a:(output,{},'fake'))
        self.assertEqual(self.store.get(cid)['analyses'],[])
        with self.assertRaises(Invalid):analyze(self.store,cid,self.cfg,caller=lambda *a:(output,{},'fake'))
    def test_model_payload_contains_only_allowed_notes(self):
        cid=self.store.ingest('demo',self.item());nid=self.note(cid)
        self.store.add_note(cid,{'author':'Test','text':'PRIVATE EXCLUDED','coverage':'test','evidence_type':'I','access_basis':'test','analysis_allowed':False})
        self.cfg['model'].update(enabled=True,name='test-model')
        def caller(settings,notes,key):
            self.assertEqual(len(notes),1);self.assertNotIn('PRIVATE EXCLUDED',json.dumps(notes));self.assertNotIn('metrics',json.dumps(notes))
            return {'summary':'Test only','primary_cohort':None,'hypotheses':[{'text':'Synthetic hypothesis','evidence_id':nid,'quote':'synthetic editorial observation'}],'limitations':['Synthetic fixture'],'recommended_action':'INVESTIGATE'},{'input_tokens':10},'fake'
        analyze(self.store,cid,self.cfg,caller=caller)
        self.assertEqual(self.store.get(cid)['analysis']['method'],'MODEL_DRAFT')

class HTTPTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.server=make_server(self.tmp.name,0)
        self.thread=threading.Thread(target=self.server.serve_forever,daemon=True);self.thread.start()
        self.base='http://127.0.0.1:'+str(self.server.server_port)
    def tearDown(self):
        self.server.shutdown();self.server.server_close();self.thread.join();self.tmp.cleanup()
    def request(self,path,body=None,headers=None):
        request=urllib.request.Request(self.base+path,data=json.dumps(body).encode() if body is not None else None,headers=headers or {})
        return urllib.request.urlopen(request,timeout=5)
    def test_ui_mutations_require_origin_and_session_token(self):
        state=json.load(self.request('/api/state'))
        with self.assertRaises(urllib.error.HTTPError) as err:self.request('/api/demo',{}, {'Content-Type':'application/json'})
        self.assertEqual(err.exception.code,403)
        with self.assertRaises(urllib.error.HTTPError):self.request('/api/demo',{}, {'Content-Type':'application/json','X-Desk-Token':state['csrf'],'Origin':'https://bad.example'})
        result=json.load(self.request('/api/demo',{}, {'Content-Type':'application/json','X-Desk-Token':state['csrf']}))
        self.assertEqual(result['dataset'],'demo')
        state=json.load(self.request('/api/state?dataset=demo'));self.assertEqual(len(state['candidates']),6)
    def test_host_guard_and_static_allowlist(self):
        with self.assertRaises(urllib.error.HTTPError) as err:self.request('/api/state',headers={'Host':'bad.example'})
        self.assertEqual(err.exception.code,403)
        with self.assertRaises(urllib.error.HTTPError) as err:self.request('/../core.py')
        self.assertEqual(err.exception.code,404)
        response=self.request('/');self.assertIn('frame-ancestors',response.headers['Content-Security-Policy']);self.assertIn(b'Intelligence desk',response.read())

if __name__=='__main__':unittest.main()
