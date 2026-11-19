"""Tests for tools/build_tokens.py. Run from this package's tools/ directory."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_rebuild_matches_committed_file(self):
        before = TOKENS.read_text()
        build_tokens.build()
        self.assertEqual(TOKENS.read_text(), before)

    def test_missing_alias_fails(self):
        doc = json.loads(TOKENS.read_text())
        doc["dark"]["color"]["bg"]["page"]["$value"] = "{color.missing}"
        with self.assertRaisesRegex(build_tokens.CheckError, "missing"):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
