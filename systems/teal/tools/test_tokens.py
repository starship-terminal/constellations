#!/usr/bin/env python3
"""Teal tokens only contain values the 2026-11-19 readings recorded."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
READINGS = json.loads((HERE / "raw" / "readings.json").read_text())


class TokensTest(unittest.TestCase):
    def test_marketing_yellow_matches_declaration(self):
        self.assertEqual(TOKENS["light"]["color"]["yellow"]["$value"], "#f5b501")
        self.assertEqual(READINGS["declaredMarketing"]["--color-teal-yellow"], "#f5b501")

    def test_marketing_face_is_roobert(self):
        self.assertIn("Roobert", TOKENS["core"]["font"]["marketing"]["$value"])

    def test_cta_height_is_measured(self):
        self.assertEqual(TOKENS["core"]["size"]["cta"]["$value"], "53px")
        self.assertEqual(READINGS["marketing"]["cta"]["height"], 53)

    def test_app_field_radius_is_measured(self):
        self.assertEqual(TOKENS["core"]["radius"]["xs"]["$value"], "3px")
        self.assertEqual(READINGS["app"]["field"]["borderRadius"], "3px")

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
        walk(TOKENS["app"], "app")
        self.assertEqual(missing, [])

    def test_no_dark_set(self):
        self.assertNotIn("dark", TOKENS)


if __name__ == "__main__":
    unittest.main()
