"""Tests for the Equals token sets. Run: python3 -m unittest discover -s tools (from this package).

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
        self.assertEqual(core["color.brand.grey-1"], "#faf9f5")
        self.assertEqual(core["color.brand.orchid"], "#b074ce")
        self.assertEqual(core["color.brand.amber"], "#ff3716")
        self.assertEqual(core["color.docs.gray.900"], "#1a181d")
        self.assertEqual(core["size.header"], "52px")
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["docs.primary"], "#7839e5")
        self.assertEqual(light["signin.action"], "{color.app.purple.600}")
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertEqual(dark["docs.surface"], "#0b0a0f")

    def test_component_geometry(self):
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["component"])}
        self.assertEqual(comp["header-height"], "52px")
        self.assertEqual(comp["signin-card-width"], "300px")
        self.assertEqual(comp["docs-sidebar-width"], "288px")


if __name__ == "__main__":
    unittest.main()
