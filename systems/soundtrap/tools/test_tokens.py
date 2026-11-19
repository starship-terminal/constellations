#!/usr/bin/env python3
"""The measured Soundtrap tokens still match the readings this package committed."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.themes = json.loads((ROOT / "raw" / "theme-sets.json").read_text())

    def test_light_page_matches_declared_background_base(self):
        self.assertEqual(self.tokens["light"]["background"]["page"]["$value"],
                         self.themes["light"]["background-base"])

    def test_dark_page_matches_declared_background_base(self):
        self.assertEqual(self.tokens["dark"]["background"]["page"]["$value"],
                         self.themes["dark"]["background-base"])

    def test_primary_is_the_login_submit(self):
        self.assertEqual(self.tokens["core"]["palette"]["primary"]["$value"], "#6551ff")
        self.assertEqual(self.tokens["light"]["component"]["button-primary-bg"]["$value"], "#6551ff")

    def test_focus_is_the_declared_ring(self):
        self.assertEqual(self.tokens["core"]["palette"]["focus"]["$value"], "#3c95ff")

    def test_every_token_names_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(".".join(path))
                return
            if isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, path + [key])

        walk(self.tokens["core"], ["core"])
        walk(self.tokens["light"], ["light"])
        walk(self.tokens["dark"], ["dark"])
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
