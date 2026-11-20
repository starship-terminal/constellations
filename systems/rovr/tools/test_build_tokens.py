"""The committed tokens.json must pass the package check."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        tree = json.loads(TOKENS.read_text())
        self.assertGreater(build_tokens.check(tree), 40)
        self.assertEqual(tree["dark"]["color"]["brand"]["$value"], "#FFF057")
        self.assertEqual(tree["dark"]["color"]["background"]["$value"], "#000000")
        self.assertIn("source", tree["dark"]["color"]["primary"]["$extensions"])


    def test_dangling_alias_fails(self):
        tree = json.loads(TOKENS.read_text())
        tree["dark"]["color"]["background"]["$value"] = "{color.nothing}"
        with self.assertRaises(KeyError):
            build_tokens.check(tree)

    def test_dark_alias_cannot_reach_light_only_names(self):
        tree = json.loads(TOKENS.read_text())
        tree["light"]["color"]["only-light"] = {"$value": "#ffffff", "$type": "color", "$extensions": {"source": "test"}}
        tree["dark"]["color"]["background"]["$value"] = "{color.only-light}"
        with self.assertRaises(KeyError):
            build_tokens.check(tree)

    def test_missing_source_fails(self):
        tree = json.loads(TOKENS.read_text())
        del tree["dark"]["color"]["brand"]["$extensions"]
        with self.assertRaises(ValueError):
            build_tokens.check(tree)

    def test_guide_keeps_decimal_points(self):
        html = (TOKENS.parent / "style-guide.html").read_text()
        self.assertNotRegex(html, r":\s*-?\d+-\d+px;")

    def test_css_value_keeps_decimals_and_dashes_aliases(self):
        import build_style_guide
        for raw in ("28.8px", "0.8px", "-0.19px"):
            self.assertEqual(build_style_guide.css_value({"$type": "dimension", "$value": raw}), raw)
        self.assertEqual(build_style_guide.css_value({"$type": "color", "$value": "{color.brand}"}), "var(--color-brand)")
        self.assertEqual(build_style_guide.css_value({"$type": "dimension", "$value": "{space.1.5}"}), "var(--space-1-5)")


if __name__ == "__main__":
    unittest.main()
