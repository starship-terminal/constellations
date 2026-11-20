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
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual(build_tokens.render(build_tokens.build()), TOKENS.read_text())

    def test_no_value_claims_a_reading_raw_does_not_hold(self):
        # raw/readings.json holds no style values, so nothing may be labelled Measured.
        doc = build_tokens.build()
        for name in ("core", "dark"):
            for path, token in build_tokens.walk(doc[name]):
                with self.subTest(token=f"{name}.{'.'.join(path)}"):
                    self.assertNotEqual(token["$extensions"]["source"]["evidence"], "Measured")

    def test_missing_alias_fails(self):
        doc = json.loads(TOKENS.read_text())
        doc["dark"]["color"]["bg"]["page"]["$value"] = "{color.missing}"
        with self.assertRaisesRegex(build_tokens.CheckError, "missing"):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
