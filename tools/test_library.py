"""Tests for server/library.py, the tool layer behind the chat and MCP.
web/lib/chat/library.ts is its twin; a fix here lands there too. Run with
`make test`."""
import importlib.util
import unittest
from pathlib import Path

SERVER = Path(__file__).resolve().parent.parent / "server"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, SERVER / path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


library = _load("agent_library_test", "library.py")


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


if __name__ == "__main__":
    unittest.main()
