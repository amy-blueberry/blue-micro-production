import argparse
import json
import os
import time
from pathlib import Path
from .core import Invalid, ROOT, config, now
from .store import Store


def main():
    parser=argparse.ArgumentParser(description='Secret Sauce local intelligence workbench')
    parser.add_argument('--data-dir',default=os.environ.get('BUMPP_DATA_DIR',str(ROOT.parent/'.runtime/intelligence')))
    sub=parser.add_subparsers(dest='command',required=True)
    sub.add_parser('init');sub.add_parser('doctor');sub.add_parser('demo');sub.add_parser('collect');sub.add_parser('purge')
    serve=sub.add_parser('serve');serve.add_argument('--port',type=int,default=8765)
    brief=sub.add_parser('brief');brief.add_argument('--dataset',choices=['demo','live'],default='live');brief.add_argument('--kind',choices=['daily','weekly'],default='daily')
    analysis=sub.add_parser('analyze');analysis.add_argument('candidate_id')
    worker=sub.add_parser('worker');worker.add_argument('--once',action='store_true')
    imp=sub.add_parser('import-v2');imp.add_argument('path');imp.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    store=Store(args.data_dir)
    try:
        if args.command=='import-v2':
            from .import_v2 import run
            print(json.dumps(run(store,args.path,args.apply),indent=2))
        elif args.command=='init':
            path=store.dir/'config.json'
            if not path.exists():
                path.write_text((ROOT/'config.example.json').read_text());os.chmod(path,0o600)
            print('Private configuration initialized. Live collection and model calls remain off.')
        elif args.command=='doctor':
            cfg=config(store.dir)
            print(json.dumps({'local_storage':str(store.dir),'live_collection_enabled':cfg['live_collection_enabled'],
                'youtube_key_present':bool(os.environ.get('YOUTUBE_API_KEY')),'model_enabled':cfg['model']['enabled'],
                'model_key_present':bool(os.environ.get('ANTHROPIC_API_KEY')),'verified_panel_channels':len(cfg['authority_channels']),
                'production_authorized':False,'youtube_derived_metrics':'DISABLED'},indent=2))
        elif args.command=='demo':
            from .demo import seed
            print(json.dumps(seed(store)))
        elif args.command=='purge':
            store.purge();print('Expired live data removed. No data was removed from YouTube.')
        elif args.command=='collect':
            from .youtube import collect
            print(json.dumps(collect(store),indent=2))
        elif args.command=='analyze':
            from .agents import analyze
            print(json.dumps({'analysis_id':analyze(store,args.candidate_id)}))
        elif args.command=='brief':
            store.purge();print(json.dumps(store.brief(args.dataset,args.kind),indent=2))
        elif args.command=='serve':
            from .server import serve
            path=store.dir;store.close();store=None
            serve(path,args.port)
        elif args.command=='worker':
            from .youtube import collect
            while True:
                try:
                    print(json.dumps(collect(store,scheduled=True)),flush=True)
                except Invalid as exc:
                    print(json.dumps({'at':now(),'status':'BLOCKED','reason':str(exc)}),flush=True)
                if args.once:break
                time.sleep(60)  # Explicitly launched foreground service, one attempt/day.
    except (Invalid,ValueError) as exc:
        parser.exit(2,str(exc)+'\n')
    finally:
        if store:store.close()

if __name__=='__main__':
    main()
