"""The /api/ routes the local docs server answers. catalog.py's serve Handler
delegates here for every request under /api/; the published static site never
sees any of it (it drops the gallery and runs no Python).

  GET  /api/status           {"ok": true, "envProvider": bool}
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


def _load(name: str):
    spec = importlib.util.spec_from_file_location(
        f"agent_{name}", Path(__file__).resolve().parent / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _reply(handler, status: int, obj: dict) -> None:
    body = json.dumps(obj, ensure_ascii=False).encode()
    handler.send_response(status)
    handler.send_header("content-type", "application/json; charset=utf-8")
    handler.send_header("content-length", str(len(body)))
    handler.send_header("cache-control", "no-store")
    handler.end_headers()
    handler.wfile.write(body)


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


def handle_get(handler) -> bool:
    """True when the path was an /api/ route this answered."""
    path = handler.path.split("?", 1)[0]
    if not path.startswith("/api/"):
        return False
    if path == "/api/status":
        chat = _load("chat")
        cfg = chat.provider_config(None)
        _reply(handler, 200, {"ok": True, "envProvider": bool(cfg)})
        return True
    _reply(handler, 404, {"error": "no such api route"})
    return True


def handle_post(handler) -> bool:
    path = handler.path.split("?", 1)[0]
    if not path.startswith("/api/"):
        return False
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
