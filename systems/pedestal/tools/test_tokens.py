"""Pedestal tokens stay tied to the measured readings.

Run from the package tools directory:

    python3 -m unittest test_tokens
"""
import json
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((PKG / "tokens.json").read_text())
READINGS = json.loads((PKG / "raw" / "readings.json").read_text())


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def hex_of(rgb):
    """rgb(250, 250, 250) as #fafafa."""
    parts = [int(n) for n in rgb[rgb.index("(") + 1:rgb.index(")")].split(",")[:3]]
    return "#{:02x}{:02x}{:02x}".format(*parts)


class TokenTest(unittest.TestCase):
    def test_every_token_names_a_source(self):
        missing = [path for path, token in walk(TOKENS["core"]) if "source" not in token.get("$extensions", {})]
        missing += [path for path, token in walk(TOKENS["light"]) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_page_and_action_match_the_computed_styles(self):
        # Each token against its own reading, not against a literal typed here.
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], hex_of(READINGS["body"]["backgroundColor"]))
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"],
                         hex_of(READINGS["components"]["primaryButton"]["background"]))
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], hex_of(READINGS["body"]["color"]))

    def test_light_only(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual(READINGS["prefersColorSchemeDarkRules"], 0)

    def test_no_reduced_motion_rule_was_invented(self):
        self.assertEqual(READINGS["motion"]["prefersReducedMotionRules"], 0)


if __name__ == "__main__":
    unittest.main()
