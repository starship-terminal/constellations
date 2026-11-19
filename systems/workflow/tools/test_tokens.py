#!/usr/bin/env python3
"""The token file matches the measured custom properties."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
VARS = json.loads((HERE / "raw" / "css-vars.json").read_text())["computed"]


class Tokens(unittest.TestCase):
    def test_page_and_ink(self):
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "{color.text}")
        self.assertEqual(TOKENS["core"]["color"]["text"]["$value"], "#1a1a1a")
        self.assertEqual(TOKENS["core"]["color"]["text"]["$value"], VARS["--color--text--default"])

    def test_button_radius_matches_variable(self):
        self.assertEqual(TOKENS["core"]["radius"]["medium"]["$value"], VARS["--radius--medium"])
        self.assertEqual(TOKENS["core"]["radius"]["medium"]["$value"], "8px")

    def test_space_scale(self):
        self.assertEqual(TOKENS["core"]["space"]["sm"]["$value"], "16px")
        self.assertEqual(TOKENS["core"]["space"]["lg"]["$value"], VARS["--space--lg"])

    def test_every_token_has_a_source(self):
        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node.get("$extensions", {}))
            elif isinstance(node, dict):
                for child in node.values():
                    walk(child)
        walk(TOKENS["core"])
        walk(TOKENS["light"])

    def test_light_only(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual(TOKENS["$themes"][0]["id"], "light")


if __name__ == "__main__":
    unittest.main()
