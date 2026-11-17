"""Tests for the hashnode.com token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set is the
painted default surface (both surfaces boot html.light; the dark set is the same roles
under html.dark, including the dark-only names), and the headline declared values
survived the build."""
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

    def test_light_is_the_painted_surface(self):
        """hashnode.com and townhall.hashnode.com paint light by default: the light
        set holds the semantic roles as :root resolves them; dark holds the same
        roles under html.dark, plus the names the stylesheets declare under .dark
        only."""
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("root.background", "root.foreground", "primary.default",
                     "primary.foreground", "border.default", "border.input",
                     "border.ring", "muted.foreground", "sidebar.background",
                     "brand.default", "link.default"):
            self.assertIn(role, dark)
            self.assertIn(role, light)
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(lv["root.background"], "#ffffff")
        self.assertEqual(lv["root.foreground"], "#13161c")
        self.assertEqual(lv["brand.default"], "#2962ff")
        self.assertEqual(dv["root.background"], "#0d0f14")
        self.assertEqual(dv["root.foreground"], "#e6e8eb")
        self.assertEqual(dv["brand.default"], "#6293ff")
        # .dark-only declarations exist in the dark set alone, never inferred
        self.assertIn("command.default", dv)
        self.assertNotIn("command.default", light)

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["font.size.2xl"], "1.5rem")
        self.assertEqual(core["radius.base"], "0.5rem")
        self.assertEqual(core["radius.xs"], "0.125rem")
        self.assertEqual(core["space.unit"], "0.25rem")
        self.assertEqual(core["font.role.reading.size"], "1.125rem")
        self.assertIn("-apple-system", core["font.family.app"])
        self.assertIn("Inter", core["font.family.inter"])
        self.assertIn("ui-monospace", core["font.family.code"])

    def test_component_geometry(self):
        comp = T["core"].get("component")
        self.assertIsNotNone(comp, "no component tokens")
        names = {n for n, _ in token_checks.tokens_of(comp)}
        # geometry emitted only when measure.mjs has run; check the shape it takes
        for n in names:
            self.assertRegex(n, r"^[a-zA-Z]+\.")


if __name__ == "__main__":
    unittest.main()
