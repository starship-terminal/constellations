"""The token builder reproduces tokens.json in memory and keeps the measured orange."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_orange_is_measured(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["dark"]["color"]["orange"]["$value"], "#ff5301")
        self.assertEqual(tokens["dark"]["color"]["page"]["$value"], "#0c0c0c")
        self.assertEqual(tokens["core"]["font"]["size"]["display"]["$value"], "72px")
        self.assertEqual(tokens["light"], {})

    def test_rebuild_matches(self):
        # Builds on import and writes only when run as a script, so a mismatch leaves tokens.json alone.
        import build_tokens
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), json.loads(json.dumps(build_tokens.doc)))

    def test_unparseable_colour_fails(self):
        import build_tokens
        with self.assertRaises(ValueError):
            build_tokens.take_color({}, "color", "x", "color-mix(in srgb, red, blue)", "test")

    def test_ua_focus_ring_is_not_labelled_measured(self):
        focus = json.loads((PKG / "tokens.json").read_text())["dark"]["color"]["focus"]
        self.assertTrue(focus["$extensions"]["source"].startswith("Observed."))


class StyleGuide(unittest.TestCase):
    def test_guide_matches_render(self):
        import build_style_guide
        self.assertEqual((PKG / "style-guide.html").read_text(), build_style_guide.html)

    def test_swatches_read_the_slim_tree(self):
        # build_style_guide inlines {v, t, s} per token; a script reading DTCG $value finds nothing.
        tpl = (HERE / "style-guide.template.html").read_text()
        self.assertNotIn("token.$value", tpl)
        self.assertIn("token.v", tpl)


if __name__ == "__main__":
    unittest.main()
