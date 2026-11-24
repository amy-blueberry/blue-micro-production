import contextlib
import datetime as dt
import hashlib
import json
import math
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
COHORTS = ['Lore Keepers', 'Drama Girls', 'Scream Team', 'The Lobby', 'The Crossover']
ROUTES = ['WATCH', 'INVESTIGATE', 'TEST', 'DEVELOP_PILOT', 'RIGHTS_REVIEW', 'REJECT']
WEIGHTS = {
    'viral': {'momentum': 30, 'independent_adoption': 25, 'cross_platform_spread': 25, 'cohort_relevance': 20},
    'story': {'character_attachment': 30, 'relationship_stakes': 25, 'continuation': 25, 'extensibility': 20},
    'execution': {'filming_feasibility': 30, 'speed_to_test': 25, 'originality_rights': 25, 'distribution_fit': 20},
}

class Invalid(ValueError):
    pass

class Busy(Invalid):
    pass

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')

def parse_time(value):
    try:
        result = dt.datetime.fromisoformat(value.replace('Z', '+00:00'))
        if result.tzinfo is None:
            raise ValueError()
        return result.astimezone(dt.timezone.utc)
    except (ValueError, AttributeError, TypeError):
        raise Invalid('Expected an ISO timestamp with timezone.') from None

def cutoff(days=29):
    return (parse_time(now()) - dt.timedelta(days=days)).isoformat().replace('+00:00', 'Z')

def ident(*parts):
    return hashlib.sha256('|'.join(parts).encode()).hexdigest()[:24]

def text(value, name, limit=6000, optional=False):
    if optional and value in (None, ''):
        return ''
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise Invalid('%s must be nonempty text, at most %s characters.' % (name, limit))
    return value.strip()

def integer(value, name, low, high):
    if isinstance(value, bool) or not isinstance(value, int) or not low <= value <= high:
        raise Invalid('%s must be an integer from %s to %s.' % (name, low, high))
    return value

def config(data_dir):
    path = Path(data_dir) / 'config.json'
    result = json.loads((path if path.exists() else ROOT / 'config.example.json').read_text())
    for key, lo, hi in [('lookback_days', 1, 29), ('max_search_calls_per_day', 1, 100),
                        ('max_requests_per_day', 1, 500), ('results_per_query', 1, 50), ('max_tracked_items', 1, 200)]:
        integer(result.get(key), key, lo, hi)
    if type(result.get('live_collection_enabled')) is not bool:
        raise Invalid('live_collection_enabled must be true or false.')
    for key in ['scripted_queries', 'gaming_queries', 'rising_game_terms']:
        if not isinstance(result.get(key), list) or len(result[key]) > 20:
            raise Invalid('Invalid query list: ' + key)
        for q in result[key]:
            text(q, key, 120)
    channels = result.get('authority_channels')
    if not isinstance(channels, list) or len(channels) > 10:
        raise Invalid('At most ten verified authority channels are allowed.')
    seen = set()
    for ch in channels:
        if not re.fullmatch(r'UC[A-Za-z0-9_-]{22}', ch.get('channel_id', '')):
            raise Invalid('Authority entries require an exact YouTube channel ID.')
        if ch['channel_id'] in seen:
            raise Invalid('Duplicate authority channel.')
        seen.add(ch['channel_id'])
        text(ch.get('name'), 'channel name', 100)
        text(ch.get('verification_note'), 'verification note', 500)
        parse_time(ch.get('verified_at'))
        if ch.get('cadence') not in ['daily', 'three_times_weekly']:
            raise Invalid('Authority cadence must be daily or three_times_weekly.')
    model = result.get('model', {})
    if type(model.get('enabled')) is not bool:
        raise Invalid('model.enabled must be boolean.')
    integer(model.get('max_calls_per_day'), 'model daily calls', 1, 20)
    integer(model.get('max_output_tokens'), 'model output tokens', 100, 4000)
    if model['enabled']:
        text(model.get('name'), 'model name', 100)
        text(model.get('api_version'), 'API version', 20)
    return result

def private_dir(path):
    path = Path(path).expanduser().resolve()
    path.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(path, 0o700)
    return path

@contextlib.contextmanager
def lock(path):
    # Kernel releases this lock after a crash; no stale lease can buy duplicate work.
    import fcntl
    path = Path(path)
    with open(path, 'a') as file:
        os.chmod(path, 0o600)
        try:
            fcntl.flock(file, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise Busy('Another worker is running. Wait for it to finish.') from None
        try:
            yield
        finally:
            fcntl.flock(file, fcntl.LOCK_UN)

def score_assessment(value, allowed_note_ids):
    if not isinstance(value, dict) or set(value) != set(WEIGHTS):
        raise Invalid('Supply separate viral, story and execution assessments.')
    result = {}
    for kind, weights in WEIGHTS.items():
        part = value[kind]
        components = part.get('components', {})
        if set(components) != set(weights):
            raise Invalid('Incorrect components for ' + kind)
        for number in components.values():
            if number is not None and (isinstance(number, bool) or not isinstance(number, (float, int)) or not math.isfinite(number) or not 0 <= number <= 100):
                raise Invalid('Components must be finite 0–100 numbers or null.')
        evidence = part.get('evidence_ids', [])
        if not isinstance(evidence, list) or any(x not in allowed_note_ids for x in evidence):
            raise Invalid('Scores must cite current, approved-for-analysis editorial notes.')
        rationale = text(part.get('rationale', ''), 'rationale', optional=True)
        if any(v is not None for v in components.values()) and (not evidence or not rationale):
            raise Invalid('Scored components require evidence and rationale.')
        total = None if any(v is None for v in components.values()) else round(sum(components[k] * w for k, w in weights.items()) / 100, 2)
        result[kind] = {'components': components, 'evidence_ids': evidence, 'rationale': rationale, 'total': total}
    return result
