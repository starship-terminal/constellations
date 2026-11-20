"""The Product Hunt tokens match the readings."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.vars = json.loads((ROOT / "raw" / "css-vars.json").read_text())

    def test_brand_matches_sign_in_button(self):
        self.assertEqual(self.tokens["light"]["color"]["brand"]["$value"], "#ff6154")

    def test_page_matches_root_background(self):
        page = self.tokens["light"]["color"]["background"]["surface"]["primary"]["$value"]
        self.assertEqual(page, "#ffffff")
        self.assertEqual(self.vars["rootLight"]["--background-primary"], "#fff")

    def test_text_matches_root(self):
        text = self.tokens["light"]["color"]["text"]["primary"]["$value"]
        self.assertEqual(text, self.vars["rootLight"]["--text-primary"])

    def test_dark_is_labelled_declared(self):
        dark = self.tokens["dark"]["color"]["background"]["surface"]["primary"]
        self.assertIn("Declared", dark["$extensions"]["source"])
        self.assertEqual(dark["$value"], self.vars["rootDarkDeclared"]["--background-primary"])

    def test_radius_full_is_the_pill(self):
        self.assertEqual(self.tokens["core"]["radius"]["full"]["$value"], "9999px")


if __name__ == "__main__":
    unittest.main()
