#!/usr/bin/env python3
"""The Meiro token builder is deterministic and keeps the measured palette."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_rebuild_changes_nothing(self):
        # Builds in memory (the builder writes only as a script), so a mismatch never rewrites tokens.json.
        import build_tokens
        self.assertEqual(json.loads(TOKENS.read_text()), json.loads(json.dumps(build_tokens.doc, ensure_ascii=False)))

    def test_check_refuses_a_dead_alias(self):
        import copy
        import build_tokens
        doc = copy.deepcopy(build_tokens.doc)
        doc["dark"]["page"]["$value"] = "{color.nothing}"
        with self.assertRaises(SystemExit):
            build_tokens.check(doc)

    def test_hand_entered_values_are_not_labelled_measured(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertEqual(tokens["core"]["spacing"]["1"]["$extensions"]["evidence"], "Reconstruction")
        self.assertEqual(tokens["core"]["typography"]["display-mobile"]["$extensions"]["evidence"], "Reconstruction")
        self.assertEqual(tokens["core"]["size"]["content"]["$extensions"]["evidence"], "Derived")
        self.assertEqual(tokens["dark"]["focus"]["$extensions"]["evidence"], "Observed")

    def test_palette_matches_the_framer_declaration(self):
        tokens = json.loads(TOKENS.read_text())
        color = tokens["core"]["color"]
        self.assertEqual(color["ink"]["$value"], "#0e0f0f")
        self.assertEqual(color["lime"]["$value"], "#d5fe52")
        self.assertEqual(color["lime-deep"]["$value"], "#c0ef2a")
        self.assertEqual(tokens["dark"]["page"]["$value"], "{color.ink}")
        self.assertEqual(tokens["dark"]["accent"]["$value"], "{color.lime}")
        self.assertIn("source", color["ink"]["$extensions"])
        self.assertIn("motion", tokens["core"])

    def test_one_theme(self):
        tokens = json.loads(TOKENS.read_text())
        self.assertNotIn("light", tokens)
        self.assertEqual(tokens["$themes"][0]["id"], "dark")


if __name__ == "__main__":
    unittest.main()
