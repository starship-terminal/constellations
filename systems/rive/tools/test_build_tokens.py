"""The Rive token builder is deterministic and keeps the measured values."""
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
        self.assertEqual(tokens["core"]["color"]["amber"]["$value"], "#ffa41c")
        self.assertEqual(tokens["core"]["color"]["authBlue"]["$value"], "#1f6fe5")
        self.assertEqual(tokens["core"]["color"]["docsPage"]["$value"], "#0e0c0b")
        self.assertEqual(tokens["dark"]["page"]["$value"], "{color.black}")
        self.assertEqual(tokens["light"]["accent"]["$value"], "{color.authBlue}")
        self.assertIn("source", tokens["core"]["color"]["amber"]["$extensions"])
        self.assertEqual(tokens["$themes"][0]["id"], "dark")


if __name__ == "__main__":
    unittest.main()
