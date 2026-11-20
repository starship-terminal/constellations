"""Tests for the gumroad.com token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the light set is the
painted default surface (gumroad.com boots light; the dark set is the same roles
under @media (prefers-color-scheme: dark) — there is no in-page toggle), and the
headline declared values survived the build."""
import json
import pathlib
import re
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
        """gumroad.com paints light by default: the light set holds the semantic roles
        as :root resolves them; dark holds the same roles under the
        prefers-color-scheme:dark media block."""
        dark = {n for n, _ in token_checks.tokens_of(T["dark"])}
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        for role in ("role.body", "role.primary", "role.accent", "role.border", "ground.bodyBg"):
            self.assertIn(role, dark)
            self.assertIn(role, light)
        dv = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(lv["ground.bodyBg"], "#f4f4f0")
        self.assertEqual(lv["role.primary"], "#000000")
        self.assertEqual(dv["ground.bodyBg"], "#242423")
        self.assertEqual(dv["role.primary"], "#dddddd")
        # the accent and status colours hold across themes; the border alpha drops
        self.assertEqual(lv["role.accent"], dv["role.accent"])
        self.assertEqual(lv["border.alpha"], 1)
        self.assertEqual(dv["border.alpha"], 0.35)

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        light = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(core["color.brand.pink"], "#ff90e8")
        self.assertEqual(core["color.brand.green"], "#23a094")
        self.assertEqual(core["color.brand.red"], "#dc341e")
        self.assertEqual(core["space.spacer.4"], "16px")
        self.assertEqual(core["radius.1"], "4px")
        self.assertEqual(core["duration.default"], "150ms")
        self.assertEqual(core["breakpoint.lg"], "1024px")
        self.assertEqual(core["component.formElementHeight"], "48px")
        self.assertEqual(core["component.borderWidth"], "1px")
        self.assertIn("ABC Favorit", core["font.family.product"])
        # roles resolve the RGB channel triplets the site declares
        self.assertEqual(light["role.accent"], "#ff90e8")
        self.assertEqual(light["role.success"], "#23a094")
        self.assertEqual(light["role.danger"], "#dc341e")
        self.assertEqual(light["channels.accent"], "#ff90e8")

    def test_component_geometry_matches_the_readings(self):
        # Each measured height/width leaf names the component and state it came from; it must equal that
        # reading in raw/components-computed.json, not just be present.
        C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
        checked = 0
        for n, t in token_checks.tokens_of(T["core"]["component"]):
            m = re.match(r"measured (\S+) (\S+) on ", t["$extensions"]["source"])
            if not m or not n.endswith(("height", "width")):
                continue
            rect = C[m.group(1)]["states"][m.group(2)]["rect"]
            want = rect["h" if n.endswith("height") else "w"]
            self.assertEqual(t["$value"], f"{float(want):g}px", n)
            checked += 1
        self.assertGreaterEqual(checked, 20)


class BuilderTest(unittest.TestCase):
    """build_tokens.py, built in memory (it writes tokens.json only when run as a script)."""

    @classmethod
    def setUpClass(cls):
        import build_tokens
        cls.b = build_tokens

    def test_committed_file_matches_a_fresh_build(self):
        self.assertEqual(T, self.b.tokens)

    def test_shadow_layers_are_read_whole(self):
        p = self.b.parse_shadow
        self.assertEqual(p("rgb(0, 0, 0) 4px 4px 0px 0px"),
                         [{"color": "#000000", "offsetX": "4px", "offsetY": "4px", "blur": "0px", "spread": "0px"}])
        two = p("inset 0 0 0 1px rgba(0, 0, 0, 0.5), rgb(221, 221, 221) .5rem .5rem 0rem")
        self.assertEqual(len(two), 2)
        self.assertTrue(two[0]["inset"])
        self.assertEqual(two[0]["spread"], "1px")
        self.assertEqual(two[1]["blur"], "0rem")
        self.assertEqual(two[1]["spread"], "0px")
        self.assertEqual(p("0px 2px 4px -1px rgb(0, 0, 0)")[0]["spread"], "-1px")

    def test_an_unreadable_layer_refuses_the_build(self):
        for bad in ("rgb(0, 0, 0) 4px 4px, 1px 1px var(--x)", "4px 4px 0px", "none",
                    "rgb(0, 0, 0) 1px2px", "#12345 4px 4px", "inset inset 0 0 0 1px #000"):
            with self.assertRaises(ValueError, msg=bad):
                self.b.parse_shadow(bad)

if __name__ == "__main__":
    unittest.main()
