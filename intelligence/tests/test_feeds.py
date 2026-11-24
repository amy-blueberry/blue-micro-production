import tempfile
import unittest
from intelligence.store import Store
from intelligence.feeds import listing, save
from intelligence.sources import listing as sources, save as save_source
from intelligence.core import Invalid

class FeedTests(unittest.TestCase):
    def test_create_edit_archive_restore_and_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Store(tmp);self.assertEqual(len(listing(db)),10);sources(db)
            f=dict(listing(db)[0]);f.pop('id');f['name']='Test research';sid=save(db,f)
            f=next(x for x in listing(db) if x['id']==sid)
            source={'name':'Test','url':'https://example.com','kind':'Creative reference','feed_id':sid,'active':True}
            source_id=save_source(db,source)
            old=dict(f);f['active']=False;save(db,f)
            with self.assertRaises(Invalid):save(db,old)
            with self.assertRaises(Invalid):save_source(db,dict(source,url='https://example.org'))
            save_source(db,dict(source,id=source_id,notes='Existing link remains editable'))
            db.close();db=Store(tmp)
            f=next(x for x in listing(db) if x['id']==sid);self.assertFalse(f['active'])
            self.assertEqual(len(listing(db)),11);f['active']=True;save(db,f)
            save_source(db,dict(source,url='https://example.org'));db.close()
    def test_rejects_duplicates_invalid_links_and_keeps_seed_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Store(tmp);f=dict(listing(db)[0]);original=dict(f)
            f['entry_points']=['javascript:alert(1)']
            with self.assertRaises(Invalid):save(db,f)
            f=dict(original);f.pop('id')
            with self.assertRaises(Invalid):save(db,f)
            f=dict(original);f['name']='Updated research';save(db,f)
            saved=listing(db)[0];self.assertEqual(saved['collect_fields'],original['collect_fields'])
            self.assertEqual(saved['activation_state'],'NOT_CONNECTED');db.close()
