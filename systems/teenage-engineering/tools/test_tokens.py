"""Teenage Engineering tokens resolve, and the measured colours are the ones that were read."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def flatten(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        return {path: node["$value"]}
    out = {}
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            out.update(flatten(child, f"{path}.{key}" if path else key))
    return out


FLAT = flatten(TOKENS)


def resolve(value, depth=0):
    if depth > 8 or not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    ref = value[1:-1]
    if ref not in FLAT:
        raise AssertionError(f"missing alias {ref}")
    return resolve(FLAT[ref], depth + 1)


class TokenFile(unittest.TestCase):
    def test_store_page_is_white(self):
        self.assertEqual(resolve(FLAT["light.background.page"]), "#ffffff")

    def test_action_is_the_measured_near_black(self):
        self.assertEqual(resolve(FLAT["light.background.action"]), "#0f0e12")

    def test_subscribe_label_is_te_white(self):
        self.assertEqual(resolve(FLAT["light.text.on-action"]), "#f5f5f5")

    def test_product_stage_is_black(self):
        self.assertEqual(resolve(FLAT["light.background.stage"]), "#000000")

    def test_desktop_button_height_is_the_computed_size(self):
        self.assertEqual(FLAT["core.size.button-md"], "73px")

    def test_every_alias_resolves(self):
        for value in FLAT.values():
            if isinstance(value, str) and value.startswith("{"):
                resolve(value)
            if isinstance(value, dict):
                for item in value.values():
                    if isinstance(item, str) and item.startswith("{"):
                        resolve(item)


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
