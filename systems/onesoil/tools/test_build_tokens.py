"""Checks for the OneSoil token file. Run from tools/: python3 -m unittest test_build_tokens."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_light_only(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)

    def test_measured_accent(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["core"]["color"]["accent"]["$value"], "#27AE60")
        self.assertEqual(doc["core"]["color"]["page"]["$value"], "#F6F4EF")
