"""style-guide.html's custom properties must be CSS: no Python repr of a
composite token (transition/animation objects have no single CSS value and
are skipped, as in the kit).

Run from the package root: python3 -m unittest discover -s tools
"""
import pathlib
import re
import unittest

HTML = (pathlib.Path(__file__).resolve().parent.parent / "style-guide.html").read_text()


class StyleGuideTest(unittest.TestCase):
    def test_custom_properties_are_css(self):
        css = "\n".join(re.findall(r"<style>(.*?)</style>", HTML, re.S))
        bad = [l.strip() for l in css.split("\n") if re.match(r"\s*--[\w-]+:\s*[\[{]", l)]
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
