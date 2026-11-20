"""The chat's model provider, held server-side, for the home server's Python
/api/ (routes.py). web/lib/provider-store.ts and web/lib/provider-api.ts are
the gallery's copy of the same rules over the same file, so a key saved in
either is the one both use.

Where: $DESIGN_SYSTEMS_CONFIG_DIR/provider.json, default
~/.config/design-systems/provider.json, outside the checkout. The folder is
created 0700 and the file written 0600 through a temporary file and a rename,
so a reader never sees half a key and a rotation swaps keys in one step.

The rules:
- A key reaches the server once, is tested with one cheap call (the model
  list) and is saved only when that passes; the old key keeps working until
  then.
- No answer carries a key: state says only where it comes from ("saved",
  "env" or "none").
- Precedence: the saved key, then ANTHROPIC_API_KEY while nothing is saved,
  then nothing. A broken saved file is reported, never replaced by env.
- A saved key only goes to the endpoint it was saved with; changing the API,
  base URL, key header or models URL needs the key again.
- Every error text passes through redact() with the keys in play.
"""
from __future__ import annotations

import json
import os
import re
import tempfile
from pathlib import Path

CONFIG_DIR_ENV = "DESIGN_SYSTEMS_CONFIG_DIR"
FILE_NAME = "provider.json"
PUBLIC_FIELDS = ("api", "base_url", "key_header", "models_url", "model", "name")
ENDPOINT_FIELDS = ("api", "base_url", "key_header", "models_url")
DEFAULT_BASE_URL = {"anthropic": "https://api.anthropic.com", "openai": "https://api.openai.com/v1"}
MAX_KEY = 1024
_BAD_KEY = re.compile(r"[\s\x00-\x1f\x7f]")
_HEADER = re.compile(r"[A-Za-z0-9-]{1,64}")


class StoreError(Exception):
    """The saved file exists but cannot be used. Never carries its text."""


class BadRequest(Exception):
    """A posted provider that cannot be used. The message never quotes it."""


def config_dir() -> Path:
    raw = (os.environ.get(CONFIG_DIR_ENV) or "").strip()
    return Path(raw).expanduser().resolve() if raw else Path.home() / ".config" / "design-systems"


def provider_file() -> Path:
    return config_dir() / FILE_NAME


def load() -> dict | None:
    """The saved provider, None when nothing is saved; StoreError when the
    file is there but unusable."""
    try:
        text = provider_file().read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    except (OSError, UnicodeDecodeError):
        raise StoreError("The saved provider file cannot be read.") from None
    try:
        raw = json.loads(text)
    except ValueError:
        raise StoreError("The saved provider file is not valid JSON.") from None
    if not isinstance(raw, dict):
        raise StoreError("The saved provider file is not an object.")
    out = {k: raw[k] for k in (*PUBLIC_FIELDS, "api_key") if isinstance(raw.get(k), str) and raw[k]}
    if not all(out.get(k) for k in ("api_key", "api", "base_url", "model")):
        raise StoreError("The saved provider file is missing its key, endpoint or model.")
    return out


def save(cfg: dict) -> None:
    """Write the provider (key included) in one atomic step, mode 0600."""
    folder = config_dir()
    folder.mkdir(parents=True, exist_ok=True, mode=0o700)
    out = {k: cfg[k] for k in (*PUBLIC_FIELDS, "api_key") if isinstance(cfg.get(k), str) and cfg[k]}
    fd, tmp = tempfile.mkstemp(prefix=f".{FILE_NAME}.", suffix=".tmp", dir=folder)
    try:
        os.fchmod(fd, 0o600)
        with os.fdopen(fd, "w", encoding="utf-8") as fh:
            fh.write(json.dumps(out, indent=2) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
        os.replace(tmp, provider_file())
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


def remove() -> bool:
    """Delete the saved provider. True when there was one."""
    try:
        provider_file().unlink()
        return True
    except FileNotFoundError:
        return False
    except OSError:
        raise StoreError("The saved provider file cannot be removed.") from None


def public(cfg: dict | None) -> dict | None:
    """The fields of a provider that may leave the server."""
    if not cfg:
        return None
    return {k: cfg[k] for k in PUBLIC_FIELDS if isinstance(cfg.get(k), str) and cfg[k]}


def redact(text: str, *keys: str | None) -> str:
    """`text` with every occurrence of each key replaced."""
    for k in keys:
        if k and len(k) >= 4:
            text = text.replace(k, "[redacted]")
    return text


def parse(body) -> dict:
    """Validate and normalise a posted provider object."""
    if not isinstance(body, dict):
        raise BadRequest("Send a JSON object.")
    s = {}
    for k in (*PUBLIC_FIELDS, "api_key"):
        v = body.get(k)
        if v is None:
            s[k] = ""
        elif isinstance(v, str):
            s[k] = v.strip()
        else:
            raise BadRequest("Provider fields must be strings.")
    api = s["api"] or "openai"
    if api not in DEFAULT_BASE_URL:
        raise BadRequest("API must be anthropic or openai.")
    if len(s["api_key"]) > MAX_KEY or _BAD_KEY.search(s["api_key"]):
        raise BadRequest("That API key has characters a key cannot hold.")
    if s["key_header"] and not _HEADER.fullmatch(s["key_header"]):
        raise BadRequest("Key header must be a header name.")
    if len(s["model"]) > 160 or len(s["name"]) > 80:
        raise BadRequest("Model or label is too long.")
    s["api"] = api
    s["base_url"] = (s["base_url"] or DEFAULT_BASE_URL[api]).rstrip("/")
    s["key_header"] = s["key_header"].lower()
    s["models_url"] = s["models_url"].rstrip("/")
    return s


def _endpoint(p: dict) -> tuple:
    out = []
    for k in ENDPOINT_FIELDS:
        v = (p.get(k) or "").strip()
        out.append(v.lower() if k == "key_header" else v if k == "api" else v.rstrip("/"))
    return tuple(out)


def same_endpoint(a: dict, b: dict) -> bool:
    return _endpoint(a) == _endpoint(b)


def to_cfg(s: dict, api_key: str) -> dict:
    cfg = {"api": s["api"], "base_url": s["base_url"], "model": s["model"], "api_key": api_key}
    for k in ("key_header", "models_url", "name"):
        if s.get(k):
            cfg[k] = s[k]
    return cfg


def state(env_cfg: dict | None) -> dict:
    """Where the key comes from, never the key. `env_cfg` is chat.py's env
    provider (provider_config(None))."""
    env = {"envAvailable": bool(env_cfg)}
    try:
        saved = load()
    except StoreError as e:
        return {"source": "saved", "configured": False, "provider": None, **env, "error": str(e)}
    if saved:
        return {"source": "saved", "configured": True, "provider": public(saved), **env}
    if env_cfg:
        return {"source": "env", "configured": True, "provider": public(env_cfg), **env}
    return {"source": "none", "configured": False, "provider": None, **env}


def resolve(env_cfg: dict | None) -> tuple[dict | None, str, str | None]:
    """(cfg, source, error) by precedence: saved, then env, then none."""
    try:
        saved = load()
    except StoreError as e:
        return None, "saved", str(e)
    if saved:
        return saved, "saved", None
    if env_cfg:
        return env_cfg, "env", None
    return None, "none", None
