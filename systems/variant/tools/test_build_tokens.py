#!/usr/bin/env python3
"""tokens.json matches the raw readings and does not invent a light theme."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
VARS = json.loads((HERE / "raw" / "css-vars.json").read_text())["declared"]
COMP = json.loads((HERE / "raw" / "components-computed.json").read_text())


class BuildTokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # The builder run in memory reproduces the committed file byte for byte.
        import sys
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_page_is_the_measured_body(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], COMP["home"]["body"]["backgroundColor"])

    def test_text_is_the_measured_headline(self):
        self.assertEqual(TOKENS["dark"]["text"]["$value"], COMP["home"]["h1"]["color"])

    def test_declared_radius_is_copied(self):
        self.assertEqual(TOKENS["core"]["radius"]["token"]["$value"], VARS["--border-radius"])

    def test_chip_radius_is_measured_not_the_token(self):
        self.assertEqual(TOKENS["core"]["radius"]["chip"]["$value"], "6px")
        self.assertNotEqual(TOKENS["core"]["radius"]["chip"]["$value"], VARS["--border-radius"])

    def test_no_light_set(self):
        self.assertNotIn("light", TOKENS)
        self.assertEqual(TOKENS["$themes"][0]["id"], "dark")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
