"""Tests for tools/refero/dump.py, the text dump of refero.db. Run with `make test`."""
import hashlib
import json
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent / "refero"))
import dump  # noqa: E402
import index_similar  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
REAL_DB = ROOT / "refero" / "refero.db"

# A small db that exercises what the real one holds and what it could: a
# TEXT primary key table dumped a file per row, a table without a primary
# key (duplicate rows, mixed types), an AUTOINCREMENT table (sqlite_sequence),
# an index, a view, and a trigger that must not fire while loading.
SCHEMA = """
CREATE TABLE styles (
  uuid TEXT PRIMARY KEY,
  slug TEXT UNIQUE,
  name TEXT,
  n INTEGER,
  score REAL,
  raw BLOB
, tags TEXT);
CREATE TABLE similar (
            uuid TEXT, business TEXT, why TEXT, rank INTEGER,
            matched_slug TEXT);
CREATE TABLE screens (
  entry_type TEXT,     -- 'ios' or 'web'
  entry_id INTEGER,
  colors_json TEXT
);
CREATE TABLE log (id INTEGER PRIMARY KEY AUTOINCREMENT, what TEXT);
CREATE TABLE fetch_errors (uuid TEXT PRIMARY KEY, error TEXT);
CREATE INDEX similar_uuid ON similar (uuid);
CREATE VIEW named AS SELECT slug, name FROM styles WHERE name IS NOT NULL;
CREATE TRIGGER styles_log AFTER INSERT ON styles
  BEGIN INSERT INTO log (what) VALUES ('insert ' || new.slug); END;
"""

STYLES = [
    ("b-2", "beta", "Béta — “quoted”\nline two\r\nCRLF\u2028sep 🚀", 2, 1.0, None, '["x"]'),
    ("a-1", "alpha", None, -9223372036854775808, 0.1 + 0.2, b"\x00\xffblob", None),
    ("c-3", "gamma", "tab\there \\ backslash \"q\"", 9223372036854775807, -1e-300, b"", "[]"),
    ("d-4", "delta", "", 0, float("inf"), None, None),
]
SIMILAR = [
    ("a-1", "Notion", "warm\u2028line\x85sep\x1cend", 2, "notion"),
    ("a-1", "Linear", "dense", 1, None),
    ("a-1", "Linear", "dense", 1, None),  # duplicate row: kept
    ("b-2", "Zed", None, 1, "zed"),
    ("b-2", 7, 3.5, None, None),          # types the column affinity keeps
]
SCREENS = [("web", 2, "[[1,2,3]]"), ("ios", 1, None), ("web", 1, "[]")]


def make_db(path: Path, *, wal=False, page_size=8192):
    db = sqlite3.connect(path)
    db.execute(f"PRAGMA page_size={page_size}")
    db.execute("PRAGMA user_version=7")
    db.execute("PRAGMA application_id=1234")
    db.executescript(SCHEMA)
    db.executemany("INSERT INTO styles VALUES (?,?,?,?,?,?,?)", STYLES)
    db.executemany("INSERT INTO similar VALUES (?,?,?,?,?)", SIMILAR)
    db.executemany("INSERT INTO screens VALUES (?,?,?)", SCREENS)
    db.execute("DELETE FROM log WHERE id = 1")  # a gap the sequence remembers
    db.commit()
    if wal:
        db.execute("PRAGMA journal_mode=WAL")
    db.close()


def snapshot(path: Path) -> dict:
    """Everything a reader can observe: PRAGMAs, schema, and every table's
    rows with each value's sqlite type, as a multiset."""
    db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
    try:
        out = {"pragmas": [db.execute(f"PRAGMA {p}").fetchone()[0]
                           for p in dump.PRAGMAS],
               "master": db.execute(
                   "SELECT type, name, tbl_name, sql FROM sqlite_master "
                   "ORDER BY type, name").fetchall()}
        for (t,) in db.execute("SELECT name FROM sqlite_master WHERE type='table'"):
            cols = [r[1] for r in db.execute(f'PRAGMA table_info("{t}")')]
            sel = ", ".join(f'typeof("{c}"), quote("{c}")' for c in cols)
            rows = db.execute(f'SELECT {sel} FROM "{t}"').fetchall()
            out[t] = sorted(rows, key=repr)
        if any(m[1] == "named" for m in out["master"]):
            out["view"] = sorted(db.execute("SELECT * FROM named").fetchall())
        return out
    finally:
        db.close()


class Tmp(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.tmp = Path(tmp.name)
        self.a = self.tmp / "a" / "refero.db"
        self.b = self.tmp / "b" / "refero.db"
        self.a.parent.mkdir()
        self.b.parent.mkdir()

    def copy_dump(self, src: Path, dst: Path):
        shutil.copytree(dump.dump_dir(src), dump.dump_dir(dst))


class RoundTripTest(Tmp):
    def test_load_of_a_dump_answers_every_query_the_same(self):
        for wal in (False, True):
            with self.subTest(wal=wal):
                make_db(self.a, wal=wal)
                dump.write(self.a, quiet=True)
                self.copy_dump(self.a, self.b)
                dump.load(self.b, quiet=True)
                self.assertEqual(snapshot(self.a), snapshot(self.b))
                shutil.rmtree(self.a.parent)
                shutil.rmtree(self.b.parent)
                self.a.parent.mkdir()
                self.b.parent.mkdir()

    def test_pragmas_carry_over(self):
        make_db(self.a, wal=True)
        dump.write(self.a, quiet=True)
        self.copy_dump(self.a, self.b)
        dump.load(self.b, quiet=True)
        db = sqlite3.connect(self.b)
        self.assertEqual([db.execute(f"PRAGMA {p}").fetchone()[0] for p in
                          ("page_size", "journal_mode", "user_version", "application_id")],
                         [8192, "wal", 7, 1234])
        db.close()

    def test_the_trigger_does_not_fire_and_the_sequence_survives(self):
        make_db(self.a)
        dump.write(self.a, quiet=True)
        self.copy_dump(self.a, self.b)
        dump.load(self.b, quiet=True)
        db = sqlite3.connect(self.b)
        self.assertEqual(db.execute("SELECT COUNT(*) FROM log").fetchone()[0], 3)
        self.assertEqual(db.execute("SELECT seq FROM sqlite_sequence").fetchone()[0], 4)
        db.close()

    def test_loading_the_same_dump_twice_gives_the_same_bytes(self):
        make_db(self.a)
        dump.write(self.a, quiet=True)
        root = dump.dump_dir(self.a)
        dump.build(root, self.tmp / "one.db")
        dump.build(root, self.tmp / "two.db")
        self.assertEqual((self.tmp / "one.db").read_bytes(),
                         (self.tmp / "two.db").read_bytes())
        # Loaded over a live db, only the header's counters move: the file
        # change counter (24), the schema cookie (40), version-valid-for (92).
        self.copy_dump(self.a, self.b)
        dump.load(self.b, quiet=True)
        first = bytearray(self.b.read_bytes())
        dump.load(self.b, quiet=True)
        second = bytearray(self.b.read_bytes())
        for buf in (first, second):
            buf[24:28] = buf[40:44] = buf[92:96] = b"\0\0\0\0"
        self.assertEqual(first, second)

    def test_a_loaded_db_dumps_to_the_same_text(self):
        make_db(self.a)
        dump.write(self.a, quiet=True)
        self.copy_dump(self.a, self.b)
        dump.load(self.b, quiet=True)
        self.assertEqual(dump.render(self.a), dump.render(self.b))
        self.assertEqual(dump.compare(self.b), [])

    def test_load_keeps_a_backup_of_the_db_it_replaces(self):
        make_db(self.a)
        dump.write(self.a, quiet=True)
        before = snapshot(self.a)
        dump.load(self.a, quiet=True)
        self.assertEqual(snapshot(self.a.parent / ".work" / "refero.db.bak"), before)


class LayoutTest(Tmp):
    def setUp(self):
        super().setUp()
        make_db(self.a)
        dump.write(self.a, quiet=True)
        self.root = dump.dump_dir(self.a)

    def test_layout(self):
        files = sorted(p.relative_to(self.root).as_posix()
                       for p in self.root.rglob("*") if p.is_file())
        self.assertEqual(files, [
            "fetch_errors.jsonl", "log.jsonl", "schema.sql", "screens.jsonl",
            "similar.jsonl", "sqlite_sequence.jsonl",
            "styles/_table", "styles/a-1.json", "styles/b-2.json", "styles/c-3.json",
            "styles/d-4.json"])

    def test_rows_are_sorted_one_per_line(self):
        lines = (self.root / "similar.jsonl").read_text().split("\n")[:-1]
        self.assertEqual([json.loads(l)["business"] for l in lines],
                         ["Linear", "Linear", "Notion", "7", "Zed"])
        screens = [json.loads(l) for l in
                   (self.root / "screens.jsonl").read_text().split("\n")[:-1]]
        self.assertEqual([(s["entry_type"], s["entry_id"]) for s in screens],
                         [("ios", 1), ("web", 1), ("web", 2)])

    def test_a_row_file_holds_one_column_per_line_with_types_kept(self):
        # Newlines inside a value are escaped, so lines are columns.
        # (U+2028 stays raw: only \n counts as a line break, as in git.)
        self.assertEqual((self.root / "styles" / "b-2.json").read_text().count("\n"), 2 + 7)
        row = json.loads((self.root / "styles" / "a-1.json").read_text())
        self.assertEqual(row["raw"], {"$blob": "AP9ibG9i"})
        self.assertEqual(row["score"], 0.1 + 0.2)
        self.assertIn('"score": 1.0', (self.root / "styles" / "b-2.json").read_text())

    def test_schema_holds_the_pragmas_then_the_ddl_verbatim(self):
        text = (self.root / "schema.sql").read_text()
        self.assertIn("PRAGMA page_size=8192;", text)
        self.assertIn("  entry_type TEXT,     -- 'ios' or 'web'\n", text)
        self.assertLess(text.index("CREATE TABLE styles"), text.index("CREATE TRIGGER"))

    def test_the_files_are_plain_lf_text(self):
        for p in self.root.rglob("*"):
            if p.is_file():
                data = p.read_bytes()
                self.assertNotIn(b"\r", data, p.name)
                data.decode("utf-8")

    def test_a_rewrite_with_nothing_changed_touches_nothing(self):
        self.assertEqual(dump.write(self.a, quiet=True), 0)

    def test_a_deleted_row_deletes_its_file(self):
        db = sqlite3.connect(self.a)
        db.execute("DELETE FROM styles WHERE uuid='c-3'")
        db.commit()
        db.close()
        (self.root / "styles" / ".DS_Store").write_text("finder")
        self.assertEqual(dump.write(self.a, quiet=True), 1)
        self.assertFalse((self.root / "styles" / "c-3.json").exists())
        self.assertEqual(dump.compare(self.a), [])

    def test_compare_names_what_disagrees(self):
        self.assertEqual(dump.compare(self.a), [])
        db = sqlite3.connect(self.a)
        db.execute("UPDATE styles SET name='new' WHERE uuid='b-2'")
        db.execute("INSERT INTO similar VALUES ('d-4', 'X', NULL, 1, NULL)")
        db.commit()
        db.close()
        (self.root / "styles" / "zz.json").write_text("{}")
        problems = "\n".join(dump.compare(self.a))
        self.assertIn("1 file(s) not backed by the db in the dump: styles/zz.json", problems)
        self.assertIn("2 file(s) out of date in the dump: similar.jsonl, styles/b-2.json",
                      problems)
        self.assertIn("make refero-db", problems)


class MergeTest(Tmp):
    """The point of the dump: text that git merges row by row."""

    def setUp(self):
        super().setUp()
        make_db(self.a)
        dump.write(self.a, quiet=True)
        self.root = dump.dump_dir(self.a)

    def test_shuffled_lines_load_and_come_back_canonical(self):
        p = self.root / "similar.jsonl"
        lines = [l + "\n" for l in p.read_text().split("\n")[:-1]]
        p.write_text("".join(reversed(lines)))
        dump.load(self.a, quiet=True)
        self.assertEqual(p.read_text(), "".join(lines))
        self.assertEqual(dump.compare(self.a), [])

    def test_an_unresolved_conflict_is_refused(self):
        p = self.root / "similar.jsonl"
        p.write_text("<<<<<<< ours\n" + p.read_text())
        before = self.a.read_bytes()
        with self.assertRaisesRegex(dump.DumpError, "merge conflict"):
            dump.load(self.a, quiet=True)
        self.assertEqual(self.a.read_bytes(), before)

    def test_a_merged_statement_load_would_not_write_is_refused(self):
        """schema.sql is a merge surface: only what render() writes may run."""
        schema = self.root / "schema.sql"
        good = schema.read_text()
        before = self.a.read_bytes()
        outside = self.tmp / "outside.db"
        for bad in (f"ATTACH DATABASE '{outside}' AS x;",
                    f"PRAGMA x.page_size=1; ATTACH '{outside}' AS y;",
                    "PRAGMA writable_schema=1;",
                    "PRAGMA user_version=7; PRAGMA journal_mode=delete;\nPRAGMA recursive_triggers=ON;",
                    "INSERT INTO styles VALUES (1,2,3,4,5,6,7);",
                    "DELETE FROM similar;",
                    "CREATE TEMP TABLE t (a);"):
            with self.subTest(bad=bad):
                schema.write_text(good + "\n" + bad + "\n")
                with self.assertRaisesRegex(dump.DumpError, "schema.sql: refusing"):
                    dump.load(self.a, quiet=True)
                self.assertFalse(outside.exists())
                self.assertEqual(self.a.read_bytes(), before)
        schema.write_text(good + "\nCREATE UNIQUE INDEX extra ON similar (uuid, rank, business);\n")
        with self.assertRaises(sqlite3.IntegrityError):  # parsed, then the rows break it
            dump.load(self.a, quiet=True)
        schema.write_text(good + "\nCREATE INDEX extra ON similar (business);\n")
        dump.load(self.a, quiet=True)  # an index is a statement render() writes

    def test_a_lost_table_file_is_refused_not_loaded_empty(self):
        before = snapshot(self.a)
        for lost in ("similar.jsonl", "styles"):
            with self.subTest(lost=lost):
                saved = self.tmp / "saved"
                shutil.move(str(self.root / lost), saved)
                with self.assertRaisesRegex(dump.DumpError, "missing"):
                    dump.load(self.a, quiet=True)
                self.assertEqual(snapshot(self.a), before)
                shutil.move(str(saved), self.root / lost)
        (self.root / "fetch_errors.jsonl").write_text("")  # empty file, empty table
        dump.load(self.a, quiet=True)
        self.assertEqual(snapshot(self.a), before)

    def test_a_file_for_no_table_is_refused(self):
        (self.root / "nope.jsonl").write_text("")
        with self.assertRaisesRegex(dump.DumpError, "nope.jsonl"):
            dump.load(self.a, quiet=True)

    def test_a_row_with_the_wrong_columns_is_refused(self):
        p = self.root / "styles" / "a-1.json"
        row = json.loads(p.read_text())
        row["extra"] = 1
        p.write_text(json.dumps(row))
        with self.assertRaisesRegex(dump.DumpError, "columns do not match"):
            dump.load(self.a, quiet=True)

    @unittest.skipUnless(shutil.which("git"), "needs git")
    def test_two_branches_that_change_different_rows_merge_cleanly(self):
        repo = self.tmp / "repo"
        repo.mkdir()
        db_path = repo / "refero.db"
        make_db(db_path)
        dump.write(db_path, quiet=True)

        def git(*args):
            return subprocess.run(
                ["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c",
                 "commit.gpgsign=false", *args],
                cwd=repo, check=True, capture_output=True, text=True).stdout

        def change(sql):
            db = sqlite3.connect(db_path)
            db.executescript(sql)
            db.close()
            dump.write(db_path, quiet=True)

        git("init", "-q", "-b", "main")
        (repo / ".gitignore").write_text("refero.db\n.work/\n")
        git("add", "-A")
        git("commit", "-qm", "base")
        git("checkout", "-qb", "relabel")
        change("UPDATE styles SET tags='[\"y\"]' WHERE uuid='a-1';"
               "INSERT INTO styles VALUES ('e-5','eps','E',5,5.0,NULL,NULL);")
        git("commit", "-qam", "relabel")
        git("add", "-A")
        git("commit", "-qm", "new row", "--allow-empty")
        git("checkout", "-q", "main")
        make_db(db_path.with_name("x.db"))  # main's db as it was at base
        db_path.unlink()
        db_path.with_name("x.db").rename(db_path)
        change("UPDATE styles SET name='Gamma' WHERE uuid='c-3';"
               "INSERT INTO similar VALUES ('d-4','Arc',NULL,1,NULL);")
        git("commit", "-qam", "rename")
        git("merge", "-q", "--no-edit", "relabel")  # raises on a conflict
        dump.load(db_path, quiet=True)
        db = sqlite3.connect(db_path)
        self.assertEqual(db.execute("SELECT tags FROM styles WHERE uuid='a-1'").fetchone(),
                         ('["y"]',))
        self.assertEqual(db.execute("SELECT name FROM styles WHERE uuid='c-3'").fetchone(),
                         ("Gamma",))
        self.assertEqual(db.execute("SELECT COUNT(*) FROM styles").fetchone(), (5,))
        self.assertEqual(db.execute("SELECT COUNT(*) FROM similar").fetchone(), (6,))
        db.close()
        self.assertEqual(git("status", "--porcelain"), "")


class ConcurrencyTest(Tmp):
    def setUp(self):
        super().setUp()
        make_db(self.a)
        dump.write(self.a, quiet=True)
        self.root = dump.dump_dir(self.a)

    def test_load_waits_for_an_open_write_and_open_connections_see_the_rebuild(self):
        writer = sqlite3.connect(self.a, check_same_thread=False)
        writer.execute("BEGIN IMMEDIATE")
        writer.execute("UPDATE styles SET name='mid-write' WHERE uuid='a-1'")
        (self.root / "styles" / "d-4.json").unlink()  # the rebuild drops a row
        done, reached = threading.Event(), threading.Event()
        connect = sqlite3.connect

        class Source:
            """The rebuilt temp db's connection: flags the copy into the live
            db just before it starts, so the wait below is measured from the
            blocking call and not from a thread that has not run yet."""
            def __init__(self, conn):
                self.conn = conn

            def backup(self, target):
                reached.set()
                return self.conn.backup(target)

            def __getattr__(self, name):
                return getattr(self.conn, name)

        def connect_spy(database, *args, **kw):
            conn = connect(database, *args, **kw)
            return Source(conn) if ".load.tmp" in str(database) and kw.get("uri") else conn

        with mock.patch.object(dump.sqlite3, "connect", side_effect=connect_spy):
            loader = threading.Thread(
                target=lambda: (dump.load(self.a, quiet=True), done.set()))
            loader.start()
            self.assertTrue(reached.wait(30), "load never reached the copy into the live db")
            time.sleep(0.3)
            self.assertFalse(done.is_set(), "load did not wait for the writer")
            writer.commit()
            loader.join(30)
        self.assertTrue(done.is_set())
        # The writer's connection keeps working, on the rebuilt db.
        writer.execute("UPDATE styles SET name='after' WHERE uuid='b-2'")
        writer.commit()
        self.assertEqual(writer.execute("SELECT COUNT(*) FROM styles").fetchone(), (3,))
        writer.close()
        db = sqlite3.connect(self.a)
        self.assertEqual(db.execute("PRAGMA integrity_check").fetchone(), ("ok",))
        self.assertEqual(db.execute("SELECT name FROM styles WHERE uuid='b-2'").fetchone(),
                         ("after",))
        db.close()

    @unittest.skipIf(dump.fcntl is None, "needs fcntl")
    def test_a_refresh_waits_for_another_holding_the_lock(self):
        db = sqlite3.connect(self.a)
        db.execute("UPDATE styles SET name='newer' WHERE uuid='a-1'")
        db.commit()
        db.close()
        reached = threading.Event()
        flock = dump.fcntl.flock

        def flock_spy(f, op):
            # Flag the worker's own lock request, just before it blocks.
            if op == dump.fcntl.LOCK_EX and threading.current_thread() is t:
                reached.set()
            return flock(f, op)

        with dump._locked(self.a), \
                mock.patch.object(dump.fcntl, "flock", side_effect=flock_spy):
            t = threading.Thread(target=dump.write, args=(self.a, True))
            t.start()
            self.assertTrue(reached.wait(30), "write never asked for the lock")
            time.sleep(0.3)
            self.assertTrue(t.is_alive(), "write did not wait for the lock")
            self.assertNotIn("newer", (self.root / "styles" / "a-1.json").read_text())
        t.join(30)
        self.assertIn("newer", (self.root / "styles" / "a-1.json").read_text())


class RefreshTest(Tmp):
    def test_refresh_never_raises(self):
        dump.refresh(self.a)  # no db: nothing to do
        self.assertFalse(dump.dump_dir(self.a).exists())
        self.a.write_text("version https://git-lfs.github.com/spec/v1\n")
        dump.refresh(self.a)  # an LFS pointer: nothing to do
        self.assertFalse(dump.dump_dir(self.a).exists())
        self.a.write_text("not a database at all, but long enough to not be empty")
        with mock.patch("sys.stderr"):
            dump.refresh(self.a)

    def test_index_similar_refreshes_the_dump(self):
        refero = self.a.parent
        db = sqlite3.connect(self.a)
        db.execute("CREATE TABLE styles (uuid TEXT PRIMARY KEY, slug TEXT, "
                   "name TEXT, result_json TEXT)")
        db.execute("INSERT INTO styles VALUES ('u1', 'acme', 'Acme', ?)", (json.dumps(
            {"designSystem": {"similar": [{"business": "Acme", "why": "self"}]}}),))
        db.commit()
        db.close()
        with mock.patch.object(sys, "argv", ["index_similar.py", "--refero", str(refero)]), \
             mock.patch("sys.stdout"):
            index_similar.main()
        self.assertIn('"matched_slug":"acme"',
                      (dump.dump_dir(self.a) / "similar.jsonl").read_text())
        self.assertEqual(dump.compare(self.a), [])


def _readable(path: Path) -> bool:
    try:
        db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
        db.execute("SELECT 1 FROM styles LIMIT 1")
        db.close()
        return True
    except sqlite3.Error:
        return False


@unittest.skipUnless(REAL_DB.is_file() and _readable(REAL_DB)
                     and (dump.dump_dir(REAL_DB) / "schema.sql").is_file(),
                     "needs refero.db from git lfs pull and its committed dump")
class RealDbTest(Tmp):
    def test_the_committed_dump_loads_back_to_the_real_db(self):
        self.copy_dump(REAL_DB, self.b)
        dump.load(self.b, quiet=True)

        def digest(path):
            return hashlib.sha256(repr(snapshot(path)).encode()).hexdigest()
        self.assertEqual(digest(REAL_DB), digest(self.b))


if __name__ == "__main__":
    unittest.main()
