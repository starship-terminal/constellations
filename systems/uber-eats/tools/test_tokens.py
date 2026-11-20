"""The Uber Eats tokens match the live readings in raw/computed.json."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "computed.json").read_text())


class TokensTest(unittest.TestCase):
    def test_page_and_ink_match_the_computed_body(self):
        light = TOKENS["light"]["background"]
        self.assertEqual(light["page"]["$value"], "#ffffff")
        self.assertEqual(light["ink"]["$value"], "#111111")
        self.assertEqual(RAW["computed"]["body"]["color"], "rgb(17, 17, 17)")

    def test_hero_size_is_the_measured_heading(self):
        hero = TOKENS["core"]["typography"]["display-hero"]["$value"]
        self.assertEqual(hero["fontSize"], "52px")
        self.assertEqual(hero["lineHeight"], "64px")
        self.assertEqual(hero["fontWeight"], 700)
        self.assertEqual(RAW["computed"]["h1"]["fontSize"], "52px")

    def test_brand_blue_is_the_declared_token_not_the_button(self):
        self.assertEqual(TOKENS["light"]["brand"]["background"]["$value"], "#276ef1")
        self.assertEqual(TOKENS["light"]["component"]["button-primary-background"]["$value"], "#111111")

    def test_search_radius_is_32px(self):
        self.assertEqual(TOKENS["core"]["radius"]["search"]["$value"], "32px")
        self.assertEqual(RAW["computed"]["searchShell"]["radius"], "32px")


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
