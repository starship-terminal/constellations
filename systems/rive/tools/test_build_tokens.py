"""The Rive token builder reproduces tokens.json in memory and keeps the measured values."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_rebuild_matches(self):
        # Builds on import and writes only when run as a script, so a mismatch leaves tokens.json alone.
        import build_tokens
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), json.loads(json.dumps(build_tokens.tokens)))

    def test_measured_colours(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["amber"]["$value"], "#ffa41c")
        self.assertEqual(tokens["core"]["color"]["authBlue"]["$value"], "#1f6fe5")
        self.assertEqual(tokens["core"]["color"]["docsPage"]["$value"], "#0e0c0b")
        self.assertEqual(tokens["dark"]["page"]["$value"], "{color.black}")
        self.assertEqual(tokens["light"]["accent"]["$value"], "{color.authBlue}")
        self.assertIn("source", tokens["core"]["color"]["amber"]["$extensions"])
        self.assertEqual(tokens["$themes"][0]["id"], "dark")


class StyleGuide(unittest.TestCase):
    def test_roles_resolve_through_core(self):
        import build_style_guide
        self.assertEqual(build_style_guide.resolve("dark.page"), "#000000")
        for theme in (build_style_guide.dark, build_style_guide.light):
            self.assertNotIn(None, theme.values())
        self.assertNotIn(": None;", (PKG / "style-guide.html").read_text())


if __name__ == "__main__":
    unittest.main()
