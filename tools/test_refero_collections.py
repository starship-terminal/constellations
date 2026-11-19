"""Tests for tools/refero/fetch_collections.py's store writes: the store is
rebuilt from the pages fetched, so a run that fetched only some of them must
write nothing. The sitemap and page fetches are patched; refero.db and
collections.json are temporary. Run with `make test`."""
import io
import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import fetch_collections  # noqa: E402

BASE = fetch_collections.BASE
UUID_A = "00000000-0000-0000-0000-00000000000a"
UUID_B = "00000000-0000-0000-0000-00000000000b"
PAGES = {f"{BASE}/collections/dark": ("Dark", "Dark styles", [{"heading": "One", "uuids": [UUID_A]}]),
         f"{BASE}/collections/calm": ("Calm", "Calm styles", [{"heading": None, "uuids": [UUID_B]}])}


def sitemap(urls):
    return ("<urlset>" + "".join(f"<url><loc>{u}</loc></url>" for u in urls)
            + "</urlset>").encode()


class CollectionsStoreTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.db_path = Path(tmp.name) / "refero.db"
        self.out = Path(tmp.name) / "collections.json"
        for patcher in (mock.patch.object(fetch_collections, "DB", self.db_path),
                        mock.patch.object(fetch_collections, "OUT", self.out),
                        mock.patch.object(fetch_collections.refero_dump, "refresh")):
            self.refresh = patcher.start()
            self.addCleanup(patcher.stop)
        db = sqlite3.connect(self.db_path)
        db.execute("CREATE TABLE styles (uuid TEXT PRIMARY KEY, slug TEXT)")
        db.executemany("INSERT INTO styles VALUES (?,?)", [(UUID_A, "alpha"), (UUID_B, "beta")])
        db.commit()
        db.close()

    def run_main(self, *argv, urls=tuple(PAGES), failing=()):
        def fetch_page(url):
            if url in failing:
                raise OSError("timed out")
            return PAGES[url]
        argv = ["fetch_collections.py", "--workers", "1", *argv]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(fetch_collections, "get", return_value=sitemap(urls)), \
             mock.patch.object(fetch_collections, "fetch_page", side_effect=fetch_page), \
             mock.patch("sys.stdout", new_callable=io.StringIO) as out, \
             mock.patch("sys.stderr", new_callable=io.StringIO):
            try:
                fetch_collections.main()
                code = None
            except SystemExit as ex:
                code = ex.code
        return code, out.getvalue()

    def stored(self):
        db = sqlite3.connect(self.db_path)
        try:
            return (sorted(r[0] for r in db.execute("SELECT slug FROM collections")),
                    db.execute("SELECT count(*) FROM collection_styles").fetchone()[0])
        finally:
            db.close()

    def test_a_full_run_writes_every_collection(self):
        code, _ = self.run_main()
        self.assertIsNone(code)
        self.assertEqual(self.stored(), (["calm", "dark"], 2))
        doc = json.loads(self.out.read_text())
        self.assertEqual(doc["count"], 2)
        self.assertEqual(doc["collections"][0]["sections"][0]["styles"],
                         [{"uuid": UUID_A, "slug": "alpha"}])
        self.refresh.assert_called_once()

    def test_a_failed_page_exits_nonzero_and_keeps_the_store(self):
        self.run_main()
        before = self.out.read_text()
        code, _ = self.run_main(failing={f"{BASE}/collections/calm"})
        self.assertIn("failed 1 pages: calm", code)
        self.assertIn("store left unchanged", code)
        self.assertEqual(self.stored(), (["calm", "dark"], 2))
        self.assertEqual(self.out.read_text(), before)
        self.assertEqual(self.refresh.call_count, 1)  # only the first, full run

    def test_limit_is_a_dry_run(self):
        self.run_main()
        before = self.out.read_text()
        code, out = self.run_main("--limit", "1")
        self.assertIsNone(code)
        self.assertIn("dry run", out)
        self.assertEqual(self.stored(), (["calm", "dark"], 2))
        self.assertEqual(self.out.read_text(), before)
        self.assertEqual(self.refresh.call_count, 1)

    def test_a_dry_run_on_a_fresh_db_creates_no_tables(self):
        code, _ = self.run_main("--limit", "1")
        self.assertIsNone(code)
        db = sqlite3.connect(self.db_path)
        try:
            tables = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        finally:
            db.close()
        self.assertEqual(tables, ["styles"])
        self.assertFalse(self.out.exists())
        self.refresh.assert_not_called()

    def test_an_empty_sitemap_writes_nothing(self):
        code, _ = self.run_main(urls=())
        self.assertIn("no collection pages", code)
        self.assertFalse(self.out.exists())
        self.refresh.assert_not_called()


if __name__ == "__main__":
    unittest.main()
