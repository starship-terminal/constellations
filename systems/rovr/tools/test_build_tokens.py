"""The committed tokens.json must pass the package check."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        tree = json.loads(TOKENS.read_text())
        self.assertGreater(build_tokens.check(tree), 40)
        self.assertEqual(tree["dark"]["color"]["brand"]["$value"], "#FFF057")
        self.assertEqual(tree["dark"]["color"]["background"]["$value"], "#000000")
        self.assertIn("source", tree["dark"]["color"]["primary"]["$extensions"])


if __name__ == "__main__":
    unittest.main()
