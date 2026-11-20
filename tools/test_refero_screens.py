"""Tests for tools/refero/fetch_screens.py's listing guard: a reply that fills
a whole page may be truncated, so the run stops before writing anything.
The API is patched and the refero/ folder is temporary. Run with `make test`."""
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS / "refero"))
import fetch_screens  # noqa: E402


def site(n):
    return {"id": n, "name": f"Site {n}", "domain": f"site{n}.example", "screenshots": []}


class ListingTest(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.refero = Path(tmp.name)
        for patcher in (mock.patch.object(fetch_screens, "PER_PAGE", 2),
                        mock.patch.object(fetch_screens.refero_dump, "refresh")):
            patcher.start()
            self.addCleanup(patcher.stop)

    def run_main(self, sites):
        self.urls = []

        def get(url):
            self.urls.append(url)
            return json.dumps({"records": sites if "/sites/" in url else []}).encode()
        argv = ["fetch_screens.py", "--refero", str(self.refero)]
        with mock.patch.object(sys, "argv", argv), \
             mock.patch.object(fetch_screens.fetch, "get", side_effect=get), \
             mock.patch("sys.stdout", new_callable=io.StringIO):
            try:
                fetch_screens.main()
            except SystemExit as ex:
                return ex.code
        return None

    def test_a_full_page_stops_before_anything_is_written(self):
        code = self.run_main([site(1), site(2)])
        self.assertIn("/v1/sites/available returned 2 records, a full page of 2", code)
        self.assertFalse((self.refero / "directory.json").exists())
        self.assertFalse((self.refero / "refero.db").exists())

    def test_a_short_page_is_the_whole_listing(self):
        self.assertIsNone(self.run_main([site(1)]))
        self.assertTrue(all("per_page=2" in u for u in self.urls))
        directory = json.loads((self.refero / "directory.json").read_text())
        self.assertEqual([s["domain"] for s in directory["web_sites"]], ["site1.example"])


if __name__ == "__main__":
    unittest.main()
