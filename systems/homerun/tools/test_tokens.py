"""Tests for the homerun.co token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set is the
painted surface (www.homerun.co, jobs.homerun.co and both sign-in boundaries all paint
a single light theme; the dark browns are content bands inside it, not a second theme),
and the headline declared/measured values survived the build."""
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

    def test_a_single_light_theme(self):
        """Homerun's signed-out surface paints one light theme: the marketing pages,
        the careers app and both login cards are all light; the dark browns are
        CTA/testimonial bands inside it, so there is a light set and no dark set."""
        self.assertEqual(len(T["$themes"]), 1)
        self.assertEqual(T["$themes"][0]["selectedTokenSets"],
                         {"core": "source", "light": "enabled"})
        self.assertNotIn("dark", T)
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        for role in ("surface.page", "surface.card", "surface.dark", "text.primary",
                     "accent", "border.subtle", "focus", "nav.link",
                     "careers.accent", "app.accent", "app.hrAccent"):
            self.assertIn(role, lv)

    def test_measured_values_survived(self):
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(lv["surface.page"], "{color.white}")
        self.assertEqual(lv["text.primary"], "{color.brown.300}")
        self.assertEqual(lv["accent"], "{color.blue.500}")
        self.assertEqual(lv["careers.accent"], "#466af6")
        self.assertEqual(lv["app.hrAccent"], "{color.secondary.green}")

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["color.white"], "#ffffff")
        self.assertEqual(core["color.brown.300"], "#4a3e3e")
        self.assertEqual(core["color.brown.500"], "#2d2323")
        self.assertEqual(core["color.blue.500"], "#4f75fe")
        self.assertEqual(core["color.beige.700"], "#e3e1dd")
        self.assertEqual(core["color.secondary.green"], "#00b16b")
        self.assertEqual(core["radius.button"], "12px")
        self.assertEqual(core["font.family.display"], '"GT Walsheim", sans-serif')
        self.assertEqual(core["font.family.sans"], '"GT America", sans-serif')


if __name__ == "__main__":
    unittest.main()
