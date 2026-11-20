"""Tests for the grow.google token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves inside each theme's sets, every token carries
evidence, there is exactly one theme (light — grow.google paints nothing else), the
declared glue palette survived the build, and the measured roles land where the
capture read them."""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import token_checks  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def source_of(tok):
    src = tok.get("$extensions", {}).get("source")
    return src if isinstance(src, str) else (src or {}).get("capture", "") + (src or {}).get("evidence", "")


class TokensTest(unittest.TestCase):
    def test_no_dead_aliases(self):
        # Each surface set resolves against core and itself ($themes pairs them).
        errors = token_checks.alias_errors(T["core"], light=T["light"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for setname in ("core", "light"):
            for name, tok in token_checks.tokens_of(T[setname]):
                self.assertTrue(source_of(tok), f"{setname}.{name} has no $extensions.source")

    def test_light_is_the_only_theme(self):
        """grow.google paints light only: no toggle, no applied dark media query; the
        certificate pages' dark hero is a section paint inside the light set."""
        self.assertNotIn("dark", T)
        self.assertEqual([t["id"] for t in T["$themes"]], ["light"])
        hero = T["light"]["surface"]["hero"]
        self.assertEqual(hero["bg"]["$value"], "{color.surface.dark}")
        self.assertEqual(T["light"]["color"]["surface"]["dark"]["$value"], "#18191d")

    def test_declared_glue_palette_survived(self):
        """The --glue-* ramps are the stylesheet's only declared variables; the
        resolved values in raw/css-vars.json must land verbatim in core."""
        palette = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["color"]["palette"])}
        self.assertEqual(palette["blue.600"], "#1a73e8")
        self.assertEqual(palette["grey.0"], "#ffffff")
        self.assertEqual(palette["grey.900"], "#202124")
        self.assertIn("red.600", palette)
        self.assertIn("yellow.600", palette)
        self.assertIn("green.600", palette)
        self.assertTrue(any(n.startswith("purple.") for n in palette))

    def test_painted_roles_not_palette_guesses(self):
        """The painted accent is the measured #3186ff, brighter than the declared
        glue-blue-600; the difference is the capture's own finding."""
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(light["button.primary.bg"], "#3186ff")
        self.assertEqual(light["button.primary.bgHover"], "#185abc")
        self.assertEqual(light["color.link.default"], "#3186ff")
        self.assertEqual(light["color.accent"], "{color.palette.blue.600}")
        self.assertEqual(light["color.focus"], "{focusRing.color}")
        self.assertEqual(T["core"]["focusRing"]["color"]["$value"], "#1a73e8")

    def test_typography_roles_measured(self):
        typo = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["typography"])}
        self.assertEqual(typo["display-1"]["fontSize"], "60px")
        self.assertEqual(typo["display-1"]["lineHeight"], "72px")
        self.assertEqual(typo["display-2"]["fontSize"], "48px")
        self.assertEqual(typo["body"]["fontSize"], "16px")
        self.assertIn("Google Sans Flex", typo["body"]["fontFamily"])
        self.assertEqual(typo["stat"]["fontWeight"], 700)

    def test_geometry_and_motion_from_probes(self):
        geo = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["geometry"])}
        self.assertEqual(geo["header.height"], "64px")
        self.assertEqual(geo["button.height"], "50px")
        self.assertEqual(geo["megaMenu.width"], "1440px")
        motion = T["core"]["motion"]
        self.assertIn("duration", motion)
        self.assertIn("transition", motion)
        self.assertIn("easing", motion)
        durations = {t["$value"] for t in motion["duration"].values()}
        self.assertIn("200ms", durations)  # the glue control timing

    def test_light_component_aliases_resolve(self):
        """The light.component group exists for DESIGN.md: each colour role is an
        alias to a measured role, each dimension to measured geometry."""
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"]["component"])}
        self.assertEqual(comp["button.bg"], "{button.primary.bg}")
        self.assertEqual(comp["hero.bg"], "{surface.hero.bg}")
        self.assertEqual(comp["tab.bar.radius"], "{radius.bar}")
        self.assertEqual(comp["header.height"], "{geometry.header.height}")

    def test_no_apac_values(self):
        """The APAC regional variant is screenshot evidence only: no token source
        may cite it."""
        for setname in ("core", "light"):
            for name, tok in token_checks.tokens_of(T[setname]):
                self.assertNotIn("ALL_sg", source_of(tok), f"{setname}.{name} cites the APAC variant")
                self.assertNotIn("intl", source_of(tok), f"{setname}.{name} cites the APAC variant")


if __name__ == "__main__":
    unittest.main()
