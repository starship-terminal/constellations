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


class TokenTest(unittest.TestCase):
    def test_every_token_names_a_source(self):
        missing = [path for path, token in walk(TOKENS["core"]) if "source" not in token.get("$extensions", {})]
        missing += [path for path, token in walk(TOKENS["light"]) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_page_and_action_match_the_computed_styles(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#fafafa")
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"], "#0a4afd")
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "#212121")
        self.assertEqual(READINGS["body"]["backgroundColor"], "rgb(250, 250, 250)")
        self.assertEqual(READINGS["components"]["primaryButton"]["background"], "rgb(10, 74, 253)")

    def test_light_only(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual(READINGS["prefersColorSchemeDarkRules"], 0)

    def test_no_reduced_motion_rule_was_invented(self):
        self.assertEqual(READINGS["motion"]["prefersReducedMotionRules"], 0)


if __name__ == "__main__":
    unittest.main()
