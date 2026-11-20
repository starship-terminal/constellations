"""The kit's capture scripts that only read files never fetch: every page they open gets a route that
lets only data: URLs load, before anything is loaded into it. A lint (the scripts need a browser to run).
Run with `make test`."""
import re
import unittest
from pathlib import Path

CAPTURE = Path(__file__).resolve().parent / "kit" / "capture"
# Scripts whose header promises no network: they read stylesheets or page copies from disk.
OFFLINE = ["vars.mjs"]


def unrouted(src):
    """Pages opened with newPage whose first setContent or goto comes before their offline route."""
    bad = []
    pages = re.findall(r"const (\w+) = await browser\.newPage\(", src)
    for p in pages:
        route = re.search(rf"await offline\({p}\);", src)
        load = re.search(rf"\b{p}\.(?:setContent|goto)\(", src)
        if not route or (load and load.start() < route.start()):
            bad.append(p)
    return pages, bad


class Offline(unittest.TestCase):
    def test_every_page_an_offline_script_opens_is_routed_before_it_loads(self):
        for name in OFFLINE:
            src = (CAPTURE / name).read_text()
            pages, bad = unrouted(src)
            self.assertTrue(pages, name)
            self.assertEqual(bad, [], name)
            self.assertIn("startsWith('data:') ? r.continue() : r.abort()", src, name)

    def test_the_lint_catches_a_late_or_missing_route(self):
        good = "const page = await browser.newPage();\nawait offline(page);\nawait page.setContent(x);\n"
        late = "const page = await browser.newPage();\nawait page.setContent(x);\nawait offline(page);\n"
        none = "const page = await browser.newPage();\nawait page.setContent(x);\n"
        self.assertEqual(unrouted(good)[1], [])
        self.assertEqual(unrouted(late)[1], ["page"])
        self.assertEqual(unrouted(none)[1], ["page"])


if __name__ == "__main__":
    unittest.main()
