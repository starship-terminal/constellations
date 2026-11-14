"""Tests for the Exa token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set holds
the marketing and sign-in roles the dark set lacks (the docs are the only dark surface),
and the headline declared values survived the build."""
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

    def test_dark_is_docs_only(self):
        """Marketing and sign-in paint no dark theme; the dark set holds docs roles."""
        only_dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        self.assertTrue(only_dark, "dark set is empty")
        for n in only_dark:
            self.assertTrue(n.startswith("docs."), f"dark.{n} is not a docs role")
        light_names = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("marketing.surface", "signin.action", "docs.primary"):
            self.assertIn(role, light_names)

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["color.brand.default"], "#1f40ed")
        self.assertEqual(core["color.neutral.cream"], "#faf9f7")
        self.assertEqual(core["color.gray.500"], "#737373")
        self.assertEqual(core["color.docs.primary"], "#1840ed")
        self.assertEqual(core["color.docs.gray.50"], "#f3f4fa")
        self.assertEqual(core["size.nav"], "55px")
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["docs.primary"], "#1840ed")
        self.assertEqual(light["docs.border"], "#eeeff5")
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertEqual(dark["docs.surface"], "#0b0b10")
        self.assertEqual(dark["docs.border"], "#26272c")

    def test_component_geometry(self):
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["component"])}
        # div.header measures the 55px nav bar; the 48px announcement strip
        # above it is a sibling, not part of the header box.
        self.assertEqual(comp["header-height"], "55px")
        self.assertEqual(comp["menu-width"], "380px")


if __name__ == "__main__":
    unittest.main()
