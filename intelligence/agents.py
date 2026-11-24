import hashlib
import json
import os
import urllib.error
import urllib.request
from .core import COHORTS, Invalid, ROOT, config, lock, text


def validate_output(value, notes):
    if not isinstance(value,dict) or set(value)!= {'summary','primary_cohort','hypotheses','limitations','recommended_action'}:
        raise Invalid('Model output did not match the review contract.')
    text(value['summary'],'model summary',1200)
    if value['primary_cohort'] not in COHORTS+[None]:
        raise Invalid('Invalid cohort hypothesis.')
    if value['recommended_action'] not in ['WATCH','INVESTIGATE','RIGHTS_REVIEW']:
        raise Invalid('Model cannot authorize development or execution.')
    if not isinstance(value['hypotheses'],list) or len(value['hypotheses'])>4:
        raise Invalid('Invalid hypothesis list.')
    refs = {n['id']:n['text'] for n in notes}
    for h in value['hypotheses']:
        if not isinstance(h,dict) or set(h)!= {'text','evidence_id','quote'}:
            raise Invalid('Invalid hypothesis evidence.')
        text(h['text'],'hypothesis',600)
        quote=text(h['quote'],'supporting quote',240)
        if h['evidence_id'] not in refs or quote not in refs[h['evidence_id']]:
            raise Invalid('Model cited nonexistent evidence or an unsupported quote.')
    if not isinstance(value['limitations'],list) or not 1<=len(value['limitations'])<=8:
        raise Invalid('Model must state its limitations.')
    for limitation in value['limitations']:
        text(limitation,'limitation',400)
    return value


def call_model(settings, notes, api_key):
    prompt=(ROOT/'prompts/reviewer.txt').read_text()
    # Deliberately omit API metadata, metrics, URLs, other candidates and private files.
    body={'model':settings['name'],'max_tokens':settings['max_output_tokens'], 'stream':False,
          'system':prompt,'messages':[{'role':'user','content':json.dumps({'editorial_notes':notes},ensure_ascii=False)}]}
    request=urllib.request.Request('https://api.anthropic.com/v1/messages',data=json.dumps(body).encode(),headers={
        'Authorization':'Bearer '+api_key, 'anthropic-version':settings['api_version'], 'Content-Type':'application/json'})
    try:
        with urllib.request.urlopen(request,timeout=60) as response:
            raw=response.read(2_000_001)
        if len(raw)>2_000_000:
            raise Invalid('Model response exceeded size limit.')
        response=json.loads(raw)
        if response.get('stop_reason')!='end_turn':
            raise Invalid('Model response was incomplete; no assessment saved.')
        content=''.join(x.get('text','') for x in response.get('content',[]) if x.get('type')=='text')
        return json.loads(content), response.get('usage',{}), response.get('id')
    except urllib.error.HTTPError as exc:
        raise Invalid('Model HTTP %s. No automatic paid retry.' % exc.code) from None
    except (urllib.error.URLError, TimeoutError, OSError):
        raise Invalid('Model request failed or timed out. Call allowance remains consumed; no automatic paid retry.') from None
    except (ValueError,TypeError):
        raise Invalid('Model returned invalid JSON; no assessment saved.') from None


def analyze(store,cid,settings=None,caller=None):
    settings=settings or config(store.dir)
    candidate=store.get(cid)
    notes=[{k:n[k] for k in ['id','text','coverage','evidence_type','access_basis']} for n in candidate['notes'] if n['analysis_allowed']]
    if not notes:
        raise Invalid('Add an editorial note and explicitly allow its analysis first.')
    with lock(store.dir/'model.lock'):
        # Rules-only check is a real non-model fallback, never labeled as AI analysis.
        if not settings['model']['enabled']:
            output={'summary':'Editorial evidence is ready for review. No model interpretation has been generated.',
                    'primary_cohort':None,'hypotheses':[], 'limitations':['Human review required; notes are not independently verified.','AI disabled. No episode viewing, audience inference or scoring performed.'],
                    'recommended_action':'WATCH'}
            method='RULES_ONLY';usage={};provider_id=None
        else:
            key=os.environ.get('ANTHROPIC_API_KEY')
            if not key and caller is None:
                raise Invalid('ANTHROPIC_API_KEY is not configured. No model call was sent.')
            if len(json.dumps(notes).encode())>24000:
                raise Invalid('Editorial packet exceeds the 24 KB input cap. Narrow the notes first.')
            store.consume('model_calls',settings['model']['max_calls_per_day'])
            output,usage,provider_id=(caller or call_model)(settings['model'],notes,key)
            output=validate_output(output,notes)
            method='MODEL_DRAFT'
        result={'method':method,'result':output,'note_ids':[n['id'] for n in notes],
                'input_hash':hashlib.sha256(json.dumps(notes,sort_keys=True).encode()).hexdigest(),
                'prompt_hash':hashlib.sha256((ROOT/'prompts/reviewer.txt').read_bytes()).hexdigest(),
                'model':settings['model']['name'] if method=='MODEL_DRAFT' else None,
                'usage':usage,'provider_request_id':provider_id,'human_approved':False}
        return store.save_analysis(cid,result)
