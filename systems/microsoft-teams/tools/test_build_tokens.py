#!/usr/bin/env python3
"""The token builder writes the painted button colour and the measured hero size."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        # The builder builds on import and writes only as a script, so the test never rewrites tokens.json.
        import build_tokens
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.text)

    def test_painted_action_and_hero(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["background"]["action"]["$value"], "#5d5bd4")
        self.assertEqual(tokens["light"]["background"]["action-hover"]["$value"], "#5553c1")
        self.assertEqual(tokens["core"]["typography"]["hero"]["$value"]["fontSize"], "62px")
        self.assertEqual(tokens["core"]["radius"]["control"]["$value"], "8px")
        self.assertTrue(tokens["light"]["text"]["heading"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
