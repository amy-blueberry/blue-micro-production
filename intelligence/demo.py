"""Entirely synthetic software fixtures, never imported into the live dataset."""
import datetime as dt
from .core import parse_time


def seed(store):
    rid=store.start_run('demo')
    current=parse_time(store.clock()).replace(hour=12,minute=0,second=0)
    if current>parse_time(store.clock()):
        current-=dt.timedelta(days=1)
    for i in range(1,7):
        for days in (3,1,0):
            observed=(current-dt.timedelta(days=days)).isoformat().replace('+00:00','Z')
            store.ingest('demo',{'source_id':'synthetic-%02d'%i, 'feed_ids':[['F02'],['F04'],['F07']][(i-1)%3],
                'title':'Synthetic %s candidate %02d' % (['scripted-series','gaming','panel'][(i-1)%3],i),
                'url':None,'channel_id':'synthetic-channel-%02d'%i,'channel_name':'Demo creator %02d'%i,
                'published_at':(current-dt.timedelta(days=7)).isoformat().replace('+00:00','Z'),
                'observed_at':observed,'duration':'PT3M', 'origin':'synthetic',
                'metrics':{'views':1000*i+(3-days)*250,'likes':None if i==2 else 30*i,'comments':None if i==3 else 5*i},
                'inspection':'Synthetic software fixture; no real content inspected','series_status':'Unconfirmed demonstration record'})
    store.finish_run(rid,'COMPLETED',{'synthetic_candidates':6},[])
    return {'status':'COMPLETED','dataset':'demo','synthetic_candidates':6}
