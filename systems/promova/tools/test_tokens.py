#!/usr/bin/env python3
"""The Promova token file matches the builder and only uses measured types."""
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class Tokens(unittest.TestCase):
    def test_builder_is_stable(self):
        before = (PKG / "tokens.json").read_text()
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=PKG)
        self.assertEqual(before, (PKG / "tokens.json").read_text())

    def test_page_is_black_and_hero_is_lavender(self):
        t = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(t["core"]["color"]["black"]["$value"], "#000000")
        self.assertEqual(t["core"]["color"]["lavender"]["$value"], "#bec8ff")
        self.assertEqual(t["light"]["background"]["page"]["$value"], "{core.color.black}")
        self.assertIn("source", t["core"]["color"]["black"]["$extensions"])

    def test_no_dark_set(self):
        t = json.loads((PKG / "tokens.json").read_text())
        self.assertNotIn("dark", t)


if __name__ == "__main__":
    unittest.main()
