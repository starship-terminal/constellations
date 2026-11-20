"""Tests for tools/refero/check.py. Run with `make test`."""
import json
import os
import shutil
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent / "refero"))
import check as refero_check  # noqa: E402
import dump as refero_dump  # noqa: E402


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
        (folder / "meta.json").write_text(json.dumps(row))
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
        refero_dump.write(self.refero / "refero.db", quiet=True)

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

    def test_a_dump_that_disagrees_with_the_db_fails(self):
        self.make(["alpha"])
        db = sqlite3.connect(self.refero / "refero.db")
        db.execute("UPDATE styles SET tagline='changed'")
        db.commit()
        db.close()
        problems = refero_check.check(self.refero)
        self.assertTrue(any("out of date in the dump: styles/u-alpha.json" in p
                            for p in problems), problems)
        refero_dump.write(self.refero / "refero.db", quiet=True)
        self.assertFalse(any(".dump" in p for p in refero_check.check(self.refero)))

    def test_a_missing_dump_fails(self):
        self.make(["alpha"])
        shutil.rmtree(self.refero / ".dump")
        self.assertIn("refero/.dump/ is missing; run make refero-dump",
                      refero_check.check(self.refero))

    def test_the_dump_folder_is_not_a_style_folder(self):
        self.make(["alpha"])
        self.assertTrue((self.refero / ".dump" / "schema.sql").is_file())
        self.assertEqual(refero_check.check(self.refero), [])

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


def git_router(base, branch, fail=False):
    """A stand-in for subprocess.run that answers `git show <ref>:catalog.json` by
    ref, as the Check workflow's fetched origin/main and refs/pr-head do."""
    def run(args, **kwargs):
        if fail:
            raise refero_check.catalog.subprocess.CalledProcessError(128, args)
        ref, _, path = args[-1].partition(":")
        assert args[:2] == ["git", "show"] and path == "catalog.json", args
        rows = {"origin/main": base, "refs/pr-head": branch}[ref]
        return mock.Mock(stdout=json.dumps({"systems": rows}), returncode=0)
    return run


class CoverageLagTest(unittest.TestCase):
    """On a pull request coverage.json may leave out packages the merge adds, and is
    otherwise re-derived from the merge's catalog, never trusted from the branch."""

    def setUp(self):
        self.directory = {"web_sites": [
            {"name": "Alpha", "domain": "alpha.example", "id": "1"},
            {"name": "Beta", "domain": "beta.example", "id": "2"},
            {"name": "Newer", "domain": "newer.example", "id": "3"},
        ], "ios_apps": []}
        self.alpha = {"slug": "alpha", "name": "Alpha", "url": "https://alpha.example"}
        self.beta = {"slug": "beta", "name": "Beta", "url": "https://beta.example"}
        self.newer = {"slug": "newer", "name": "Newer", "url": "https://newer.example"}  # landed on main later
        self.added = {"slug": "added", "name": "Added", "url": "https://added.example"}  # this pull request's
        self.base = [self.alpha, self.beta, self.newer]
        self.branch = [self.alpha, self.beta, self.added]
        self.head = [self.alpha, self.beta, self.newer, self.added]

    def build(self, rows):
        return refero_check.coverage_mod.build(self.directory, {"systems": rows})

    def matches(self, actual, head=None, base=None, branch=None, env=None, fail=False):
        env = {"GITHUB_BASE_REF": "main", "GITHUB_HEAD_SHA": "refs/pr-head"} if env is None else env
        head_catalog = {"systems": head or self.head}
        run = git_router(base or self.base, branch or self.branch, fail)
        with mock.patch.dict(os.environ, env, clear=True), \
                mock.patch.object(refero_check.catalog.subprocess, "run", run):
            return refero_check.coverage_matches_base(
                self.directory, head_catalog, actual, self.build(head_catalog["systems"]))

    def test_a_file_that_lags_main_or_this_pull_request_is_accepted(self):
        for subset in ([self.alpha, self.beta], [self.alpha, self.beta, self.added],
                       [self.alpha, self.beta, self.newer]):
            self.assertTrue(self.matches(self.build(subset)), [s["slug"] for s in subset])

    def test_hand_edits_are_rejected_without_any_domain_moving(self):
        # The branch's own regenerated file, edited by hand. No domain moves between
        # matched and missing, so only a whole-file comparison catches these.
        regenerated = self.build(self.branch)
        for edit in (lambda d: d["totals"].__setitem__("system_packages", 99),
                     lambda d: d["totals"].__setitem__("catalog_entries", 999),
                     lambda d: d.__setitem__("about", "hand written"),
                     lambda d: d["matched"]["alpha.example"]["catalog"][0].__setitem__("name", "Renamed"),
                     lambda d: d["missing"].pop("newer.example"),
                     # A fake row in a second group for a domain another group holds.
                     lambda d: d["matched"].__setitem__("newer.example", {"catalog": [], "pkgs": []}),
                     lambda d: d.__setitem__("note", "extra top-level field")):
            edited = json.loads(json.dumps(regenerated))
            edit(edited)
            self.assertFalse(self.matches(edited))

    def test_leaving_out_a_package_the_branch_and_main_share_is_rejected(self):
        self.assertFalse(self.matches(self.build([self.alpha, self.added])))

    def test_a_removed_package_still_named_is_rejected(self):
        # This pull request removes beta and adds added, keeping the base file.
        head, branch = [self.alpha, self.newer, self.added], [self.alpha, self.added]
        self.assertFalse(self.matches(self.build(self.base), head=head, branch=branch))
        self.assertTrue(self.matches(self.build([self.alpha, self.added]), head=head, branch=branch))

    def test_an_edited_existing_row_is_rejected(self):
        edited = json.loads(json.dumps(self.head))
        edited[0]["name"] = "Alpha edited"
        self.assertFalse(self.matches(self.build([self.alpha, self.beta]), head=edited))

    def test_no_pull_request_or_an_unreadable_ref_keeps_the_exact_rule(self):
        prior = self.build([self.alpha, self.beta])
        self.assertFalse(self.matches(prior, env={}))
        self.assertFalse(self.matches(prior, env={"GITHUB_BASE_REF": "main"}))
        self.assertFalse(self.matches(prior, fail=True))
        self.assertFalse(self.matches(prior, base=[{"name": "no slug"}]))


class CoverageSameRowsTest(unittest.TestCase):
    def setUp(self):
        CoverageLagTest.setUp(self)
        self.prior = refero_check.coverage_mod.build(self.directory, {"systems": [self.alpha, self.beta]})

    def test_the_same_rows_in_another_order_are_equal(self):
        shared = {"slug": "shared", "name": "Shared", "url": "https://alpha.example"}
        first = refero_check.coverage_mod.build(self.directory, {"systems": [self.alpha, shared]})
        reordered = refero_check.coverage_mod.build(self.directory, {"systems": [shared, self.alpha]})
        self.assertNotEqual(first, reordered)
        self.assertTrue(refero_check.coverage_same_rows(first, reordered))

    def test_a_changed_package_field_total_or_row_differs(self):
        for edit in (lambda d: d["matched"]["alpha.example"]["pkgs"][0].__setitem__("name", "Renamed"),
                     lambda d: d["totals"].__setitem__("matched_domains", 0),
                     lambda d: d["matched"]["alpha.example"].__setitem__("pkgs", [{"slug": "other"}])):
            edited = json.loads(json.dumps(self.prior))
            edit(edited)
            self.assertFalse(refero_check.coverage_same_rows(self.prior, edited))


if __name__ == "__main__":
    unittest.main()
