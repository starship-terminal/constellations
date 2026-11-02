#!/usr/bin/env python3
"""The /api/ server for the deployed docs site.

`catalog.py serve` already answers /api/ for local browsing, but on the
deployment host `deploy.sh` owns the site build and nginx serves site/
statically — this process exists only to answer the /api/ routes nginx
proxies to it:

    GET  /api/status          GET  /api/redeploy*   POST /api/provider/test
    POST /api/chat

(*redeploy is answered by the separate trigger service, not here.)

nginx keeps its longer /api/redeploy location and adds, roughly:

    location /api/ {
        proxy_pass http://127.0.0.1:8190;
        proxy_set_header Host $http_host;
    }

`proxy_set_header Host $http_host` is required: the origin check in server.py
compares the browser's Origin against Host, and without it every call 403s.
It must be $http_host, not $host — $host drops the port while Origin keeps
it, so on https://host:8108 the guard would still reject its own gallery.

The repo clone's root .env is loaded the same way the refero tools load it,
so ANTHROPIC_API_KEY on the host gives every browser on the tailnet a working
chat with no per-browser setup. Every request re-loads the agent modules, so
a `git pull` by deploy.sh updates the API with no restart of this unit.
"""
from __future__ import annotations

import argparse
import http.server
import importlib.util
import sys
from pathlib import Path

_HERE = Path(__file__).resolve()
ROOT = _HERE.parents[2]


def _dotenv() -> None:
    spec = importlib.util.spec_from_file_location(
        "refero_media", ROOT / "tools" / "refero" / "refero_media.py")
    spec.loader.exec_module(importlib.util.module_from_spec(spec))


def _server():
    spec = importlib.util.spec_from_file_location(
        "agent_server", _HERE.parent / "server.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "designs-api/1"

    def do_GET(self) -> None:
        if not _server().handle_get(self):
            self.send_error(404)

    def do_POST(self) -> None:
        if not _server().handle_post(self):
            self.send_error(404)

    def log_message(self, fmt: str, *args) -> None:
        print(f"[api] {self.address_string()} {fmt % args}", file=sys.stderr, flush=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8190)
    # 127.0.0.1 for local use. nginx in the deployment's container reaches the
    # host over the docker gateway, which is not loopback — pass --host with
    # that bridge IP there so nothing else on the network can call the API.
    parser.add_argument("--host", default="127.0.0.1")
    args = parser.parse_args()
    _dotenv()
    with http.server.ThreadingHTTPServer((args.host, args.port), Handler) as httpd:
        print(f"design-systems api: http://{args.host}:{args.port}/api/", flush=True)
        httpd.serve_forever()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
