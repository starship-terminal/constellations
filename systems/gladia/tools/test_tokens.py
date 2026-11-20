"""Tests for the Gladia token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the dark set is the
painted :root surface (the marketing site paints dark by default; the light set is the
body.light-mode scope /library mounts), and the headline declared values survived the
build."""
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
        """Marketing paints dark by default: the dark set holds the semantic roles
        as :root resolves them; light holds the same roles under body.light-mode."""
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("bg.primary", "text.primary", "border.primary", "bg.glass"):
            self.assertIn(role, dark)
            self.assertIn(role, light)
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(dv["bg.primary"], "#000000")
        self.assertEqual(dv["text.primary"], "#ffffff")
        self.assertEqual(lv["bg.primary"], "#ffffff")
        self.assertEqual(lv["text.primary"], "#000000")

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["color.purple.default"], "#947afc")
        self.assertEqual(core["color.purple.500"], "#925bff")
        self.assertEqual(core["color.neutral.0"], "#ffffff")
        self.assertEqual(core["color.neutral.1000"], "#000000")
        self.assertEqual(core["font.size.80"], "80px")
        self.assertEqual(core["radius.full"], "9999px")
        self.assertEqual(core["space.4"], "16px")
        self.assertEqual(core["duration.240"], "240ms")

    def test_component_geometry(self):
        """Pin component tokens to the readings they came from (a name-shape check passed for {})."""
        comp = T["core"].get("component")
        self.assertIsNotNone(comp, "no component tokens")
        raw = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]

        def reading(c, field):
            s = raw[c]["states"]["default"]
            v = s["rect"][field] if field in s.get("rect", {}) else s["style"][field]
            return v if isinstance(v, str) else "%gpx" % v

        def tok(path):
            node = comp
            for k in path.split("."):
                node = node[k]
            return node["$value"]

        for path, c, field in [("header.height", "mkt-header", "h"), ("button.headerCta.height", "nav-cta", "h"),
                               ("button.headerCta.radius", "nav-cta", "borderTopLeftRadius"),
                               ("planCard.width", "plan-card", "w"), ("planCard.radius", "plan-card", "borderTopLeftRadius")]:
            self.assertEqual(tok(path), reading(c, field), path)
        # a transparent reading is never published as a fill
        self.assertNotIn("auth", comp)


if __name__ == "__main__":
    unittest.main()
