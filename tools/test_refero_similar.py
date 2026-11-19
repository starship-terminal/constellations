"""Tests for tools/refero/index_similar.py: how a `similar` business name
resolves to a style slug, and that the result does not depend on the db's
row order. The db is a temporary file and the dump refresh is patched.
Run with `make test`."""
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
import index_similar  # noqa: E402


def result(*businesses):
    return json.dumps({"designSystem": {"similar": [
        {"business": b, "why": "close"} for b in businesses]}})


# Two styles share the name "Acme Corp"; one style has a unique name whose
# slug differs from the name ("zed-2" for "Zed Studio").
ROWS = [("u1", "acme-one", "Acme Corp", None),
        ("u2", "acme-two", "Acme Corp", None),
        ("u3", "zed-2", "Zed Studio", None),
        ("u4", "viewer", "Viewer", result("Acme Corp", "Zed Studio", "Elsewhere"))]


class NamesTest(unittest.TestCase):
    def test_a_shared_name_is_left_out(self):
        self.assertEqual(index_similar.names_by_lower(ROWS),
                         {"zed studio": "zed-2", "viewer": "viewer"})

    def test_rows_without_a_name_are_ignored(self):
        self.assertEqual(index_similar.names_by_lower([("u", "s", None, None)]), {})


class MainTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.refero = Path(tmp.name)
        patcher = mock.patch.object(index_similar.refero_dump, "refresh")
        patcher.start()
        self.addCleanup(patcher.stop)

    def index(self, rows):
        path = self.refero / "refero.db"
        path.unlink(missing_ok=True)
        db = sqlite3.connect(path)
        db.execute("CREATE TABLE styles (uuid TEXT PRIMARY KEY, slug TEXT, "
                   "name TEXT, result_json TEXT)")
        db.executemany("INSERT INTO styles VALUES (?,?,?,?)", rows)
        db.commit()
        db.close()
        with mock.patch.object(sys, "argv", ["index_similar.py", "--refero", str(self.refero)]), \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            index_similar.main()
        db = sqlite3.connect(path)
        try:
            return db.execute("SELECT business, matched_slug FROM similar ORDER BY rank").fetchall()
        finally:
            db.close()

    def test_an_ambiguous_name_stays_unlinked_and_a_unique_one_links(self):
        self.assertEqual(self.index(ROWS),
                         [("Acme Corp", None), ("Zed Studio", "zed-2"), ("Elsewhere", None)])
        styles = json.loads((self.refero / "similar.json").read_text())["styles"]
        self.assertEqual([s["slug"] for s in styles[0]["similar"]], [None, "zed-2", None])

    def test_the_links_do_not_depend_on_row_order(self):
        self.assertEqual(self.index(ROWS), self.index(list(reversed(ROWS))))


if __name__ == "__main__":
    unittest.main()
