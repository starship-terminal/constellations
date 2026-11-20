#!/usr/bin/env python3
"""The Skiff tokens resolve, and the measured accent is the orange from the page."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(TOKENS.read_text())

    def test_accent_is_measured_orange(self):
        accent = self.doc["light"]["accent"]["default"]
        self.assertEqual(accent["$value"], "{color.orange.500}")
        self.assertEqual(self.doc["core"]["color"]["orange"]["500"]["$value"], "#ef5a3c")
        self.assertIn("Measured", accent["$extensions"]["source"] + self.doc["core"]["color"]["orange"]["500"]["$extensions"]["source"])

    def test_light_theme_only(self):
        self.assertEqual([t["id"] for t in self.doc["$themes"]], ["light"])
        self.assertNotIn("dark", self.doc)


if __name__ == "__main__":
    unittest.main()
