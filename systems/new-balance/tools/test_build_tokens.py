"""Checks that every alias in tokens.json points at a token, and that colours are hex."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_missing_alias_fails(self):
        doc = json.loads(TOKENS.read_text())
        doc["light"]["text"]["primary"]["$value"] = "{color.missing}"
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
