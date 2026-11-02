"""Tests for tools/site.py. Run with `make test`.

tools/site.py shares its name with the stdlib `site` module (already imported by
the interpreter), so it is loaded here by file path.
"""
import importlib.util
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
spec = importlib.util.spec_from_file_location("sitegen", HERE / "site.py")
sitegen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sitegen)


class PublishTest(unittest.TestCase):
    def page(self):
        p = sitegen.Page(sitegen.DOCS / "index.md", "", None)
        p.title = "Home"
        return p

    def test_publish_drops_the_gallery_nav_links_and_search_form(self):
        local = sitegen.render(self.page(), "<p>x</p>", set())
        published = sitegen.render(self.page(), "<p>x</p>", set(), publish=True)
        self.assertIn("gallery/index.html", local)
        self.assertNotIn("gallery/", published)
        # The rail's search field is gone in both modes; the gallery's own
        # composer is the only search surface.
        for rendered in (local, published):
            self.assertNotIn('class="search"', rendered)
        for keep in ("scorecard/", "DESIGN-SYSTEM/"):
            self.assertIn(keep, published)

    def test_home_renders_the_dashboard(self):
        body = sitegen.dashboard()
        self.assertIn('class="dash', body)
        self.assertIn("refero styles", body)
        # Every audited package shows up in either the recent or attention list
        # source data; the roll-up bar tallies three grades.
        for cls in ("dash-meets", "dash-partly", "dash-missing"):
            self.assertIn(cls, body)

    def test_dashboard_math_with_fixed_data(self):
        catalog = {"systems": [
            {"name": "New", "slug": "new", "category": "a", "captured": "2026-02-01", "themes": ["dark"]},
            {"name": "Old", "slug": "old", "category": "b", "captured": "2025-01-01", "themes": ["light"]},
            {"name": "Mid", "slug": "mid", "category": "a", "captured": "2025-06-01", "themes": ["light", "dark"]}],
            "categories": {"a": "Alpha", "b": "Beta"}}
        audit = {"date": "2026-03-01", "rubric": 4, "systems": [
            {"slug": "new", "name": "New", "grades": {
                "F1": {"grade": "missing"}, "F2": {"grade": "meets"}, "F3": {"grade": "meets"}}},
            {"slug": "mid", "name": "Mid", "grades": {
                "F1": {"grade": "partly"}, "F2": {"grade": "meets"}}}]}
        body = sitegen.dashboard(catalog, audit, 7)
        self.assertIn("<b>3</b><span>systems", body)
        self.assertIn("<b>7</b><span>refero styles", body)
        self.assertIn("<b>2</b><span>categories", body)
        self.assertIn("<b>2</b><span>with a dark theme", body)
        # 3 met + 1 partial + 1 missing over five grades is 60%.
        self.assertIn("60% of graded criteria met", body)
        self.assertIn("3 met, 1 partial, 1 missing", body)
        # Newest captures run newest first; attention runs most-missing first.
        recent = body.split("Newest captures")[1]
        self.assertTrue(recent.index("New") < recent.index("Mid") < recent.index("Old"))
        attention = body.split("Needs attention")[1]
        self.assertTrue(attention.index("New") < attention.index("Mid"))


class AppIconTest(unittest.TestCase):
    ASSETS = sitegen.DOCS / "assets"

    def page(self, url=""):
        p = sitegen.Page(sitegen.DOCS / "index.md", url, None)
        p.title = "Home"
        return p

    def test_the_head_links_the_flat_set_then_loads_the_swap(self):
        head = sitegen.render(self.page("scorecard/"), "<p>x</p>", set()).split("</head>")[0]
        self.assertIn(sitegen.ICON_LINKS.format(rel="../"), head)
        # app-icon.js replaces the icon links it finds, so none may follow it.
        after = head.split('assets/app-icon.js"></script>')[1]
        self.assertNotIn('rel="icon"', after)
        self.assertNotIn('rel="apple-touch-icon"', after)

    def test_the_bar_mark_is_the_flat_favicon(self):
        svg = (self.ASSETS / "favicon.svg").read_text()
        for polygon in re.findall(r'<polygon points="[^"]+"', svg):
            self.assertIn(polygon, sitegen.MARK_SVG)
        self.assertNotIn('id="c"', sitegen.MARK_SVG)

    def test_the_gallery_carries_the_same_head_and_mark(self):
        gallery = (sitegen.DOCS / "gallery" / "index.html").read_text()
        self.assertIn(sitegen.ICON_LINKS.format(rel="../"), gallery)
        self.assertIn(sitegen.MARK_SVG, gallery)
        self.assertIn('href="../settings/"', gallery)

    def test_every_page_links_settings_and_it_offers_both_icons(self):
        for publish in (False, True):
            self.assertIn('href="settings/"', sitegen.render(self.page(), "<p>x</p>", set(), publish))
        body = sitegen.SETTINGS_BODY.replace("{rel}", "../")
        self.assertEqual(re.findall(r'name="app-icon" value="(\w+)"', body), ["flat", "glass"])
        for src in re.findall(r'src="\.\./(assets/[^"]+)"', body):
            self.assertTrue((sitegen.DOCS / src).exists(), src)

    def test_every_icon_the_swap_names_exists(self):
        js = (self.ASSETS / "app-icon.js").read_text()
        hrefs = re.findall(r"href: '([^']+)'", js)
        self.assertTrue(any(h.startswith("icons/glass/") for h in hrefs))
        for href in hrefs:
            self.assertTrue((self.ASSETS / href).exists(), href)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required to run assets/app-icon.js")
    def test_the_swap_script(self):
        result = subprocess.run(["node", "--test", str(HERE / "test_app_icon.mjs")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_the_glass_set_mirrors_the_flat_rasters(self):
        flat = {p.name for p in (self.ASSETS / "icons").iterdir() if p.is_file()}
        glass = {p.name for p in (self.ASSETS / "icons" / "glass").iterdir()}
        self.assertEqual(flat, glass)


if __name__ == "__main__":
    unittest.main()
