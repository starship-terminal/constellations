"""Tests for the Fingerprint token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the dark set holds only
the declared-not-painted .dark-scoped syntax colours (the marketing site paints no dark
theme; the Mintlify docs' dark preference is captured as screenshots, not tokens), and
the headline declared values survived the build."""
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
        errors = token_checks.alias_errors(T["core"], T["light"], T["dark"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "light", "dark"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_dark_is_syntax_only(self):
        """Marketing paints no dark theme; the dark set holds only .dark code colours."""
        only_dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        self.assertTrue(only_dark, "dark set is empty")
        for n in only_dark:
            self.assertTrue(n.startswith("syntax."), f"dark.{n} is not a syntax role")
        for role in ("theme.ink.default", "theme.action.primary", "theme.border.default",
                     "theme.surface.raised", "background.page"):
            self.assertIn(role, {n for n, _ in token_checks.tokens_of(T["light"])})

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["color.orange.700"], "#f35820")
        self.assertEqual(core["color.gray.900"], "#484946")
        self.assertEqual(core["fpds.blue.7"], "204 68% 51%")
        self.assertEqual(core["font.size.6xl"], "48px")
        self.assertEqual(core["radius.md"], "6px")
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["theme.action.primary"], "#f35820")
        self.assertEqual(light["theme.action.primaryHover"], "#bd400f")
        self.assertEqual(light["action.ctaFill"], "{theme.action.primary}")
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertEqual(dark["syntax.keyword"], "#bfb6fc")

    def test_component_geometry(self):
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["component"])}
        self.assertEqual(comp["topbar-height"], "56px")
        self.assertEqual(comp["cta-height"], "32px")
        self.assertEqual(comp["dropdown-width"], "1288px")
        self.assertIn("productShell", T["core"]["component"])


if __name__ == "__main__":
    unittest.main()
