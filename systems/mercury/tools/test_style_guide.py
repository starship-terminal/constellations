#!/usr/bin/env python3
"""style-guide.html matches a fresh render, and its token script is a real <script>."""
import pathlib
import re
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class StyleGuideTest(unittest.TestCase):
    def test_committed_guide_matches_render(self):
        import build_style_guide  # renders in memory; writes only when run as a script
        self.assertEqual((HERE / "style-guide.html").read_text(), build_style_guide.html)

    def test_tokens_are_inside_a_script(self):
        html = (HERE / "style-guide.html").read_text()
        self.assertIn("<script>\nconst TOK = ", html)
        self.assertEqual(html.count("<script>"), html.count("</script>"))

    def test_every_script_target_exists(self):
        # A renderer whose #id is missing throws, and the error stops every later renderer and
        # the final setTheme() (an elevation() aimed at a #shadow-out the page did not have).
        html = (HERE / "style-guide.html").read_text()
        script = html[html.index("<script>"):]
        ids = set(re.findall(r'\bid="([^"]+)"', html[:html.index("<script>")]))
        self.assertEqual(set(re.findall(r"\$\('#([A-Za-z0-9_-]+)'\)", script)) - ids, set())

    def test_no_web_font_is_fetched(self):
        self.assertNotIn("fonts.googleapis.com", (HERE / "style-guide.html").read_text())


if __name__ == "__main__":
    unittest.main()
