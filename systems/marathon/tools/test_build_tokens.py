"""tokens.json is what the builder writes, and the builder refuses malformed shadows and mistyped aliases."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_shadow_layer_needs_px_lengths(self):
        with self.assertRaises(ValueError):
            build_tokens.check("x", "shadow", [{"offsetX": "0", "offsetY": "0px", "blur": "0px", "spread": "1px", "color": "#000000"}])

    def test_shadow_layer_needs_a_colour(self):
        with self.assertRaises(ValueError):
            build_tokens.check("x", "shadow", [{"offsetX": "0px", "offsetY": "0px", "blur": "0px", "spread": "1px", "color": "nope"}])

    def test_gradient_needs_stops(self):
        with self.assertRaises(ValueError):
            build_tokens.check("x", "gradient", "linear-gradient(red, blue)")

    def test_committed_shadow_passes(self):
        ring = build_tokens.core["elevation"]["ring"]
        build_tokens.check("core.elevation.ring", "shadow", ring["$value"])


if __name__ == "__main__":
    unittest.main()
