import tempfile
import unittest
from intelligence.store import Store
from intelligence.sources import listing, save
from intelligence.core import Invalid

class SourceTests(unittest.TestCase):
    def test_seed_create_update_archive_and_persistence(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Store(tmp)
            self.assertEqual(len(listing(db)),9)
            self.assertEqual(len(listing(db)),9)
            data={'name':'Software test','url':'https://example.com/reference','kind':'Creative reference','feed_id':'F09','notes':'Test only','active':True}
            sid=save(db,data)
            with self.assertRaises(Invalid):save(db,data)
            save(db,dict(data,id=sid,active=False,name='Archived test'))
            db.close();db=Store(tmp)
            row=next(x for x in listing(db) if x['id']==sid)
            self.assertFalse(row['active']);self.assertFalse(row['monitoring'])
            self.assertEqual(row['name'],'Archived test')
            self.assertEqual(db.list('live'),[])
            db.close()
    def test_reject_unsafe_links_and_invalid_feed(self):
        with tempfile.TemporaryDirectory() as tmp:
            db=Store(tmp);listing(db)
            for url in ['javascript:alert(1)','http://example.com','https://user:password@example.com','https://localhost/']:
                with self.assertRaises(Invalid):save(db,{'name':'Bad','url':url,'kind':'Creative reference','feed_id':'F09'})
            with self.assertRaises(Invalid):save(db,{'name':'Bad','url':'https://example.com','kind':'Creative reference','feed_id':'F99'})
            self.assertEqual(len(listing(db)),9);db.close()
