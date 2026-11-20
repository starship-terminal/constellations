"""Tests for the joinhandshake token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the `light` set is
the painted marketing surface and the `access` set is the consumer app's Rosetta
layer (both surfaces paint light only — there is no dark set), and the headline
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
        errors = token_checks.alias_errors(T["core"], T["light"], T["access"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "light", "access"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_two_surfaces_no_dark(self):
        """The marketing surface and the consumer app both paint light only:
        there is a light set and an access set, and no dark set was invented."""
        self.assertIn("light", T)
        self.assertIn("access", T)
        self.assertNotIn("dark", T)
        light = {n for n, _ in token_checks.tokens_of(T["light"])}
        access = {n for n, _ in token_checks.tokens_of(T["access"])}
        # The measured painted roles of the marketing surface:
        for role in ("button.primary.bg", "button.primary.fg", "cta.bg"):
            self.assertIn(role, light)
        # The Rosetta semantic roles of the app surface:
        for role in ("rosettaBg.primary", "rosettaFg.primary",
                     "rosettaInteractive.primary", "rosettaBg.surface"):
            self.assertIn(role, access)

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        # The declared utility colours:
        self.assertEqual(core["color.site.cta"], "#2e6aff")
        self.assertEqual(core["color.site.ctaHover"], "#1552d6")
        self.assertEqual(core["color.site.text"], "#14151c")
        # The Framer page's declared lime:
        fr = [v for n, v in core.items() if n.startswith("color.framer.") and v == "#d3fb52"]
        self.assertTrue(fr, "the Framer palette lost its lime #d3fb52")
        self.assertEqual(core["space.unit"], "0.25rem")
        self.assertEqual(core["duration.default"], "150ms")
        self.assertEqual(core["layout.desktopNavHeight"], "3.5rem")
        self.assertEqual(core["font.weight.semibold"], 600)
        self.assertIn("NoiGrotesk", core["font.family.noiGrotesk"])
        self.assertIn("SansPlomb", core["font.family.sansPlomb"])

    def test_access_values_survived(self):
        access = {n: t["$value"] for n, t in token_checks.tokens_of(T["access"])}
        self.assertEqual(access["rosettaBg.primary"], "#ffffff")
        self.assertEqual(access["rosettaFg.primary"], "#121212")
        self.assertEqual(access["rosettaInteractive.primary"], "#04191b")

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
        self.assertGreaterEqual(checked, 20)


if __name__ == "__main__":
    unittest.main()
