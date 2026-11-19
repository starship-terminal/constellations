#!/usr/bin/env python3
"""The package tokens match the measured readings."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


class BuildTokensTest(unittest.TestCase):
    def test_tokens_match_readings(self):
        raw = json.loads((ROOT / "raw" / "foundations.json").read_text())
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["surface"]["page"]["$value"], raw["colors"]["page"])
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], raw["colors"]["text"])
        self.assertEqual(tokens["light"]["accent"]["$value"], raw["colors"]["accent"])
        self.assertEqual(tokens["light"]["border"]["default"]["$value"], raw["colors"]["text"])
        self.assertEqual(tokens["core"]["typography"]["hero"]["$value"]["fontSize"], raw["type"]["hero"]["size"])
        self.assertEqual(tokens["core"]["radius"]["pill"]["$value"], "100px")
        self.assertIn("source", tokens["light"]["accent"]["$extensions"])
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
