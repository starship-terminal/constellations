"""Tests that the refero derived-table rebuilds (index_similar.py's `similar`,
fetch_screens.py's `screens`) are one transaction: an insert that fails
leaves the old table and its rows. The db is a temporary file, the API is
patched and the dump refresh is patched. Run with `make test`."""
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
import fetch_screens  # noqa: E402
import index_similar  # noqa: E402


class Tmp(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.refero = Path(tmp.name)
        self.db_path = self.refero / "refero.db"
        for mod in (index_similar, fetch_screens):
            patcher = mock.patch.object(mod.refero_dump, "refresh")
            patcher.start()
            self.addCleanup(patcher.stop)

    def rows(self, table):
        db = sqlite3.connect(self.db_path)
        try:
            return db.execute(f"SELECT * FROM {table}").fetchall()
        finally:
            db.close()

    def run_main(self, mod, argv):
        with mock.patch.object(sys, "argv", argv), \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            mod.main()


def similar_result(why):
    return json.dumps({"designSystem": {"similar": [{"business": "Zed", "why": why}]}})


class SimilarTransactionTest(Tmp):
    def setUp(self):
        super().setUp()
        db = sqlite3.connect(self.db_path)
        db.execute("CREATE TABLE styles (uuid TEXT PRIMARY KEY, slug TEXT, name TEXT, result_json TEXT)")
        db.execute("INSERT INTO styles VALUES ('u1', 'zed', 'Zed', ?)", (similar_result("close"),))
        db.commit()
        db.close()
        self.argv = ["index_similar.py", "--refero", str(self.refero)]

    def test_a_failed_insert_keeps_the_old_table(self):
        self.run_main(index_similar, self.argv)
        before = self.rows("similar")
        self.assertEqual(before, [("u1", "Zed", "close", 1, "zed")])
        db = sqlite3.connect(self.db_path)
        # A `why` that is an object cannot bind: the INSERT fails mid-rebuild.
        db.execute("UPDATE styles SET result_json=?", (similar_result({"not": "text"}),))
        db.commit()
        db.close()
        with self.assertRaises(sqlite3.Error):
            self.run_main(index_similar, self.argv)
        self.assertEqual(self.rows("similar"), before)


class ScreensTransactionTest(Tmp):
    def api(self, page_id):
        record = {"id": 1, "name": "Acme", "domain": "acme.example",
                  "screenshots": [{"uuid": "s1", "url": ["https://cdn/s1.jpg"],
                                   "thumbnail_url": "https://cdn/t1.jpg",
                                   "page_url": "https://acme.example/", "page_id": page_id,
                                   "colors": [[1, 2, 3]], "created_at": "2026-01-01"}]}

        def get(url):
            records = [record] if "/sites/" in url else []
            return json.dumps({"records": records}).encode()
        return mock.patch.object(fetch_screens.fetch, "get", side_effect=get)

    def test_a_failed_insert_keeps_the_old_table(self):
        argv = ["fetch_screens.py", "--refero", str(self.refero)]
        with self.api(7):
            self.run_main(fetch_screens, argv)
        before = self.rows("screens")
        self.assertEqual(len(before), 1)
        directory = (self.refero / "directory.json").read_text()
        with self.api({"not": "an id"}), self.assertRaises(sqlite3.Error):
            self.run_main(fetch_screens, argv)
        self.assertEqual(self.rows("screens"), before)
        self.assertEqual((self.refero / "directory.json").read_text(), directory)


if __name__ == "__main__":
    unittest.main()
