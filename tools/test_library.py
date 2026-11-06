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


if __name__ == "__main__":
    unittest.main()
