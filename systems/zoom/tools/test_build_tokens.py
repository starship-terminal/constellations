#!/usr/bin/env python3
"""The public Zoom token file names the colours that were computed."""
import json
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((PKG / "tokens.json").read_text())

    def test_sets(self):
        self.assertEqual(set(self.tokens), {"core", "dark", "light", "$themes"})

    def test_accent_is_the_measured_blue(self):
        self.assertEqual(self.tokens["light"]["accent"]["$value"], "#0b5cff")
        self.assertEqual(self.tokens["dark"]["page"]["$value"], "#00053d")

    def test_every_token_has_a_source(self):
        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node["$extensions"])
            elif isinstance(node, dict):
                for key, value in node.items():
                    if not key.startswith("$"):
                        walk(value)
        walk(self.tokens["core"])
        walk(self.tokens["light"])


if __name__ == "__main__":
    unittest.main()
