"""The Mural token builder is deterministic and keeps the measured values."""
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_rebuild_matches(self):
        before = (PKG / "tokens.json").read_bytes()
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=PKG)
        self.assertEqual((PKG / "tokens.json").read_bytes(), before)

    def test_measured_colours(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["jade"]["$value"], "#00c27a")
        self.assertEqual(tokens["core"]["color"]["authRed"]["$value"], "#e02935")
        self.assertEqual(tokens["core"]["color"]["authFocus"]["$value"], "#306ae3")
        self.assertEqual(tokens["light"]["accent"]["$value"], "{color.jade}")
        self.assertIn("source", tokens["core"]["color"]["jade"]["$extensions"])
        self.assertEqual(tokens["$themes"][0]["id"], "light")


if __name__ == "__main__":
    unittest.main()
