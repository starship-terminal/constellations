#!/usr/bin/env python3
"""The committed tokens.json matches a rebuild, and the painted readings survived."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class Tokens(unittest.TestCase):
    def test_rebuild_matches(self):
        # Built in memory; the committed file is never rewritten by the test.
        import build_tokens
        self.assertEqual((PKG / "tokens.json").read_text(), build_tokens.render())

    def test_components_without_a_reading_are_labelled_by_hand(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        for key, group in tokens["light"]["component"].items():
            for name, token in group.items():
                source = token["$extensions"]["source"]
                with self.subTest(token=f"{key}.{name}"):
                    if key in ("button-glass", "price"):
                        self.assertIn("raw/declared-tokens.json computed.", source)
                    else:
                        self.assertTrue(source.startswith("Reconstruction: entered by hand"))

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
