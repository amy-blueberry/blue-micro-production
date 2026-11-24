import os
import tempfile
import threading
import unittest
import urllib.request
import urllib.error
from unittest.mock import patch
from intelligence import cloud_auth
from intelligence.server import make_server

class CloudAuthTests(unittest.TestCase):
    def test_incomplete_config_fails_closed(self):
        with patch.dict(os.environ, {'BUMPP_PUBLIC_ORIGIN':'https://intelligence.bumpp.gg','BUMPP_IAP_AUDIENCE':''}):
            with self.assertRaises(ValueError):cloud_auth.settings()

    def test_hosted_routes_require_verified_identity(self):
        with tempfile.TemporaryDirectory() as d, patch.dict(os.environ, {'BUMPP_PUBLIC_ORIGIN':'https://intelligence.bumpp.gg','BUMPP_IAP_AUDIENCE':'/projects/123/global/backendServices/456'}):
            server=make_server(d,0)
            thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
            url='http://127.0.0.1:'+str(server.server_port)
            try:
                self.assertEqual(urllib.request.urlopen(url+'/healthz').status,200)
                with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(url+'/')
                self.assertEqual(e.exception.code,401)
                with patch.object(cloud_auth,'verify',return_value='admin@example.com'):
                    req=urllib.request.Request(url+'/',headers={'Host':'intelligence.bumpp.gg'})
                    self.assertEqual(urllib.request.urlopen(req).status,200)
                    req=urllib.request.Request(url+'/api/state?dataset=live',headers={'Host':'intelligence.bumpp.gg'})
                    self.assertEqual(urllib.request.urlopen(req).status,200)
                    req=urllib.request.Request(url+'/',headers={'Host':'attacker.example'})
                    with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(req)
                    self.assertEqual(e.exception.code,403)
                    req=urllib.request.Request(url+'/api/research/start',data=b'{}',headers={'Host':'intelligence.bumpp.gg','Origin':'https://attacker.example','Content-Type':'application/json'})
                    with self.assertRaises(urllib.error.HTTPError) as e:urllib.request.urlopen(req)
                    self.assertEqual(e.exception.code,403)
            finally:server.shutdown();server.server_close();thread.join()
