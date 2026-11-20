"""Every type specimen in style-guide.html keeps its whole style attribute (findings 19-5, 19-8)."""
import html.parser
import pathlib
import unittest

GUIDE = (pathlib.Path(__file__).resolve().parent.parent / "style-guide.html").read_text()


class Styles(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.styles = []

    def handle_starttag(self, tag, attrs):
        style = dict(attrs).get("style")
        if style and ("font-family" in style or style.startswith("font:")):
            self.styles.append(style)


class StyleGuide(unittest.TestCase):
    def test_specimen_styles_are_whole_and_resolved(self):
        parser = Styles()
        parser.feed(GUIDE)
        specimens = [s for s in parser.styles if "font-size" in s or s.startswith("font:")]
        self.assertTrue(specimens, "no type specimens found")
        for style in parser.styles:
            with self.subTest(style=style[:60]):
                # A quoted family that closed the attribute early leaves only "font-family:".
                self.assertNotRegex(style, r"font-family:\s*$")
                if style.startswith("font-family:"):
                    self.assertIn("font-size:", style)
                self.assertNotIn("{", style)  # an unresolved {alias} is not CSS


if __name__ == "__main__":
    unittest.main()
