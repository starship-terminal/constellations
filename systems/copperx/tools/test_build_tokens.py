#!/usr/bin/env python3
"""The Copperx token builder round-trips and keeps the measured ink."""
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_rebuild_is_stable_and_keeps_indigo(self):
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=HERE)
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["indigo"]["$value"], "#4c63ed")
        self.assertEqual(tokens["light"]["action"]["primary"]["$value"], "{color.black}")
        self.assertIn("light", tokens["$themes"][0]["selectedTokenSets"])
        before = (ROOT / "tokens.json").read_bytes()
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=HERE)
        self.assertEqual(before, (ROOT / "tokens.json").read_bytes())


if __name__ == "__main__":
    unittest.main()
