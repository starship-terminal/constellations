"""The Washington Post builder reproduces tokens.json and reads each theme from its own capture."""
import json
import pathlib
import unittest

import build_tokens

HERE = pathlib.Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; importing the builder writes nothing.
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_light_accent_is_the_light_sign_in_reading(self):
        accent = build_tokens.tokens["light"]["accent"]
        self.assertEqual(accent["$value"], "#166dfc")
        self.assertNotIn("wpds-dark", accent["$extensions"]["source"])

    def test_colours_are_hex_and_unknown_values_are_refused(self):
        self.assertEqual(build_tokens.rgba_to_hex("rgba(0, 0, 0, 0.1)"), "#0000001a")
        self.assertEqual(build_tokens.rgba_to_hex("rgb(20, 20, 20)"), "#141414")
        with self.assertRaises(ValueError):
            build_tokens.rgba_to_hex("currentColor")


if __name__ == "__main__":
    unittest.main()
