"""The Dinner Ladies tokens match the computed styles read on 2026-11-19."""

import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


def load():
    return json.loads(TOKENS.read_text())


def value(tree, path):
    node = tree
    for part in path.split("."):
        node = node[part]
    return node["$value"]


class TokenReadings(unittest.TestCase):
    def setUp(self):
        self.tokens = load()

    def test_page_is_the_measured_cream(self):
        self.assertEqual(value(self.tokens, "core.color.brand.cream"), "#fff1e6")
        self.assertEqual(value(self.tokens, "light.background.page"), "{core.color.brand.cream}")

    def test_action_red_matches_the_button(self):
        self.assertEqual(value(self.tokens, "core.color.brand.red"), "#dd1f26")
        self.assertEqual(value(self.tokens, "core.color.brand.red-hot"), "#dd1d1d")

    def test_body_type_matches_computed(self):
        self.assertEqual(value(self.tokens, "core.font.size.body"), "16px")
        self.assertEqual(value(self.tokens, "core.font.line-height.body"), "28.8px")
        self.assertIn("Denim Regular", value(self.tokens, "core.font.family.body"))

    def test_button_radius_is_square(self):
        self.assertEqual(value(self.tokens, "core.radius.none"), "0px")
        self.assertEqual(value(self.tokens, "light.component.button.radius"), "{core.radius.none}")

    def test_motion_duration_is_declared(self):
        self.assertEqual(value(self.tokens, "core.motion.duration.short"), "100ms")
        self.assertEqual(value(self.tokens, "core.motion.easing.out-slow"), "cubic-bezier(0, 0, 0.3, 1)")

    def test_selected_fill_is_brand_grey(self):
        self.assertEqual(value(self.tokens, "core.color.brand.grey"), "#dbe7ef")
        self.assertEqual(value(self.tokens, "light.action.selected"), "{core.color.brand.grey}")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                ext = node.get("$extensions") or {}
                if not ext.get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, f"{path}.{key}" if path else key)

        walk(self.tokens, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
