"""Tests for the huddlekit.com token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set is the
painted default surface (huddlekit.com is light-only and the app login boots light;
the dark set is the same roles re-pointed under html.dark / the nested .dark panels),
and the headline declared values survived the build."""
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
        """huddlekit.com paints light only (its .dark rules re-point the same
        names inside nested dark panels, never on <html>) and app.huddlekit.com
        paints html.dark under prefers-color-scheme: the light set holds the
        semantic roles as :root resolves them, dark the same roles re-pointed."""
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("root.background", "root.foreground", "primary.default",
                     "primary.foreground", "border.default", "border.input",
                     "border.ring", "muted.foreground", "card.default",
                     "popover.default", "sidebar.background", "canvas.default",
                     "upgrade.default", "color.page"):
            self.assertIn(role, dark)
            self.assertIn(role, light)
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(lv["root.background"], "#ffffff")
        # 2026-11-21 reading of oklch(20.5% .004 70). The Nov 17 harvest
        # resolved the same declaration to #111827.
        self.assertEqual(lv["root.foreground"], "#181715")
        self.assertEqual(lv["primary.default"], "#ea580d")
        self.assertEqual(lv["color.page"], "#f5f3f2")
        # 2026-11-21 reading of oklch(15.43% .004 70). The footer computed
        # fill is still #0e0b0d (core.component.footer.bg).
        self.assertEqual(dv["root.background"], "#0d0c0a")
        self.assertEqual(dv["root.foreground"], "#eeeceb")
        # the orange primary is kept in the dark set; borders go white-alpha
        self.assertEqual(dv["primary.default"], "#ea580d")
        self.assertEqual(dv["border.default"], "rgba(255, 255, 255, 0.08)")

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["font.size.2xl"], "1.5rem")
        self.assertEqual(core["radius.base"], "0.75rem")
        self.assertEqual(core["radius.xs"], "0.125rem")
        self.assertEqual(core["space.unit"], "0.25rem")
        self.assertIn("Inter", core["font.family.sans"])
        self.assertIn("inter", core["font.family.inter"])
        self.assertIn("Geist Mono", core["font.family.geistMono"])
        self.assertIn("ui-monospace", core["font.family.mono"])

    def test_component_geometry(self):
        """Every measured component leaf equals the raw reading it cites."""
        import re
        C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
        comp = T["core"]["component"]
        checked = 0
        src = (HERE / "tools" / "build_component_tokens.py").read_text()
        GEOM = {path: field for _c, _s, field, path in re.findall(r'geom\("([^"]+)", "([^"]+)", "(\w+)", "([^"]+)"', src)}
        self.assertGreater(len(GEOM), 5)
        for n, t in token_checks.tokens_of(comp):
            m = re.match(r"measured (\S+) (\S+) on ", t["$extensions"]["source"])
            self.assertIsNotNone(m, n)
            st = C[m.group(1)]["states"][m.group(2)]
            v = t["$value"]
            if n in GEOM:
                # the builder's own geom() call names the field it read
                field = GEOM[n]
                raw = st["rect"][field] if field in st.get("rect", {}) else st["style"][field]
                self.assertEqual(v, f"{float(str(raw).replace('px', '')):g}px", n)
            elif n.endswith(".height") or n.endswith(".width"):
                raw = st["rect"]["h" if n.endswith(".height") else "w"]
                self.assertEqual(v, f"{raw:g}px", n)
            elif n.endswith(".radius"):
                raw = st["style"]["borderTopLeftRadius"]
                self.assertEqual(v, "9999px" if float(raw[:-2]) >= 9999 else raw, n)
            elif n.endswith(".size"):
                self.assertEqual(v, st["style"]["fontSize"], n)
            elif n.endswith(".tracking"):
                self.assertEqual(v, st["style"]["letterSpacing"], n)
            else:
                continue
            checked += 1
        self.assertGreaterEqual(checked, 15)


if __name__ == "__main__":
    unittest.main()
