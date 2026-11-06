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


if __name__ == "__main__":
    unittest.main()
