"""Tests for tools/site.py. Run with `make test`.

tools/site.py shares its name with the stdlib `site` module (already imported by
the interpreter), so it is loaded here by file path.
"""
import importlib.util
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
        self.assertIn('class="search"', local)
        self.assertNotIn("gallery/", published)
        self.assertNotIn('class="search"', published)
        for keep in ("scorecard/", "DESIGN-SYSTEM/"):
            self.assertIn(keep, published)

    def test_publish_strips_only_the_card_linking_to_the_gallery(self):
        md = (sitegen.DOCS / "index.md").read_text()
        stripped = sitegen.GALLERY_CARD.sub("", md)
        self.assertIn("gallery/index.html", md)
        self.assertNotIn("gallery/", stripped)
        for keep in ("[Scorecard]", "[What a design system contains]", "[Capturing a product]"):
            self.assertIn(keep, stripped)


if __name__ == "__main__":
    unittest.main()
