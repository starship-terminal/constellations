"""tokens.json must rebuild from the raw readings, hold no token inside a token, and label the
hand-entered spacing scale; the style guide must render Instagram, not the kit's Claude page.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent


def nested_tokens(node, path=""):
    """Paths of tokens that also hold child keys, which DTCG walkers never reach."""
    out = []
    if isinstance(node, dict):
        if "$value" in node and any(not k.startswith("$") for k in node):
            out.append(path)
        for k, v in node.items():
            if not k.startswith("$"):
                out += nested_tokens(v, f"{path}.{k}" if path else k)
    return out


class TokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), build_tokens.build())

    def test_no_token_holds_tokens(self):
        self.assertEqual(nested_tokens(build_tokens.build()), [])

    def test_spacing_is_labelled_reconstruction(self):
        for step, tok in build_tokens.build()["core"]["spacing"].items():
            self.assertTrue(tok["$extensions"]["source"].startswith("Reconstruction"), step)


class StyleGuideTest(unittest.TestCase):
    def test_guide_is_instagram(self):
        html = (PKG / "style-guide.html").read_text()
        self.assertNotIn("Claude", html)
        self.assertNotIn("fonts.googleapis.com", html)
        for section in ("roles-out", "palette-out", "type-out", "radius-out", "motion-out"):
            self.assertIn(f'id="{section}"', html)


if __name__ == "__main__":
    unittest.main()
