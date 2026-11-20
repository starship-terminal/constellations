"""Rork tokens match the computed readings."""

import json
import pathlib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())

    def test_page_is_the_body_background(self):
        self.assertEqual(self.tokens["dark"]["surface"]["page"]["$value"], "#171717")

    def test_text_is_white(self):
        self.assertEqual(self.tokens["dark"]["text"]["primary"]["$value"], "#ffffff")

    def test_sign_in_button_is_white(self):
        self.assertEqual(self.tokens["dark"]["action"]["primary"]["$value"], "#ffffff")

    def test_max_gradient_stops_are_the_canvas_readings(self):
        accent = self.tokens["dark"]["accent"]
        self.assertEqual(accent["max-start"]["$value"], "#e17100")
        self.assertEqual(accent["max-end"]["$value"], "#ca3500")

    def test_composer_radius(self):
        self.assertEqual(self.tokens["core"]["radius"]["composer"]["$value"], "28px")

    def test_body_size(self):
        self.assertEqual(self.tokens["core"]["fontSize"]["body"]["$value"], "16px")

class Sources(unittest.TestCase):
    """EVIDENCE.md makes a source mandatory on every token."""

    def test_every_token_has_a_source(self):
        doc = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not (node.get("$extensions") or {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v, f"{path}.{k}" if path else k)

        for name, tree in doc.items():
            if not name.startswith("$"):
                walk(tree, name)
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
