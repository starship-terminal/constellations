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


if __name__ == "__main__":
    unittest.main()
