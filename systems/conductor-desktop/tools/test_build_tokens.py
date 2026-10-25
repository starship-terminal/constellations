"""Tests for the colour conversions and the committed tokens.json. Run from this package:
python3 -m unittest discover -s tools. Generic: the colour cases hold for any Electron capture, and
the token checks read whatever tokens.json the package has."""
import json
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, shadow  # noqa: E402

TOKENS = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())


def flat(tree, prefix=()):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from flat(v, prefix + (k,))


def aliases(v):
    if isinstance(v, str):
        return re.findall(r"^\{([^{}]+)\}$", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    if isinstance(v, list):
        return [a for x in v for a in aliases(x)]
    return []


class Colour(unittest.TestCase):
    def test_forms_chromium_computes(self):
        self.assertEqual(color("oklch(0.955 0 0)"), "#f0f0f0")
        self.assertEqual(color("oklch(0.191 0 0)"), "#141414")
        self.assertEqual(color("color(srgb 0.940872 0.941044 0.94106 / 0.74)"), "rgba(240, 240, 240, 0.74)")
        self.assertEqual(color("rgb(89, 156, 231)"), "#599ce7")
        self.assertEqual(color("#F0F0F099"), "rgba(240, 240, 240, 0.6)")
        self.assertEqual(color("lch(100 0 0)"), "#ffffff")
        self.assertEqual(color("lab(50 0 0)"), "#777777")
        self.assertEqual(color("transparent"), "rgba(0, 0, 0, 0)")

    def test_rejects_what_it_cannot_read(self):
        with self.assertRaises(ValueError):
            color("var(--x)")

    def test_shadow_layers(self):
        layers = shadow("oklch(1 0 0 / 0.05) 0px 0px 4px 0px inset, color(srgb 0 0 0 / 0.12) 0px 16px 24px 0px")
        self.assertEqual(len(layers), 2)
        self.assertTrue(layers[0]["inset"])
        self.assertEqual(layers[1]["color"], "rgba(0, 0, 0, 0.12)")
        self.assertEqual(shadow("none"), [])


class CommittedTokens(unittest.TestCase):
    def setUp(self):
        self.core = dict(flat(TOKENS["core"]))
        self.sets = {t: dict(flat(TOKENS[t])) for t in ("light", "dark")}

    def test_every_token_has_a_source(self):
        for name, tree in [("core", self.core)] + list(self.sets.items()):
            for p, t in tree.items():
                self.assertIn("source", t.get("$extensions", {}), f"{name}.{'.'.join(p)}")

    def test_aliases_resolve(self):
        for theme, tree in self.sets.items():
            names = {**self.core, **tree}
            for p, t in tree.items():
                for a in aliases(t["$value"]):
                    self.assertIn(tuple(a.split(".")), names, f"{theme}.{'.'.join(p)} -> {a}")

    def test_themes_have_the_same_names(self):
        self.assertEqual(set(self.sets["light"]), set(self.sets["dark"]))

    def test_checklist_roles_exist(self):
        for role in ("page", "surface", "raised", "overlay", "scrim", "text.primary", "text.secondary", "text.disabled",
                     "text.on-accent", "text.link", "border.default", "border.strong", "border.focus", "accent.default",
                     "accent.hover", "accent.pressed"):
            for theme, tree in self.sets.items():
                self.assertIn(("role",) + tuple(role.split(".")), tree, f"{theme}.role.{role}")


if __name__ == "__main__":
    unittest.main()
