"""sink.py : the local sink extract.js POSTs its dumps to; writes dumps/<NAME>.json.

    python3 tools/capture/sink.py        prints the token to set in the page

Listens on 127.0.0.1:8765 and takes a write only from a Duolingo page (the Origin
header must be https://duolingo.com or a subdomain of it) that knows this run's
token, which it prints at start (or reads from SINK_TOKEN). Any other page the
browser has open could otherwise write files here. A dump larger than MAX_BYTES
is refused unread.
"""
import http.server, json, os, re, secrets

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dumps')
PORT = 8765
MAX_BYTES = 64 * 1024 * 1024
ORIGIN = re.compile(r'https://([a-z0-9-]+\.)*duolingo\.com')
NAME = re.compile(r'[A-Za-z0-9][A-Za-z0-9._-]{0,127}')


def handler(token, out_dir=D, max_bytes=MAX_BYTES):
    """A request handler class that writes to out_dir for requests carrying token."""

    class H(http.server.BaseHTTPRequestHandler):
        def allowed_origin(self):
            o = self.headers.get('Origin', '')
            return o if ORIGIN.fullmatch(o) else None

        def cors(self, origin):
            self.send_header('Access-Control-Allow-Origin', origin)
            self.send_header('Access-Control-Allow-Headers', 'Content-Type, X-Sink-Token')
            self.send_header('Access-Control-Allow-Methods', 'POST')
            self.send_header('Access-Control-Allow-Private-Network', 'true')
            self.send_header('Vary', 'Origin')

        def refuse(self, code, why):
            self.send_response(code)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Connection', 'close')
            self.end_headers()
            self.wfile.write(why.encode())
            self.close_connection = True

        def do_OPTIONS(self):
            origin = self.allowed_origin()
            if not origin:
                return self.refuse(403, 'origin not allowed')
            self.send_response(204)
            self.cors(origin)
            self.end_headers()

        def do_POST(self):
            origin = self.allowed_origin()
            if not origin:
                return self.refuse(403, 'origin not allowed')
            if not secrets.compare_digest(self.headers.get('X-Sink-Token', ''), token):
                return self.refuse(403, 'bad token')
            name = self.path.strip('/').replace('/', '_')
            if not NAME.fullmatch(name) or '..' in name:
                return self.refuse(400, 'bad name')
            try:
                n = int(self.headers.get('Content-Length', ''))
            except ValueError:
                return self.refuse(411, 'length required')
            if n < 0 or n > max_bytes:
                return self.refuse(413, 'too large')
            b = self.rfile.read(n)
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, name + '.json'), 'wb') as f:
                f.write(b)
            self.send_response(200)
            self.cors(origin)
            self.end_headers()
            self.wfile.write(b'ok %d' % len(b))

        def log_message(self, *a):
            pass

    return H


if __name__ == '__main__':
    token = os.environ.get('SINK_TOKEN') or secrets.token_urlsafe(16)
    print(f"sink on 127.0.0.1:{PORT}; in the page run: const SINK_TOKEN = {json.dumps(token)};", flush=True)
    http.server.ThreadingHTTPServer(('127.0.0.1', PORT), handler(token)).serve_forever()
