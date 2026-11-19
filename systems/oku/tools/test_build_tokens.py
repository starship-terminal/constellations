#!/usr/bin/env python3
"""The measured values this package is not allowed to drift from."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if not key.startswith("$"):
                yield from walk(value)


class Tokens(unittest.TestCase):
    def test_every_token_names_a_source(self):
        missing = [token for token in walk(TOKENS) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_dark_page_is_the_painted_milk(self):
        self.assertEqual(TOKENS["dark"]["color"]["page"]["$value"], "#131314")

    def test_light_page_is_white(self):
        self.assertEqual(TOKENS["light"]["color"]["page"]["$value"], "#FFFFFF")

    def test_display_is_fabric_serif(self):
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontFamily"], "FabricSerifWeb")
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontSize"], "48px")

    def test_control_radius_is_8(self):
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], "8px")


if __name__ == "__main__":
    unittest.main()
