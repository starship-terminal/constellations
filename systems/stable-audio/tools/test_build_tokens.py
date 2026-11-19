"""The package tokens file passes build_tokens.check."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_dark_page_is_black(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["dark"]["background"]["page"]["$value"], "#000000")
        self.assertNotIn("light", doc)


if __name__ == "__main__":
    unittest.main()
