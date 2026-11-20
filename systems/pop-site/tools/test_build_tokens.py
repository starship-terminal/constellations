"""The Pop Site builder reproduces the committed tokens.json from raw/, in memory.

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

    def test_every_token_has_a_type_and_a_source(self):
        for set_name in ("core", "light"):
            for path, token in leaves(TOKENS[set_name]):
                self.assertIn("$type", token, f"{set_name}.{path}")
                self.assertTrue(token.get("$extensions", {}).get("source"), f"{set_name}.{path}")

    def test_measured_roles(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["text"]["$value"], "#171717")
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#3b82f6")
        self.assertEqual(TOKENS["core"]["color"]["marketing"]["cyan"]["$value"], "#00a8f5")
        self.assertEqual(TOKENS["core"]["radius"]["claim"]["$value"], "26px")
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontSize"], "51px")
        self.assertIn("duration", TOKENS["core"]["motion"])


if __name__ == "__main__":
    unittest.main()
