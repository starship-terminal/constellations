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


class ViewMediaTest(unittest.TestCase):
    def test_accepts_the_url_list_media_returns(self):
        item = library.call("list_media", {"slug": "linear"})["items"][0]
        self.assertTrue(item["url"].startswith("/media/systems/linear/"), item)
        out = library.call("view_media", {"slug": "linear", "path": item["url"]})
        self.assertEqual(out["_image"]["url"], item["url"])
        rel = item["url"][len("/media/systems/linear/"):]
        for form in (rel, "systems/linear/" + rel, "/systems/linear/" + rel, "media/systems/linear/" + rel):
            self.assertEqual(library.call("view_media", {"slug": "linear", "path": form})["_image"]["url"],
                             item["url"], form)

    def test_media_url_still_bounded(self):
        for bad in ("/media/systems/linear/../polaris/README.md", "/media/systems/polaris/icon.png",
                    "/media/systems/linear/%2e%2e/polaris/icon.png"):
            with self.assertRaises(library.ToolError, msg=bad):
                library.call("view_media", {"slug": "linear", "path": bad})

    def test_site_url_quotes_like_encode_uri_component(self):
        self.assertEqual(library._site_url(library.ROOT / "systems" / "x" / "a b(1)!.png"),
                         "/media/systems/x/a%20b(1)!.png")


class ReadDocPagingTest(unittest.TestCase):
    def test_long_file_pages_back_together(self):
        whole = (library.ROOT / "systems" / "claude" / "tokens.json").read_text(errors="replace")
        self.assertGreater(len(whole), library.DOC_CAP)
        page = library.call("read_doc", {"slug": "claude", "path": "tokens.json"})
        self.assertTrue(page["truncated"])
        self.assertEqual((page["offset"], page["length"], page["nextOffset"]), (0, len(whole), library.DOC_CAP))
        text = page["text"]
        while page["truncated"]:
            page = library.call("read_doc", {"slug": "claude", "path": "tokens.json",
                                             "offset": page["nextOffset"]})
            text += page["text"]
        self.assertEqual(text, whole)
        self.assertNotIn("nextOffset", page)

    def test_short_file_keeps_the_old_shape(self):
        slug = next(e["slug"] for e in library._catalog()["systems"]
                    if len((library.ROOT / e["entry"]).read_text(errors="replace")) < library.DOC_CAP)
        page = library.call("read_doc", {"slug": slug})
        self.assertEqual(page["path"], f"systems/{slug}/README.md")
        self.assertFalse(page["truncated"])
        self.assertEqual(page["offset"], 0)
        past = library.call("read_doc", {"slug": slug, "offset": page["length"] + 10})
        self.assertEqual((past["text"], past["truncated"]), ("", False))
        with self.assertRaises(library.ToolError):
            library.call("read_doc", {"slug": "linear", "offset": -1})

    def test_empty_path_means_the_readme(self):
        self.assertEqual(library.call("read_doc", {"slug": "linear", "path": ""})["path"],
                         "systems/linear/README.md")


class FileBoundsTest(unittest.TestCase):
    """A fake checkout in a temp dir: one package with a symlink out, a symlink
    into raw/, private folders and a symlinked screenshot."""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name).resolve()
        pkg = root / "systems" / "fake"
        for rel in ("README.md", "raw/reading.json", "fonts/f.css", ".hidden/a.md",
                    "tools/capture/out/x.md", "screenshots/a.png", "screenshots/sub/b.png"):
            (pkg / rel).parent.mkdir(parents=True, exist_ok=True)
            (pkg / rel).write_text("x")
        (root / "secret.md").write_text("outside")
        os.symlink("../../secret.md", pkg / "out.md")
        os.symlink("raw/reading.json", pkg / "alias.json")
        os.symlink("../../../secret.md", pkg / "screenshots" / "c.png")
        self.saved = library.ROOT
        library.ROOT = root
        self.entry = {"slug": "fake"}

    def tearDown(self):
        library.ROOT = self.saved
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

    def test_walk_skips_symlinks_and_sorts_by_path(self):
        files = library._walk_files(library._pkg_dir(self.entry) / "screenshots")
        self.assertEqual([p.name for p in files], ["a.png", "b.png"])


if __name__ == "__main__":
    unittest.main()
