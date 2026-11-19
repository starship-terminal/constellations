#!/usr/bin/env python3
"""The committed tokens.json matches a rebuild, and the painted readings survived."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class Tokens(unittest.TestCase):
    def test_rebuild_matches(self):
        import build_tokens
        committed = json.loads((PKG / "tokens.json").read_text())
        built = build_tokens.build()
        self.assertEqual(committed, built)

    def test_painted_brand_and_ink(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["accent"]["$value"], "#ff5b49")
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "#181818")
        self.assertEqual(tokens["light"]["surface"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["core"]["radius"]["2"]["$value"], "8px")
        self.assertEqual(tokens["core"]["spacing"]["6"]["$value"], "16px")
        self.assertIn("Measured", tokens["light"]["accent"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
