"""stage.so tokens stay inside colours measured on the Spaceship listing."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())

MEASURED = {
    "#171f66", "#ffffff", "#2b2b2d", "#575758", "#cbcbcc", "#f9f9f9",
    "#394eff", "#ffffffcc", "#ffffffb3", "#ffffff0d", "#07070c36", "#17181a",
    "#17181a0f", "#17181a17", "#17181a12",
}


def colours(node):
    if isinstance(node, dict):
        if node.get("$type") == "color" and isinstance(node.get("$value"), str):
            if node["$value"].startswith("#"):
                yield node["$value"].lower()
        for child in node.values():
            yield from colours(child)


class Tokens(unittest.TestCase):
    def test_every_literal_colour_was_measured(self):
        found = set(colours(TOKENS))
        self.assertTrue(found, "no colour tokens")
        self.assertEqual(found - MEASURED, set())

    def test_listing_theme_only(self):
        self.assertIn("listing", TOKENS)
        self.assertNotIn("light", TOKENS)
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["listing"])

    def test_cover_screenshot_exists(self):
        self.assertTrue((ROOT / "screenshots" / "listing-desktop-default.png").is_file())


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
