"""Loopback-only, single-user review desk. Not a public deployment server."""
import json
import re
import secrets
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from .core import COHORTS, Invalid, REPO, ROOT, ROUTES, WEIGHTS, config, now
from .store import Store
from .frameworks import listing as framework_list
from . import web_collection, findings, research_agent

STATIC={'/':'index.html','/app.js':'app.js','/style.css':'style.css'}
TYPES={'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8'}

def brief_markdown(brief):
    def clean(value):
        return str(value).replace('\r',' ').replace('\n',' ').replace('<','&lt;').replace('>','&gt;')
    lines=['# Secret Sauce '+brief['kind']+' brief', '', '**Dataset: '+brief['dataset'].upper()+'** · '+brief['period'], '', brief['note'], '']
    if brief['dataset']=='demo':lines+=['**SYNTHETIC SOFTWARE DEMONSTRATION — not market findings.**','']
    if not brief['items']:lines+=['No new reviewed findings in this brief.','']
    for item in brief['items']:
        source=item['latest'];decision=item['decision']
        lines+=['## '+clean(source['title']),'', 'Source: '+clean(source.get('url') or 'Synthetic fixture'),
            'Observed: '+clean(source['observed_at']), 'Inspection: '+clean(source['inspection']),
            'Route: '+decision['route']+' (recommendation only; no execution authorized)',
            'Primary cohort: '+clean(decision['primary_cohort'] or 'Unassigned'),
            'Reviewer rationale: '+clean(decision['rationale']),
            'Confidence: '+clean(decision['confidence'])+'; sample: '+clean(decision['sample_size_note']),
            'Rights: '+decision['rights_status'],'']
        for kind,assessment in decision['assessment'].items():
            lines.append('- '+kind+': '+('Incomplete' if assessment['total'] is None else str(assessment['total'])+'/100')+'; '+clean(assessment['rationale']))
        lines+=['']
    lines+=['Source data may expire or change. Do not retain API-data exports beyond applicable storage limits.']
    return '\n'.join(lines)

def make_server(data_dir,port=8765):
    from .frameworks import initialize as init_frameworks
    initial=Store(data_dir);init_frameworks(initial);research_agent.initialize(initial,recover=True);initial.close()
    token=secrets.token_urlsafe(32)
    class Handler(BaseHTTPRequestHandler):
        def log_message(self,*args):
            pass  # No URLs, notes, credentials or request bodies in access logs.

        def respond(self,status,body,ctype='application/json; charset=utf-8',download=None):
            payload=json.dumps(body,ensure_ascii=False).encode() if ctype.startswith('application/json') else body if isinstance(body,bytes) else body.encode()
            self.send_response(status)
            self.send_header('Content-Type',ctype)
            self.send_header('Content-Length',str(len(payload)))
            self.send_header('Cache-Control','no-store')
            self.send_header('X-Content-Type-Options','nosniff')
            self.send_header('Referrer-Policy','no-referrer')
            self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
            if download:self.send_header('Content-Disposition','attachment; filename="'+download+'"')
            self.end_headers();self.wfile.write(payload)

        def permitted(self,mutate=False):
            allowed='127.0.0.1:'+str(self.server.server_port)
            if self.headers.get('Host') != allowed:
                self.respond(403,{'error':'Open this local desk using its 127.0.0.1 address.'});return False
            origin=self.headers.get('Origin')
            if origin and origin!='http://'+allowed:
                self.respond(403,{'error':'Cross-origin access is blocked.'});return False
            if mutate and not secrets.compare_digest(self.headers.get('X-Desk-Token',''),token):
                self.respond(403,{'error':'Refresh the desk before submitting a change.'});return False
            return True

        def do_GET(self):
            if not self.permitted():return
            path=urllib.parse.urlsplit(self.path)
            if path.path in STATIC:
                file=ROOT/'static'/STATIC[path.path]
                return self.respond(200,file.read_bytes(),TYPES[file.suffix])
            store=Store(data_dir)
            try:
                store.purge()
                if path.path=='/api/state':
                    dataset=urllib.parse.parse_qs(path.query).get('dataset',['demo'])[0]
                    if dataset not in ['demo','live']:raise Invalid('Invalid dataset.')
                    cfg=config(store.dir)
                    runs=[dict(r) for r in store.db.execute('SELECT * FROM runs WHERE dataset=? ORDER BY started_at DESC,rowid DESC LIMIT 20',(dataset,))]
                    for r in runs:
                        r['counts']=json.loads(r['counts']);r['errors']=json.loads(r['errors'])
                    from .sources import listing
                    sources=listing(store)
                    from .feeds import listing as feed_list
                    registry={'feeds':feed_list(store)}
                    self.respond(200,{'csrf':token,'dataset':dataset,'candidates':store.list(dataset),'runs':runs,
                        'briefs':[dict(r) for r in store.db.execute('SELECT * FROM briefs WHERE dataset=? ORDER BY created_at DESC',(dataset,))],
                        'findings':findings.listing(store,dataset),
                        'research_agent':research_agent.state(store),
                        'website_collection':web_collection.readiness(store),
                        'collection_previews':web_collection.history(store),
                        'frameworks':framework_list(store),
                        'registry_imports':[dict(r) for r in store.db.execute('SELECT digest,created_at,report FROM registry_imports ORDER BY created_at DESC')],
                        'performance_records':store.db.execute('SELECT count(*) FROM first_party_outcomes').fetchone()[0],
                        'sources':sources,'authority_panel':json.loads((REPO/'docs/production-engine/authority_panel.json').read_text())['panel'],'cohorts':COHORTS,'routes':ROUTES,'weights':WEIGHTS,'feeds':registry['feeds'],
                        'settings':{'live_enabled':cfg['live_collection_enabled'],'model_enabled':cfg['model']['enabled'],
                            'panel_configured':len(cfg['authority_channels']),'max_daily_requests':cfg['max_requests_per_day'],
                            'scheduler':'Not installed; explicit foreground worker available','production_authorized':False},
                        'now':now()})
                elif re.fullmatch(r'/api/candidate/[a-f0-9]{24}',path.path):
                    self.respond(200,store.get(path.path.rsplit('/',1)[-1]))
                elif re.fullmatch(r'/api/brief/[a-f0-9]{24}(?:/export)?',path.path):
                    bid=path.path.split('/')[3];brief=store.brief_view(bid)
                    if path.path.endswith('/export'):
                        self.respond(200,brief_markdown(brief),'text/markdown; charset=utf-8','secret-sauce-'+brief['kind']+'-'+brief['period']+'.md')
                    else:self.respond(200,brief)
                else:self.respond(404,{'error':'Not found.'})
            except Invalid as exc:self.respond(400,{'error':str(exc)})
            except Exception:self.respond(500,{'error':'Local desk error. Check configuration and run the tests; no private details logged.'})
            finally:store.close()

        def do_POST(self):
            if not self.permitted(True):return
            if self.headers.get('Content-Type','').split(';')[0]!='application/json':
                return self.respond(415,{'error':'JSON required.'})
            try:length=int(self.headers.get('Content-Length','0'))
            except ValueError:return self.respond(400,{'error':'Invalid request size.'})
            if length<1 or length>65536:return self.respond(413,{'error':'Request too large or empty.'})
            store=Store(data_dir)
            try:
                value=json.loads(self.rfile.read(length));store.purge()
                if not isinstance(value,dict):raise Invalid('Expected a JSON object.')
                path=urllib.parse.urlsplit(self.path).path
                if path=='/api/research/start':
                    rid=research_agent.begin(store,value.get('candidate_ids'))
                    research_agent.launch(data_dir,rid)
                    result={'id':rid,'status':'RUNNING'}
                elif path=='/api/research/connect':
                    result=research_agent.setup(store,value)
                elif path=='/api/finding/review':
                    result=research_agent.review(store,value)
                elif path=='/api/finding':
                    result={'id':findings.save(store,value)}
                elif path=='/api/collection/extract':
                    from .title_extraction import process
                    result=process(store,value.get('candidate_id'),apply=value.get('save') is True)
                elif path=='/api/connection/firecrawl':
                    result=web_collection.save_credential(store,value.get('key'))
                elif path=='/api/collection/test':
                    result=web_collection.run(store,value.get('source_ids'))
                elif path=='/api/collection/save':
                    result=web_collection.save_preview(store,value.get('preview_id'),value.get('source_ids'))
                    from .title_extraction import process
                    titles=[]
                    for cid in result['candidate_ids']:
                        host=(urllib.parse.urlsplit(store.get(cid)['latest']['url']).hostname or '').removeprefix('www.')
                        if host in ('a24films.com','webtoons.com'):
                            titles.extend(process(store,cid,apply=True)['candidate_ids'])
                    result['title_ids']=titles
                elif path=='/api/framework':
                    from .frameworks import save
                    result={'id':save(store,value)}
                elif path=='/api/framework/approve':
                    from .frameworks import approve
                    result={'id':approve(store,value)}
                elif path=='/api/feed':
                    from .feeds import save as save_feed
                    result={'id':save_feed(store,value)}
                elif path=='/api/source':
                    from .sources import initialize, save
                    initialize(store)
                    result={'id':save(store,value)}
                elif path=='/api/demo':
                    from .demo import seed
                    result=seed(store)
                elif path=='/api/collect':
                    from .youtube import collect
                    result=collect(store)
                elif path=='/api/brief':
                    if value.get('dataset') not in ['demo','live']:raise Invalid('Invalid dataset.')
                    result=store.brief(value['dataset'],value.get('kind','daily'))
                elif path=='/api/note':result={'id':store.add_note(value.get('candidate_id'),value)}
                elif path=='/api/decision':result={'id':store.decide(value.get('candidate_id'),value)}
                elif path=='/api/analyze':
                    from .agents import analyze
                    result={'id':analyze(store,value.get('candidate_id'))}
                elif path=='/api/delete':
                    store.delete(value.get('candidate_id'));result={'deleted':True}
                else:return self.respond(404,{'error':'Not found.'})
                self.respond(200,result)
            except (Invalid,ValueError,TypeError) as exc:
                self.respond(400,{'error':str(exc) if isinstance(exc,Invalid) else 'Invalid request.'})
            except Exception:
                self.respond(500,{'error':'Operation failed. No private details logged; inspect the run status before retrying.'})
            finally:store.close()
    return ThreadingHTTPServer(('127.0.0.1',port),Handler)

def serve(data_dir,port):
    server=make_server(data_dir,port)
    print('Secret Sauce desk: http://127.0.0.1:%s — local only; no scheduler installed.'%server.server_port,flush=True)
    try:server.serve_forever()
    except KeyboardInterrupt:pass
    finally:server.server_close()
