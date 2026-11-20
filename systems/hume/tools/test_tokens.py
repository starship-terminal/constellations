"""Tests for the hume.ai token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the dark set holds
only the dev.hume.ai docs' painted dark (www.hume.ai has no theme control and no
dark theme is invented), and the headline declared values survived the build."""
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
        """www.hume.ai paints one light theme: the light set holds the
        product layer's roles — the #fdfdfc ground and #1b1918 ink."""
        lv = {n: t["$value"] for n, t in token_checks.tokens_of(T["light"])}
        self.assertEqual(lv["bg.default"], "#fdfdfc")
        self.assertEqual(lv["ink.default"], "#1b1918")

    def test_dark_is_docs_only(self):
        """The dark set records only the dev.hume.ai docs' painted dark —
        no www semantic role may leak into it."""
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertTrue(dark, "the dark set is empty")
        for name in dark:
            self.assertTrue(name.startswith("docs.") or name.startswith("component."),
                            f"dark.{name} is not a docs or component token")
        self.assertEqual(dark["docs.color.background"], "#1c1917")

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("Inter", core["font.family.sans"])
        self.assertIn("Martina Plantijn", core["font.family.serif"])
        self.assertIn("Fraktion", core["font.family.code"])
        # the brand ramp survived
        self.assertEqual(core["accent.pink"], "#f7bbe6")
        self.assertEqual(core["accent.mint"], "#85e4c5")
        self.assertEqual(core["gradientStop.cream"], "#fff3e5")
        # the literal palette harvest made it into core.palette
        pal = {n: v for n, v in core.items() if n.startswith("palette.")}
        self.assertTrue(pal, "no palette literals emitted")

    def test_component_geometry(self):
        """Every measured component leaf equals the raw reading it cites."""
        import re
        C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
        comp = T["core"]["component"]
        checked = 0
        for n, t in token_checks.tokens_of(comp):
            m = re.match(r"measured (\S+) (\S+) on ", t["$extensions"]["source"])
            self.assertIsNotNone(m, n)
            st = C[m.group(1)]["states"][m.group(2)]
            v = t["$value"]
            if n.endswith(".height") or n.endswith(".width"):
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
        self.assertGreaterEqual(checked, 20)

    def test_font_stacks_are_measured_verbatim(self):
        C = json.loads((HERE / "raw" / "components-computed.json").read_text())["components"]
        core = {n: t for n, t in token_checks.tokens_of(T["core"])}
        for path, comp in (("font.family.body", "site-nav"), ("font.family.display", "hero-headline"),
                           ("font.family.monoWww", "player-card"), ("font.family.docs", "docs-side-link"),
                           ("font.family.code", "docs-code-block")):
            st = C[comp]["states"]["default"]
            raw = (st.get("textStyle") or {}).get("fontFamily") or st["style"]["fontFamily"]
            self.assertEqual(core[path]["$value"], raw, path)
        # the Japanese face is the declared variable, not a hand-written stack
        self.assertIn("--font-japanese", core["font.family.japanese"]["$extensions"]["source"])

    def test_exotic_palette_literals_are_kept(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertIn("#101828", core.values())  # the docs oklch(21% .034 264.665)


if __name__ == "__main__":
    unittest.main()
