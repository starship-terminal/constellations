"""The model side of the gallery chat: provider adapters and the tool-use loop.

Two wire shapes are supported, picked by the provider config's `api` field:

- "anthropic": POST {base_url}/v1/messages, x-api-key + anthropic-version.
  tools as top-level `tools`, tool_use/tool_result content blocks.
- "openai": POST {base_url}/chat/completions, Authorization: Bearer (or the
  config's key_header). tools as `tools` function wrappers, role:"tool"
  replies. Covers OpenAI, xAI/Grok, Gemini's OpenAI-compatible surface and
  self-hosted compatible endpoints.

The conversation lives in one canonical turn list that each adapter serializes
per call, so a transcript is provider-agnostic. Tool results pass through
library.call; `view_media`'s {"_image": ...} marker becomes an image block in
whichever shape the provider takes.
"""
from __future__ import annotations

import importlib.util
import ipaddress
import json
import os
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

_lib_spec = importlib.util.spec_from_file_location(
    "agent_library", Path(__file__).resolve().parent / "library.py")
library = importlib.util.module_from_spec(_lib_spec)
_lib_spec.loader.exec_module(library)

ANTHROPIC_VERSION = "2023-06-01"
DEFAULT_MODEL = "claude-sonnet-4-5"
MAX_ROUNDS = 8
REQUEST_TIMEOUT = 120
MODELS_TIMEOUT = 25

SYSTEM = """You are the librarian of a private design-systems library. It holds two stores:

- systems/: 40 style packages captured and measured from real products. Every
  value carries an evidence label. These are the only values to design from.
- refero/: a snapshot of styles.refero.design (~1,300 styles), third-party
  interpreted data at lower confidence. Breadth for inspiration, never the
  source for a value a systems package holds.

Help the user pick a style. Rank candidates with search_styles, then read the
ones that matter: get_style for the catalogue entry, get_tokens for measured
values, read_doc for the README (which says what to distrust), list_media and
view_media when a question needs eyes (density, layout, mood) that tags cannot
answer. Compare out loud only what you actually looked at.

Answer in markdown, short paragraphs. Name each recommendation by slug and say
why it fits, not just that it matched. The page renders cards for every slug
your tools return, so a bare list adds nothing. When the user settles on one,
offer handoff_prompt. Never invent a slug; the only ones that exist come from
the tools."""


class ProviderError(Exception):
    """A failed provider call, surfaced to the page as the reply error."""


def provider_config(body: dict | None) -> dict | None:
    """Normalise the page's provider object, or fall back to .env's
    ANTHROPIC_API_KEY (loaded by catalog's refero_media import)."""
    if body and body.get("api_key") and body.get("model"):
        cfg = dict(body)
        cfg["api"] = cfg.get("api") or "openai"
        cfg["base_url"] = (cfg.get("base_url") or "").rstrip("/")
        return cfg
    key = os.environ.get("ANTHROPIC_API_KEY")
    if key:
        return {"api": "anthropic", "base_url": "https://api.anthropic.com",
                "api_key": key, "model": os.environ.get("DS_CHAT_MODEL") or DEFAULT_MODEL,
                "name": "env ANTHROPIC_API_KEY"}
    return None


def _headers(cfg: dict, key_header: str | None = None) -> dict:
    hdr = key_header or cfg.get("key_header")
    if not hdr:
        hdr = "x-api-key" if cfg.get("api") == "anthropic" else "authorization"
    if hdr == "authorization":
        out = {"authorization": f"Bearer {cfg['api_key']}"}
    else:
        out = {hdr: cfg["api_key"]}
    if cfg.get("api") == "anthropic":
        out["anthropic-version"] = ANTHROPIC_VERSION
    return out


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse every redirect: a provider URL comes from the caller, and a 3xx
    must not walk the request (with its key) to a host nobody checked."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


_opener = urllib.request.build_opener(_NoRedirect)


def _is_loopback(host: str) -> bool:
    host = host.lower()
    if host == "localhost" or host.endswith(".localhost"):
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def check_url(url: str) -> None:
    """Only https anywhere, or plain http to this machine (a self-hosted model).
    Anything else (file:, ftp:, http to another host) is refused before a
    socket opens, so the endpoint cannot be used to read local files or reach
    internal plain-http services."""
    try:
        u = urlparse(url)
        host = u.hostname or ""
    except ValueError:
        raise ProviderError("invalid provider URL")
    if not host:
        raise ProviderError("invalid provider URL")
    if u.scheme == "https" or (u.scheme == "http" and _is_loopback(host)):
        return
    raise ProviderError("provider URL must be https (http only for localhost)")


def _same_origin(a: str, b: str) -> bool:
    try:
        ua, ub = urlparse(a), urlparse(b)
        return (ua.scheme, ua.hostname, ua.port) == (ub.scheme, ub.hostname, ub.port)
    except ValueError:
        return False


def _request(method: str, url: str, cfg: dict, body: dict | None, timeout: int,
             key_header: str | None = None) -> dict:
    """Errors name the URL and status only: the upstream body is never echoed
    back, so the endpoint cannot be used to read another server's responses."""
    check_url(url)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "content-type": "application/json", **_headers(cfg, key_header)})
    try:
        with _opener.open(req, timeout=timeout) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as e:
        e.close()
        if 300 <= e.code < 400:
            raise ProviderError(f"{url} answered HTTP {e.code} (redirects are not followed)")
        raise ProviderError(f"{url} answered HTTP {e.code}")
    except (urllib.error.URLError, TimeoutError, OSError):
        raise ProviderError(f"{url} unreachable")


# ---------------------------------------------------------------- models list


def _parse_models(resp: dict) -> list[dict]:
    """Normalise the three list shapes: OpenAI's {data:[{id}]}, Anthropic's
    {data:[{id,display_name}]}, Gemini's {models:[{name:'models/x',displayName}]}."""
    out = []
    for m in resp.get("data") or []:
        if isinstance(m, dict) and m.get("id"):
            out.append({"id": m["id"], "label": m.get("display_name") or m["id"]})
    for m in resp.get("models") or []:
        if isinstance(m, dict) and m.get("name"):
            name = m["name"].split("/", 1)[-1]
            out.append({"id": name, "label": m.get("displayName") or name})
    return out


def list_models(cfg: dict) -> dict:
    """The provider's models, for the settings page's gated combobox. A reachable
    host with no models endpoint still passes so the field unlocks for typing."""
    base = (cfg.get("base_url") or "").rstrip("/")
    if cfg.get("api") == "anthropic":
        url = f"{base}/v1/models"
    else:
        url = cfg.get("models_url") or f"{base}/models"
        # models_url exists for Gemini, whose list lives beside its
        # OpenAI-compatible base; it may not point anywhere base_url does not.
        if not _same_origin(url, base):
            return {"ok": False, "error": "models_url must share base_url's origin"}
    try:
        resp = _request("GET", url, cfg, None, MODELS_TIMEOUT, cfg.get("key_header"))
    except ProviderError as e:
        # Only a 404 or 405 means "the provider is real but lists no models";
        # auth failures, unreachable hosts and server errors all fail the test.
        if "HTTP 404" in str(e) or "HTTP 405" in str(e):
            return {"ok": True, "models": [],
                    "note": "no model list at this endpoint; type the model name"}
        return {"ok": False, "error": str(e)}
    return {"ok": True, "models": _parse_models(resp)}


# ---------------------------------------------------------------- wire adapters


def _anthropic_tools() -> list[dict]:
    return [{"name": s["name"], "description": s["description"],
             "input_schema": s["parameters"]} for s in library.SPECS]


def _openai_tools() -> list[dict]:
    return [{"type": "function", "function": {"name": s["name"], "description": s["description"],
             "parameters": s["parameters"]}} for s in library.SPECS]


def _image_anthropic(img: dict) -> list[dict]:
    return [{"type": "text", "text": json.dumps({"url": img["url"], "name": img["name"]})},
            {"type": "image", "source": {"type": "base64", "media_type": img["media_type"],
                                         "data": img["data"]}}]


def _image_openai(img: dict) -> list[dict]:
    return [{"type": "text", "text": json.dumps({"url": img["url"], "name": img["name"]})},
            {"type": "image_url", "image_url": {"url": f"data:{img['media_type']};base64,{img['data']}"}}]


def _anthropic_messages(turns: list[dict]) -> list[dict]:
    """Canonical turns -> Anthropic messages. Consecutive tool results merge
    into one user message, as the API requires."""
    out = []
    for t in turns:
        if t["role"] == "user":
            out.append({"role": "user", "content": [{"type": "text", "text": t["text"]}]})
        elif t["role"] == "assistant":
            content = ([{"type": "text", "text": t["text"]}] if t.get("text") else [])
            content += [{"type": "tool_use", "id": c["id"], "name": c["name"], "input": c["args"]}
                        for c in t["calls"]]
            out.append({"role": "assistant", "content": content})
        else:  # tool result
            if "_image" in t["result"]:
                content = _image_anthropic(t["result"]["_image"])
            else:
                content = [{"type": "text", "text": json.dumps(t["result"], ensure_ascii=False)}]
            block = {"type": "tool_result", "tool_use_id": t["id"], "content": content}
            if out and out[-1]["role"] == "user" and \
                    out[-1]["content"] and out[-1]["content"][0].get("type") == "tool_result":
                out[-1]["content"].append(block)
            else:
                out.append({"role": "user", "content": [block]})
    return out


def _openai_messages(turns: list[dict]) -> list[dict]:
    out = [{"role": "system", "content": SYSTEM}]
    pending_images = []
    for i, t in enumerate(turns):
        if t["role"] == "user":
            out.append({"role": "user", "content": t["text"]})
        elif t["role"] == "assistant":
            msg = {"role": "assistant", "content": t.get("text") or None}
            if t.get("calls"):
                msg["tool_calls"] = [{"id": c["id"], "type": "function",
                                      "function": {"name": c["name"], "arguments": json.dumps(c["args"])}}
                                     for c in t["calls"]]
            out.append(msg)
        else:
            if "_image" in t["result"]:
                img = t["result"]["_image"]
                # OpenAI tool messages take text parts only; the image rides in a
                # user message right after the run of tool replies it belongs to.
                content = json.dumps({"url": img["url"], "name": img["name"],
                                      "note": "image follows as a user message"})
                pending_images.append(img)
            else:
                content = json.dumps(t["result"], ensure_ascii=False)
            out.append({"role": "tool", "tool_call_id": t["id"], "content": content})
            if pending_images and (i + 1 >= len(turns) or turns[i + 1]["role"] != "tool"):
                out.append({"role": "user",
                            "content": sum((_image_openai(x) for x in pending_images), [])})
                pending_images = []
    return out


def _complete(cfg: dict, turns: list[dict]) -> dict:
    """One provider call -> {text, calls:[{id,name,args}]}."""
    if cfg["api"] == "anthropic":
        resp = _request("POST", f"{cfg['base_url']}/v1/messages", cfg, {
            "model": cfg["model"], "max_tokens": 2048, "system": SYSTEM,
            "tools": _anthropic_tools(), "messages": _anthropic_messages(turns)}, REQUEST_TIMEOUT)
        text = "".join(b.get("text", "") for b in resp.get("content", []) if b.get("type") == "text")
        calls = [{"id": b["id"], "name": b["name"], "args": b.get("input") or {}}
                 for b in resp.get("content", []) if b.get("type") == "tool_use"]
        return {"text": text.strip() or None, "calls": calls}
    resp = _request("POST", f"{cfg['base_url']}/chat/completions", cfg, {
        "model": cfg["model"], "messages": _openai_messages(turns),
        "tools": _openai_tools(), "tool_choice": "auto"}, REQUEST_TIMEOUT)
    msg = (resp.get("choices") or [{}])[0].get("message") or {}
    calls = [{"id": c.get("id") or f"call_{i}", "name": c["function"]["name"],
              "args": _json_args(c["function"].get("arguments"))}
             for i, c in enumerate(msg.get("tool_calls") or [])]
    return {"text": (msg.get("content") or "").strip() or None, "calls": calls}


def _json_args(raw) -> dict:
    try:
        out = json.loads(raw or "{}")
        return out if isinstance(out, dict) else {}
    except (TypeError, ValueError):
        return {}


# ---------------------------------------------------------------- the loop


def run(messages: list[dict], provider: dict) -> dict:
    """Drive the tool loop for one page-side conversation. Returns the reply
    plus the artifacts the page renders: result slugs and media URLs."""
    turns = []
    for m in messages[-24:]:
        if m.get("role") in ("user", "assistant") and m.get("content"):
            turns.append({"role": m["role"], "text": str(m["content"])[:8000],
                          **({"calls": []} if m["role"] == "assistant" else {})})
    if not turns or turns[-1]["role"] != "user":
        turns.append({"role": "user", "text": "Help me pick a design style."})

    results: dict[str, dict] = {}
    media: dict[str, dict] = {}
    calls_log = []
    for _ in range(MAX_ROUNDS):
        step = _complete(provider, turns)
        if not step["calls"]:
            if step["text"]:
                turns.append({"role": "assistant", "text": step["text"], "calls": []})
            return {"reply": step["text"] or "", "results": list(results.values()),
                    "media": list(media.values()), "calls": calls_log}
        turns.append({"role": "assistant", "text": step["text"], "calls": step["calls"]})
        for c in step["calls"]:
            calls_log.append(c["name"])
            try:
                result = library.call(c["name"], c["args"])
            except Exception as e:
                result = {"error": str(e)[:400]}
            _collect(c["name"], c["args"], result, results, media)
            turns.append({"role": "tool", "id": c["id"], "result": result})
    return {"reply": "", "error": f"stopped after {MAX_ROUNDS} tool rounds",
            "results": list(results.values()), "media": list(media.values()), "calls": calls_log}


def _collect(name: str, args: dict, result: dict, results: dict, media: dict) -> None:
    """Pull page-renderable artifacts out of a tool result. Error payloads are
    skipped so a failed call never turns the whole turn into a 500."""
    if not isinstance(result, dict) or "error" in result:
        return
    if name == "search_styles":
        for h in result.get("hits", []):
            results.setdefault(f"{h['store']}:{h['slug']}",
                               {"store": h["store"], "slug": h["slug"], "name": h["name"]})
    elif name == "get_style":
        results.setdefault(f"{result.get('store', 'systems')}:{result.get('slug')}",
                           {"store": result.get("store", "systems"), "slug": result["slug"],
                            "name": result["name"]})
    elif name == "list_media":
        for i in result.get("items", []):
            media.setdefault(i["url"], {"url": i["url"], "name": f"{result['slug']}/{i['name']}"})
    elif name == "view_media" and "_image" in result:
        img = result["_image"]
        media.setdefault(img["url"], {"url": img["url"], "name": img["name"]})
    elif name == "handoff_prompt" and result.get("prompt"):
        results.setdefault(f"prompt:{result['slug']}",
                           {"store": "prompt", "slug": result["slug"], "name": "Agent prompt",
                            "prompt": result["prompt"]})
