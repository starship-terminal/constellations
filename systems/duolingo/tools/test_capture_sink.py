"""capture/sink.py writes a dump only for a Duolingo page that knows the run's token."""
import http.client
import http.server
import importlib.util
import os
import socket
import tempfile
import threading
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('sink', os.path.join(HERE, 'capture', 'sink.py'))
sink = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sink)


class SinkTest(unittest.TestCase):
    def setUp(self):
        self.dir = tempfile.TemporaryDirectory()
        self.server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), sink.handler('t0k', self.dir.name, max_bytes=100))
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.dir.cleanup()

    def post(self, path, body=b'{}', origin='https://www.duolingo.com', token='t0k', method='POST'):
        c = http.client.HTTPConnection('127.0.0.1', self.server.server_address[1])
        h = {}
        if origin:
            h['Origin'] = origin
        if token:
            h['X-Sink-Token'] = token
        c.request(method, path, body=body if method == 'POST' else None, headers=h)
        r = c.getresponse()
        try:
            r.read()
        except ConnectionResetError:  # a refusal closes without reading the body
            pass
        c.close()
        return r

    def files(self):
        return sorted(os.listdir(self.dir.name)) if os.path.isdir(self.dir.name) else []

    def test_writes_for_duolingo_with_token(self):
        r = self.post('/learn-dark')
        self.assertEqual(r.status, 200)
        self.assertEqual(r.getheader('Access-Control-Allow-Origin'), 'https://www.duolingo.com')
        self.assertEqual(self.files(), ['learn-dark.json'])

    def test_refuses_other_origin_and_no_origin(self):
        for o in ('https://evil.example', 'https://duolingo.com.evil.example', None):
            self.assertEqual(self.post('/x', origin=o).status, 403, o)
        self.assertEqual(self.post('/x', origin='https://evil.example', method='OPTIONS').status, 403)
        self.assertEqual(self.files(), [])

    def test_refuses_bad_token(self):
        self.assertEqual(self.post('/x', token='nope').status, 403)
        self.assertEqual(self.post('/x', token=None).status, 403)
        self.assertEqual(self.files(), [])

    def test_refuses_oversize_and_bad_names(self):
        self.assertEqual(self.post('/big', body=b'x' * 101).status, 413)
        self.assertEqual(self.post('/..').status, 400)
        self.assertEqual(self.files(), [])

    def raw(self, length_line):
        with socket.create_connection(('127.0.0.1', self.server.server_address[1])) as s:
            s.sendall(('POST /x HTTP/1.1\r\nHost: 127.0.0.1\r\nOrigin: https://www.duolingo.com\r\n'
                       'X-Sink-Token: t0k\r\n' + length_line + '\r\n{}').encode())
            return s.recv(1024).split(b' ')[1]

    def test_refuses_missing_and_malformed_length(self):
        self.assertEqual(self.raw(''), b'411')
        self.assertEqual(self.raw('Content-Length: abc\r\n'), b'411')
        self.assertEqual(self.files(), [])

    def test_preflight_allows_token_header(self):
        r = self.post('/x', method='OPTIONS', token=None)
        self.assertEqual(r.status, 204)
        self.assertIn('X-Sink-Token', r.getheader('Access-Control-Allow-Headers'))


if __name__ == '__main__':
    unittest.main()
