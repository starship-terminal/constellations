#!/usr/bin/env python3
"""The Peerlist token builder reproduces the committed tokens.json from raw/readings.json.

The build runs in memory: nothing here writes tokens.json.
"""
import json
import re
import unittest
from pathlib import Path

import build_tokens

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "readings.json").read_text())


def resolve(doc, theme, value):
    """Follow `{a.b}` aliases the way the catalog does: the theme's set first, then core."""
    seen = set()
    while isinstance(value, str) and value.startswith("{"):
        if value in seen:
            raise AssertionError(f"alias cycle at {value}")
        seen.add(value)
        path = value.strip("{}").split(".")
        node = None
        for root in (doc[theme], doc["core"]):
            node = root
            for part in path:
                node = node.get(part) if isinstance(node, dict) else None
            if node is not None:
                break
        if node is None:
            raise AssertionError(f"{value} resolves to nothing")
        value = node["$value"]
    return value


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
    elif isinstance(node, dict):
        for key, child in node.items():
            if not key.startswith("$"):
                yield from leaves(child, f"{path}.{key}" if path else key)


def triplet(hex_value):
    return " ".join(str(int(hex_value[i:i + 2], 16)) for i in (1, 3, 5))


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_measured_green_and_page(self):
        self.assertEqual(TOKENS["core"]["color"]["green"]["$value"], "#00aa45")
        self.assertEqual(TOKENS["light"]["page"]["$value"], "{color.gray.00}")
        self.assertEqual(TOKENS["core"]["radius"]["button"]["$value"], "12px")

    def test_dark_set_resolves_to_the_declared_dark_ramp(self):
        dark = RAW["rootTokens"]["darkDeclared"]
        page = resolve(TOKENS, "dark", TOKENS["dark"]["page"]["$value"])
        text = resolve(TOKENS, "dark", TOKENS["dark"]["text"]["$value"])
        self.assertEqual(triplet(page), dark["--gray-00"])
        self.assertEqual(triplet(text), dark["--gray-1k"])
        self.assertNotEqual(page, resolve(TOKENS, "light", TOKENS["light"]["page"]["$value"]))
        for name, token in TOKENS["dark"].items():
            self.assertNotRegex(token["$value"], r"^\{color\.gray\.", name)

    def test_gray_ramps_are_the_readings(self):
        for group, theme in (("gray", "light"), ("gray-dark", "darkDeclared")):
            for step, token in TOKENS["core"]["color"][group].items():
                self.assertEqual(triplet(token["$value"]), RAW["rootTokens"][theme][f"--gray-{step}"])

    def test_every_alias_resolves_and_every_leaf_has_a_source(self):
        for theme in ("light", "dark"):
            for path, token in leaves(TOKENS[theme]):
                resolve(TOKENS, theme, token["$value"])
        for set_name in ("core", "light", "dark"):
            for path, token in leaves(TOKENS[set_name]):
                self.assertTrue(token.get("$extensions", {}).get("source"), f"{set_name}.{path}")
                if token["$type"] == "color" and not token["$value"].startswith("{"):
                    self.assertRegex(token["$value"], r"^#[0-9a-f]{6}([0-9a-f]{2})?$", path)

    def test_measured_type_matches_the_readings(self):
        computed = RAW["computed"]
        for token, reading in (("body", "body"), ("display", "h1"), ("section", "sectionH2"),
                               ("title", "h3"), ("subhead", "subhead"), ("ui", "navLink"),
                               ("label", "label"), ("app-title", "appH1")):
            value = TOKENS["core"]["typography"][token]["$value"]
            for prop in ("fontSize", "lineHeight", "fontWeight"):
                self.assertEqual(value[prop], computed[reading][prop], f"{token}.{prop}")


if __name__ == "__main__":
    unittest.main()
