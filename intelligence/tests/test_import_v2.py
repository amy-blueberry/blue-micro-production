import copy
import json
import tempfile
import unittest
from pathlib import Path
from intelligence.store import Store
from intelligence import feeds, sources, frameworks
from intelligence.import_v2 import run
from intelligence.core import Invalid

class ImportTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.db=Store(self.tmp.name)
        sources.listing(self.db);frameworks.initialize(self.db)
        self.path=Path(self.tmp.name)/'input.json'
    def tearDown(self):self.db.close();self.tmp.cleanup()
    def document(self):
        def f(id,name,kind='External research'):
            return {'feed_id':id,'feed_name':name,'kind':kind,'priority':'P1','what_should_this_feed_discover':'**Framework:** Synthetic principle.\n\n**Persistent lens:** Test only.\n\n**Live pull:** Collect test signals.', 'what_should_it_include_or_exclude':'Synthetic scope','desired_review_frequency':'Daily','starting_links':[], 'discovery_searches_hashtags':['{candidate}'] if id!='F10' else [],'communities_to_review':[]}
        def s(name,url,feed):return {'name':name,'source_link':url,'source_type':'Reference','feed':feed,'learning_objective':'Synthetic objective only','active':True,'verification_required':True}
        return {'import_mode':'upsert_preserve_existing','feeds':[f('F01','Roblox research'),f('F10','Owned learning','Internal analytics'),f('F11','A24 creative framework and emerging entertainment trends')],
            'sources':[s('Google Trends','https://trends.google.com/trends/','F03'),s('Synthetic corroboration','https://trends.google.com/trends/','F11'),s('KreekCraft','https://www.youtube.com/results?search_query=test','F07'),s('Private endpoint',None,'F10')]}
    def write(self,d):self.path.write_text(json.dumps(d))
    def test_preview_upsert_preserves_verified_url_history_and_repeat(self):
        old=sources.listing(self.db);kreek=next(x for x in old if x['name']=='KreekCraft');kreek.update(url='https://www.youtube.com/@verified-test',verification_status='VERIFIED')
        self.db.db.execute('UPDATE sources SET payload=? WHERE id=?',(json.dumps({k:v for k,v in kreek.items() if k!='id'}),kreek['id']));self.db.db.commit()
        self.write(self.document());preview=run(self.db,self.path)
        self.assertEqual(len(feeds.listing(self.db)),10);self.assertEqual(len(frameworks.listing(self.db)),0)
        result=run(self.db,self.path,True);self.assertEqual(result['sources_added'],2);self.assertEqual(result['sources_updated'],2)
        after=sources.listing(self.db);saved=next(x for x in after if x['id']==kreek['id'])
        self.assertEqual(saved['url'],kreek['url']);self.assertEqual(saved['kind'],'Creator / channel');self.assertEqual(saved['verification_status'],'VERIFIED')
        for item in old:
            self.assertIn(item['id'],{x['id'] for x in after})
        self.assertEqual(next(x for x in feeds.listing(self.db) if x['id']=='F10')['kind'],'internal')
        n=len(frameworks.listing(self.db));self.assertTrue(run(self.db,self.path,True)['already_applied']);self.assertEqual(len(frameworks.listing(self.db)),n)
        self.assertGreater(self.db.db.execute('SELECT count(*) FROM registry_history').fetchone()[0],0)
        self.assertFalse(any(x['monitoring'] for x in after))
        # Same URL may be assigned to distinct feeds; same-feed duplicates remain blocked.
        sources.save(self.db,dict(saved,name='Other',feed_id='F01',id=None))
    def test_legacy_url_keys_are_canonicalized_before_duplicate_check(self):
        source=next(x for x in sources.listing(self.db) if x['url'])
        self.db.db.execute("DELETE FROM meta WHERE key='source_url_keys_v3'")
        self.db.db.execute('UPDATE sources SET url=? WHERE id=?',(source['feed_id']+'|'+source['url'],source['id']))
        self.db.db.commit()
        sources.initialize(self.db)
        with self.assertRaises(Invalid):sources.save(self.db,dict(source,id=None))

    def test_framework_approval_survives_live_changes_and_new_import(self):
        self.write(self.document());run(self.db,self.path,True)
        proposal=next(x for x in frameworks.listing(self.db) if x['feed_id']=='F01')
        frameworks.approve(self.db,{'id':proposal['id'],'reviewer':'Test editor','rationale':'Synthetic test','evidence':'Synthetic test only'})
        self.assertNotIn('Collect test signals',proposal['content'])
        d=self.document();d['feeds'][0]['what_should_this_feed_discover']=d['feeds'][0]['what_should_this_feed_discover'].replace('Synthetic principle','Revised principle')
        self.write(d);run(self.db,self.path,True)
        versions=[v for v in frameworks.listing(self.db) if v['feed_id']=='F01']
        self.assertEqual(len(versions),2);self.assertFalse(versions[0]['approvals']);self.assertTrue(versions[1]['approvals'])
        feed=feeds.listing(self.db)[0];feed['universe']='New live research instruction';feeds.save(self.db,feed)
        self.assertEqual(len([v for v in frameworks.listing(self.db) if v['feed_id']=='F01']),2)
        self.assertEqual(self.db.db.execute('SELECT count(*) FROM first_party_outcomes').fetchone()[0],0)
    def test_invalid_mapping_rolls_back_and_f11_conflict_is_not_overwritten(self):
        before=feeds.listing(self.db)
        d=self.document();d['sources'][0]['source_type']='Unmapped';self.write(d)
        with self.assertRaises(Invalid):run(self.db,self.path,True)
        self.assertEqual(feeds.listing(self.db),before);self.assertEqual(frameworks.listing(self.db),[])
        f=dict(before[0]);f.pop('id');f['name']='Different custom research';feeds.save(self.db,f)
        self.write(self.document())
        with self.assertRaises(Invalid):run(self.db,self.path,True)
        self.assertEqual(feeds.listing(self.db)[-1]['name'],'Different custom research')
    def test_metadata_survives_admin_edit_and_long_fields_are_not_truncated(self):
        d=self.document();d['sources'][0]['learning_objective']='x'*7000;d['feeds'][0]['what_should_this_feed_discover']='x'*7000
        self.write(d);run(self.db,self.path,True)
        s=next(x for x in sources.listing(self.db) if x['name']=='Google Trends')
        sources.save(self.db,s);updated=next(x for x in sources.listing(self.db) if x['id']==s['id'])
        self.assertEqual(updated['verification_status'],'UNVERIFIED');self.assertEqual(len(updated['notes']),7000)
        f=feeds.listing(self.db)[0];feeds.save(self.db,f);self.assertEqual(len(feeds.listing(self.db)[0]['universe']),7000)

if __name__=='__main__':unittest.main()
