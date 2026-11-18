"""Tests for the IFTTT token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, and the light set is
the single painted theme (IFTTT has no theme control — the dark grounds on explore
and the detail heroes are painted sections, recorded under light.component.dark)."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import token_checks  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


class TokensTest(unittest.TestCase):
    def test_no_dead_aliases(self):
        errors = token_checks.alias_errors(T["core"], T["light"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "light"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_one_theme_only(self):
        """IFTTT paints one theme: no theme control exists on any signed-out
        surface, so there is a light set and nothing else. Dark-painted
        sections live under light.component.dark as measured values."""
        self.assertNotIn("dark", T)
        self.assertEqual(T["$metadata"]["tokenSetOrder"], ["core", "light"])
        self.assertEqual([t["id"] for t in T["$themes"]], ["light"])

    def test_roles_present(self):
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("color.bg.page", "color.text.body", "color.action.fill",
                     "color.action.outline"):
            self.assertIn(role, light, role)
        # the dark painted sections were recorded as component tokens
        dark = {n for n, _ in token_checks.tokens_of(T["light"])}
        self.assertTrue(any(n.startswith("component.dark.") for n in dark),
                        "no dark-painted component tokens under light.component.dark")

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("Museo Sans Rounded", core["font.family.brand"])
        # the brand face is evidence only: the licensed file is never the value
        self.assertNotIn("woff2", str(core["font.family.brand"]))


if __name__ == "__main__":
    unittest.main()
