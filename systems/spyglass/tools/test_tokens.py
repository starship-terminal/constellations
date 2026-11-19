#!/usr/bin/env python3
"""The Spyglass token file only contains values that raw/readings.json recorded."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
READINGS = json.loads((HERE / "raw" / "readings.json").read_text())


class TokensTest(unittest.TestCase):
    def test_public_primary_matches_declaration(self):
        self.assertEqual(TOKENS["light"]["color"]["primary"]["$value"], "#171717")
        self.assertEqual(READINGS["declared"]["light"]["--primary"], "#171717")

    def test_display_face_is_familjen(self):
        self.assertIn("Familjen Grotesk", TOKENS["core"]["font"]["display"]["$value"])

    def test_button_height_is_measured(self):
        self.assertEqual(TOKENS["core"]["size"]["buttonMd"]["$value"], "36px")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", "")
                if not source.startswith("Measured") and not source.startswith("Derived"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, f"{path}.{key}" if path else key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])

    def test_dark_page_is_declared_not_invented(self):
        self.assertEqual(TOKENS["dark"]["color"]["page"]["$value"], "#161616")
        self.assertIn("stylesheet", TOKENS["dark"]["color"]["page"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
