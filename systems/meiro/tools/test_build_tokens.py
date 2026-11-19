#!/usr/bin/env python3
"""The Meiro token builder is deterministic and keeps the measured palette."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = ROOT / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_rebuild_changes_nothing(self):
        before = TOKENS.read_bytes()
        subprocess.check_call([sys.executable, str(ROOT / "tools" / "build_tokens.py")], cwd=ROOT)
        self.assertEqual(TOKENS.read_bytes(), before)

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
