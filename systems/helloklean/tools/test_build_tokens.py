"""The committed tokens.json must rebuild from the raw readings, with set-free aliases and
the measured button and heading-1 line heights.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import re
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.tokens)

    def test_aliases_name_no_set(self):
        # {core.color.ink} only resolves through a set-prefix fallback; DTCG tools call it dangling.
        text = json.dumps(build_tokens.tokens)
        self.assertEqual(re.findall(r"\{(?:core|light)\.[^}]*\}", text), [])

    def test_measured_line_heights(self):
        typ = build_tokens.tokens["core"]["typography"]
        self.assertEqual(typ["heading-1"]["$value"]["lineHeight"], round(41.8 / 38, 3))
        self.assertEqual(typ["button"]["$value"]["lineHeight"], 1.0)
        self.assertEqual(typ["button"]["$value"]["fontWeight"], "{fontWeight.regular}")

    def test_hand_values_say_so(self):
        muted = build_tokens.tokens["light"]["text"]["muted"]
        self.assertTrue(muted["$extensions"]["source"].startswith("Reconstruction"))


if __name__ == "__main__":
    unittest.main()
