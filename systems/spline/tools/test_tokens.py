"""The Spline tokens resolve, and the measured colours are the ones that were read."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parent.parent / "tokens.json"


def load():
    return json.loads(TOKENS.read_text())


def lookup(data, path):
    node = data
    for part in path.split("."):
        node = node[part]
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return lookup(data, value[1:-1])
    return value


class Tokens(unittest.TestCase):
    def test_measured_colours(self):
        data = load()
        self.assertEqual(lookup(data, "dark.background.page"), "#000000")
        self.assertEqual(lookup(data, "dark.background.surface"), "#101010")
        self.assertEqual(lookup(data, "dark.text.primary"), "#eeeeee")
        self.assertEqual(lookup(data, "dark.text.secondary"), "#8a8a8a")
        self.assertEqual(lookup(data, "dark.background.action"), "#eeeeee")
        self.assertEqual(lookup(data, "dark.border.stroke"), "#2e2e2e")

    def test_button_aliases_resolve(self):
        data = load()
        self.assertEqual(lookup(data, "dark.component.button.bg"), "#eeeeee")
        self.assertEqual(lookup(data, "dark.component.button.radius"), "999px")
        self.assertEqual(lookup(data, "dark.component.button.height"), "44px")

    def test_type_uses_the_computed_hero(self):
        data = load()
        display = lookup(data, "core.typography.display")
        self.assertEqual(display["fontSize"], "72px")
        self.assertEqual(display["fontWeight"], 450)
        self.assertEqual(display["letterSpacing"], "-4.32px")

    def test_one_dark_theme(self):
        data = load()
        self.assertEqual([t["id"] for t in data["$themes"]], ["dark"])
        self.assertNotIn("light", data)

    def test_login_extracted_stays_not_started(self):
        review = json.loads((Path(__file__).resolve().parent.parent / "login-review.json").read_text())
        self.assertEqual(review["login_extracted"], "not-started")
        self.assertIs(review["signed_in"], False)
        self.assertIn("Email", review["wall"]["login_fields_empty"])
        self.assertIn("Continue with Google", review["wall"]["identity_providers_not_clicked"])
        tree = (Path(__file__).resolve().parent.parent / "site-tree.md").read_text()
        self.assertIn("2026-11-22", tree)
        self.assertIn("https://spline.design/", tree)


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
