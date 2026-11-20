"""The On tokens match the readings taken on 2026-11-19.

These checks compare tokens.json with raw/readings.json. They do not open the site.
"""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text())


class TokenReadings(unittest.TestCase):
    def setUp(self):
        self.tokens = load("tokens.json")
        self.readings = load("raw/readings.json")

    def token(self, *path):
        node = self.tokens
        for part in path:
            node = node[part]
        return node["$value"]

    def test_page_and_ink_match_the_body(self):
        self.assertEqual(self.token("light", "background", "page"), "#ffffff")
        self.assertEqual(self.token("light", "text", "primary"), "#000000")
        self.assertEqual(self.readings["computed"]["body"]["background"], "rgb(255, 255, 255)")
        self.assertEqual(self.readings["computed"]["body"]["color"], "rgb(0, 0, 0)")

    def test_button_and_radius_match_the_readings(self):
        self.assertEqual(self.token("core", "size", "button"), "48px")
        self.assertEqual(self.token("core", "radius", "pill"), "40px")
        self.assertEqual(self.readings["computed"]["button"]["height"], "48px")
        self.assertEqual(self.readings["computed"]["button"]["borderRadius"], "40px")

    def test_circle_radius_is_the_computed_percent(self):
        self.assertEqual(self.token("core", "radius", "circle"), "50%")
        self.assertEqual(self.readings["computed"]["iconButton"]["borderRadius"], "50%")

    def test_label_and_focus_are_the_measured_colours(self):
        self.assertEqual(self.token("light", "text", "label"), "#995c00")
        self.assertEqual(self.token("light", "border", "focus"), "#2f7efe")

    def test_every_token_names_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source")
                if not isinstance(source, str) or not source.strip():
                    missing.append(".".join(path))
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + [key])

        walk(self.tokens, [])
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
