"""The Mural token builder is deterministic and keeps the measured values."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_rebuild_matches(self):
        # Builds on import; writes only as a script, so a mismatch leaves tokens.json alone.
        import build_tokens
        self.assertEqual((PKG / "tokens.json").read_text(), build_tokens.out)

    def test_display_stack_is_the_declared_one(self):
        family = json.loads((PKG / "tokens.json").read_text())["core"]["font"]["family"]["display"]["$value"]
        self.assertEqual(family, '"STK Bureau", "Times New Roman", sans-serif')

    def test_measured_colours(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["jade"]["$value"], "#00c27a")
        self.assertEqual(tokens["core"]["color"]["authRed"]["$value"], "#e02935")
        self.assertEqual(tokens["core"]["color"]["authFocus"]["$value"], "#306ae3")
        self.assertEqual(tokens["light"]["accent"]["$value"], "{color.jade}")
        self.assertIn("source", tokens["core"]["color"]["jade"]["$extensions"])
        self.assertEqual(tokens["$themes"][0]["id"], "light")


if __name__ == "__main__":
    unittest.main()
