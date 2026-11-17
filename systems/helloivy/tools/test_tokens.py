"""Tests for the helloivy.co token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set is the
marketing site's painted default (www.helloivy.co boots html[toggle-theme=light];
the dark set is the same roles after the footer "Change theme" control's verified
repaint), the app's own semantic layer sits in core.app.* (light-only — the product
paints no dark pass on its public routes), and the headline measured values survived
the build."""
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
        """www.helloivy.co paints light by default: the light set holds the five
        Framer --token-* roles as resolved on the painted page; dark holds the same
        names after the footer's real 'Change theme' repaint. The app layer lives
        in core.app.* and has no dark pass — none was inferred."""
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        for role in ("color.ground", "color.ink", "color.muted",
                     "color.inverseSurface", "color.inverseInk",
                     "color.link", "color.linkHover"):
            self.assertIn(role, light)
            self.assertIn(role, dark)
        # The verified painted values — light default and the repainted dark.
        self.assertEqual(light["color.ground"], "#faf6f0")
        self.assertEqual(light["color.ink"], "#000000")
        self.assertEqual(light["color.link"], "#0099ff")
        self.assertEqual(dark["color.ground"], "#16161a")
        self.assertEqual(dark["color.ink"], "#edecda")
        self.assertEqual(dark["color.muted"], "#666662")
        self.assertEqual(dark["color.inverseInk"], "#faf6f0")
        # The marketing pill re-points: ink in light, inverse ink in dark.
        self.assertEqual(light["component.button.cta.bg"], "{color.ink}")
        self.assertEqual(dark["component.button.cta.bg"], "{color.inverseInk}")

    def test_the_app_layer_is_light_only(self):
        """The product's semantic layer is the share page's inline theme — it
        lives in core.app.* and paints light only. No app colour may sit in the
        dark set (nothing was ever painted dark on the app's public routes)."""
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        self.assertEqual(core["app.color.brand"], "#3f40f2")
        self.assertEqual(core["app.color.mainColor"], "#3f40f2")
        self.assertEqual(core["app.color.ink"], "#37352f")
        self.assertEqual(core["app.color.sidebar"], "#f5f6f4")
        self.assertEqual(core["app.color.comment"], "#fdffe4")
        self.assertEqual(core["app.color.textSelection"], "#e4f2ff")
        self.assertEqual(core["app.layout.sidebarWidth"], "242px")
        self.assertEqual(core["app.layout.headerHeight"], "66px")
        self.assertEqual(core["app.font.family"], "Inter")
        for n in dark:
            self.assertFalse(n.startswith("app."), f"dark.{n} — the app paints no dark pass")

    def test_measured_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("Unbounded", core["font.family.display"])
        self.assertIn("Inter", core["font.family.body"])
        self.assertIn("General Sans", core["font.family.docs"])
        self.assertEqual(core["radius.pill"], "9999px")
        self.assertEqual(core["radius.field"], "10px")
        self.assertEqual(core["font.size.displayXl"], "82px")
        self.assertEqual(core["font.size.base"], "16px")
        # The measured typography composites read off the live DOM.
        self.assertIn("typography.display", core)
        self.assertIn("typography.navLink", core)
        self.assertIn("typography.appButton", core)

    def test_component_geometry(self):
        comp = T["core"].get("component")
        self.assertIsNotNone(comp, "no component tokens")
        names = {n for n, _ in token_checks.tokens_of(comp)}
        # The measured chrome that defines the surfaces.
        for n in ("navBar.height", "button.cta.height", "loginCard.width",
                  "input.height", "shareHeader.height"):
            self.assertIn(n, names, f"component.{n} missing")
        comp_light = {n for n, _ in token_checks.tokens_of(T["light"].get("component", {}))}
        self.assertIn("button.cta.bg", comp_light)


if __name__ == "__main__":
    unittest.main()
