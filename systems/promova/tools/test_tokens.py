#!/usr/bin/env python3
"""The Promova builder reproduces the committed tokens.json, in memory, with measured types only.

Nothing here writes tokens.json: build() returns the checked document and the test compares it.
"""
import json
import pathlib
import unittest

import build_tokens

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)


class Tokens(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_page_is_black_and_hero_is_lavender(self):
        self.assertEqual(TOKENS["core"]["color"]["black"]["$value"], "#000000")
        self.assertEqual(TOKENS["core"]["color"]["lavender"]["$value"], "#bec8ff")
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "{core.color.black}")

    def test_no_dark_set_and_no_unpainted_focus(self):
        self.assertNotIn("dark", TOKENS)
        # Focusing the email field painted no ring, so no focus role is published.
        self.assertNotIn("focus", TOKENS["light"]["border"])

    def test_dimensions_are_one_length(self):
        for set_name in ("core", "light"):
            for path, token in leaves(TOKENS[set_name]):
                self.assertTrue(token["$extensions"].get("source"), path)
                if token["$type"] == "dimension" and not token["$value"].startswith("{"):
                    self.assertRegex(token["$value"], r"^-?\d+(\.\d+)?(px|rem)$", path)


if __name__ == "__main__":
    unittest.main()
