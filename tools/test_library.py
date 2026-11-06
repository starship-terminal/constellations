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


class PlatformFilterTest(unittest.TestCase):
    def _platforms(self, platform):
        hits = library.call("search_styles", {"query": "", "store": "systems", "platform": platform,
                                              "limit": 20})["hits"]
        return {h["platform"] for h in hits}, {h["slug"] for h in hits}

    def test_catalog_platforms_filter(self):
        for platform in ("web", "mobile", "desktop"):
            seen, slugs = self._platforms(platform)
            self.assertEqual(seen, {platform}, platform)
            self.assertTrue(slugs)

    def test_ios_is_an_alias_for_mobile(self):
        self.assertEqual(self._platforms("ios"), self._platforms("mobile"))

    def test_schema_offers_the_catalog_values(self):
        spec = next(s for s in library.SPECS if s["name"] == "search_styles")
        self.assertEqual(set(spec["parameters"]["properties"]["platform"]["enum"]),
                         {"web", "mobile", "desktop", "ios"})


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
