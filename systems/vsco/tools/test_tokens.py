"""The VSCO token file keeps the measured colours and the light theme only."""
import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_gold_and_ink_are_measured(self):
        self.assertEqual(TOKENS["core"]["color"]["gold"]["$value"], "#ffbc3c")
        self.assertEqual(TOKENS["core"]["color"]["blackIsh"]["$value"], "#111111")
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "{color.gold}")
        self.assertEqual(TOKENS["light"]["focus"]["$value"], "{color.ink525}")

    def test_no_dark_set(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
