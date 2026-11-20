#!/usr/bin/env python3
"""Squarespace tokens stay inside the captured set, and only raw/-backed ones claim a reading."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

CAPTURED = {
    "#ffffff", "#000000", "#0e0e0e", "#666666", "#5a5a5a", "#898989",
    "#adadad", "#b7b7b7", "#f2f2f2", "#dddddd", "#0072f0", "#242424",
    "#e7e7e7", "#c32d38", "#f9f9f9",
}


class Tokens(unittest.TestCase):
    def test_light_only(self):
        self.assertEqual([theme["id"] for theme in T["$themes"]], ["light"])
        self.assertNotIn("dark", T)

    def test_accent_is_the_captured_blue(self):
        self.assertEqual(T["light"]["color"]["accent"]["$value"], "#0072f0")
        self.assertEqual(T["light"]["color"]["ink"]["$value"], "#000000")

    def test_hex_colours_stay_in_the_captured_set(self):
        for name, tok in T["light"]["color"].items():
            value = tok["$value"]
            if isinstance(value, str) and value.startswith("#"):
                self.assertIn(value, CAPTURED, name)

    def test_control_radius(self):
        self.assertEqual(T["core"]["radius"]["control"]["$value"], "4px")
        self.assertEqual(T["core"]["radius"]["none"]["$value"], "0px")


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


# raw/readings.json holds no colour or type readings apart from four colours in its notes (the
# Get Started hover, the login error text, the settled plan CTA and its text). Every other value
# was entered by hand at capture time (docs/EVIDENCE.md: Reconstruction), so only these four
# tokens may claim a reading, and each must still find it in raw/.
RAW = HERE / "raw"
HAND = "Reconstruction: entered by hand at capture time"
RAW_BACKED = {
    "light.color.hover": "background rgb(221, 221, 221)",
    "light.color.error": "Error color rgb(195, 45, 56)",
    "light.component.button-primary.background": "plan CTA at rgb(0, 0, 0)",
    "light.component.button-primary.text": "rgb(0, 0, 0) with white text",
}


def unbacked_claims(tree, backed, raw_text):
    """Token paths whose source claims a reading that raw/ does not hold."""
    bad = []

    def walk(node, path):
        if isinstance(node, dict) and "$value" in node:
            source = (node.get("$extensions") or {}).get("source", "")
            reading = backed.get(path)
            if reading is not None:
                if reading not in raw_text:
                    bad.append(path)
            elif not source.startswith(HAND):
                bad.append(path)
            return
        if isinstance(node, dict):
            for k, v in node.items():
                if not k.startswith("$"):
                    walk(v, f"{path}.{k}" if path else k)

    walk(tree, "")
    return bad


class Provenance(unittest.TestCase):
    def test_only_raw_backed_tokens_claim_a_reading(self):
        raw_text = "".join(p.read_text() for p in sorted(RAW.glob("*.json")))
        self.assertEqual(unbacked_claims(T, RAW_BACKED, raw_text), [])

    def test_raw_backed_values_match_their_reading(self):
        def rgb(hex_):
            return "rgb(%d, %d, %d)" % tuple(int(hex_[i:i + 2], 16) for i in (1, 3, 5))
        light = T["light"]
        self.assertEqual(rgb(light["color"]["hover"]["$value"]), "rgb(221, 221, 221)")
        self.assertEqual(rgb(light["color"]["error"]["$value"]), "rgb(195, 45, 56)")
        self.assertEqual(rgb(light["component"]["button-primary"]["background"]["$value"]), "rgb(0, 0, 0)")
        self.assertEqual(light["component"]["button-primary"]["text"]["$value"], "#ffffff")

    def test_a_measured_claim_without_a_reading_fails(self):
        tree = {"light": {"a": {"$value": "#000000", "$extensions": {"source": "Measured: h2 color"}},
                          "b": {"$value": "#ffffff", "$extensions": {"source": HAND + "; no raw/ file holds this reading."}}}}
        self.assertEqual(unbacked_claims(tree, {}, ""), ["light.a"])
        self.assertEqual(unbacked_claims(tree, {"light.a": "rgb(0, 0, 0)"}, ""), ["light.a"])


if __name__ == "__main__":
    unittest.main()
