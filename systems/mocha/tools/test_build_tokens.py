"""tokens.json and style-guide.html match a fresh in-memory build (nothing is written)."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_rebuild_matches(self):
        import build_tokens  # builds on import; writes only when run as a script
        committed = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(committed, json.loads(json.dumps(build_tokens.tokens)))

    def test_motion_is_a_token_group(self):
        # motion.build returns (group, notTokenised); assigning the pair made core.motion a list.
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertIsInstance(tokens["core"]["motion"], dict)
        self.assertIn("duration", tokens["core"]["motion"])
        for item in tokens["core"]["$extensions"]["notTokenised"]:
            self.assertIn("why", item)

    def test_style_guide_matches_render(self):
        import build_style_guide
        self.assertEqual((PKG / "style-guide.html").read_text(), build_style_guide.html)

    def test_token_table_is_not_capped(self):
        # A cap hid the light tokens once the motion group came first.
        self.assertNotIn("slice(0, 80)", (HERE / "style-guide.template.html").read_text())

    def test_primary_is_measured(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["primary"]["$value"], "#513a06")
        self.assertEqual(tokens["core"]["color"]["primaryLight"]["$value"], "#b4ff6a")
        self.assertEqual(tokens["light"]["page"]["$value"], "{color.backgroundLight}")


if __name__ == "__main__":
    unittest.main()
