"""Checks for the Weather Channel token file."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(build_tokens.check(data), [])

    def test_rejects_a_token_with_no_source(self):
        data = {"core": {"color": {"white": {"$type": "color", "$value": "#ffffff"}}}, "light": {}}
        errors = build_tokens.check(data)
        self.assertTrue(any("missing $extensions.source" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
