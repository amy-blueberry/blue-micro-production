import re
import unicodedata
import urllib.parse
from .core import Invalid, text

def norm(value):
    value=unicodedata.normalize('NFKC',value).casefold().replace('’',"'")
    return re.sub(r'[^\w]+','',value)

def canonical(value):
    if not value:return ''
    value=text(value,'Source URL',2000)
    p=urllib.parse.urlsplit(value)
    if p.scheme!='https' or not p.hostname or p.username or p.password:raise Invalid('Invalid supplied source link.')
    host=p.hostname.lower().removeprefix('www.')
    query=urllib.parse.urlencode(sorted((k,v) for k,v in urllib.parse.parse_qsl(p.query) if not k.startswith('utm_') and k not in ['fbclid']))
    return urllib.parse.urlunsplit(('https',host,p.path.rstrip('/'),query,''))

