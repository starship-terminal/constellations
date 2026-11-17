"""Tests for the www.hbomax.com token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the single `dark`
set holds the --color_* semantic roles the site's own token sheet declares (the
only theme the bundle ships — html data-theme="max"), and the headline declared
values survived the build."""
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
        errors = token_checks.alias_errors(core=T["core"], dark=T["dark"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "dark"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_single_painted_dark_theme(self):
        """www.hbomax.com ships one theme (html data-theme="max"): the token sets
        are core plus dark alone — no light set is ever inferred."""
        self.assertNotIn("light", T)
        self.assertEqual([t["id"] for t in T["$themes"]], ["dark"])
        self.assertEqual(T["$metadata"]["tokenSetOrder"], ["core", "dark"])

    def test_color_roles_present(self):
        """The site's own --color_* sheet is the semantic layer: the action,
        surface, card and captions families land under dark.color."""
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        for role in ("color.action.link.text.base", "color.action.link.text.hover",
                     "color.action.primary.fill.high", "color.action.primary.text",
                     "color.captions.white.self", "color.card.border.high"):
            self.assertIn(role, dark)
        self.assertEqual(dark["color.action.primary.fill.high"], "#ffffff")
        self.assertEqual(dark["color.action.primary.text"], "#000000")
        self.assertEqual(dark["color.action.link.text.base"], "#71b8f2")
        self.assertEqual(dark["color.captions.white.self"], "#ffffff")

    def test_scales_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["border.corner.action.sm.self"], "2px")
        self.assertEqual(core["border.corner.action.md.self"], "4px")
        self.assertEqual(core["border.corner.action.lg.self"], "8px")
        self.assertEqual(core["spacer.space.horizontal.far.sm.self"], "10px")
        self.assertEqual(core["font.action.md.bp05.fontSize"], "20px")
        self.assertEqual(core["font.action.md.bp05.lineHeight"], 1.35)
        self.assertIn("Max Sans", core["font.family.primary"])

    def test_component_geometry(self):
        comp = T["core"].get("component")
        self.assertIsNotNone(comp, "no component tokens")
        names = {n for n, _ in token_checks.tokens_of(comp)}
        # geometry emitted only when measure.mjs has run; check the shape it takes
        for n in names:
            self.assertRegex(n, r"^[a-zA-Z]+\.")


if __name__ == "__main__":
    unittest.main()
