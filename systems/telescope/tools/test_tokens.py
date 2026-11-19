"""The committed tokens resolve, and the measured marketing and login colours stay put."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads(TOKENS.read_text())

    def test_measured_marketing_page_and_accent(self):
        light = self.tokens["light"]["color"]
        self.assertEqual(light["page"]["$value"], "#f4f3f0")
        self.assertEqual(light["ink"]["$value"], "#1a1915")
        self.assertEqual(light["accent"]["$value"], "#e3f794")

    def test_measured_login_dark(self):
        dark = self.tokens["dark"]["color"]
        self.assertEqual(dark["page"]["$value"], "#2b2b2e")
        self.assertEqual(dark["ink"]["$value"], "#e3e5e7")
        self.assertEqual(dark["surface"]["$value"], "#3b3d3f")

    def test_every_token_names_a_source(self):
        missing = []

        def walk(node, path):
            if not isinstance(node, dict):
                return
            if "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(path)
                return
            for key, child in node.items():
                if not key.startswith("$"):
                    walk(child, f"{path}.{key}" if path else key)

        walk(self.tokens, "")
        self.assertEqual(missing, [])
