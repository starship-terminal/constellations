"""Doctronic tokens match the declared CSS variables."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Measured(unittest.TestCase):
    def test_accent_is_the_declared_blue(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        accent = tokens["light"]["accent"]
        self.assertEqual(accent["$value"], "#2463eb")
        self.assertIn("--color-accent-bg", accent["$extensions"]["source"])
        self.assertNotIn("dark", tokens)

    def test_page_is_the_declared_canvas(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["page"]["$value"], "#fdfdf7")

    def test_display_comes_from_the_text_shorthand(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        display = tokens["core"]["typography"]["display"]["48"]
        self.assertEqual(display["$value"]["fontSize"], "48px")
        self.assertIn("fraunces", display["$value"]["fontFamily"])

    def test_login_review_does_not_claim_a_session(self):
        review = json.loads((ROOT / "login-review.json").read_text())
        self.assertFalse(review["signed_in"])
        self.assertEqual(review["probe"], "no-form")
        self.assertIn("Get Login Code", review["not_submitted"])


if __name__ == "__main__":
    unittest.main()
