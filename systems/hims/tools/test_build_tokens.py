"""tokens.json must rebuild from raw/css-vars.json, and every typed typography part must say it
was entered by hand.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = build_tokens.build()

    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), self.doc)

    def test_typography_hand_parts_are_labelled(self):
        for name, tok in self.doc["core"]["typography"].items():
            src = tok["$extensions"]["source"]
            self.assertIn("Reconstruction", src, name)
            self.assertNotIn("derived", src, name)
            self.assertIsInstance(tok["$value"]["lineHeight"], (int, float), name)

    def test_declared_heading_weight(self):
        # --fontWeights-headingLarge is declared 700 beside --fontSizes-headingLarge.
        self.assertEqual(self.doc["core"]["typography"]["heading-large"]["$value"]["fontWeight"],
                         "{type.weight.headinglarge}")
        self.assertEqual(self.doc["core"]["type"]["weight"]["headinglarge"]["$value"], 700)

    def test_core_is_the_source_set(self):
        self.assertEqual(self.doc["$themes"][0]["selectedTokenSets"]["core"], "source")


if __name__ == "__main__":
    unittest.main()
