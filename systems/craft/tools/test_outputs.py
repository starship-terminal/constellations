"""Checks on craft's committed tokens."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_pill_radius_is_not_the_css_maximum(self):
        self.assertEqual(T["core"]["radius"]["full"]["$value"], "9999px")

    def test_hand_entered_and_wrong_element_values_say_so(self):
        self.assertTrue(T["core"]["border"]["hairline"]["width"]["$extensions"]["source"].startswith("Reconstruction:"))
        self.assertIn("not the TEAM card", T["core"]["shadow"]["block"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
