#!/usr/bin/env python3
"""SoundCloud tokens stay inside the measured set."""
import json, pathlib, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

MEASURED = {
    "#121212", "#303030", "#ffffff", "#999999", "#ff5500", "#ffffff29",
    "#f3f3f3", "#699fff", "#044dd2", "#ffffff66", "#666666", "#12121229",
    "#e76b9f", "#ab87e2", "#1a1b1f",
}


class Tokens(unittest.TestCase):
    def test_both_themes(self):
        self.assertEqual([t["id"] for t in T["$themes"]], ["dark", "light"])

    def test_page_and_accent(self):
        self.assertEqual(T["dark"]["color"]["page"]["$value"], "#121212")
        self.assertEqual(T["dark"]["color"]["accent"]["$value"], "#ff5500")
        self.assertEqual(T["light"]["color"]["page"]["$value"], "#ffffff")

    def test_hex_colours_were_measured(self):
        for theme in ("dark", "light"):
            for name, tok in T[theme]["color"].items():
                value = tok["$value"]
                if isinstance(value, str) and value.startswith("#"):
                    self.assertIn(value, MEASURED, f"{theme}.{name}")

    def test_pill_radius(self):
        self.assertEqual(T["core"]["radius"]["pill"]["$value"], "9999px")


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
