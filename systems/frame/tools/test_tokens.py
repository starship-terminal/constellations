"""Tests for the Frame.io token sets. Run: python3 -m unittest discover -s tools (from this package).

build_tokens.py refuses bad values at build time; these tests re-check the committed
tokens.json: every alias resolves, every token carries evidence, the single `dark` set
holds the painted roles, the measured component geometry survived the build, and the
probe-read motion group is merged in."""
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
        errors = token_checks.alias_errors(T["core"], T["dark"])
        self.assertEqual(errors, [])

    def test_every_token_has_a_source(self):
        for theme in ("core", "dark"):
            for name, tok in token_checks.tokens_of(T[theme]):
                src = tok.get("$extensions", {}).get("source", "")
                self.assertTrue(src, f"{theme}.{name} has no $extensions.source")

    def test_one_painted_theme(self):
        """frame.io paints one dark surface signed out; core + dark are the only sets."""
        self.assertEqual(sorted(k for k in T if not k.startswith("$")), ["core", "dark"])
        themes = T["$themes"]
        self.assertEqual(len(themes), 1)
        self.assertEqual(themes[0]["id"], "dark")
        self.assertEqual(themes[0]["selectedTokenSets"], {"core": "source", "dark": "enabled"})

    def test_declared_values_survived(self):
        core = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"])}
        self.assertEqual(core["color.grey.00"], "#000000")
        self.assertEqual(core["color.grey.100"], "#fcfcfc")
        self.assertEqual(core["color.brand.cobalt.default"], "#5b53ff")
        self.assertEqual(core["color.brand.cobalt.20"], "rgba(91, 83, 255, 0.2)")
        self.assertEqual(core["font.family.gothic"], '"FrameGothic","FrameGothic Fallback"')
        self.assertEqual(core["layout.grid.columns"], 12)
        dark = {n: t["$value"] for n, t in token_checks.tokens_of(T["dark"])}
        self.assertEqual(dark["theme.bg"], "{color.grey.00}")
        self.assertEqual(dark["theme.fg.default"], "{color.grey.100}")

    def test_component_geometry(self):
        comp = {n: t["$value"] for n, t in token_checks.tokens_of(T["core"]["component"])}
        self.assertEqual(comp["topbar-height"], "80px")
        self.assertEqual(comp["announcement-height"], "36px")
        self.assertEqual(comp["cta-height"], "39.75px")
        self.assertEqual(comp["nav-panel-width"], "1440px")
        self.assertEqual(comp["field-height"], "48px")
        self.assertEqual(comp["plan-card-width"], "252px")
        self.assertEqual(comp["mobile-topbar-height"], "120px")

    def test_product_shell_is_labelled(self):
        """The accounts.frame.io/welcome readings stay literals under productShell."""
        shell = {n: t for n, t in token_checks.tokens_of(T["core"]["component"]["productShell"])}
        self.assertEqual(shell["login-panel-width"]["$value"], "346px")
        self.assertEqual(shell["login-field-height"]["$value"], "40px")
        self.assertEqual(shell["login-submit-fill"]["$value"], "#5b53ff")
        for n, tok in shell.items():
            self.assertIn("accounts sign-in surface", tok["$extensions"]["source"],
                          f"component.productShell.{n} lost its stack label")

    def test_motion_probe_merged(self):
        """raw/motion.json's measured transition group and reduced-motion verdict are in."""
        motion = T["core"]["motion"]
        self.assertIn("transition", motion)
        ext = motion.get("$extensions", {}).get("reducedMotion", {})
        self.assertTrue(ext.get("verified"), "the reduce emulation did not verify")
        self.assertEqual(ext.get("behaviour"), "partial")


if __name__ == "__main__":
    unittest.main()
