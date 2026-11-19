"""The kit's capture scripts that only read files never fetch: every page they open has a route that
lets only data: URLs load. A lint (the scripts need a browser to run). Run with `make test`."""
import re
import unittest
from pathlib import Path

CAPTURE = Path(__file__).resolve().parent / "kit" / "capture"
# Scripts whose header promises no network: they read stylesheets or page copies from disk.
OFFLINE = ["vars.mjs"]


class Offline(unittest.TestCase):
    def test_every_page_an_offline_script_opens_is_routed(self):
        for name in OFFLINE:
            src = (CAPTURE / name).read_text()
            pages = re.findall(r"const (\w+) = await browser\.newPage\(", src)
            self.assertTrue(pages, name)
            for p in pages:
                self.assertRegex(src, rf"await offline\({p}\);", f"{name}: {p} opens with no route")
            self.assertIn("startsWith('data:') ? r.continue() : r.abort()", src, name)


if __name__ == "__main__":
    unittest.main()
