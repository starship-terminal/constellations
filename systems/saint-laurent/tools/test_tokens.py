"""Saint Laurent tokens stay tied to the measured readings."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class Tokens(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.raw = json.loads((ROOT / "raw" / "css-vars.json").read_text())

    def test_page_is_measured_white(self):
        self.assertEqual(self.tokens["light"]["page"]["$value"], "#ffffff")
        self.assertIn("255,255,255", self.raw["vars"]["--color-background-primary"])

    def test_text_is_black(self):
        self.assertEqual(self.tokens["light"]["text"]["$value"], "#000000")
        self.assertEqual(self.raw["vars"]["--color-text-primary"], "#000")

    def test_button_radius_is_zero(self):
        self.assertEqual(self.tokens["light"]["component"]["button"]["radius"]["$value"], "{core.radius.none}")
        self.assertEqual(self.tokens["core"]["radius"]["none"]["$value"], "0px")

    def test_ui_size_is_twelve(self):
        self.assertEqual(self.tokens["core"]["typography"]["ui"]["$value"]["fontSize"], "12px")


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
