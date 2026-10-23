"""Tests for tools/refero/check.py. Run with `make test`."""
import json
import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "refero"))
import check as refero_check  # noqa: E402


SCHEMA = """
CREATE TABLE styles (uuid TEXT PRIMARY KEY, slug TEXT UNIQUE, name TEXT, tagline TEXT,
 page_url TEXT, source_url TEXT, theme TEXT, extracted_at TEXT, fetched_at TEXT,
 screenshot_url TEXT, video_url TEXT, video_poster_url TEXT, video_detail_url TEXT,
 video_detail_poster_url TEXT, product_type TEXT, design_style TEXT, tags TEXT);
CREATE TABLE fetch_errors (uuid TEXT PRIMARY KEY, page_url TEXT, error TEXT, at TEXT);
"""


class ReferoCheckTest(unittest.TestCase):
    """check() against a refero/ tree built in a temporary directory."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.refero = Path(self.tmp.name) / "refero"
        self.refero.mkdir()

    def tearDown(self):
        self.tmp.cleanup()

    def row(self, slug, name=None):
        return {"uuid": f"u-{slug}", "slug": slug, "name": name or slug.title(),
                "tagline": "tag", "page_url": f"https://p/{slug}",
                "source_url": "https://s.example", "theme": "light",
                "extracted_at": "e", "fetched_at": "f", "screenshot_url": "shot",
                "video_url": None, "video_poster_url": None, "video_detail_url": None,
                "video_detail_poster_url": None, "product_type": "devtools",
                "design_style": "minimal", "tags": ["a"]}

    def make_dir(self, row):
        folder = self.refero / row["slug"]
        folder.mkdir()
        for name in refero_check.STYLE_FILES:
            (folder / name).write_text("{}" if name.endswith("json") else "x")
        meta = {**row, "video_w": None, "video_h": None, "video_ms": None}
        (folder / "meta.json").write_text(json.dumps(meta))
        return folder

    def write_db(self, rows):
        db = sqlite3.connect(self.refero / "refero.db")
        db.executescript(SCHEMA)
        for r in rows:
            db.execute("INSERT INTO styles VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                       (r["uuid"], r["slug"], r["name"], r["tagline"], r["page_url"],
                        r["source_url"], r["theme"], r["extracted_at"], r["fetched_at"],
                        r["screenshot_url"], r["video_url"], r["video_poster_url"],
                        r["video_detail_url"], r["video_detail_poster_url"],
                        r["product_type"], r["design_style"], json.dumps(r["tags"])))
        db.commit()
        db.close()

    def write_catalog(self, rows):
        styles = [{k: r[k] for k in refero_check.CATALOG_FIELDS} for r in rows]
        (self.refero / "catalog.json").write_text(
            json.dumps({"version": 1, "count": len(styles), "styles": styles}))

    def make(self, slugs):
        rows = []
        for slug in slugs:
            row = self.row(slug)
            self.make_dir(row)
            rows.append(row)
        self.write_db(rows)
        self.write_catalog(rows)
        (self.refero / "README.md").write_text(f"{len(slugs)} styles\n")
        return rows

    def test_a_consistent_tree_is_clean(self):
        self.make(["alpha", "beta"])
        self.assertEqual(refero_check.check(self.refero), [])

    def test_a_row_without_a_folder_fails(self):
        self.make(["alpha", "beta"])
        shutil.rmtree(self.refero / "beta")
        problems = refero_check.check(self.refero)
        self.assertIn("refero.db: beta has no refero/beta/ folder", problems)
        self.assertIn("refero/catalog.json: beta has no refero/beta/ folder", problems)

    def test_a_folder_without_a_row_or_entry_fails(self):
        self.make(["alpha"])
        self.make_dir(self.row("beta"))
        problems = refero_check.check(self.refero)
        self.assertIn("refero/beta: no styles row in refero.db", problems)
        self.assertIn("refero/beta: no catalog.json entry", problems)

    def test_a_missing_style_file_fails(self):
        self.make(["alpha"])
        (self.refero / "alpha" / "theme.css").unlink()
        self.assertIn("refero/alpha: theme.css is missing",
                      refero_check.check(self.refero))

    def test_an_unparseable_meta_fails(self):
        self.make(["alpha"])
        (self.refero / "alpha" / "meta.json").write_text("{not json")
        problems = refero_check.check(self.refero)
        self.assertTrue(any("meta.json does not parse" in p for p in problems))

    def test_a_meta_field_mismatch_fails(self):
        rows = self.make(["alpha"])
        folder = self.refero / "alpha"
        meta = json.loads((folder / "meta.json").read_text())
        meta["name"] = "Renamed"
        (folder / "meta.json").write_text(json.dumps(meta))
        self.assertIn("refero/alpha: meta.json name does not match the styles row",
                      refero_check.check(self.refero))

    def test_a_meta_slug_must_equal_the_folder_name(self):
        self.make(["alpha"])
        folder = self.refero / "alpha"
        meta = json.loads((folder / "meta.json").read_text())
        meta["slug"] = "other"
        (folder / "meta.json").write_text(json.dumps(meta))
        problems = refero_check.check(self.refero)
        self.assertIn("refero/alpha: meta.json slug is 'other'", problems)

    def test_a_uuid_shared_by_two_metas_fails(self):
        rows = self.make(["alpha"])
        second = self.row("beta")
        second["uuid"] = rows[0]["uuid"]
        self.make_dir(second)
        self.assertIn(f"uuid {rows[0]['uuid']} appears in more than one meta.json",
                      refero_check.check(self.refero))

    def test_a_nonempty_fetch_errors_fails(self):
        self.make(["alpha"])
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("INSERT INTO fetch_errors VALUES ('u', 'p', 'boom', 'now')")
        db.commit()
        db.close()
        self.assertIn("refero.db: fetch_errors holds 1 rows",
                      refero_check.check(self.refero))

    def test_a_stale_readme_count_fails(self):
        self.make(["alpha"])
        (self.refero / "README.md").write_text("1,999 styles\n")
        self.assertIn("refero/README.md says 1,999 styles; 1 folders exist",
                      refero_check.check(self.refero))

    def test_a_bad_catalog_count_and_shape_fail(self):
        rows = self.make(["alpha"])
        self.write_catalog(rows)
        cat = json.loads((self.refero / "catalog.json").read_text())
        cat["count"] = 5
        (self.refero / "catalog.json").write_text(json.dumps(cat))
        self.assertIn("refero/catalog.json: count 5 != 1 styles",
                      refero_check.check(self.refero))
        (self.refero / "catalog.json").write_text("[]")
        self.assertIn("refero/catalog.json: styles is not a list",
                      refero_check.check(self.refero))
        (self.refero / "catalog.json").write_text('{"styles": [null]}')
        self.assertIn("refero/catalog.json: a styles entry is not an object",
                      refero_check.check(self.refero))

    def test_a_db_that_is_not_sqlite_only_skips_the_db_side(self):
        # A clone without `git lfs pull` holds the pointer file; the folder and
        # catalog checks still run, and the two files are compared directly.
        rows = self.make(["alpha"])
        (self.refero / "refero.db").write_text("version https://git-lfs.github.com/spec/v1\n")
        self.assertEqual(refero_check.check(self.refero), [])
        cat = json.loads((self.refero / "catalog.json").read_text())
        cat["styles"][0]["name"] = "Stale"
        (self.refero / "catalog.json").write_text(json.dumps(cat))
        self.assertIn("refero/catalog.json: alpha name does not match meta.json",
                      refero_check.check(self.refero))


if __name__ == "__main__":
    unittest.main()
