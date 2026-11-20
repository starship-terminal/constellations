"""Checks on craftwork's committed tokens."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_wrong_element_readings_say_so(self):
        for name in ("plan-card", "menu-button"):
            self.assertIn("recapture needed", T["light"]["component"][name]["$extensions"]["source"], name)

    def test_font_sizes_are_dimensions(self):
        for name in ("promo-text", "nav-link-size"):
            self.assertEqual(T["light"]["component"][name]["$type"], "dimension", name)


if __name__ == "__main__":
    unittest.main()
