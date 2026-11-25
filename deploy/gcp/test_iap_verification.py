"""Run with the deployment venv; exercise real ES256 signatures, no real tokens."""
import time
import unittest
from unittest.mock import patch
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from google.auth import jwt
from google.auth.crypt import es256
from intelligence.cloud_auth import verify

class IAPSignatureTests(unittest.TestCase):
    def setUp(self):
        key=ec.generate_private_key(ec.SECP256R1())
        self.signer=es256.ES256Signer(key,key_id='test-key')
        self.certs={'test-key':key.public_key().public_bytes(serialization.Encoding.PEM,serialization.PublicFormat.SubjectPublicKeyInfo).decode()}
        self.audience='/projects/123/global/backendServices/456'
        self.claims={'iss':'https://cloud.google.com/iap','aud':self.audience,'sub':'test-user','email':'test@example.com','iat':int(time.time())-5,'exp':int(time.time())+300}

    def token(self,**changes):
        return jwt.encode(self.signer,dict(self.claims,**changes),header={'alg':'ES256'}).decode()

    def test_valid_and_rejected_tokens(self):
        with patch('google.oauth2.id_token._fetch_certs',return_value=self.certs):
            self.assertEqual(verify(self.token(),self.audience),'test@example.com')
            for token,aud in [(self.token(),'wrong'),(self.token(iss='wrong'),self.audience),(self.token(exp=int(time.time())-60),self.audience),('forged',self.audience)]:
                with self.assertRaises(ValueError):verify(token,aud)

if __name__=='__main__':unittest.main()
