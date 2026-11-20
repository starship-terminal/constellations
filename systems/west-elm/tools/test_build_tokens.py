"""build_tokens.check refuses a leaf with no source and a bad dimension."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_translucent_colours_are_hex(self):
        self.assertEqual(build_tokens.color("rgba(0, 0, 0, 0.4)"), "#00000066")
        bad = {"core": {"scrim": {"$type": "color", "$value": "rgba(0, 0, 0, 0.4)",
                                  "$extensions": {"source": "test"}}}}
        with self.assertRaises(ValueError):
            build_tokens.check(bad)

    def test_leaf_needs_a_source(self):
        bad = {"core": {"color": {"ink": {"$type": "color", "$value": "#212121"}}}}
        with self.assertRaises(ValueError):
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
