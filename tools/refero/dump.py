#!/usr/bin/env python3
"""Dump refero.db to line-oriented text, and load it back.

    python3 tools/refero/dump.py dump  [--db PATH]   # db -> refero/.dump/
    python3 tools/refero/dump.py load  [--db PATH]   # refero/.dump/ -> fresh db
    python3 tools/refero/dump.py check [--db PATH]   # exit 1 if they disagree

refero.db stays the canonical store every reader opens. The dump beside it
is the merge surface: git cannot merge two versions of a binary sqlite file,
but it can merge text, so on a refero.db conflict you take either side of the
db, merge the dump as text and rebuild the db with `load` (refero/README.md,
"Merging").

Layout of refero/.dump/ (a dot folder, so nothing that walks refero/<slug>/
style folders ever mistakes it for a style):

    schema.sql              the PRAGMAs a fresh file needs to match the db
                            (page_size, auto_vacuum, encoding, journal_mode,
                            user_version, application_id), then every CREATE
                            statement verbatim from sqlite_master
    styles/<uuid>.json      one file per styles row, one column per line: the
                            rows are tens of KB each, so a file per row keeps
                            two branches that touch different styles from
                            ever touching the same file (styles/_table marks
                            the folder, so losing it is an error, not an
                            empty table)
    <table>.jsonl           every other table: one JSON object per row, one
                            row per line

Rows are sorted by primary key, or for a table without one by a natural key
(ORDER_HINTS) and then every column, so the same db always writes the same
bytes. Values keep their sqlite type: TEXT is a JSON string, INTEGER and REAL
JSON numbers (a REAL always carries a decimal point or exponent), NULL is
null and a BLOB is {"$blob": "<base64>"}.

`load` replays schema.sql, inserts the rows in that same sorted order into a
new file next to the db and checks the row counts. A missing table file is
refused (an empty table is an empty file), and so is a conflict marker. The
old db is copied to refero/.work/refero.db.bak, then the new pages are copied
into the live db with the sqlite backup API, which waits for any writer's
open transaction and leaves open connections reading the rebuilt db. Dumps
and loads take refero/.work/dump.lock, so two never interleave.
Building the same dump twice with the same sqlite library gives byte-identical
files, and loading it twice over a live db differs only in the header's
counters (change counter, schema cookie); the db it replaces can differ in bytes (page layout follows its
history, and the header records the sqlite version that wrote it) while
holding the same rows. Rowids of tables without an INTEGER PRIMARY KEY are
not kept: they follow the sorted order. sqlite_stat* (ANALYZE output) is not
dumped.

Every script that writes refero.db calls refresh() when it finishes, and
tools/refero/check.py (part of `make check`) fails when the committed dump
and the db disagree.
"""

import argparse
import base64
import contextlib
import json
import os
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

try:
    import fcntl
except ImportError:  # not POSIX: no cross-process lock
    fcntl = None

ROOT = Path(__file__).resolve().parents[2]
DB = ROOT / "refero" / "refero.db"
DUMP_DIRNAME = ".dump"

# Tables written one file per row (big rows). Every other table is one .jsonl.
ROW_FILE_TABLES = ("styles",)
# Leading sort columns for tables without a primary key. Every column follows
# as a tie-break, so the order is total whatever the hint.
ORDER_HINTS = {
    "similar": ("uuid", "rank"),
    "collection_styles": ("collection_slug", "section", "rank"),
    "screens": ("entry_type", "entry_id", "shot_uuid"),
}
PRAGMAS = ("page_size", "auto_vacuum", "encoding", "journal_mode",
           "user_version", "application_id")
SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
# Written into every file-per-row folder, so the folder exists (git keeps no
# empty folders) and a merge that lost the whole folder is caught. A row file
# never starts with "_" (SAFE_NAME), so it cannot collide.
TABLE_MARK = "_table"


class DumpError(Exception):
    pass


def dump_dir(db_path: Path) -> Path:
    return Path(db_path).parent / DUMP_DIRNAME


# ------------------------------------------------------------------ values

def encode_value(v):
    if isinstance(v, (bytes, bytearray, memoryview)):
        return {"$blob": base64.b64encode(bytes(v)).decode("ascii")}
    return v


def decode_value(v):
    if isinstance(v, dict):
        if set(v) != {"$blob"}:
            raise DumpError(f"unknown encoded value {v!r}")
        return base64.b64decode(v["$blob"])
    if isinstance(v, list):
        raise DumpError(f"a column value cannot be a list: {v!r}")
    return v


def sort_value(v):
    """Python key that orders values the way sqlite's ORDER BY does under
    the BINARY collation: NULL, then numbers, then text (UTF-8 byte order is
    code point order), then blobs. The int/real tag splits 1 from 1.0."""
    if v is None:
        return (0,)
    if isinstance(v, bool):  # never from sqlite; keep it out of the numbers
        raise DumpError("boolean values are not sqlite values")
    if isinstance(v, (int, float)):
        return (1, v, 0 if isinstance(v, int) else 1)
    if isinstance(v, str):
        return (2, v)
    return (3, bytes(v))


def row_key(columns, key_cols):
    # A hint column a schema change dropped is skipped, not an error.
    idx = [columns.index(c) for c in key_cols if c in columns] \
        + list(range(len(columns)))
    return lambda row: tuple(sort_value(row[i]) for i in idx)


# ------------------------------------------------------------------ reading

def _tables(db):
    """[(name, sql)] of user tables in sqlite_master order."""
    out = []
    for name, sql in db.execute(
            "SELECT name, sql FROM sqlite_master WHERE type='table' "
            "ORDER BY rowid"):
        if name.startswith("sqlite_"):
            continue
        if sql and re.match(r"\s*CREATE\s+VIRTUAL\s", sql, re.I):
            raise DumpError(f"virtual table {name} is not supported")
        out.append((name, sql))
    return out


def _columns(db, table):
    info = db.execute(f'PRAGMA table_info("{table}")').fetchall()
    cols = [r[1] for r in info]
    pk = [r[1] for r in sorted((r for r in info if r[5]), key=lambda r: r[5])]
    return cols, pk


def _jsonl(columns, rows):
    return "".join(
        json.dumps(dict(zip(columns, map(encode_value, r))),
                   ensure_ascii=False, separators=(",", ":")) + "\n"
        for r in rows)


def render(db_path: Path) -> dict:
    """{relative path: text} of the whole dump of the db at db_path."""
    db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    try:
        db.execute("BEGIN")  # one read snapshot across every table
        files = {}
        lines = [
            "-- refero.db schema, written by tools/refero/dump.py from the db.",
            "-- Generated: never edit by hand. `make refero-db` rebuilds the",
            "-- db from this folder; `make refero-dump` rewrites it.",
        ]
        for p in PRAGMAS:
            v = db.execute(f"PRAGMA {p}").fetchone()[0]
            if p == "journal_mode":
                v = "wal" if str(v).lower() == "wal" else "delete"
            lines.append(f"PRAGMA {p}={v if isinstance(v, int) else repr(str(v))};")
        objects = db.execute(
            "SELECT type, name, sql FROM sqlite_master "
            "WHERE sql IS NOT NULL ORDER BY rowid").fetchall()
        for typ, name, sql in objects:
            if name.startswith("sqlite_"):
                continue
            lines.append("")
            lines.append(sql.rstrip().rstrip(";") + ";")
        files["schema.sql"] = "\n".join(lines) + "\n"

        tables = _tables(db)
        if db.execute("SELECT 1 FROM sqlite_master "
                      "WHERE name='sqlite_sequence'").fetchone():
            tables.append(("sqlite_sequence", None))
        for table, _ in tables:
            columns, pk = _columns(db, table)
            rows = db.execute(f'SELECT * FROM "{table}"').fetchall()
            if table == "sqlite_sequence":
                pk = ["name"]
            rows.sort(key=row_key(columns, pk or ORDER_HINTS.get(table, ())))
            if table in ROW_FILE_TABLES:
                if len(pk) != 1:
                    raise DumpError(f"{table}: a file per row needs a "
                                    f"single-column primary key")
                i = columns.index(pk[0])
                files[f"{table}/{TABLE_MARK}"] = (
                    f"{table}: one <primary key>.json file per row\n")
                seen = set()
                for r in rows:
                    name = str(r[i])
                    if not SAFE_NAME.match(name) or name.lower() in seen:
                        raise DumpError(f"{table}: primary key {name!r} "
                                        "cannot name a file")
                    seen.add(name.lower())
                    obj = dict(zip(columns, map(encode_value, r)))
                    files[f"{table}/{name}.json"] = json.dumps(
                        obj, ensure_ascii=False, indent=1) + "\n"
            else:
                files[f"{table}.jsonl"] = _jsonl(columns, rows)
        return files
    finally:
        db.close()


def _read_tree(root: Path) -> dict:
    """{relative path: text} of every file in a dump folder. Dot files
    (.DS_Store, a writer's half-written temp file) are not part of it."""
    if not root.is_dir():
        return {}
    out = {}
    for p in sorted(root.rglob("*")):
        rel = p.relative_to(root)
        if p.is_file() and not any(part.startswith(".") for part in rel.parts):
            out[rel.as_posix()] = p.read_text(encoding="utf-8")
    return out


def _expected_name(rel: str, tables) -> bool:
    if rel == "schema.sql":
        return True
    parts = rel.split("/")
    if len(parts) == 2:
        return parts[0] in ROW_FILE_TABLES and parts[0] in tables \
            and (parts[1].endswith(".json") or parts[1] == TABLE_MARK)
    return len(parts) == 1 and rel.endswith(".jsonl") \
        and rel[:-6] in tables and rel[:-6] not in ROW_FILE_TABLES


# ------------------------------------------------------------------ writing

def write_atomic(path: Path, text: str):
    """Write text to path through a temp file unique to the call and a
    rename, mode 0644. Two writers of one path cannot rename each other's
    half-written file, and a failed write leaves no temp file behind. Every
    tools/refero writer uses this one."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.",
                               suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write(text)
        os.chmod(tmp, 0o644)  # mkstemp makes it 0600
        os.replace(tmp, path)
    except BaseException:
        Path(tmp).unlink(missing_ok=True)
        raise


@contextlib.contextmanager
def _locked(db_path: Path):
    """Hold refero/.work/dump.lock: one dump or load at a time across
    processes, so a slower refresh can never write an older snapshot over a
    newer one, and a load never interleaves with a refresh."""
    if fcntl is None:
        yield
        return
    lock = Path(db_path).parent / ".work" / "dump.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def write(db_path: Path = DB, quiet: bool = False) -> int:
    with _locked(db_path):
        return _write(db_path, quiet)


def _write(db_path: Path, quiet: bool) -> int:
    """Bring the dump beside db_path in line with the db. Rewrites only the
    files whose text changed and deletes the ones no row backs any more.
    Returns the number of files written or deleted."""
    root = dump_dir(db_path)
    want = render(db_path)
    have = _read_tree(root)
    changed = 0
    for rel, text in want.items():
        if have.get(rel) != text:
            write_atomic(root / rel, text)
            changed += 1
    for rel in sorted(set(have) - set(want)):
        (root / rel).unlink()
        changed += 1
    for d in sorted((p for p in root.rglob("*") if p.is_dir()), reverse=True):
        if not any(d.iterdir()):
            d.rmdir()
    if not quiet:
        print(f"refero dump: {changed} file(s) updated in {root}")
    return changed


def refresh(db_path: Path = DB) -> None:
    """The hook every refero.db writer calls when it is done. Never raises:
    a failed dump must not turn a finished fetch into a failed one, and
    check.py reports the stale dump anyway."""
    try:
        if Path(db_path).is_file() and not _is_lfs_pointer(Path(db_path)):
            write(db_path)
    except Exception as e:  # noqa: BLE001
        print(f"warning: refero dump not refreshed ({e}); "
              "run make refero-dump", file=sys.stderr)


def compare(db_path: Path = DB, limit: int = 5) -> list[str]:
    """Problems, empty when the committed dump is exactly the db's dump."""
    root = dump_dir(db_path)
    if not root.is_dir():
        return [f"refero/{DUMP_DIRNAME}/ is missing; run make refero-dump"]
    want, have = render(db_path), _read_tree(root)
    missing = sorted(set(want) - set(have))
    extra = sorted(set(have) - set(want))
    differ = sorted(k for k in set(want) & set(have) if want[k] != have[k])
    problems = []
    for label, paths in (("missing from", missing), ("not backed by the db in", extra),
                         ("out of date in", differ)):
        if paths:
            shown = ", ".join(paths[:limit]) + (" …" if len(paths) > limit else "")
            problems.append(f"refero/{DUMP_DIRNAME}: {len(paths)} file(s) "
                            f"{label} the dump: {shown}")
    if problems:
        problems.append(f"refero/{DUMP_DIRNAME} disagrees with refero.db: run "
                        "make refero-dump if the db is right (a writer ran), "
                        "or make refero-db if the dump is (a merge)")
    return problems


# ------------------------------------------------------------------ loading

def _statements(sql_text: str):
    buf = []
    for line in (part + "\n" for part in sql_text.split("\n")):
        if not buf and (not line.strip() or line.lstrip().startswith("--")):
            continue
        buf.append(line)
        stmt = "".join(buf)
        if sqlite3.complete_statement(stmt):
            yield stmt.strip()
            buf = []
    if "".join(buf).strip():
        raise DumpError("schema.sql ends inside a statement")


# What render() writes into schema.sql, and so all load() will run from it:
# `PRAGMA <one of PRAGMAS>=<integer or quoted string>`, CREATE TABLE, and the
# other objects sqlite_master can hold. schema.sql merges like any text file,
# so anything else (ATTACH, a write, another PRAGMA) is refused, not run.
PRAGMA_STMT = re.compile(r"PRAGMA\s+(\w+)\s*=\s*(?:-?\d+|'[^']*')\s*;?\Z", re.I)
OTHER_OBJECTS = (["CREATE", "INDEX"], ["CREATE", "UNIQUE", "INDEX"],
                 ["CREATE", "VIEW"], ["CREATE", "TRIGGER"])


def parse(root: Path):
    """schema.sql split into (PRAGMA statements, CREATE TABLE statements,
    every other statement: indexes, views, triggers), each in file order.
    Raises DumpError for any statement render() would not have written."""
    schema = (root / "schema.sql").read_text(encoding="utf-8")
    pragmas, tables, others = [], [], []
    for stmt in _statements(schema):
        kw = [w.upper() for w in stmt.split(None, 3)[:3]]
        if kw[0] == "PRAGMA":
            m = PRAGMA_STMT.match(stmt)
            if not (m and m.group(1).lower() in PRAGMAS):
                raise DumpError(f"schema.sql: refusing {stmt[:80]!r}: only "
                                f"PRAGMA {', '.join(PRAGMAS)} may be set")
            pragmas.append(stmt)
        elif kw[:2] == ["CREATE", "TABLE"]:
            tables.append(stmt)
        elif any(kw[:len(head)] == head for head in OTHER_OBJECTS):
            others.append(stmt)
        else:
            raise DumpError(f"schema.sql: refusing {stmt[:80]!r}: only PRAGMAs "
                            "and CREATE TABLE/INDEX/VIEW/TRIGGER statements load")
    return pragmas, tables, others


def _json(text: str, where: str):
    try:
        return json.loads(text)
    except ValueError as e:
        raise DumpError(f"{where} is not JSON ({e}); "
                        "an unresolved merge conflict?") from None


def _load_rows(root: Path, table: str, columns: list):
    def row_of(obj, where):
        if not isinstance(obj, dict) or set(obj) != set(columns):
            raise DumpError(f"{where}: columns do not match the table "
                            f"({sorted(set(obj) ^ set(columns)) if isinstance(obj, dict) else obj!r})")
        return tuple(decode_value(obj[c]) for c in columns)

    rows = []
    if table in ROW_FILE_TABLES:
        d = root / table
        if not (d / TABLE_MARK).is_file():
            raise DumpError(f"{table}/{TABLE_MARK} is missing: the dump of "
                            f"{table} is gone (a bad merge?); refusing to load "
                            "an empty table over the db")
        for p in sorted(d.glob("*.json")):
            rows.append(row_of(_json(p.read_text(encoding="utf-8"),
                                     f"{table}/{p.name}"), f"{table}/{p.name}"))
    else:
        p = root / f"{table}.jsonl"
        if not p.is_file():
            if table == "sqlite_sequence":
                return rows
            raise DumpError(f"{table}.jsonl is missing (a bad merge?); an "
                            "empty table is an empty file, so refusing to load")
        # Split on \n only: str.splitlines() would also break at U+2028,
        # U+0085 and friends, which JSON leaves raw inside strings.
        for n, line in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
            if line.strip():
                where = f"{table}.jsonl:{n}"
                rows.append(row_of(_json(line, where), where))
    return rows


def build(root: Path, out: Path) -> dict:
    """Write a fresh sqlite file at `out` from the dump in `root`.
    Returns {table: row count}."""
    pragmas, tables, others = parse(root)
    if out.exists():
        out.unlink()
    db = sqlite3.connect(out, isolation_level=None)
    try:
        journal = "delete"
        for p in pragmas:
            m = re.match(r"PRAGMA\s+journal_mode\s*=\s*'?(\w+)'?", p, re.I)
            if m:
                journal = m.group(1).lower()
            else:
                db.execute(p)
        db.execute("PRAGMA journal_mode=OFF")
        db.execute("PRAGMA synchronous=OFF")
        db.execute("BEGIN")
        for stmt in tables:
            db.execute(stmt)
        names = [n for n, _ in _tables(db)]
        known = set(names) | {"sqlite_sequence"}
        stray = [rel for rel in _read_tree(root) if not _expected_name(rel, known)]
        if stray:
            raise DumpError(f"files for no table in schema.sql: {', '.join(stray[:5])}")
        counts = {}
        for table in names:
            columns, pk = _columns(db, table)
            rows = _load_rows(root, table, columns)
            rows.sort(key=row_key(columns, pk or ORDER_HINTS.get(table, ())))
            marks = ",".join("?" * len(columns))
            db.executemany(f'INSERT INTO "{table}" VALUES ({marks})', rows)
            counts[table] = len(rows)
        for stmt in others:
            db.execute(stmt)
        if db.execute("SELECT 1 FROM sqlite_master "
                      "WHERE name='sqlite_sequence'").fetchone():
            rows = _load_rows(root, "sqlite_sequence", ["name", "seq"])
            db.execute("DELETE FROM sqlite_sequence")
            db.executemany("INSERT INTO sqlite_sequence VALUES (?,?)",
                           sorted(rows, key=row_key(["name", "seq"], ["name"])))
        db.execute("COMMIT")
        for table, n in counts.items():
            got = db.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
            if got != n:
                raise DumpError(f"{table}: loaded {got} rows, dump holds {n}")
        db.execute(f"PRAGMA journal_mode={journal}")
    finally:
        db.close()
    return counts


def backup(db_path: Path, to: Path) -> None:
    """Copy a db with sqlite's backup API (never cp: a hot journal or WAL
    would be left behind)."""
    to.parent.mkdir(parents=True, exist_ok=True)
    src = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
    dst = sqlite3.connect(to)
    try:
        src.backup(dst)
    finally:
        dst.close()
        src.close()


def load(db_path: Path = DB, quiet: bool = False) -> dict:
    """Rebuild db_path from the dump beside it, then rewrite the dump in its
    canonical form (a text merge can leave lines out of order)."""
    db_path = Path(db_path)
    root = dump_dir(db_path)
    if not (root / "schema.sql").is_file():
        raise DumpError(f"no dump at {root}")
    with _locked(db_path):
        counts = _load(db_path, root, quiet)
        _write(db_path, quiet)
    return counts


def _load(db_path: Path, root: Path, quiet: bool) -> dict:
    tmp = db_path.with_name(f".{db_path.name}.load.tmp")
    try:
        counts = build(root, tmp)
        if db_path.is_file() and not _is_lfs_pointer(db_path):
            bak = db_path.parent / ".work" / f"{db_path.name}.bak"
            backup(db_path, bak)
            if not quiet:
                print(f"previous db kept at {bak}")
            # Copy the new pages into the live file through sqlite rather
            # than swapping the file: the backup takes sqlite's own locks, so
            # it waits for a writer's open transaction to commit, and every
            # connection still open on the db sees the rebuilt content
            # instead of writing on into a replaced file.
            src = sqlite3.connect(f"file:{tmp}?mode=ro", uri=True)
            dst = sqlite3.connect(db_path, timeout=60)
            try:
                dst.execute("PRAGMA busy_timeout=60000")
                src.backup(dst)
            finally:
                dst.close()
                src.close()
        else:
            os.replace(tmp, db_path)
    finally:
        tmp.unlink(missing_ok=True)
    if not quiet:
        print("loaded " + ", ".join(f"{t} {n}" for t, n in counts.items())
              + f" into {db_path}")
    return counts


def _is_lfs_pointer(path: Path) -> bool:
    with open(path, "rb") as f:
        return f.read(64).startswith(b"version https://git-lfs")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("command", choices=("dump", "load", "check"))
    ap.add_argument("--db", type=Path, default=DB,
                    help="the sqlite file (default: refero/refero.db); the "
                         "dump lives in .dump/ beside it")
    args = ap.parse_args()
    try:
        if args.command == "load":
            load(args.db)
            return
        if not args.db.is_file() or _is_lfs_pointer(args.db):
            sys.exit(f"error: {args.db} is missing or a Git LFS pointer; "
                     "run git lfs pull, or make refero-db to build it from the dump")
        if args.command == "dump":
            write(args.db)
        else:
            problems = compare(args.db)
            print("\n".join(problems) if problems else "refero dump ok")
            sys.exit(1 if problems else 0)
    except DumpError as e:
        sys.exit(f"error: {e}")


if __name__ == "__main__":
    main()
