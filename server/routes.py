"""The /api/ route handlers behind the gallery chat. api.py delegates here for
every request under /api/; the published static site never sees any of it (it
drops the gallery and runs no Python), and local browsing gets the same routes
from the Next.js app.

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
import json
from pathlib import Path
from urllib.parse import urlparse


_ROOT = Path(__file__).resolve().parent.parent


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
    if host:
        return f"{proto}://{host}"
    addr = getattr(handler.server, "server_address", ("127.0.0.1", 80))
    return f"http://{addr[0]}:{addr[1]}"


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
    if not _origin_ok(handler):
        _reply(handler, 403, {"error": "cross-origin request"})
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
    if not _origin_ok(handler):
        _reply(handler, 403, {"error": "cross-origin request"})
        return True
    if path == "/api/mcp":
        try:
            n = int(handler.headers.get("content-length") or 0)
        except ValueError:
            n = 0
        if n <= 0 or n > 256_000:
            _reply(handler, 400, {"jsonrpc": "2.0", "id": None,
                                  "error": {"code": -32600, "message": "a JSON-RPC body is required"}})
            return True
        try:
            raw = json.loads(handler.rfile.read(n))
        except (ValueError, UnicodeDecodeError):
            _reply(handler, 400, {"jsonrpc": "2.0", "id": None,
                                  "error": {"code": -32700, "message": "unparseable JSON"}})
            return True
        mcp = _load("mcp")
        msgs = raw if isinstance(raw, list) else [raw]
        replies = [r for r in (mcp.handle(m) for m in msgs if isinstance(m, dict)) if r]
        if not replies:
            _empty(handler, 202)
            return True
        _reply(handler, 200, replies[0] if isinstance(raw, dict) else replies)
        return True
    chat = _load("chat")
    if path == "/api/provider/test":
        body = _body(handler)
        if not body or not body.get("api_key") or not body.get("base_url"):
            _reply(handler, 400, {"ok": False, "error": "base_url and api_key are required"})
            return True
        body["api"] = body.get("api") or "openai"
        body["base_url"] = body["base_url"].rstrip("/")
        try:
            _reply(handler, 200, chat.list_models(body))
        except chat.ProviderError as e:
            _reply(handler, 200, {"ok": False, "error": str(e)})
        return True
    if path == "/api/chat":
        body = _body(handler)
        if not body:
            _reply(handler, 400, {"error": "JSON body required"})
            return True
        cfg = chat.provider_config(body.get("provider"))
        if not cfg:
            _reply(handler, 503, {"error": "no_provider",
                                  "message": "no model configured: set one under Settings, "
                                             "or ANTHROPIC_API_KEY in .env"})
            return True
        messages = [m for m in body.get("messages") or [] if isinstance(m, dict)]
        try:
            _reply(handler, 200, chat.run(messages, cfg))
        except chat.ProviderError as e:
            _reply(handler, 200, {"reply": "", "error": str(e), "results": [], "media": []})
        except Exception as e:
            _reply(handler, 500, {"error": f"{type(e).__name__}: {e}"})
        return True
    _reply(handler, 404, {"error": "no such api route"})
    return True
