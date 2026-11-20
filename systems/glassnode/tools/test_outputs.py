"""Committed tokens: readings sit in the theme they were painted in, and every theme sources core."""
import json
import pathlib
import unittest

T = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class Outputs(unittest.TestCase):
    def test_dark_surface_reading_is_in_the_dark_set(self):
        self.assertNotIn("tokenization", T["light"].get("measured", {}))
        self.assertEqual(T["dark"]["measured"]["tokenization"]["tokNavInk"]["$value"], "#b8b8b5")

    def test_every_theme_sources_core(self):
        for th in T["$themes"]:
            self.assertEqual(th["selectedTokenSets"].get("core"), "source", th["id"])


if __name__ == "__main__":
    unittest.main()
