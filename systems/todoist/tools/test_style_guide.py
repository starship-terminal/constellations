"""style-guide.html's token table and button fill match tokens.json."""
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_style_guide  # noqa: E402


class StyleGuide(unittest.TestCase):
    def test_committed_page_is_current(self):
        page = (HERE.parent / "style-guide.html").read_text()
        self.assertEqual(build_style_guide.render(page), page)  # rendered in memory, nothing written

    def test_no_removed_or_oklch_values(self):
        page = (HERE.parent / "style-guide.html").read_text()
        self.assertNotIn("oklch(", page)
        self.assertIn("component-button-primary-padding-block", page)


if __name__ == "__main__":
    unittest.main()
