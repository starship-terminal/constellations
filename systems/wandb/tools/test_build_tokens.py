"""build_tokens.check refuses a token with no source."""
import json
import pathlib
import tempfile
import unittest

import sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens


class CheckTest(unittest.TestCase):
    def test_committed_tokens_have_sources(self):
        self.assertEqual(build_tokens.check(), [])

    def test_missing_source_fails(self):
        original = build_tokens.TOKENS
        try:
            build_tokens.TOKENS = {"core": {"color": {"ink": {"$type": "color", "$value": "#111111"}}}}
            problems = build_tokens.check()
            self.assertTrue(any("missing source" in p for p in problems))
        finally:
            build_tokens.TOKENS = original


if __name__ == "__main__":
    unittest.main()
