"""The committed tokens.json passes the package check."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_red_is_the_measured_action(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["core"]["color"]["red"]["$value"], "#e50914")
        self.assertEqual(doc["dark"]["background"]["page"]["$value"], "{color.page}")
