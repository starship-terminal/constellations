"""Tests for the Front token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the nine sets hold the
layers they claim (the marketing site's three section themes, the app shell's light and
real dark repaint, the embedded Froyo/Companion layer, the Knowledge Base block), and
the headline declared values survived the build."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import token_checks  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
SETS = ("core", "violet", "light", "gray", "app", "dark", "companion", "companionDark", "help")


class TokensTest(unittest.TestCase):
    def test_no_dead_aliases(self):
        # Each semantic set pairs with core (every front leaf resolves to a
        # literal today; keep the check so a future alias cannot point nowhere).
        errors = []
        for s in SETS:
            errors += token_checks.alias_errors(T["core"], T[s], {})
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in SETS:
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_marketing_sets_are_section_themes(self):
        """violet/light/gray carry the same .surface-*/.text-*/.button-* roles repainted."""
        for theme in ("violet", "light", "gray"):
            names = {n for n, _ in token_checks.tokens_of(T[theme])}
            for role in ("surface.l0", "surface.l1", "text.primary", "text.secondary",
                         "button.surface", "button.textDefault"):
                self.assertIn(role, names, f"{theme}.{role} missing")
        # The same role names, different paints — the plum theme is not a light page.
        v = {n: t["$value"] for n, t in token_checks.tokens_of(T["violet"])}
        l = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(v["surface.l0"], "#300c41")
        self.assertEqual(l["surface.l0"], "#ffffff")
        self.assertNotEqual(v["surface.l0"], l["surface.l0"])

    def test_app_dark_repaints_the_same_names(self):
        """The dark set is the auth shell's data-theme=dark repaint of the app names."""
        app = {n for n, _ in token_checks.tokens_of(T["app"])}
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        self.assertEqual(app, dark, "app and dark should name the same roles")
        av = {n: t["$value"] for n, t in token_checks.tokens_of(T["app"])}
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertNotEqual(av["color.bg.base.default"], dv["color.bg.base.default"])

    def test_companion_parity(self):
        """The embedded Froyo layer repaints the same --colors-* names light/dark."""
        c = {n for n, _ in token_checks.tokens_of(T["companion"])}
        d = {n for n, _ in token_checks.tokens_of(T["companionDark"])}
        self.assertEqual(c, d)

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["palette.violet.900"], "#300c41")
        self.assertEqual(core["palette.citron.500"], "#dee948")
        self.assertEqual(core["font.size.display1"], "62px")
        self.assertEqual(core["radius.20"], "20px")
        self.assertEqual(core["motion.easing.appear"], [0.16, 1.0, 0.3, 1.0])
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["button.surface"], "#8034bf")
        self.assertEqual(light["text.primary"], "#0d1d39")
        violet = {n: t["$value"] for n, t in token_checks.tokens_of(T["violet"])}
        self.assertEqual(violet["surface.highlight"], "#dee948")
        self.assertEqual(violet["text.primary"], "#f8f1fe")
        app = {n: t["$value"] for n, t in token_checks.tokens_of(T["app"])}
        self.assertIn("color.bg.surface.primary.default", app)
        self.assertIn("color.bg.surface.primary.hover", app)
        self.assertIn("color.bg.fill.brand.default", app)
        self.assertIn("color.bg.fill.brand.hover", app)
        help_ = {n: t["$value"] for n, t in token_checks.tokens_of(T["help"])}
        self.assertIn("primary.color", help_)

    def test_component_geometry(self):
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["component"])}
        self.assertEqual(comp["marketing.header.height"], "80px")
        self.assertEqual(comp["marketing.billingSwitch.width"], "66px")
        self.assertIn("app", T["core"]["component"])
        self.assertIn("appDark", T["core"]["component"])


if __name__ == "__main__":
    unittest.main()
