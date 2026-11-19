#!/usr/bin/env python3
"""The portrait token file resolves, and the page colour is the measured gray-10."""

import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_page_colour_is_the_measured_gray(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["gray"]["10"]["$value"], "#f7f7f7")
        self.assertEqual(tokens["light"]["color"]["bg"]["page"]["$value"], "{color.gray.10}")

    def test_every_token_names_a_source(self):
        tokens = json.loads((HERE / "tokens.json").read_text())

        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node.get("$extensions", {}))
            elif isinstance(node, dict):
                for value in node.values():
                    walk(value)

        walk(tokens["core"])
        walk(tokens["light"])
        walk(tokens["dark"])


if __name__ == "__main__":
    unittest.main()
