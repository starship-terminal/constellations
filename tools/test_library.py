"""Tests for server/library.py, the tool layer behind the chat and MCP.
web/lib/chat/library.ts is its twin; a fix here lands there too. Run with
`make test`."""
import importlib.util
import os
import tempfile
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent / "server"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, SERVER / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


library = _load("agent_library_test", "library.py")


def _has_refero() -> bool:
    db = library._refero_db()
    if db is None:
        return False
    db.close()
    return True


@unittest.skipUnless(_has_refero(), "refero.db is an LFS pointer here")
class ReferoFieldsTest(unittest.TestCase):
    def test_get_style_tags_are_a_list(self):
        out = library.get_style("linear", "refero")
        self.assertIsInstance(out["tags"], list)
        self.assertTrue(all(isinstance(t, str) for t in out["tags"]))

    def test_search_scores_and_reports_the_host(self):
        hits = library.search_styles("stripe.com", store="refero", limit=5)["hits"]
        self.assertEqual(hits[0]["slug"], "stripe")
        self.assertEqual(hits[0]["src"], "stripe.com")
        # The scheme is not part of what is scored, so it matches nothing.
        self.assertEqual(library.search_styles("https", store="refero")["hits"], [])


class GetTokensPagingTest(unittest.TestCase):
    def _biggest_group(self):
        best = None
        for e in library._catalog()["systems"]:
            for group, n in library.get_tokens(e["slug"])["groups"].items():
                if best is None or n > best[2]:
                    best = (e["slug"], group, n)
        return best

    def test_big_group_pages_instead_of_truncating(self):
        slug, group, n = self._biggest_group()
        page = library.call("get_tokens", {"slug": slug, "group": group})
        self.assertNotIn("partial", page)
        self.assertTrue(page["truncated"])
        self.assertEqual((page["count"], page["offset"]), (n, 0))
        self.assertLessEqual(library._json_size(page), library.RESULT_CAP)
        merged = dict(page["tokens"])
        while page["truncated"]:
            page = library.call("get_tokens", {"slug": slug, "group": group, "offset": page["nextOffset"]})
            self.assertNotIn("partial", page)
            merged.update(page["tokens"])
        self.assertEqual(len(merged), n)
        self.assertNotIn("nextOffset", page)

    def test_small_group_keeps_the_old_shape(self):
        out = library.call("get_tokens", {"slug": "linear", "group": "dark"})
        self.assertFalse(out["truncated"])
        self.assertEqual(len(out["tokens"]), out["count"])
        self.assertEqual(list(out["tokens"]), sorted(out["tokens"]))

    def test_limit_and_bad_values(self):
        out = library.call("get_tokens", {"slug": "linear", "group": "dark", "limit": 3})
        self.assertEqual((len(out["tokens"]), out["nextOffset"]), (3, 3))
        for bad in ({"offset": -1}, {"limit": 0}):
            with self.assertRaises(library.ToolError):
                library.call("get_tokens", {"slug": "linear", "group": "dark", **bad})

    def test_cap_counts_utf8_bytes_of_compact_json(self):
        # Buffer.byteLength(JSON.stringify(...)) in the web twin: '{"a":"é","b":[1,2]}'.
        self.assertEqual(library._json_size({"a": "é", "b": [1, 2]}), 20)


class FileBoundsTest(unittest.TestCase):
    """A fake checkout in a temp dir: one package with a symlink out, a symlink
    into raw/, private folders and a symlinked screenshot."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name).resolve()
        pkg = root / "systems" / "fake"
        for rel in ("README.md", "raw/reading.json", "fonts/f.css", ".hidden/a.md",
                    "tools/capture/out/x.md", "screenshots/a-b.png", "screenshots/a/b.png",
                    "screenshots/.hidden/h.png", "screenshots/raw/r.png", "boards/real/d.png"):
            (pkg / rel).parent.mkdir(parents=True, exist_ok=True)
            (pkg / rel).write_text("x")
        (root / "secret.md").write_text("outside")
        os.symlink("../../secret.md", pkg / "out.md")
        os.symlink("raw/reading.json", pkg / "alias.json")
        os.symlink("../../../secret.md", pkg / "screenshots" / "c.png")
        os.symlink("boards/real", pkg / "icons")
        self.saved = library.ROOT, library._entry
        library.ROOT = root
        library._entry = lambda slug: {"slug": slug}
        self.entry = {"slug": "fake"}

    def tearDown(self):
        library.ROOT, library._entry = self.saved
        self.tmp.cleanup()

    def test_symlink_out_of_the_package_is_refused(self):
        with self.assertRaisesRegex(library.ToolError, "leaves the package"):
            library._bounded(self.entry, "out.md")
        with self.assertRaisesRegex(library.ToolError, "leaves the package"):
            library._bounded(self.entry, "screenshots/c.png")

    def test_private_folders_are_refused_under_any_name(self):
        for rel in ("raw/reading.json", "alias.json", "fonts/f.css", ".hidden/a.md",
                    "tools/capture/out/x.md", "./raw/../raw/reading.json"):
            with self.assertRaisesRegex(library.ToolError, "not readable", msg=rel):
                library._bounded(self.entry, rel)
        self.assertEqual(library._bounded(self.entry, "README.md").name, "README.md")

    def test_walk_skips_symlinks_and_sorts_by_path_string(self):
        shots = library._pkg_dir(self.entry) / "screenshots"
        files = [p.relative_to(shots).as_posix() for p in library._walk_files(shots)]
        # String order puts "a-b.png" before "a/b.png"; sorting Path objects by
        # their parts (the old rglob order) would not. c.png is a symlink.
        self.assertEqual(files, [".hidden/h.png", "a-b.png", "a/b.png", "raw/r.png"])

    def test_list_media_skips_private_folders_and_symlinked_dirs(self):
        urls = [i["url"] for i in library.list_media("fake")["items"]]
        # icons/ is a symlink to boards/real, so d.png is listed once, as a board.
        self.assertEqual(urls, ["/media/systems/fake/screenshots/a-b.png",
                                "/media/systems/fake/screenshots/a/b.png",
                                "/media/systems/fake/boards/real/d.png"])


if __name__ == "__main__":
    unittest.main()
