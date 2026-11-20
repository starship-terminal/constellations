"""The marketing tokens still match the computed styles in raw/home.json."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())
HOME = json.loads((ROOT / "raw" / "home.json").read_text())


def value(set_name, *path):
    node = TOKENS[set_name]
    for part in path:
        node = node[part]
    return node["$value"]


class Tokens(unittest.TestCase):
    def test_page_and_ink(self):
        self.assertEqual(value("core", "color", "page"), "#ffffff")
        self.assertEqual(value("core", "color", "ink"), "#000000")
        self.assertEqual(value("core", "color", "hero-wash"), "#edf1f5")
        self.assertEqual(value("core", "color", "secondary-fill"), "#dadfe5")

    def test_display_size_matches_the_live_read(self):
        display = value("core", "typography", "display")
        self.assertEqual(display["fontSize"], "68px")
        self.assertEqual(display["lineHeight"], "64px")
        self.assertEqual(display["letterSpacing"], "-2.04px")
        phone = value("core", "typography", "display-phone")
        self.assertEqual(phone["fontSize"], "44px")
        self.assertEqual(phone["letterSpacing"], "-1.32px")

    def test_button_radius_and_height(self):
        self.assertEqual(value("core", "radius", "pill"), "52px")
        self.assertEqual(value("core", "size", "button-height"), "48px")
        self.assertEqual(value("light", "component", "button-primary", "bg"), "{color.action.fill}")

    def test_framer_body_tokens_are_recorded(self):
        declared = HOME["framerColorTokensOnBody"]
        self.assertEqual(declared["--token-5e57362f-188d-445c-b361-1c6deda8f965"], "#edf1f5")
        self.assertEqual(value("core", "color", "text-footer"), "#4c5259")

    def test_login_was_not_submitted(self):
        login = json.loads((ROOT / "raw" / "login-boundary.json").read_text())
        self.assertIn("Nothing typed", login["boundary"])
        self.assertNotIn("app.wynde.io", json.dumps(TOKENS["light"]))


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
