import datetime as dt
import json
import os
import tempfile
import unittest
from unittest.mock import patch
from intelligence.store import Store
from intelligence import sources, feeds, web_collection as web
from intelligence.core import Invalid

class WebsiteTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.now='2026-11-23T12:00:00Z'
        self.store=Store(self.tmp.name,clock=lambda:self.now)
        sources.initialize(self.store)
        self.a=sources.save(self.store,{'name':'Test page','url':'https://a24films.com/films/test','kind':'Creative reference','feed_id':'F01','active':True})
        self.b=sources.save(self.store,{'name':'Second test','url':'https://a24films.com/films/second','kind':'Creative reference','feed_id':'F01','active':True})
        self.key=patch.dict(os.environ,{'FIRECRAWL_API_KEY':'synthetic-test-key'});self.key.start()
    def tearDown(self):self.key.stop();self.store.close();self.tmp.cleanup()
    def page(self,url,key):return {'markdown':'Synthetic fixture content. '*10,'metadata':{'title':'Fixture','sourceURL':url,'statusCode':200}}
    def test_preview_then_save_is_idempotent_and_keeps_provenance(self):
        p=web.run(self.store,[self.a],self.page)
        self.assertEqual(self.store.list('live'),[])
        result=web.save_preview(self.store,p['id'],[self.a]);web.save_preview(self.store,p['id'],[self.a])
        rows=self.store.list('live');self.assertEqual(len(rows),1);self.assertEqual(len(rows[0]['observations']),1)
        self.assertEqual(rows[0]['latest']['origin'],'firecrawl');self.assertIsNone(rows[0]['latest']['published_at'])
        self.assertEqual(rows[0]['latest']['registry_source_id'],self.a)
        self.assertIn('Website text',rows[0]['measurement_note'])
        self.assertEqual(json.loads(self.store.db.execute('SELECT counts FROM runs').fetchone()[0])['saved_to_inbox'],1)
        self.assertEqual(web.history(self.store)[0]['results'][0]['saved_candidate_id'],result['candidate_ids'][0])
    def test_private_key_is_not_returned_and_youtube_does_not_refresh_web_pages(self):
        import stat
        from intelligence.youtube import collect
        from intelligence.core import config
        with patch.dict(os.environ,{'FIRECRAWL_API_KEY':''}):
            response=web.save_credential(self.store,'synthetic-private-key')
        self.assertNotIn('synthetic-private-key',json.dumps(response))
        self.assertEqual(stat.S_IMODE((self.store.dir/'firecrawl-key').stat().st_mode),0o600)
        p=web.run(self.store,[self.a],self.page);web.save_preview(self.store,p['id'],[self.a])
        settings=config(self.store.dir);settings.update(live_collection_enabled=True,scripted_queries=[],gaming_queries=[],rising_game_terms=[])
        calls=[]
        collect(self.store,settings,lambda *args:calls.append(args),key='test')
        self.assertFalse(calls);self.assertEqual(len(self.store.list('live')),1)

    def test_partial_failure_and_failed_item_cannot_be_saved(self):
        def fetch(url,key):
            if 'second' in url:raise Invalid('Unavailable')
            return self.page(url,key)
        p=web.run(self.store,[self.a,self.b],fetch);self.assertEqual(p['status'],'PARTIAL')
        with self.assertRaises(Invalid):web.save_preview(self.store,p['id'],[self.a,self.b])
        self.assertEqual(self.store.list('live'),[])
    def test_missing_key_limits_archived_and_unsupported_no_requests(self):
        with patch.dict(os.environ,{'FIRECRAWL_API_KEY':''}):
            with self.assertRaisesRegex(Invalid,'Connect Firecrawl'):web.run(self.store,[self.a],self.page)
        self.assertEqual(self.store.db.execute('SELECT count(*) FROM runs').fetchone()[0],0)
        with self.assertRaises(Invalid):web.run(self.store,[self.a]*4,self.page)
        for url in ['https://127.0.0.1','https://a24films.com.evil.test','https://a24films.com/login','https://a24films.com/?secret=x','https://a24films.com:444/']:
            s=next(x for x in sources.listing(self.store) if x['id']==self.a)
            self.assertTrue(web.eligibility(dict(s,url=url),feeds.listing(self.store)))
        s=next(x for x in sources.listing(self.store) if x['id']==self.a);sources.save(self.store,dict(s,active=False))
        with self.assertRaises(Invalid):web.run(self.store,[self.a],self.page)
    def test_budget_expiry_and_redirect_rejection(self):
        def bad(url,key):return {'markdown':'x'*100,'metadata':{'url':'https://127.0.0.1/private'}}
        self.assertEqual(web.run(self.store,[self.a],bad)['status'],'FAILED')
        for _ in range(9):web.run(self.store,[self.a],self.page)
        called=[]
        p=web.run(self.store,[self.a],lambda *x:called.append(x));self.assertEqual(p['status'],'FAILED');self.assertFalse(called)
        self.now='2026-11-25T12:00:00Z';self.store.purge();self.assertEqual(web.history(self.store),[])

if __name__=='__main__':unittest.main()
