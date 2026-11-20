"""tokens.json must rebuild from the raw readings: motion as a group (not the (group,
notTokenised) tuple), lab() converted on the D50 white, no token inside a token, and shadows as
DTCG layers.

Run from the package root: python3 -m unittest discover -s tools
"""
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def nested_tokens(node, path=""):
    out = []
    if isinstance(node, dict):
        if "$value" in node and any(not k.startswith("$") for k in node):
            out.append(path)
        for k, v in node.items():
            if not k.startswith("$"):
                out += nested_tokens(v, f"{path}.{k}" if path else k)
    return out


class BuildTokensTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = build_tokens.build()

    def test_committed_tokens_match_builder(self):
        self.assertEqual(json.loads(TOKENS.read_text()), self.doc)

    def test_motion_is_a_group(self):
        self.assertIsInstance(self.doc["core"]["motion"], dict)
        self.assertIn("duration", self.doc["core"]["motion"])

    def test_lab_is_d50(self):
        # raw/css-vars.json declares red-600 and violet-300 as these lab() values and as hex.
        self.assertEqual(build_tokens.color("lab(48.7982% 67.6999 48.8037)"), "#dc2626")
        self.assertEqual(build_tokens.color("lab(76.8977% 16.5389 -33.9104)"), "#c4b5fd")
        self.assertEqual(self.doc["light"]["theme"]["destructive"]["$value"], "#dc2626")
        self.assertEqual(self.doc["light"]["theme"]["ring"]["$value"], "#c4b5fd")
        # L is 0..100 even below 1: lab(0.5 0 0) is near-black, not mid grey.
        self.assertEqual(build_tokens.color("lab(0.5 0 0)"), "#020202")

    def test_no_token_holds_tokens(self):
        self.assertEqual(nested_tokens(self.doc), [])

    def test_shadows_are_layers(self):
        raised = self.doc["light"]["elevation"]["raised"]["$value"]
        self.assertEqual(raised[2], {"color": "rgba(0, 0, 0, 0.05)", "offsetX": "0px", "offsetY": "2px",
                                     "blur": "6px", "spread": "-2px"})
        with self.assertRaises(ValueError):
            build_tokens.shadow_layers("0px 2px oops")


if __name__ == "__main__":
    unittest.main()
