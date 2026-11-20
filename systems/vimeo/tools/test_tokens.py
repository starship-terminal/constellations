#!/usr/bin/env python3
"""The measured brand, page, and button values survive the token build."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def get(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node["$value"]


class Tokens(unittest.TestCase):
    def test_brand_and_page(self):
        self.assertEqual(get("core.color.fill-brand"), "#17d5ff")
        self.assertEqual(get("core.color.background"), "#f6f8fa")
        self.assertEqual(get("core.color.text-primary"), "#0e1216")
        self.assertEqual(get("core.color.focus"), "#17d5ff")

    def test_semantic_alias(self):
        self.assertEqual(get("light.background.page"), "{color.background}")
        self.assertEqual(get("light.background.fill-brand"), "{color.fill-brand}")

    def test_button_metrics(self):
        self.assertEqual(get("light.component.button-brand.radius"), "16px")
        self.assertEqual(get("light.component.button-brand.height"), "48px")
        self.assertEqual(get("light.component.button-marketing.radius"), "12px")

    def test_no_dark_set(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual(TOKENS["$themes"][0]["id"], "light")


# ---- every token records where its value came from (docs/EVIDENCE.md)
import json as _json
import pathlib as _pathlib

_TOKENS_FILE = _pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def _unsourced(node, path=()):
    """Dotted paths of leaves whose $extensions.source is missing or empty."""
    out = []
    for key, child in node.items():
        if key.startswith("$") or not isinstance(child, dict):
            continue
        if "$value" in child:
            source = (child.get("$extensions") or {}).get("source")
            if not source:
                out.append(".".join(path + (key,)))
        else:
            out.extend(_unsourced(child, path + (key,)))
    return out


class EverySourcedTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = _unsourced(_json.loads(_TOKENS_FILE.read_text()))
        self.assertEqual(missing, [], "tokens with no $extensions.source")

    def test_unsourced_leaf_is_reported(self):
        tree = {"core": {"a": {"$value": "#000", "$extensions": {"source": {}}},
                         "b": {"$value": "#fff", "$extensions": {"source": {"evidence": "Measured"}}}}}
        self.assertEqual(_unsourced(tree), ["core.a"])


if __name__ == "__main__":
    unittest.main()
