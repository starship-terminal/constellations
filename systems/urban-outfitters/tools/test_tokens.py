"""Checks that the Urban Outfitters tokens match the measured readings."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
VARS = json.loads((ROOT / "raw" / "css-vars.json").read_text())["vars"]


def resolve(value, seen=None):
    seen = seen or set()
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        path = value[1:-1]
        if path in seen:
            raise AssertionError(path)
        seen.add(path)
        node = TOKENS
        for part in path.split("."):
            node = node[part]
        return resolve(node["$value"], seen)
    return value


class TokenTests(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, f"{path}.{key}" if path else key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        self.assertEqual(missing, [])

    def test_measured_roles(self):
        self.assertEqual(resolve("{light.background.page}"), "#ffffff")
        self.assertEqual(resolve("{light.text.primary}"), "#222222")
        self.assertEqual(resolve("{light.text.secondary}"), "#707070")
        self.assertEqual(resolve("{light.border.default}"), "#dddddd")
        self.assertEqual(resolve("{light.action.primary}"), "#222222")
        self.assertEqual(resolve("{light.text.sale}"), "#d83604")
        self.assertEqual(resolve("{light.text.promotion}"), "#3a8700")
        self.assertEqual(resolve("{core.color.promo-strip}"), "#eb4034")

    def test_css_vars_agree(self):
        self.assertIn("34, 34, 34", VARS["--grey-dark"])
        self.assertIn("216, 54, 4", VARS["--red"])
        self.assertIn("58, 135, 0", VARS["--green"])
        self.assertEqual(VARS["--font-body"], "Helvetica, Arial, sans-serif")
        self.assertTrue(VARS["--button-primary-background"].endswith("34, 34, 34)"))

    def test_light_only(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual(TOKENS["$themes"][0]["id"], "light")


if __name__ == "__main__":
    unittest.main()
