"""The Overflow token builder is deterministic and keeps measured colours.

Run from the package tools directory, which is how tools/package_tests.py calls it.
"""
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"


class BuildTokens(unittest.TestCase):
    def test_rebuild_is_deterministic(self):
        before = TOKENS.read_bytes()
        subprocess.run([sys.executable, str(HERE / "build_tokens.py")], check=True, cwd=PKG)
        self.assertEqual(TOKENS.read_bytes(), before)

    def test_measured_roles(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["background"]["action"]["$value"], "{color.ink}")
        self.assertEqual(data["core"]["color"]["ink"]["$value"], "#000000")
        self.assertEqual(data["light"]["background"]["app-action"]["$value"], "#0071db")
        self.assertEqual(data["light"]["background"]["auth-panel"]["$value"], "{color.auth-panel}")
        self.assertEqual(data["core"]["color"]["auth-panel"]["$value"], "#d6f3ff")
        self.assertNotIn("dark", data)
        self.assertIn("$extensions", data["light"]["text"]["primary"])


if __name__ == "__main__":
    unittest.main()
