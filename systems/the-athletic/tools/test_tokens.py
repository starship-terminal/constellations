#!/usr/bin/env python3
"""The Athletic package: every token has a source, and the live pairs match the readings."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())
RAW = json.loads((ROOT / "raw" / "css-vars.json").read_text())
COMPUTED = json.loads((ROOT / "raw" / "components-computed.json").read_text())


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        here = f"{path}.{key}" if path else key
        if isinstance(value, dict) and "$value" in value:
            yield here, value
        elif isinstance(value, dict):
            yield from walk(value, here)


class TokensTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, token in walk(TOKENS) if not token.get("$extensions", {}).get("source")]
        self.assertEqual(missing, [])

    def test_painted_theme_matches_legacy_vars(self):
        self.assertEqual(TOKENS["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(RAW["themes"]["legacy"]["--Gray10"], "#fff")
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#b72424")
        self.assertEqual(RAW["themes"]["legacy"]["--Red10"], "#b72424")
        self.assertEqual(COMPUTED["home"]["trial"]["bg"], "rgb(183, 36, 36)")

    def test_dark_set_is_labelled_declared(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#000000")
        self.assertEqual(RAW["themes"]["dark"]["--Gray10"], "#000")
        self.assertIn("not painted", TOKENS["dark"]["page"]["$extensions"]["source"])

    def test_story_measure(self):
        story = TOKENS["core"]["typography"]["story"]["$value"]
        self.assertEqual(story["fontSize"], "20px")
        self.assertEqual(story["lineHeight"], "30px")
        self.assertEqual(COMPUTED["article"]["body"]["size"], "20px")
        self.assertEqual(COMPUTED["article"]["body"]["lh"], "30px")


if __name__ == "__main__":
    unittest.main()
