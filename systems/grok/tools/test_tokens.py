"""Tests for the docs.x.ai token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set is the
painted default surface (docs.x.ai boots html.light; the dark set is the same roles
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
        """docs.x.ai paints light by default: the light set holds the semantic roles
        as :root resolves them; dark holds the same roles under html.dark, plus the
        names the stylesheets declare under .dark only."""
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("bg.base", "fg.default", "primary.default", "border.muted"):
            self.assertIn(role, dark)
            self.assertIn(role, light)
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(lv["bg.base"], "#ffffff")
        self.assertEqual(lv["fg.default"], "#0a0a0a")
        self.assertEqual(dv["bg.base"], "#0a0a0a")
        self.assertEqual(dv["fg.default"], "#d5d9e2")
        # .dark-only declarations exist in the dark set alone, never inferred
        for name in ("border.default", "border.input", "border.ring",
                     "alert.default", "content.muted", "sb.thumbColor"):
            self.assertIn(name, dv)
            self.assertNotIn(name, {n for n, _ in token_checks.tokens_of(T["light"])})

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["color.brand.solar"], "#ff640a")
        self.assertEqual(core["color.brand.darksolar"], "#cd7532")
        self.assertEqual(core["color.neutral.2"], "#080808")
        self.assertEqual(core["color.neutral.98"], "#fafafa")
        self.assertEqual(core["font.size.2xl"], "1.5rem")
        self.assertEqual(core["radius.lg"], "0.5rem")
        self.assertEqual(core["space.unit"], "0.25rem")
        self.assertEqual(core["duration.default"], "150ms")
        self.assertEqual(core["layout.topbarHeight"], "4rem")
        self.assertIn("xVf", core["font.family.xVf"])
        self.assertIn("xMono", core["font.family.xMono"])

    def test_component_geometry(self):
        """Pin component tokens to the readings they came from (a name-shape check passed for {})."""
        comp = T["core"].get("component")
        self.assertIsNotNone(comp, "no component tokens")
        raw = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]

        def tok(path):
            node = comp
            for k in path.split("."):
                node = node[k]
            return node["$value"]

        for path, c, state, field in [("header.height", "docs-header", "default", "h"),
                                      ("sidebar.width", "docs-sidebar", "default", "w"),
                                      ("button.cta.height", "docs-cta", "default", "h"),
                                      ("mobileDrawer.width", "m-docs-drawer", "opened", "w")]:
            self.assertEqual(tok(path), "%gpx" % float(raw[c]["states"][state]["rect"][field]), path)


if __name__ == "__main__":
    unittest.main()
