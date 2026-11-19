#!/usr/bin/env python3
"""Slite package: every token has a source, and the measured colours match."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())


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
        missing = [path for path, token in walk(TOKENS) if not token.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_measured_colours(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#fdfdfd")
        self.assertEqual(TOKENS["light"]["surface"]["$value"], "#fdf9f4")
        self.assertEqual(TOKENS["light"]["text"]["$value"], "#3f434a")
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#f67748")
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"], "#2d2f34")
        self.assertEqual(TOKENS["core"]["fontSize"]["hero"]["$value"], "56px")
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "999px")


if __name__ == "__main__":
    unittest.main()
