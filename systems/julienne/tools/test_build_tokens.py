"""tokens.json must rebuild from the raw readings, with every declared glass-shadow layer.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.tokens)

    def test_glass_rim_keeps_both_inset_rims(self):
        # --glass-rim: inset 1px 1px 0 rgba(255, 255, 255, .95), inset -1px -1px 0 rgba(255, 255, 255, .45)
        rim = build_tokens.tokens["core"]["shadow"]["glassRim"]["$value"]
        self.assertEqual([l["color"] for l in rim], ["rgba(255, 255, 255, 0.95)", "rgba(255, 255, 255, 0.45)"])
        self.assertTrue(all(l.get("inset") for l in rim))
        self.assertEqual((rim[1]["offsetX"], rim[1]["offsetY"], rim[1]["blur"]), ("-1px", "-1px", "0px"))

    def test_unreadable_shadow_raises(self):
        with self.assertRaises(ValueError):
            build_tokens.shadow_layers("0 1px 2px", "test", "no colour")
        with self.assertRaises(ValueError):
            build_tokens.shadow_layers("0 1px 2px var(--x)", "test", "unresolved colour")


if __name__ == "__main__":
    unittest.main()
