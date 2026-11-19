#!/usr/bin/env python3
"""The Uber token builder resolves the public stylesheet and keeps measured chrome."""
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

    def test_signup_wall_is_not_a_filled_field(self):
        wall = json.loads((ROOT / "raw" / "auth-wall.json").read_text())
        self.assertEqual(wall["entered"], "nothing. No phone, email, card, or continue click.")
        self.assertIn("phone-or-email", wall["gap"])

    def test_committed_tokens_match_builder(self):
        built = build_tokens.build()
        committed = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(built["light"]["background"]["primary"], committed["light"]["background"]["primary"])
        self.assertIn("source", committed["light"]["background"]["primary"]["$extensions"])


if __name__ == "__main__":
    unittest.main()
