"""Tests for the httpie.io token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the dark set is the
painted default surface (the site boots html.dark; the light set is the same roles
under html.light, painted by the footer's own LIGHT MODE radio), and the headline
declared values survived the build."""
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

    def test_dark_is_the_painted_surface(self):
        """httpie.io boots html.dark: the dark set holds the semantic roles as
        .dark:root resolves them; light holds the same roles under html.light
        (the footer ThemeToggle's own LIGHT MODE press)."""
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("bg.z0", "bg.z3", "text.primary", "text.secondary",
                     "accent.default", "accent.hover", "altAccent.default",
                     "warning.default", "focus.ring", "border.default",
                     "code.green", "code.pink", "code.blue"):
            self.assertIn(role, dark, role)
            self.assertIn(role, light, role)
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        # the painted dark surface: warm near-black ground, warm-white ink
        self.assertEqual(dv["bg.z0"], "#191515")
        self.assertEqual(dv["text.primary"], "#f5f5f0")
        self.assertEqual(dv["accent.default"], "#73dc8c")
        self.assertEqual(dv["altAccent.default"], "#3b5eba")
        # the switched light surface: warm paper ground, near-black ink
        self.assertEqual(lv["bg.z0"], "#edede8")
        self.assertEqual(lv["text.primary"], "#1c1818")
        self.assertEqual(lv["accent.default"], "#52ab66")
        # the selection wash is one declaration, same in both themes
        self.assertEqual(dv["selection.default"], lv["selection.default"])

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("Pie Headline", core["font.family.headline"])
        self.assertIn("Pie Body", core["font.family.body"])
        self.assertIn("Pie Monospace", core["font.family.mono"])
        # the literal palette harvest made it into core.palette
        pal = {n: v for n, v in core.items() if n.startswith("palette.")}
        self.assertTrue(pal, "no palette literals emitted")
        self.assertIn("rgba(250, 155, 250, 0.25)", pal.values())  # the pink border literal (border-pink/25)

    def test_component_geometry(self):
        comp = T["core"].get("component")
        self.assertIsNotNone(comp, "no component tokens")
        names = {n for n, _ in token_checks.tokens_of(comp)}
        # geometry emitted only when measure.mjs has run; check the shape it takes
        for n in names:
            self.assertRegex(n, r"^[a-zA-Z]+\.")


if __name__ == "__main__":
    unittest.main()
