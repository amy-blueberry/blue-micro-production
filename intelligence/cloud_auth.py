"""Fail-closed IAP authentication for the optional hosted deployment."""
import os
from urllib.parse import urlsplit


def settings():
    origin = os.environ.get('BUMPP_PUBLIC_ORIGIN', '')
    audience = os.environ.get('BUMPP_IAP_AUDIENCE', '')
    if not origin and not audience:
        return None
    parsed = urlsplit(origin)
    if not audience or parsed.scheme != 'https' or not parsed.netloc or parsed.path or parsed.query or parsed.fragment:
        raise ValueError('Hosted mode requires an HTTPS origin and IAP audience.')
    return origin, audience


def verify(assertion, audience):
    if not assertion:
        raise ValueError('Missing IAP assertion')
    from google.auth.transport.requests import Request
    from google.oauth2 import id_token
    claims = id_token.verify_token(assertion, Request(), audience=audience,
        certs_url='https://www.gstatic.com/iap/verify/public_key')
    if claims.get('iss') != 'https://cloud.google.com/iap' or not claims.get('sub') or not claims.get('email'):
        raise ValueError('Invalid IAP identity')
    return claims['email']
