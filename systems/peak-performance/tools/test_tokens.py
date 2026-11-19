"""Checks the committed Peak Performance tokens against the readings.

Run from the package tools directory, which is what tools/package_tests.py does.
"""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
RAW = pathlib.Path(__file__).resolve().parent.parent / "raw" / "computed.json"


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from flat(value, path)


class TokenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tokens = json.loads(TOKENS.read_text())
        cls.flat = dict(flat(cls.tokens))
        cls.raw = json.loads(RAW.read_text())

    def test_every_token_has_a_source(self):
        missing = [path for path, token in self.flat.items()
                   if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_live_colours_match_the_reading(self):
        self.assertEqual(self.flat["core.color.lime"]["$value"], "#effda4")
        self.assertEqual(self.flat["core.color.ink"]["$value"], "#000000")
        self.assertEqual(self.flat["core.color.paper"]["$value"], "#ffffff")
        self.assertEqual(self.flat["core.color.sand"]["$value"], "#ebe9e1")
        banner = self.raw["computed"]["rotatingBanner"]["backgroundColor"]
        self.assertEqual(banner, "rgb(239, 253, 164)")

    def test_hero_type_matches_the_reading(self):
        hero = self.flat["core.typography.hero"]["$value"]
        reading = self.raw["computed"]["heroTitle"]
        self.assertEqual(hero["fontSize"], reading["fontSize"])
        self.assertEqual(hero["letterSpacing"], reading["letterSpacing"])
        self.assertEqual(hero["lineHeight"], reading["lineHeight"])

    def test_pill_radius_is_24px(self):
        self.assertEqual(self.flat["core.radius.pill"]["$value"], "24px")
        self.assertEqual(self.raw["computed"]["pillOnPhoto"]["borderRadius"], "24px")

    def test_only_a_light_theme_set(self):
        self.assertIn("light", self.tokens)
        self.assertNotIn("dark", self.tokens)
        self.assertEqual(self.raw["colorScheme"], "normal")

    def test_viewport_was_1440(self):
        self.assertEqual(self.raw["viewport"]["innerWidth"], 1440)
        self.assertEqual(self.raw["viewport"]["devicePixelRatio"], 2)


if __name__ == "__main__":
    unittest.main()
