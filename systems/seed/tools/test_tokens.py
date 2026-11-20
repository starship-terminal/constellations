"""Checks that the Seed token file still holds the values read on 2026-11-19."""
import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_seed_green_and_snow(self):
        self.assertEqual(TOKENS["core"]["color"]["primary"]["seed-green"]["$value"], "#1c3a13")
        self.assertEqual(TOKENS["light"]["bg"]["page"]["$value"], "{color.primary.snow-white}")
        self.assertEqual(TOKENS["core"]["color"]["primary"]["snow-white"]["$value"], "#fcfcf7")

    def test_pill_radius_and_light_only(self):
        self.assertEqual(TOKENS["light"]["component"]["button"]["radius"]["$value"], "1000px")
        self.assertNotIn("dark", TOKENS)
        self.assertEqual(TOKENS["$themes"][0]["id"], "light")

    def test_every_token_is_measured_or_derived(self):
        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                evidence = node["$extensions"]["source"]["evidence"]
                self.assertIn(evidence, ("Measured", "Derived"))
            elif isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value)
        walk(TOKENS["core"])
        walk(TOKENS["light"])


if __name__ == "__main__":
    unittest.main()
