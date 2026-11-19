"""Checks for the Unsplash token file."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokenCheck(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_missing_source_fails(self):
        doc = {"core": {"color": {"ink": {"$type": "color", "$value": "#111111"}}}}
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
