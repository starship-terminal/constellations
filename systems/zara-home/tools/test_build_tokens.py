"""build_tokens.check refuses a leaf with no source, a bad dimension or colour, and a broken alias."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_leaf_needs_a_source(self):
        bad = {"core": {"color": {"ink": {"$type": "color", "$value": "#1e1e1e"}}}}
        with self.assertRaises(ValueError):
            build_tokens.check(bad)

    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual(TOKENS.read_text(), build_tokens.render())

    def test_translucent_colours_are_hex(self):
        self.assertEqual(build_tokens.color("rgba(0, 0, 0, 0.87)"), "#000000de")
        self.assertEqual(build_tokens.color("rgb(30, 30, 30)"), "#1e1e1e")

    def test_colour_and_alias_are_checked(self):
        src = {"$extensions": {"source": "test"}}
        bad = {"core": {"color": {"ink": {"$type": "color", "$value": "rgba(0, 0, 0, 0.5)", **src}}}}
        with self.assertRaises(ValueError):
            build_tokens.check(bad)
        bad = {"core": {}, "light": {"text": {"$type": "color", "$value": "{color.nothing}", **src}}}
        with self.assertRaises(ValueError):
            build_tokens.check(bad)

    def test_alias_inside_typography_must_resolve(self):
        bad = json.loads(TOKENS.read_text())
        bad["core"]["typography"]["body"]["$value"]["fontSize"] = "{fontSize.missing}"
        with self.assertRaisesRegex(ValueError, "points at nothing"):
            build_tokens.check(bad)

    def test_alias_cycle_is_refused(self):
        bad = json.loads(TOKENS.read_text())
        bad["core"]["color"]["ink"]["$value"] = "{color.ink}"
        with self.assertRaisesRegex(ValueError, "cycle"):
            build_tokens.check(bad)

    def test_malformed_alias_is_refused(self):
        bad = json.loads(TOKENS.read_text())
        bad["core"]["color"]["ink"]["$value"] = "{color.white}oops"
        with self.assertRaisesRegex(ValueError, "malformed"):
            build_tokens.check(bad)

    def test_dimension_is_one_length(self):
        bad = {
            "core": {
                "space": {
                    "bad": {
                        "$type": "dimension",
                        "$value": "8px 16px",
                        "$extensions": {"source": "test"},
                    }
                }
            }
        }
        with self.assertRaises(ValueError):
            build_tokens.check(bad)


if __name__ == "__main__":
    unittest.main()
