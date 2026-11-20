"""tokens.json matches an in-memory build, and the type ramp is in px at the site's 10px root."""
import json
import pathlib
import re
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        import build_tokens  # builds on import; writes only when run as a script
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()),
                         json.loads(json.dumps(build_tokens.tokens, ensure_ascii=False)))

    def test_type_ramp_is_px_at_the_10px_root(self):
        typography = json.loads((PKG / "tokens.json").read_text())["core"]["typography"]
        self.assertEqual(typography["h1"]["$value"]["fontSize"], "72px")  # 7.2rem with html { font-size: 10px }
        self.assertEqual(typography["h1"]["$value"]["letterSpacing"], "-1.44px")  # -.02em of 72px
        for step, token in typography.items():
            self.assertRegex(token["$value"]["fontSize"], r"^\d+(\.\d+)?px$", step)
            self.assertRegex(token["$value"]["letterSpacing"], r"^-?\d+(\.\d+)?px$", step)

    def test_no_empty_theme_set(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["$metadata"]["tokenSetOrder"], [k for k in ("core", "light", "dark") if k in tokens])



class StyleGuide(unittest.TestCase):
    def test_type_samples_read_px(self):
        # The table multiplied every size by 10 (a rem rule), so px sizes all hit the 72px cap.
        tpl = (PKG / "tools" / "style-guide.template.html").read_text()
        self.assertNotIn("Math.min(rem * 10, 72)", tpl)
        self.assertIn("endsWith('rem') ? size * 10 : size", tpl)

if __name__ == "__main__":
    unittest.main()
