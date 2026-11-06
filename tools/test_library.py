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


if __name__ == "__main__":
    unittest.main()
