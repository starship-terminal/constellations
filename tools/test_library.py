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


class CatalogReadsTest(unittest.TestCase):
    def test_search_reads_the_catalog_a_fixed_number_of_times(self):
        real, calls = library.catalog.load_catalog, []

        def counting():
            calls.append(1)
            return real()

        library.catalog.load_catalog = counting
        try:
            hits = library.search_styles("", store="systems", limit=20)["hits"]
        finally:
            library.catalog.load_catalog = real
        self.assertEqual(len(hits), 20)
        # catalog.find reads it once and search_styles once, whatever the hit count.
        self.assertLessEqual(len(calls), 2)


if __name__ == "__main__":
    unittest.main()
