"""Tests for tools/site.py. Run with `make test`.

tools/site.py shares its name with the stdlib `site` module (already imported by
the interpreter), so it is loaded here by file path.
"""
import importlib.util
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
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

    def test_no_page_links_the_gallery(self):
        # The gallery lives in the Next.js app now; the static site never ships
        # it (it shows the captures), so no page may link into it.
        rendered = sitegen.render(self.page(), "<p>x</p>", set())
        self.assertNotIn("gallery/", rendered)
        for keep in ("scorecard/", "DESIGN-SYSTEM/"):
            self.assertIn(keep, rendered)

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

    def test_the_app_rail_carries_the_same_mark(self):
        rail = (sitegen.ROOT / "web" / "components" / "Rail.tsx").read_text()
        self.assertIn('id="ds-mark-clip"', rail)
        svg = (self.ASSETS / "favicon.svg").read_text()
        for polygon in re.findall(r'<polygon points="([^"]+)"', svg):
            self.assertIn(f'points="{polygon}"', rail)

    def test_every_page_links_settings_and_it_offers_both_icons(self):
        self.assertIn('href="settings/"', sitegen.render(self.page(), "<p>x</p>", set()))
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


class FrontmatterTest(unittest.TestCase):
    def test_hide_block_is_split_off(self):
        hidden, body = sitegen.frontmatter("---\nhide:\n  - navigation\n  - toc\n---\n# Title\n")
        self.assertEqual((hidden, body), ({"navigation", "toc"}, "# Title\n"))

    def test_no_block_or_a_later_rule_is_left_alone(self):
        self.assertEqual(sitegen.frontmatter("# Title\n"), (set(), "# Title\n"))
        md = "# Title\n\n---\nhide:\n  - toc\n---\n"
        self.assertEqual(sitegen.frontmatter(md), (set(), md))

    def test_page_title_strips_markup_and_falls_back_to_the_stem(self):
        self.assertEqual(sitegen.page_title("intro\n# The **`tokens`** file\n", "x"), "The tokens file")
        self.assertEqual(sitegen.page_title("<div>raw</div>\n", "PACKAGE"), "PACKAGE")


class RewriteLinksTest(unittest.TestCase):
    def rewrite(self, href, src="index.md", url=""):
        page = sitegen.Page(sitegen.DOCS / src, url, None)
        return sitegen.rewrite_links(f'<a href="{href}">x</a>', page)

    def test_md_links_become_dir_urls_relative_to_the_page(self):
        self.assertEqual(self.rewrite("PACKAGE.md"), '<a href="PACKAGE/">x</a>')
        self.assertEqual(self.rewrite("PACKAGE.md#layout", "EVIDENCE.md", "EVIDENCE/"),
                         '<a href="../PACKAGE/#layout">x</a>')
        self.assertEqual(self.rewrite("index.md", "EVIDENCE.md", "EVIDENCE/"), '<a href="../">x</a>')

    def test_links_resolve_from_the_source_folder(self):
        self.assertEqual(self.rewrite("../PACKAGE.md", "scorecard/linear.md", "scorecard/linear/"),
                         '<a href="../../PACKAGE/">x</a>')
        self.assertEqual(self.rewrite("index.md", "scorecard/linear.md", "scorecard/linear/"),
                         '<a href="../">x</a>')

    def test_external_and_non_md_links_are_untouched(self):
        for href in ("https://example.test/a.md", "//host/a.md", "mailto:a@example.test", "assets/x.png"):
            self.assertEqual(self.rewrite(href), f'<a href="{href}">x</a>')


@unittest.skipUnless(importlib.util.find_spec("markdown"), "needs markdown (requirements.txt)")
class BuildTest(unittest.TestCase):
    """build() into a temporary folder: pages, the statics and nothing else."""

    @classmethod
    def setUpClass(cls):
        # A copy of docs/ with two scorecard pages, since docs/scorecard/ is generated
        # (gitignored) and absent on a fresh checkout.
        cls.tmp = tempfile.TemporaryDirectory()
        cls.docs = Path(cls.tmp.name) / "docs"
        shutil.copytree(sitegen.DOCS, cls.docs, ignore=shutil.ignore_patterns("scorecard"))
        (cls.docs / "scorecard").mkdir()
        (cls.docs / "scorecard" / "index.md").write_text("# Scorecard\n\nSee [linear](linear.md).\n")
        (cls.docs / "scorecard" / "linear.md").write_text("# Linear\n\nBack to [the docs](../PACKAGE.md).\n")
        cls.out = Path(cls.tmp.name) / "site"
        with mock.patch.object(sitegen, "DOCS", cls.docs), mock.patch.object(sitegen, "OUT", cls.out), \
             mock.patch.object(sitegen.scorecard, "load", wraps=sitegen.scorecard.load) as load, \
             mock.patch("sys.stdout"):
            cls.pages = sitegen.pages()
            sitegen.build()
        cls.loads = load.call_count

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def files(self):
        return sorted(p.relative_to(self.out).as_posix() for p in self.out.rglob("*") if p.is_file())

    def test_no_gallery_and_no_package_media(self):
        files = self.files()
        self.assertFalse((self.out / "gallery").exists())
        self.assertFalse([f for f in files if "gallery" in f or f.startswith("systems/")])
        self.assertFalse([f for f in files if f in ("search.json", "sitemap.xml")])

    def test_only_pages_and_exact_copies_of_the_docs_statics_are_written(self):
        statics = ["site.webmanifest"] + sorted(
            p.relative_to(self.docs).as_posix() for d in ("assets", "stylesheets")
            for p in (self.docs / d).rglob("*") if p.is_file())
        files = self.files()
        self.assertEqual([f for f in files if not f.endswith(".html")],
                         sorted(f for f in statics if not f.endswith(".html")))
        for f in statics:
            self.assertEqual((self.out / f).read_bytes(), (self.docs / f).read_bytes(), f)

    def test_every_page_is_written(self):
        files = set(self.files())
        self.assertTrue({"scorecard/index.html", "scorecard/linear/index.html"} <= files)
        for page in self.pages:
            if page.src.exists():
                self.assertIn(f"{page.url}index.html", files)
        self.assertTrue({"settings/index.html", "404.html"} <= files)

    def test_the_404_page_resolves_its_links_from_the_site_root(self):
        head = (self.out / "404.html").read_text().split("</head>")[0]
        self.assertIn('<base href="/">', head)
        self.assertLess(head.index('<base href="/">'), head.index("stylesheet"))
        self.assertNotIn("document.write", head)

    def test_the_scorecard_snapshots_are_parsed_once(self):
        # load() parses every snapshot; per page that is hundreds of MB per page.
        self.assertEqual(self.loads, 1)

    def test_the_scorecard_rail_lists_the_newest_audit(self):
        html = (self.out / "scorecard" / "linear" / "index.html").read_text()
        newest = sitegen.newest_audit()
        first = sitegen.scorecard.ranked(newest["systems"])[0]
        self.assertIn(f'href="../../scorecard/systems/{first["slug"]}/"', html)

    def test_nested_scorecard_links_are_rewritten(self):
        html = (self.out / "scorecard" / "linear" / "index.html").read_text()
        self.assertIn('href="../../PACKAGE/"', html)
        self.assertIn('href="linear/"', (self.out / "scorecard" / "index.html").read_text())


if __name__ == "__main__":
    unittest.main()
