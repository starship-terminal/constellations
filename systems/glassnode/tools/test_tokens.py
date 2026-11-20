"""Tests for the Glassnode token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the dark.studio set
is labelled declared-not-painted (the studio's html[data-theme="dark-theme"] layer
has no public control), and the headline declared values survived the build."""
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

    def test_studio_dark_is_declared_not_painted(self):
        """The studio dark-theme roles exist but were never painted publicly —
        every dark.studio token's source must say so."""
        stu = {n: t for n, t in token_checks.tokens_of(T["dark"]) if n.startswith("studio.")}
        self.assertTrue(stu, "dark.studio is empty")
        for n, tok in stu.items():
            src = tok.get("$extensions", {}).get("source", "")
            self.assertIn("DECLARED-NOT-PAINTED", src, f"dark.{n} is missing the declared-not-painted label")
        # The painted dark surfaces, by contrast, are resolved css-vars.
        for n, tok in token_checks.tokens_of(T["dark"]):
            if n.startswith(("research.", "tokenization.")):
                self.assertIn("css-var", tok["$extensions"]["source"])

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["palette.ultramarine.50"], "#4559dc")
        self.assertEqual(core["palette.grey.90"], "#1a1a1a")
        self.assertEqual(core["palette.accent"], "#16cc8c")
        self.assertEqual(core["spacing.200"], "16px")
        self.assertEqual(core["font.size.200"], "16px")
        self.assertEqual(core["radius.02"], "4px")
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["theme.bg.default"], "#ffffff")
        self.assertEqual(light["theme.section.bgDark"], "#1a1a1a")
        self.assertEqual(light["studio.background.accent.default"], "#4559dc")
        self.assertEqual(light["research.bg.default"], "#ffffff")
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertEqual(dark["studio.background.default"], "#1a1a1a")
        self.assertEqual(dark["research.bg.default"], "#08090a")
        self.assertEqual(dark["tokenization.color.panel"], "#1c1c1c")

    def test_component_geometry(self):
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["component"])}
        self.assertIn("topbar-height", comp)
        self.assertIn("auth-card-width", comp)
        self.assertIn("docs", T["core"]["component"])


if __name__ == "__main__":
    unittest.main()
