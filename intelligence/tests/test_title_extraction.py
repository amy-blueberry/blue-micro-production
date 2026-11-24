import tempfile
import unittest
from intelligence.title_extraction import extract,process,title_url
from intelligence.store import Store

class TitleTests(unittest.TestCase):
    def source(self,body):
        return dict(source_id='web:test',origin='firecrawl',url='https://www.webtoons.com/en/',feed_ids=['F06'],title='Catalog',published_at=None,observed_at='2026-11-23T12:00:00Z',captured_text=body,truncated=True)
    def test_titles_and_metrics_stay_with_their_cards(self):
        body='''## Trending & Popular Series
- [![Alpha](https://img.test/a.jpg) mature **"1"** **Alpha** Romance](https://www.webtoons.com/en/romance/alpha/list?title_no=123)
- [![Beta](https://img.test/b.jpg) **"2"** **Beta** Action](https://www.webtoons.com/en/action/beta/list?title_no=124)
## Popular Series by Category
- [![Alpha](https://img.test/a.jpg) **Alpha** 2M Views](https://www.webtoons.com/en/romance/alpha/list?title_no=123)
[Buy now](https://shop.test/item)
'''
        rows=extract(self.source(body));self.assertEqual(len(rows),2)
        self.assertEqual(rows[0]['listings'][1]['displayed_views'],'2M');self.assertEqual(len(rows[0]['listings']),2)
        self.assertEqual(rows[1]['age_status'],'AGE_SUITABILITY_UNVERIFIED');self.assertEqual(rows[0]['age_status'],'MATURE_LABEL_REVIEW_REQUIRED')
        self.assertTrue(any('truncated' in x for x in rows[0]['limitations']))
    def test_a24_dedup_ignores_products_navigation_and_private_links(self):
        body='''[![Sample Film](https://a24films.com/_next/image?x=1)](https://a24films.com/films/sample)
[Buy Tickets](https://a24films.com/films/sample)
[![Sample Film clean poster](https://img.test/x) Now Playing](https://a24films.com/films/sample)
[![Mug](https://img.test/x)](https://shop.a24films.com/products/mug)
'''
        rows=extract(dict(self.source(body),url='https://a24films.com'));self.assertEqual(len(rows),1);self.assertEqual(rows[0]['title'],'Sample Film')
        for url in ['https://a24films.com.evil.test/films/x','https://a24films.com:444/films/x','http://a24films.com/films/x','https://www.webtoons.com/en/action/x/list?title_no=abc']:
            self.assertIsNone(title_url(url))
    def test_canvas_is_not_a_genre(self):
        row=extract(self.source('[![Example](https://img.test/x) **Example**](https://www.webtoons.com/en/canvas/example/list?title_no=111)'))[0]
        self.assertIsNone(row['genre'])

    def test_repeat_extraction_preserves_original_and_deduplicates(self):
        with tempfile.TemporaryDirectory() as path:
            store=Store(path,clock=lambda:'2026-11-23T12:00:00Z')
            cid=store.ingest('live',self.source('[![Alpha](https://img.test/x) **Alpha**](https://www.webtoons.com/en/romance/alpha/list?title_no=123)'))
            self.assertEqual(process(store,cid)['count'],1);self.assertEqual(len(store.list('live')),1)
            process(store,cid,True);process(store,cid,True)
            self.assertEqual(len(store.list('live')),2);self.assertEqual(store.get(cid)['latest']['title'],'Catalog')
            title=next(x for x in store.list('live') if x['id']!=cid)
            self.assertEqual(title['latest']['parent_candidate_id'],cid);self.assertEqual(len(title['observations']),1)
            self.assertIsNone(title['latest']['metrics']['views']);store.close()
