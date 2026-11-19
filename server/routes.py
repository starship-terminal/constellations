"""The /api/ route handlers behind the gallery chat. api.py delegates here for
every request under /api/ on the home-server deployment, where nginx serves
the docs site statically from site/ and proxies only /api/ to Python; local
browsing gets the same routes from the Next.js app.

  GET  /api/status           {"ok": true, "envProvider": bool}
  GET  /api/mcp              405 — streamable HTTP is POST-only here
  POST /api/mcp              MCP over streamable HTTP: one JSON-RPC message (or
                             a batch) in, the replies as application/json out;
                             notification-only bodies get 202. Stateless —
                             no session header.
  GET  /api/ds               the ds CLI client (cli/ds), verbatim
  GET  /api/install.sh       cli/install.sh with @DS_BASE@ filled from the
                             request's forwarded Host/proto
  POST /api/provider/test    {api, base_url, api_key, key_header?, models_url?}
                             (https to a known model API or a host listed in
                             DESIGN_SYSTEMS_PROVIDER_HOSTS, http only for a
                             listed loopback host; models_url must share
                             base_url's origin; redirects refused)
                             -> {ok, models:[{id,label}], error?} for the
                             settings page's test-gated model field
  POST /api/chat             {messages, provider?} -> {reply, results, media}
                             provider comes from the browser's settings; without
                             one the .env ANTHROPIC_API_KEY fallback applies.

Everything is read-only; the provider key arrives per request from the same
browser session, so nothing secret touches the checkout.
"""
from __future__ import annotations

import importlib.util
import ipaddress
import json
import os
import re
import sys
import traceback
from pathlib import Path
from urllib.parse import urlparse


_ROOT = Path(__file__).resolve().parent.parent
_SAFE_HOST = re.compile(r"[A-Za-z0-9.:\[\]-]+")


def _load(name: str):
    spec = importlib.util.spec_from_file_location(
        f"agent_{name}", Path(__file__).resolve().parent / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _reply(handler, status: int, obj) -> None:
    body = json.dumps(obj, ensure_ascii=False).encode()
    _send(handler, status, body, "application/json; charset=utf-8")


def _send(handler, status: int, body: bytes, ctype: str) -> None:
    handler.send_response(status)
    handler.send_header("content-type", ctype)
    handler.send_header("content-length", str(len(body)))
    handler.send_header("cache-control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


def _empty(handler, status: int) -> None:
    handler.send_response(status)
    handler.send_header("content-length", "0")
    handler.end_headers()


def _base_url(handler) -> str:
    """The origin a remote client should call: the Host the proxy forwarded,
    or our own bind address as a fallback for a headerless request."""
    def fwd(name: str) -> str:
        return (handler.headers.get(name) or "").split(",")[0].strip()
    host = fwd("x-forwarded-host") or fwd("host")
    proto = fwd("x-forwarded-proto") or "http"
    # The value lands inside BASE="..." in a script piped to sh, so anything
    # beyond host characters (quotes, $, backticks) falls back to the bind
    # address instead of being spliced in.
    if host and _SAFE_HOST.fullmatch(host) and proto in ("http", "https"):
        return f"{proto}://{host}"
    addr = getattr(handler.server, "server_address", ("127.0.0.1", 80))
    return f"http://{addr[0]}:{addr[1]}"


MCP_BODY_LIMIT = 256_000  # POST /api/mcp; web/proxy.ts holds the same cap


def _body(handler, cap: int = 128_000) -> dict | None:
    try:
        n = int(handler.headers.get("content-length") or 0)
    except ValueError:
        n = 0
    if n <= 0 or n > cap:
        return None
    try:
        out = json.loads(handler.rfile.read(n))
        return out if isinstance(out, dict) else None
    except (ValueError, UnicodeDecodeError):
        return None


# The provider object's fields chat.py builds URLs and headers from. A number or
# list in one of them would raise outside the handlers' error replies and drop
# the connection with no answer, so a request carrying one is refused instead.
_PROVIDER_FIELDS = ("api", "base_url", "api_key", "key_header", "models_url", "model")


def _strings(obj: dict, keys) -> bool:
    """Whether every key of `keys` present in `obj` holds a string (or null)."""
    return all(obj.get(k) is None or isinstance(obj[k], str) for k in keys)


def _host_name(value: str) -> str | None:
    """The bare host of a Host header value (no port, no IPv6 brackets), or
    None when it is malformed."""
    try:
        u = urlparse(f"//{value}")
        u.port  # raises on a non-numeric or out-of-range port
    except ValueError:
        return None
    if u.username is not None or u.path or u.query or u.fragment:
        return None
    return u.hostname


def _host_ok(handler) -> bool:
    """Answer only for a Host this server is meant to be reached by. The
    Origin check below cannot see DNS rebinding: a page on evil.test whose name
    is re-pointed at this machine sends Origin and Host both as evil.test, so
    they match. A rebinding attacker can only put a name whose DNS they control
    in Host, so the allowlist accepts names they cannot: loopback, IP literals,
    Tailscale's *.ts.net (MagicDNS), and the hosts listed in
    DESIGN_SYSTEMS_ALLOWED_HOSTS (comma-separated `name` or `name:port`; a
    bare name matches any port). A request with no Host header is not from a
    browser and passes."""
    raw = (handler.headers.get("host") or "").strip().lower()
    if not raw:
        return True
    name = _host_name(raw)
    if not name:
        return False
    if name == "localhost" or name.endswith(".localhost") or name.endswith(".ts.net"):
        return True
    try:
        ipaddress.ip_address(name)
        return True
    except ValueError:
        pass
    for entry in (os.environ.get("DESIGN_SYSTEMS_ALLOWED_HOSTS") or "").split(","):
        entry = entry.strip().lower()
        if entry and entry in (raw, name):
            return True
    return False


def _guard(handler) -> bool:
    """True when the request was refused (and answered)."""
    if not _host_ok(handler):
        _reply(handler, 403, {"error": "unknown host: add it to DESIGN_SYSTEMS_ALLOWED_HOSTS"})
        return True
    if not _origin_ok(handler):
        _reply(handler, 403, {"error": "cross-origin request"})
        return True
    return False


def _origin_ok(handler) -> bool:
    """Only this server's own pages may call the API. A browser POST to a
    loopback host is a 'simple' request — CORS never blocks it — so any site
    could otherwise spend the fallback key or use this server to reach
    internal URLs through the provider endpoints. An Origin or Referer that
    does not match our Host header means the request came from another page.
    Headerless clients (curl, MCP hosts) are not browsers and pass."""
    host = (handler.headers.get("host") or "").lower()
    for name in ("origin", "referer"):
        value = handler.headers.get(name)
        if value and urlparse(value).netloc.lower() != host:
            return False
    return True


def handle_get(handler) -> bool:
    """True when the path was an /api/ route this answered."""
    path = handler.path.split("?", 1)[0]
    if not path.startswith("/api/"):
        return False
    if _guard(handler):
        return True
    if path == "/api/status":
        chat = _load("chat")
        cfg = chat.provider_config(None)
        _reply(handler, 200, {"ok": True, "envProvider": bool(cfg)})
        return True
    if path == "/api/mcp":
        _reply(handler, 405, {"error": "streamable HTTP is POST-only on this server"})
        return True
    if path == "/api/ds":
        target = _ROOT / "cli" / "ds"
        if not target.is_file():
            _reply(handler, 404, {"error": "cli/ds not in this checkout"})
            return True
        _send(handler, 200, target.read_bytes(), "text/plain; charset=utf-8")
        return True
    if path == "/api/install.sh":
        target = _ROOT / "cli" / "install.sh"
        if not target.is_file():
            _reply(handler, 404, {"error": "cli/install.sh not in this checkout"})
            return True
        body = target.read_text().replace("@DS_BASE@", _base_url(handler)).encode()
        _send(handler, 200, body, "text/x-shellscript; charset=utf-8")
        return True
    _reply(handler, 404, {"error": "no such api route"})
    return True


def handle_post(handler) -> bool:
    path = handler.path.split("?", 1)[0]
    if not path.startswith("/api/"):
        return False
    if _guard(handler):
        return True
    if path == "/api/mcp":
        try:
            n = int(handler.headers.get("content-length") or 0)
        except ValueError:
            n = 0
        if n > MCP_BODY_LIMIT:
            _reply(handler, 413, {"jsonrpc": "2.0", "id": None,
                                  "error": {"code": -32600,
                                            "message": f"request body exceeds the {MCP_BODY_LIMIT}-byte limit"}})
            return True
        if n <= 0:
            _reply(handler, 400, {"jsonrpc": "2.0", "id": None,
                                  "error": {"code": -32600, "message": "a JSON-RPC body is required"}})
            return True
        try:
            raw = json.loads(handler.rfile.read(n))
        except (ValueError, UnicodeDecodeError):
            _reply(handler, 400, {"jsonrpc": "2.0", "id": None,
                                  "error": {"code": -32700, "message": "unparseable JSON"}})
            return True
        out = _load("mcp").handle_batch(raw)
        if out is None:
            _empty(handler, 202)
        else:
            _reply(handler, 200, out)
        return True
    chat = _load("chat")
    if path == "/api/provider/test":
        body = _body(handler)
        if not body or not body.get("api_key") or not body.get("base_url"):
            _reply(handler, 400, {"ok": False, "error": "base_url and api_key are required"})
            return True
        if not _strings(body, _PROVIDER_FIELDS):
            _reply(handler, 400, {"ok": False, "error": "provider fields must be strings"})
            return True
        body["api"] = body.get("api") or "openai"
        body["base_url"] = body["base_url"].rstrip("/")
        try:
            _reply(handler, 200, chat.list_models(body))
        except chat.ProviderError as e:
            _reply(handler, 200, {"ok": False, "error": str(e)})
        except Exception:
            traceback.print_exc(file=sys.stderr)
            _reply(handler, 500, {"ok": False, "error": "internal error"})
        return True
    if path == "/api/chat":
        body = _body(handler)
        if not body:
            _reply(handler, 400, {"error": "JSON body required"})
            return True
        provider = body.get("provider")
        # Absent or null means none; any other non-list (0, "", {}) is refused, not defaulted.
        messages = body.get("messages")
        messages = [] if messages is None else messages
        if (provider is not None and not (isinstance(provider, dict) and _strings(provider, _PROVIDER_FIELDS))) \
                or not isinstance(messages, list):
            _reply(handler, 400, {"error": "provider must be an object of strings and messages a list"})
            return True
        cfg = chat.provider_config(provider)
        if not cfg:
            _reply(handler, 503, {"error": "no_provider",
                                  "message": "no model configured: set one under Settings, "
                                             "or ANTHROPIC_API_KEY in .env"})
            return True
        messages = [m for m in messages if isinstance(m, dict)]
        try:
            _reply(handler, 200, chat.run(messages, cfg))
        except chat.ProviderError as e:
            _reply(handler, 200, {"reply": "", "error": str(e), "results": [], "media": []})
        except Exception:
            # The detail (paths, upstream text) goes to the server log only.
            traceback.print_exc(file=sys.stderr)
            _reply(handler, 500, {"error": "internal error"})
        return True
    _reply(handler, 404, {"error": "no such api route"})
    return True
