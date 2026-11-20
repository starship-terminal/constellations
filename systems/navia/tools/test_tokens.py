#!/usr/bin/env python3
"""Navia: every token names a source, and the measured pairs match the readings."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
VARS = json.loads((ROOT / "raw" / "css-vars.json").read_text())


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        here = f"{path}.{key}" if path else key
        if isinstance(value, dict) and "$value" in value:
            yield here, value
        elif isinstance(value, dict):
            yield from walk(value, here)


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        # every token, component aliases included: a token without a source is a gap whatever it aliases
        missing = [path for path, token in walk(TOKENS) if not (token.get("$extensions") or {}).get("source")]
        self.assertEqual(missing, [])

    def test_page_accent_and_orange_match_the_sheet(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "{core.color.cream}")
        self.assertEqual(TOKENS["core"]["color"]["cream"]["$value"], "#faf4e6")
        self.assertEqual(TOKENS["core"]["color"]["yellow"]["$value"], "#e8ff39")
        self.assertEqual(TOKENS["core"]["color"]["orange"]["$value"], "#f88450")
        self.assertEqual(TOKENS["core"]["color"]["ink"]["$value"], "#36312a")
        self.assertEqual(VARS["root"]["--_primitives---colors--neutral-lightest"], "#faf4e6")
        self.assertEqual(VARS["root"]["--_primitives---colors--yellow"], "#e8ff39")

    def test_app_gate_focus_is_the_orange_ring(self):
        self.assertEqual(TOKENS["core"]["color"]["focus"]["$value"], "#f88450")
        self.assertEqual(VARS["appGate"]["vars"]["--ring"], "#f88450")


if __name__ == "__main__":
    unittest.main()
