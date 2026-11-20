"""Partiful tokens stay tied to the capture readings."""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((ROOT / name).read_text())


class TokenTests(unittest.TestCase):
    def test_measured_colours_match_readings(self):
        tokens = load("tokens.json")
        readings = load("raw/readings.json")
        self.assertEqual(tokens["light"]["background"]["page"]["$value"], "#f7f7f7")
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "#111111")
        self.assertEqual(tokens["light"]["action"]["fill"]["$value"], "#111111")
        self.assertEqual(tokens["dark"]["background"]["page"]["$value"], "#111111")
        self.assertEqual(tokens["dark"]["text"]["link"]["$value"], "#9ccfff")
        self.assertEqual(readings["marketing"]["page"], "rgb(247, 247, 247)")
        self.assertEqual(readings["app"]["paintedPage"], "rgb(17, 17, 17)")
        self.assertEqual(readings["app"]["resolvedOnLoginAndExplore"]["--primary-color"], "#ab76f6")
        self.assertEqual(readings["app"]["resolvedOnLoginAndExplore"]["--link-color"], "#9CCFFF")

    def test_radius_and_type_are_the_computed_ones(self):
        tokens = load("tokens.json")
        self.assertEqual(tokens["core"]["radius"]["pill"]["$value"], "200px")
        self.assertEqual(tokens["core"]["radius"]["round"]["$value"], "800px")
        self.assertEqual(tokens["core"]["radius"]["control"]["$value"], "4px")
        self.assertEqual(tokens["core"]["typography"]["marketing-hero"]["$value"]["fontSize"], "64px")
        self.assertEqual(tokens["core"]["typography"]["app-header"]["$value"]["fontSize"], "28px")
        self.assertEqual(
            tokens["core"]["font"]["family"]["janky"]["$value"],
            "Partiful Janky Inter Display Regular, sans-serif",
        )

    def test_screenshot_gap_and_phone_gate_are_recorded(self):
        readings = load("raw/readings.json")
        self.assertIn("not producing screenshot frames", readings["screenshotNote"])
        self.assertIn("Phone number", readings["pages"]["login"]["gate"])
        self.assertIn("No phone number was typed.", readings["notEntered"])

    def test_every_token_has_a_source(self):
        # docs/EVIDENCE.md: every value says where it came from.
        doc = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(doc, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
