"""Checks for the Visual Electric token file.

Run from this folder: python3 -m unittest test_build_tokens
package_tests.py discovers this file because it sits in tools/, not tools/native/.
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent / "native"))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_measured_accent_and_page(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["core"]["color"]["orange"]["$value"], "#FF3C00")
        self.assertEqual(doc["core"]["color"]["white"]["$value"], "#FFFFFF")
        self.assertEqual(doc["core"]["color"]["black"]["$value"], "#000000")
        self.assertEqual(doc["light"]["background"]["page"]["$value"], "{color.white}")
        self.assertEqual(doc["dark"]["background"]["canvas"]["$value"], "{color.black}")

    def test_light_and_dark_share_keys(self):
        doc = json.loads(TOKENS.read_text())
        keys = lambda name: sorted(".".join(p) for p, _ in build_tokens.walk(doc[name]))
        self.assertEqual(keys("light"), keys("dark"))


if __name__ == "__main__":
    unittest.main()
