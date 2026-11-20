#!/usr/bin/env python3
"""The /api/ server for the deployed docs site.

Local browsing gets /api/ from the Next.js app (`make dev`), but on the
deployment host `deploy.sh` owns the site build and nginx serves site/
statically — this process exists only to answer the /api/ routes nginx
proxies to it:

    GET  /api/status          GET  /api/redeploy*   POST /api/provider/test
    POST /api/chat            POST /api/mcp         GET /api/ds
    GET  /api/install.sh      GET/POST/DELETE /api/provider

(*redeploy is answered by the separate trigger service, not here.)

/api/mcp is the remote MCP transport: coding agents anywhere on the tailnet
connect with the URL instead of spawning server/mcp.py locally. /api/ds and
/api/install.sh bootstrap the ds CLI client for it.

nginx keeps its longer /api/redeploy location and adds, roughly:

    location /api/ {
        proxy_pass http://127.0.0.1:8190;
        proxy_set_header Host $http_host;
    }

`proxy_set_header Host $http_host` is required: the origin check in routes.py
compares the browser's Origin against Host, and without it every call 403s.
It must be $http_host, not $host — $host drops the port while Origin keeps
it, so on https://host:8108 the guard would still reject its own gallery.

routes.py also refuses a Host it does not know (DNS rebinding). Loopback, IP
literals and *.ts.net names pass; any other name the site is served under
must be listed in DESIGN_SYSTEMS_ALLOWED_HOSTS (comma-separated, `name` or
`name:port`), in the unit's environment or the clone's .env.

The repo clone's root .env is loaded the same way the refero tools load it,
so ANTHROPIC_API_KEY on the host gives every browser on the tailnet a working
chat with no per-browser setup. A key saved through a Settings page is kept
by provider_store.py in $DESIGN_SYSTEMS_CONFIG_DIR/provider.db (default
~/.config/design-systems/ of the user this unit runs as), outside the clone,
and takes precedence over ANTHROPIC_API_KEY until it is removed. The gallery's
unit reads and writes the same file, so both must run with the same
DESIGN_SYSTEMS_CONFIG_DIR (or the same HOME). Every request re-loads the agent modules, so
a `git pull` by deploy.sh updates the API with no restart of this unit
(catalog, which library.py imports by name, is reloaded in place when
catalog.py changes, for the same reason).
"""
from __future__ import annotations

import argparse
import http.server
import importlib.util
import sys
import threading
from pathlib import Path

_HERE = Path(__file__).resolve()
ROOT = _HERE.parents[1]


def _dotenv() -> None:
    spec = importlib.util.spec_from_file_location(
        "refero_media", ROOT / "tools" / "refero" / "refero_media.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    # Only what the API server reads: the allowed hosts, the chat key and model,
    # and where a saved provider lives.
    mod.load_env(("DESIGN_SYSTEMS_ALLOWED_HOSTS", "ANTHROPIC_API_KEY", "DS_CHAT_MODEL",
                  "DESIGN_SYSTEMS_CONFIG_DIR"))


def _server():
    spec = importlib.util.spec_from_file_location(
        "agent_server", _HERE.parent / "routes.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_TOOLS = str(ROOT / "tools")
_CATALOG = ROOT / "tools" / "catalog.py"
_lock = threading.Lock()
_catalog_mtime: float | None = None


def _refresh_catalog() -> None:
    """library.py imports catalog by name, so the module cache would pin the
    code from the first request and a `git pull` would never reach it. Reload
    it in place (the module object stays in sys.modules, so a request that is
    importing or using it concurrently never loses it) when catalog.py
    changed, under a lock so only one thread reloads."""
    global _catalog_mtime
    with _lock:
        mod = sys.modules.get("catalog")
        try:
            mtime = _CATALOG.stat().st_mtime
        except OSError:
            return
        if mod is not None and _catalog_mtime is not None and mtime != _catalog_mtime:
            importlib.reload(mod)
        _catalog_mtime = mtime


def _trim_path() -> None:
    """library.py puts tools/ on sys.path each time it runs; keep one copy so
    sys.path does not grow per request."""
    with _lock:
        while sys.path.count(_TOOLS) > 1:
            sys.path.remove(_TOOLS)


def _dispatch(method: str, handler) -> bool:
    """Run one request against freshly loaded modules."""
    _refresh_catalog()
    try:
        return getattr(_server(), method)(handler)
    finally:
        _trim_path()


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "designs-api/1"

    def do_GET(self) -> None:
        if not _dispatch("handle_get", self):
            self.send_error(404)

    def do_POST(self) -> None:
        if not _dispatch("handle_post", self):
            self.send_error(404)

    def do_DELETE(self) -> None:
        # DELETE /api/provider removes the saved provider. Any other DELETE is
        # the streamable-HTTP session teardown; the server is stateless, so
        # there is nothing to clean up — acknowledge and move on.
        if _dispatch("handle_delete", self):
            return
        self.send_response(200)
        self.send_header("content-length", "0")
        self.end_headers()

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
