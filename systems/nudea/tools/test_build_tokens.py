"""Checks for the Nudea token builder. Run from this folder, or via tools/package_tests.py."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_build_passes_check(self):
        doc = build_tokens.build()
        flat = build_tokens.check(doc)
        self.assertIn("color.cotton", flat)
        self.assertEqual(flat["color.cotton"]["$value"], "#fbfaf2")
        self.assertEqual(flat["color.raven"]["$value"], "#333333")
        self.assertEqual(flat["color.red"]["$value"], "#ad2c2c")

    def test_committed_tokens_match_build(self):
        self.assertTrue(TOKENS.exists(), "tokens.json missing")
        committed = json.loads(TOKENS.read_text())
        built = build_tokens.build()
        self.assertEqual(committed, built)

    def test_missing_alias_fails(self):
        doc = build_tokens.build()
        doc["light"]["color"]["page"]["$value"] = "{color.does-not-exist}"
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)

    def test_missing_source_fails(self):
        doc = build_tokens.build()
        doc["core"]["color"]["cotton"].pop("$extensions")
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)

    def test_easings_are_four_number_lists(self):
        easing = build_tokens.build()["core"]["motion"]["easing"]
        self.assertEqual(easing["out-slow"]["$value"], [0, 0, 0.3, 1])
        self.assertEqual(easing["in-out"]["$value"], [0.42, 0, 0.58, 1])

    def test_a_string_easing_fails(self):
        doc = build_tokens.build()
        doc["core"]["motion"]["easing"]["out-slow"]["$value"] = "cubic-bezier(0, 0, 0.3, 1)"
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)


if __name__ == "__main__":
    unittest.main()
