#!/usr/bin/env python3
"""The Polaroid builder reproduces the committed tokens.json from raw/, in memory.

Nothing here writes tokens.json: build() returns the document and the test compares it.
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


class BuildTokens(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_every_token_has_a_source_and_one_light_theme(self):
        self.assertIn("light", TOKENS)
        self.assertNotIn("dark", TOKENS)
        for set_name in ("core", "light"):
            for path, token in leaves(TOKENS[set_name]):
                self.assertTrue(token.get("$extensions", {}).get("source"), f"{set_name}.{path}")

    def test_roles_are_the_readings(self):
        raw = build_tokens.C
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["accent"]["$value"], build_tokens.hex_of(raw["login-details"]["continue"]["bg"]))
        self.assertEqual(TOKENS["light"]["nav-active"]["$value"], build_tokens.hex_of(raw["chrome"]["holidays"]["color"]))
        self.assertEqual(TOKENS["core"]["control"]["continue-height"]["$value"], f'{raw["login-details"]["continue"]["h"]}px')

    def test_muted_is_a_text_colour_not_the_grey_fill(self):
        # The grey --color-grey-200 is a surface; as text it reads about 1.2:1 on white.
        self.assertNotEqual(TOKENS["light"]["muted"]["$value"], TOKENS["light"]["surface"]["$value"])
        self.assertEqual(TOKENS["light"]["muted"]["$value"],
                         build_tokens.hex_of(build_tokens.C["login-details"]["label"]["color"]))


if __name__ == "__main__":
    unittest.main()
