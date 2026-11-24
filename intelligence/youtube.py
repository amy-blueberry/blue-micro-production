"""Read-only API adapter. No scraping, downloads, inferred ages or derived metrics."""
import datetime as dt
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from .core import Invalid, config, lock, now, parse_time

class APIError(Invalid):
    pass

class YouTube:
    def __init__(self, store, settings, key, transport=None):
        self.store, self.settings, self.key = store, settings, key
        self.transport = transport or self._transport

    def _transport(self, resource, params):
        url = 'https://www.googleapis.com/youtube/v3/' + resource + '?' + urllib.parse.urlencode(dict(params, key=self.key))
        request = urllib.request.Request(url, headers={'Accept': 'application/json'})
        try:
            with urllib.request.urlopen(request, timeout=20) as response:
                raw = response.read(5_000_001)
            if len(raw) > 5_000_000:
                raise APIError('YouTube response exceeded size limit.')
            result = json.loads(raw)
            if not isinstance(result, dict) or not isinstance(result.get('items'), list):
                raise APIError('YouTube returned an unexpected response.')
            return result
        except urllib.error.HTTPError as exc:
            # Never log a request URL, API response body, or credential.
            raise APIError('YouTube HTTP %s; check access/quota in Cloud Console.' % exc.code) from None
        except (urllib.error.URLError, TimeoutError, OSError):
            raise APIError('YouTube network request failed; no automatic retry.') from None
        except (ValueError, TypeError):
            raise APIError('YouTube returned invalid JSON.') from None

    def get(self, resource, **params):
        if resource not in ['search', 'videos']:
            raise APIError('Unsupported API resource.')
        self.store.consume('youtube_requests', self.settings['max_requests_per_day'])
        if resource == 'search':
            self.store.consume('youtube_searches', self.settings['max_search_calls_per_day'])
        return self.transport(resource, params)

    def search(self, query=None, channel=None, maximum=None):
        since = parse_time(self.store.clock()) - dt.timedelta(days=self.settings['lookback_days'])
        params = {'part':'snippet', 'type':'video', 'order':'date', 'maxResults': maximum or self.settings['results_per_query'],
                  'publishedAfter':since.isoformat().replace('+00:00','Z')}
        if query:
            params['q'] = query
        if channel:
            params['channelId'] = channel
        return self.get('search', **params)['items']

    def details(self, ids):
        return self.get('videos', part='snippet,statistics,contentDetails', id=','.join(ids))['items']

def safe_count(value):
    if value is None:
        return None
    try:
        result = int(value)
        return result if result >= 0 else None
    except (ValueError, TypeError):
        return None

def collect(store, settings=None, transport=None, key=None, scheduled=False):
    store.purge()  # Cleanup also runs when collection is disabled or credentials are absent.
    settings = settings or config(store.dir)
    if not settings['live_collection_enabled']:
        raise Invalid('Live collection is off. Enable it in the private config after access is configured.')
    key = key or os.environ.get('YOUTUBE_API_KEY')
    if not key:
        raise Invalid('YOUTUBE_API_KEY is not configured. No request was sent.')
    with lock(store.dir / 'worker.lock'):
        store.purge()
        store.recover_runs()
        day = store.clock()[:10]
        if scheduled and store.db.execute('SELECT 1 FROM slots WHERE day=?',(day,)).fetchone():
            return {'status':'ALREADY_ATTEMPTED', 'day':day}
        rid = store.start_run('live')
        if scheduled:
            with store.db:
                store.db.execute('INSERT INTO slots VALUES (?,?)',(day,rid))
        client = YouTube(store, settings, key, transport)
        errors, counts = [], {'searched':0, 'refreshed':0, 'removed':0}
        found = {}
        tracked = [x for x in store.list('live') if x['latest'].get('origin')=='youtube_api'][:settings['max_tracked_items']]
        for item in tracked:
            found[item['source_id']] = set(item['latest']['feed_ids'])
        panel_ids = {x['channel_id'] for x in settings['authority_channels']}
        jobs = [('F02', q, None, None) for q in settings['scripted_queries']]
        jobs += [('F04', q, None, None) for q in settings['gaming_queries'] + settings['rising_game_terms']]
        weekday = parse_time(store.clock()).weekday()
        for member in settings['authority_channels']:
            if member['cadence']=='daily' or weekday in (0,2,4):
                jobs.append(('F07', 'roblox', member['channel_id'], 5))
        if not panel_ids:
            errors.append('F07 skipped: no verified authority channel IDs configured.')
        try:
            for feed, query, channel, maximum in jobs:
                try:
                    rows = client.search(query, channel, maximum)
                    counts['searched'] += 1
                    for row in rows:
                        vid = row.get('id',{}).get('videoId','')
                        channel_id = row.get('snippet',{}).get('channelId')
                        if not re.fullmatch(r'[A-Za-z0-9_-]{11}',vid):
                            continue
                        if feed=='F04' and channel_id in panel_ids:
                            continue
                        found.setdefault(vid, set()).add(feed)
                except Invalid as exc:
                    errors.append(str(exc))
                    break  # Avoid repeatedly hitting a quota or authorization failure.
            tracked_ids = {x['source_id'] for x in tracked}
            ids = ([v for v in found if v not in tracked_ids] + [v for v in found if v in tracked_ids])[:settings['max_tracked_items']]
            for offset in range(0,len(ids),50):
                batch = ids[offset:offset+50]
                try:
                    rows = client.details(batch)
                except Invalid as exc:
                    errors.append(str(exc))
                    break
                returned = {r.get('id') for r in rows}
                for vid in set(batch)-returned:
                    prior = next((x for x in tracked if x['source_id']==vid),None)
                    if prior:
                        store.delete(prior['id'])
                        counts['removed'] += 1
                observed = store.clock()
                for row in rows:
                    vid = row.get('id')
                    if vid not in found:
                        continue
                    snippet = row.get('snippet',{})
                    stats = row.get('statistics',{})
                    try:
                        parse_time(snippet.get('publishedAt'))
                    except Invalid:
                        errors.append('Skipped an item with missing publication time.')
                        continue
                    feeds = found[vid]
                    if snippet.get('channelId') in panel_ids:
                        feeds.discard('F04')
                    if not feeds:
                        continue
                    item = {'source_id':vid, 'feed_ids':sorted(feeds), 'title':str(snippet.get('title',''))[:1000],
                            'url':'https://www.youtube.com/watch?v='+vid,
                            'channel_id':str(snippet.get('channelId',''))[:100], 'channel_name':str(snippet.get('channelTitle',''))[:300],
                            'published_at':snippet['publishedAt'], 'observed_at':observed,
                            'duration':row.get('contentDetails',{}).get('duration'),
                            'metrics':{'views':safe_count(stats.get('viewCount')), 'likes':safe_count(stats.get('likeCount')), 'comments':safe_count(stats.get('commentCount'))},
                            'origin':'youtube_api', 'inspection':'Metadata only; no episode watched',
                            'series_status':'UNCONFIRMED: reviewer must identify series and episode order'}
                    store.ingest('live', item)
                    counts['refreshed'] += 1
            status = 'PARTIAL' if errors and counts['refreshed'] else 'FAILED' if errors else 'COMPLETED'
            store.finish_run(rid,status,counts,errors)
            return {'id':rid,'status':status,'counts':counts,'errors':errors}
        except Exception:
            store.finish_run(rid,'FAILED',counts,['Unexpected collector failure. No API response or credentials logged.'])
            raise
