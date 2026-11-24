"""Deterministic title discovery from saved A24/WEBTOON evidence, not story analysis."""
import hashlib
import re
import urllib.parse
from .core import Invalid, lock

VERSION='catalog-v1'

def title_url(url):
    try:
        u=urllib.parse.urlsplit(url);host=(u.hostname or '').removeprefix('www.')
        if u.scheme!='https' or u.username or u.password or u.port not in (None,443):return None
        if host=='a24films.com' and re.fullmatch(r'/(films|television)/[a-z0-9-]+/?',u.path):
            return 'https://a24films.com'+u.path.rstrip('/'), 'Film' if u.path.startswith('/films/') else 'TV series'
        if host=='webtoons.com' and re.fullmatch(r'/en/[^/]+/[^/]+/list',u.path):
            ids=urllib.parse.parse_qs(u.query).get('title_no',[])
            if len(ids)==1 and ids[0].isdigit():return 'https://www.webtoons.com'+u.path+'?title_no='+ids[0], 'Serialized comic'
    except ValueError:pass
    return None

def extract(source):
    body=source.get('captured_text','');found={}
    for m in re.finditer(r'\]\((https://[^\s)]+)\)',body):
        parsed=title_url(m.group(1))
        if not parsed:continue
        url,kind=parsed
        # Markdown cards can contain image links nested inside the outer title link.
        start=body.rfind('[![',max(0,m.start()-2500),m.start())
        if start<0:continue
        chunk=body[start:m.end()]
        # Do not associate a prior card's text with a later text-only navigation link.
        if any(title_url(u) for u in re.findall(r'\]\((https://[^\s)]+)\)',chunk[:m.start()-start])):continue
        bold=[x.strip('" ') for x in re.findall(r'\*\*([^*]+)\*\*',chunk)]
        names=[x for x in bold if not x.isdigit()]
        alt=re.search(r'\[!\[([^\]]+)\]',chunk)
        name=names[-1] if names else alt.group(1) if alt else ''
        name=re.sub(r'\s+(?:clean poster|Image)$','',name,flags=re.I).strip()
        if not name:continue
        headings=list(re.finditer(r'^#{1,3}\s+(.+)$',body[:start],re.M))
        section=headings[-1].group(1) if headings and kind=='Serialized comic' else 'Homepage promotion'
        # Strip embedded image URLs from evidence, retaining visible text and labels.
        plain=re.sub(r'!\[[^\]]*\]\([^\n]*?\)', '',chunk[:chunk.rfind('](')])
        plain=re.sub(r'[\\*_\[\]]',' ',plain)
        plain=re.sub(r'\s+',' ',plain).strip()
        genre=None
        if kind=='Serialized comic':
            path=urllib.parse.urlsplit(url).path.split('/')
            genre=path[2].replace('-',' ').title() if path[2]!='canvas' else None
        views=re.search(r'\b(\d[\d,.]*\s*[KMB]?)\s+Views\b',plain,re.I)
        rank=next((int(x) for x in bold if x.isdigit()),None)
        obs={'section':section,'displayed_position':rank,'displayed_views':views.group(1).strip() if views else None,
             'mature_label':bool(re.search(r'\bmature\b',plain,re.I)), 'excerpt':plain[:1000] or name}
        row=found.setdefault(url,{'title':name,'url':url,'kind':kind,'genre':genre,'listings':[]})
        if obs not in row['listings']:row['listings'].append(obs)
        if len(name)>len(row['title']) and names:row['title']=name
    for row in found.values():
        mature=any(o['mature_label'] for o in row['listings'])
        row['age_status']='MATURE_LABEL_REVIEW_REQUIRED' if mature else 'AGE_SUITABILITY_UNVERIFIED'
        row['relevance_hypothesis']=('Possible serial-story reference; check character relationships and continuation mechanics.' if row['kind']=='Serialized comic' else 'Possible craft reference; inspect the title synopsis and creator interviews.')
        row['limitations']=['Listing evidence only; title page and story have not been inspected.','Audience age, Roblox affinity, retention and causal success factors are not established.','Positions are copied from page context, not an independently verified trend or growth score.']
        if source.get('truncated'):row['limitations'].append('Parent capture was truncated; discovery is incomplete.')
        row['next_step']='Review the maturity label before audience-facing use.' if mature else 'Inspect the title page for premise, characters and content suitability.'
    return list(found.values())

def process(store,cid,apply=False):
    with lock(store.dir/'worker.lock'):
        parent=store.get(cid);source=parent['latest']
        if source.get('origin')!='firecrawl' or not source.get('captured_text'):raise Invalid('Choose a saved website capture with readable text.')
        host=(urllib.parse.urlsplit(source.get('url','')).hostname or '').removeprefix('www.')
        if host not in ('a24films.com','webtoons.com'):raise Invalid('Title extraction currently supports A24 and WEBTOON captures.')
        rows=extract(source);ids=[]
        if apply:
            for row in rows:
                identity='title:'+hashlib.sha256((source['feed_ids'][0]+'|'+row['url']).encode()).hexdigest()
                item=dict(row,source_id=identity,feed_ids=source['feed_ids'],origin='catalog_title',record_type='title',
                    channel_name='WEBTOON' if host=='webtoons.com' else 'A24',channel_id='',published_at=None,
                    observed_at=source['observed_at'],metrics={'views':None,'likes':None,'comments':None},
                    parent_candidate_id=cid,discovered_on=source['url'],registry_source_id=source.get('registry_source_id'),
                    extraction_version=VERSION,inspection='Title listing extracted; no episode watched or read.',
                    series_status='Bumpp relevance is a hypothesis; requires editorial investigation.')
                ids.append(store.ingest('live',item))
        return {'titles':rows,'candidate_ids':ids,'count':len(rows),'parent_truncated':bool(source.get('truncated')),'parent_url':source['url']}
