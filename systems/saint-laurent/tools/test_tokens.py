"""Saint Laurent tokens stay tied to the measured readings."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())

    def test_page_is_measured_white(self):
        self.assertEqual(self.tokens["light"]["page"]["$value"], "#ffffff")
        self.assertIn("255,255,255", self.raw["vars"]["--color-background-primary"])

    def test_text_is_black(self):
        self.assertEqual(self.tokens["light"]["text"]["$value"], "#000000")
        self.assertEqual(self.raw["vars"]["--color-text-primary"], "#000")

    def test_button_radius_is_zero(self):
        self.assertEqual(self.tokens["light"]["component"]["button"]["radius"]["$value"], "{core.radius.none}")
        self.assertEqual(self.tokens["core"]["radius"]["none"]["$value"], "0px")

    def test_ui_size_is_twelve(self):
        self.assertEqual(self.tokens["core"]["typography"]["ui"]["$value"]["fontSize"], "12px")


if __name__ == "__main__":
    unittest.main()
