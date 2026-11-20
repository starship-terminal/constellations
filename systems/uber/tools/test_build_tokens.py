#!/usr/bin/env python3
"""The Uber builder output keeps the measured light and dark chrome, and its primary background agrees with the committed tokens.json."""
import json
import unittest
from pathlib import Path

import build_tokens

ROOT = Path(__file__).resolve().parent.parent


class BuildTokensTest(unittest.TestCase):
    def test_light_page_and_accent_resolve(self):
        tokens = build_tokens.build()
        self.assertEqual(tokens["light"]["background"]["primary"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["content"]["primary"]["$value"], "#111111")
        self.assertEqual(tokens["light"]["accent"]["background"]["primary"]["bold"]["$value"], "#1175dd")
        self.assertEqual(tokens["dark"]["background"]["primary"]["$value"], "#1c1c1c")

    def test_signup_wall_records_nothing_entered(self):
        wall = json.loads((ROOT / "raw" / "auth-wall.json").read_text())
        self.assertEqual(wall["entered"], "nothing. No phone, email, card, or continue click.")
        self.assertIn("phone-or-email", wall["gap"])

    def test_committed_primary_background_matches_builder(self):
        built = build_tokens.build()
        committed = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(built["light"]["background"]["primary"], committed["light"]["background"]["primary"])
        self.assertIn("source", committed["light"]["background"]["primary"]["$extensions"])


if __name__ == "__main__":
    unittest.main()
