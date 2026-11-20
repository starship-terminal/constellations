"""The chat's model provider, held server-side, for the home server's Python
/api/ (routes.py). web/lib/provider-store.ts and web/lib/provider-api.ts are
the gallery's copy of the same rules over the same file, so a key saved in
either is the one both use.

Where: $DESIGN_SYSTEMS_CONFIG_DIR/provider.db, default
~/.config/design-systems/provider.db, outside the checkout. The folder is
created 0700 and the database file 0600. It uses the rollback journal
(journal_mode DELETE), not the WAL the stack conventions default to: with
secure_delete on, a replaced or removed key is overwritten in place and the
journal is deleted at commit, so no copy of an old key survives in a -wal file
that an open reader could keep from being checkpointed. Writes are rare and
the table has one row, so WAL's concurrency buys nothing here.

Every change is one SQL statement, so SQLite's own locking, which a crashed
process never leaves behind, makes each one atomic across both servers: a model-only save applies only while the row still holds the key and
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
from urllib.parse import quote, unquote
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
    """The saved provider exists but cannot be used. Never carries its text.
    `damaged` is set only when SQLite said the file is not a database or is
    corrupt: only then may a remove or a checked save delete it. A busy lock,
    a full disk or a permission error must never cost a working provider."""
    damaged = False


_SQLITE_CORRUPT = 11
_SQLITE_NOTADB = 26


# SQLite's own text for those two codes, for Pythons before 3.11, where
# sqlite3 errors carry no sqlite_errorcode.
_DAMAGED_TEXT = ("file is not a database", "database disk image is malformed")


def _error_code(cause: BaseException | None):
    """SQLite's result code on an error (Python 3.11 and later), else None."""
    code = getattr(cause, "sqlite_errorcode", None)
    return code if isinstance(code, int) else None


def _store_error(message: str, cause: BaseException | None = None) -> StoreError:
    err = StoreError(message)
    code = _error_code(cause)
    if code is not None:
        err.damaged = (code & 0xFF) in (_SQLITE_CORRUPT, _SQLITE_NOTADB)
    elif isinstance(cause, sqlite3.DatabaseError):
        text = str(cause).lower()
        err.damaged = any(t in text for t in _DAMAGED_TEXT)
    return err


class BadRequest(Exception):
    """A posted provider that cannot be used. The message never quotes it."""


REPO_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR_HELP = (f"{CONFIG_DIR_ENV} must be an absolute path outside the checkout (a leading ~/ is "
                   "expanded), for example ~/.config/design-systems.")


def config_dir() -> Path:
    """The folder that holds provider.db. web/lib/provider-store.ts applies the
    same rules, and server/provider-config-cases.json holds the cases both test
    suites run, so the gallery and this API always name the same file: a
    leading ~ or ~/ is the home folder (systemd's Environment= and a .env file
    do not expand it); a relative path, a ~user path or a path inside the
    checkout is refused with a StoreError that says how to set it, never
    resolved against whatever folder the server started in."""
    raw = (os.environ.get(CONFIG_DIR_ENV) or "").strip()
    home = Path.home()
    if not raw:
        d = home / ".config" / "design-systems"
    elif raw == "~":
        d = home
    elif raw.startswith("~/"):
        d = home / raw[2:]
    elif os.path.isabs(raw):
        d = Path(raw)
    else:
        raise StoreError(CONFIG_DIR_HELP)
    d = Path(os.path.normpath(d))
    if inside_checkout(d, REPO_ROOT):
        raise StoreError(CONFIG_DIR_HELP)
    return d


def _inside(child: str, parent: str) -> bool:
    return child == parent or child.startswith(parent.rstrip(os.sep) + os.sep)


def _real_of_nearest(p: Path) -> str:
    """`p` with its nearest existing ancestor replaced by that ancestor's real
    path (symlinks resolved), and the part that does not exist yet appended."""
    cur = os.path.normpath(os.path.abspath(p))
    rest: list[str] = []
    while True:
        if os.path.exists(cur):
            return os.path.join(os.path.realpath(cur), *reversed(rest))
        up = os.path.dirname(cur)
        if up == cur:
            return os.path.normpath(os.path.abspath(p))
        rest.append(os.path.basename(cur))
        cur = up


def case_insensitive_at(existing: str) -> bool:
    """Whether the filesystem holding `existing` ignores letter case, found by
    testing it rather than by platform: the same path with the case of its
    last lettered part swapped is the same file."""
    parts = existing.split(os.sep)
    for i in range(len(parts) - 1, -1, -1):
        swapped = parts[i].swapcase()
        if swapped == parts[i]:
            continue
        variant = os.sep.join(parts[:i] + [swapped] + parts[i + 1:])
        try:
            a, b = os.stat(existing), os.stat(variant)
        except OSError:
            return False
        return (a.st_dev, a.st_ino) == (b.st_dev, b.st_ino)
    return False


def is_checkout(root: Path) -> bool:
    """Whether `root` really is a checkout (it holds catalog.json or .git)."""
    return (root / "catalog.json").exists() or (root / ".git").exists()


def inside_checkout(d: Path, root: Path) -> bool:
    """Whether `d` is inside the checkout at `root`: compared as typed, and as
    real paths (a symlink into the checkout counts), case-folded where the
    filesystem ignores case. web/lib/provider-store.ts has the same rule."""
    if not is_checkout(root):
        return False
    if _inside(os.path.normpath(os.path.abspath(d)), os.path.normpath(os.path.abspath(root))):
        return True
    real_root = _real_of_nearest(root)
    real_d = _real_of_nearest(d)
    if case_insensitive_at(real_root):
        real_d, real_root = real_d.lower(), real_root.lower()
    return _inside(real_d, real_root)


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
);
-- Set by the first save and kept by Remove: a one-time migration from a
-- browser only fills a store that has never held a provider, so a browser
-- that kept its old key after a lost reply cannot bring back a key the user
-- has since removed.
CREATE TABLE IF NOT EXISTS meta (k TEXT PRIMARY KEY);
CREATE TRIGGER IF NOT EXISTS provider_saved AFTER INSERT ON provider
BEGIN INSERT OR IGNORE INTO meta (k) VALUES ('saved'); END;"""
COLUMNS = ("api", "base_url", "key_header", "models_url", "model", "name", "api_key")
_UPDATE = ", ".join(f"{c} = excluded.{c}" for c in COLUMNS)
_INSERT = f"INSERT INTO provider (id, {', '.join(COLUMNS)}) VALUES (1, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(id) DO "
SAVE_SQL = {
    # Only into a store that has never held a provider (see meta in SCHEMA).
    "create": (f"INSERT INTO provider (id, {', '.join(COLUMNS)}) SELECT 1, ?, ?, ?, ?, ?, ?, ? "
               "WHERE NOT EXISTS (SELECT 1 FROM meta WHERE k = 'saved') ON CONFLICT(id) DO NOTHING"),
    "same-key": _INSERT + f"UPDATE SET {_UPDATE} WHERE provider.api_key = excluded.api_key",
    "replace": _INSERT + f"UPDATE SET {_UPDATE}",
}


@contextlib.contextmanager
def _db(create: bool):
    """The open database, or None when none exists (nothing saved). `create`
    makes the folder (0700) and the file (0600) first. Any other failure (a
    permission change, a damaged file) is a StoreError, never "nothing saved",
    so the env key cannot quietly take over. secure_delete overwrites a
    replaced or removed key's bytes in place, and the rollback journal is
    deleted at commit (see the module notes on journal_mode)."""
    path = provider_file()
    try:
        if create:
            config_dir().mkdir(parents=True, exist_ok=True, mode=0o700)
            # Create the file 0600 only when it is new. Opening and closing an
            # existing database outside SQLite would drop the POSIX locks
            # another connection in this process holds on it.
            try:
                fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
            except FileExistsError:
                pass
            else:
                os.close(fd)
            # By path, so no descriptor is opened: a restored or copied file
            # with a looser mode is tightened before a key is written into it.
            os.chmod(path, 0o600)
        else:
            os.stat(path)
    except FileNotFoundError:
        if not create:
            yield None
            return
        raise StoreError("The saved provider file cannot be read.") from None
    except OSError:
        raise StoreError("The saved provider file cannot be read.") from None
    try:
        conn = sqlite3.connect(path, timeout=5, isolation_level=None)
    except sqlite3.Error as e:
        raise _store_error("The saved provider file cannot be read.", e) from None
    try:
        try:
            conn.execute("PRAGMA busy_timeout = 5000")
            conn.execute("PRAGMA secure_delete = ON")
            conn.execute("PRAGMA journal_mode = DELETE")
            conn.executescript(SCHEMA)
        except sqlite3.Error as e:
            raise _store_error("The saved provider file cannot be read.", e) from None
        try:
            yield conn
        except sqlite3.Error as e:
            raise _store_error("The saved provider file cannot be used.", e) from None
    finally:
        conn.close()


def _discard_files() -> None:
    """Delete the database and its side files: the way out of a damaged one."""
    path = provider_file()
    for f in (path, *(path.with_name(path.name + x) for x in ("-journal", "-wal", "-shm"))):
        f.unlink(missing_ok=True)


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
    provider checked); "create" only when the store has never held a provider
    (a migration from a browser; one saved and later removed still counts); "same-key" only when none is saved or it holds this same key (a
    key the provider could not check). True when the row was written. A
    checked key may replace a damaged file outright; the other modes may not,
    since they only write when they can see what is there."""
    def attempt() -> bool:
        with _db(True) as conn:
            return conn.execute(SAVE_SQL[mode], _values(cfg)).rowcount > 0
    try:
        return attempt()
    except StoreError as e:
        if mode != "replace" or not e.damaged:
            raise
        _discard_files()
        return attempt()


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
    """Delete the saved provider. True when there was one. A file SQLite calls
    damaged is deleted outright, so Remove recovers from it."""
    try:
        with _db(False) as conn:
            if conn is None:
                return False
            return conn.execute("DELETE FROM provider WHERE id = 1").rowcount > 0
    except StoreError as e:
        if not e.damaged:
            raise
        try:
            _discard_files()
        except OSError:
            raise StoreError("The saved provider file cannot be removed.") from None
        return True


URL_KEY = "Put the API key in the API key field only, not in the base URL, models URL, label or model."


def _carries(value: str, key: str) -> bool:
    """Whether `value` holds `key`, as typed or percent-encoded."""
    if not value or len(key) < 4:
        return False
    return key in value or key in unquote(value) or quote(key, safe="") in value


def public(cfg: dict | None) -> dict | None:
    """The fields of a provider that may leave the server, each passed through
    redact() with the provider's own key: parsing already refuses a key in any
    of them, and this guards anything saved some other way."""
    if not cfg:
        return None
    key = cfg.get("api_key")
    keys = (key, quote(key, safe="")) if isinstance(key, str) and key else ()
    return {k: redact(cfg[k], *keys) for k in PUBLIC_FIELDS if isinstance(cfg.get(k), str) and cfg[k]}


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
    # The URLs are shown back on the page; a key inside one would be too.
    if s["api_key"] and any(_carries(s[k], s["api_key"]) for k in ("base_url", "models_url", "name", "model")):
        raise BadRequest(URL_KEY)
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
