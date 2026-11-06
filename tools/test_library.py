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
