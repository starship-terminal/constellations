#!/usr/bin/env python3
"""The Superlist tokens still match the readings this package committed."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.computed = json.loads((ROOT / "raw" / "components-computed.json").read_text())

    def test_page_is_the_measured_body(self):
        self.assertEqual(self.tokens["light"]["background"]["page"]["$value"], "{core.palette.page}")
        self.assertEqual(self.tokens["core"]["palette"]["page"]["$value"], "#fffdf9")

    def test_primary_stops_are_sampled_pixels(self):
        self.assertEqual(self.tokens["core"]["palette"]["coral-top"]["$value"], "#ff502f")
        self.assertEqual(self.tokens["core"]["palette"]["coral-bottom"]["$value"], "#dc0000")
        self.assertIn("display-p3", self.computed["primaryButton"]["backgroundImage"])

    def test_plan_card_radius(self):
        self.assertEqual(self.tokens["core"]["radius"]["card"]["$value"], "20px")

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
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
