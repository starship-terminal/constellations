"""The chat's model provider, held server-side, for the home server's Python
/api/ (routes.py). web/lib/provider-store.ts and web/lib/provider-api.ts are
the gallery's copy of the same rules over the same file, so a key saved in
either is the one both use.

Where: $DESIGN_SYSTEMS_CONFIG_DIR/provider.db, default
~/.config/design-systems/provider.db, outside the checkout. The folder is
created 0700 and the database file 0600 (SQLite gives its -wal and -shm files
the same mode). Every change is one SQL statement, so SQLite's own locking,
which a crashed process never leaves behind, makes each one atomic across both
servers: a model-only save applies only while the row still holds the key and
endpoint it read, a migration only inserts into an empty table, and an
unchecked key only replaces a row holding the same key.

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
- A key the provider never checked (an endpoint with no model list) never
  replaces a saved one, and a one-time migration from a browser (migrate:
  true) never replaces any saved provider.
"""
from __future__ import annotations

import contextlib
import os
import re
import sqlite3
from pathlib import Path

CONFIG_DIR_ENV = "DESIGN_SYSTEMS_CONFIG_DIR"
FILE_NAME = "provider.db"
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


# The same schema web/lib/provider-store.ts creates.
SCHEMA = """CREATE TABLE IF NOT EXISTS provider (
  id INTEGER PRIMARY KEY CHECK (id = 1),
  api TEXT NOT NULL,
  base_url TEXT NOT NULL,
  key_header TEXT NOT NULL DEFAULT '',
  models_url TEXT NOT NULL DEFAULT '',
  model TEXT NOT NULL,
  name TEXT NOT NULL DEFAULT '',
  api_key TEXT NOT NULL
)"""
COLUMNS = ("api", "base_url", "key_header", "models_url", "model", "name", "api_key")
_UPDATE = ", ".join(f"{c} = excluded.{c}" for c in COLUMNS)
_INSERT = f"INSERT INTO provider (id, {', '.join(COLUMNS)}) VALUES (1, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO "
SAVE_SQL = {
    "create": _INSERT + "NOTHING",
    "same-key": _INSERT + f"UPDATE SET {_UPDATE} WHERE provider.api_key = excluded.api_key",
    "replace": _INSERT + f"UPDATE SET {_UPDATE}",
}


@contextlib.contextmanager
def _db(create: bool):
    """The open database, or None when none exists (nothing saved). `create`
    makes the folder (0700) and the file (0600) first."""
    path = provider_file()
    if create:
        config_dir().mkdir(parents=True, exist_ok=True, mode=0o700)
        fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
        os.close(fd)
        os.chmod(path, 0o600)
    elif not path.exists():
        yield None
        return
    try:
        conn = sqlite3.connect(path, timeout=5, isolation_level=None)
    except sqlite3.Error:
        raise StoreError("The saved provider file cannot be read.") from None
    try:
        try:
            conn.execute("PRAGMA busy_timeout = 5000")
            conn.execute("PRAGMA journal_mode = WAL")
            conn.execute(SCHEMA)
        except sqlite3.Error:
            raise StoreError("The saved provider file cannot be read.") from None
        try:
            yield conn
        except sqlite3.Error:
            raise StoreError("The saved provider file cannot be used.") from None
    finally:
        conn.close()


def load() -> dict | None:
    """The saved provider, None when nothing is saved; StoreError when the
    database is there but unusable."""
    with _db(False) as conn:
        if conn is None:
            return None
        row = conn.execute(f"SELECT {', '.join(COLUMNS)} FROM provider WHERE id = 1").fetchone()
    if row is None:
        return None
    out = {k: v for k, v in zip(COLUMNS, row) if isinstance(v, str) and v}
    if not all(out.get(k) for k in ("api_key", "api", "base_url", "model")):
        raise StoreError("The saved provider is missing its key, endpoint or model.")
    return out


def _values(cfg: dict) -> tuple:
    return tuple(cfg.get(c) or "" for c in COLUMNS)


def save_provider(cfg: dict, mode: str) -> bool:
    """Write the provider in one statement. `mode`: "replace" always (a key the
    provider checked); "create" only when none is saved (a migration from a
    browser); "same-key" only when none is saved or it holds this same key (a
    key the provider could not check). True when the row was written."""
    with _db(True) as conn:
        return conn.execute(SAVE_SQL[mode], _values(cfg)).rowcount > 0


def update_model(seen: dict, model: str, name: str) -> bool:
    """Change the model and label only while the row still holds exactly the
    key and endpoint in `seen`. False when it changed or went away."""
    with _db(False) as conn:
        if conn is None:
            return False
        cur = conn.execute(
            "UPDATE provider SET model = ?, name = ? WHERE id = 1 AND api_key = ? AND api = ? "
            "AND base_url = ? AND key_header = ? AND models_url = ?",
            (model, name, seen.get("api_key") or "", seen.get("api") or "", seen.get("base_url") or "",
             seen.get("key_header") or "", seen.get("models_url") or ""))
        return cur.rowcount > 0


def remove() -> bool:
    """Delete the saved provider. True when there was one."""
    with _db(False) as conn:
        if conn is None:
            return False
        return conn.execute("DELETE FROM provider WHERE id = 1").rowcount > 0


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
    if body.get("migrate") is not None and not isinstance(body.get("migrate"), bool):
        raise BadRequest("migrate must be true or false.")
    s = {"migrate": body.get("migrate") is True}
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


def default_header(api: str) -> str:
    """The header a key goes in when none is named: chat.py's rule."""
    return "x-api-key" if api == "anthropic" else "authorization"


def _endpoint(p: dict) -> tuple:
    """Where a key goes, normalised: a blank key header is its API's default."""
    api = (p.get("api") or "").strip() or "openai"
    out = []
    for k in ENDPOINT_FIELDS:
        v = (p.get(k) or "").strip()
        if k == "api":
            out.append(api)
        elif k == "key_header":
            out.append((v or default_header(api)).lower())
        else:
            out.append(v.rstrip("/"))
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
