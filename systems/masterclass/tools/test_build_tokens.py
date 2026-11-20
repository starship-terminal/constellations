"""tokens.json and style-guide.html match an in-memory build, and the values are DTCG shapes."""
import json
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class Build(unittest.TestCase):
    def test_tokens_match_build(self):
        import build_tokens  # builds and checks on import; writes only when run as a script
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), json.loads(json.dumps(build_tokens.tokens)))

    def test_check_refuses_a_bad_shape(self):
        import build_tokens
        bad = {"x": {"$value": "0", "$type": "dimension", "$extensions": {"source": "test"}}}
        with self.assertRaises(SystemExit):
            build_tokens.check(bad)

    def test_line_heights_are_numbers(self):
        for name, token in json.loads((PKG / "tokens.json").read_text())["core"]["lineHeight"].items():
            self.assertIsInstance(token["$value"], (int, float), name)

    def test_guide_matches_render_and_escapes(self):
        import build_style_guide
        self.assertEqual((PKG / "style-guide.html").read_text(), build_style_guide.html)
        self.assertEqual(build_style_guide.esc('"Sohne", x'), "&quot;Sohne&quot;, x")


if __name__ == "__main__":
    unittest.main()
