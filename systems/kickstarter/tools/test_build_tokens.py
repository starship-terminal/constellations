"""Checks for the Kickstarter token builder. Run from this folder, or via tools/package_tests.py kickstarter.

The builder runs in memory; nothing here writes tokens.json.
"""
import json
import pathlib
import unittest

import build_tokens

PKG = pathlib.Path(__file__).resolve().parent.parent
TOKENS = PKG / "tokens.json"


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, f"{path}.{k}" if path else k)


class BuildTokensTest(unittest.TestCase):
    def setUp(self):
        self.doc = build_tokens.build()

    def test_committed_tokens_match_build(self):
        self.assertEqual(json.loads(TOKENS.read_text()), self.doc)

    def test_display_is_the_measured_hero(self):
        h1 = build_tokens.COMP["hero-h1"]["states"]["default"]["style"]
        display = self.doc["core"]["typography"]["display"]["$value"]
        self.assertEqual((display["fontSize"], display["lineHeight"], str(display["fontWeight"])),
                         (h1["fontSize"], h1["lineHeight"], h1["fontWeight"]))
        self.assertEqual(self.doc["core"]["fontSize"]["display"]["$value"], h1["fontSize"])

    def test_ease_out_is_the_css_keyword(self):
        self.assertEqual(self.doc["core"]["motion"]["easing"]["out"]["$value"], [0, 0, 0.58, 1])

    def test_no_token_holds_tokens(self):
        """catalog.py's flatten stops at $value, so a token nested in another is invisible."""
        for set_name in ("core", "light"):
            for path, leaf in leaves(self.doc[set_name]):
                kids = [k for k in leaf if not k.startswith("$")]
                self.assertEqual(kids, [], f"{set_name}.{path} holds child tokens {kids}")

    def test_every_declared_colour_is_a_token(self):
        sources = {leaf["$extensions"]["source"] for _, leaf in leaves(self.doc["light"]["color"])}
        for name, value in build_tokens.RESOLVED.items():
            if name.startswith("--kds-color-") and not name.endswith("-foo") and value.strip() != "bar":
                self.assertIn(f"css-var {name}", sources)

    def test_aliases_name_no_set(self):
        """An alias is written without its set name ({font.family.sans}, not {core.font...})."""
        text = json.dumps(self.doc)
        self.assertNotIn("{core.", text)
        self.assertNotIn("{light.", text)

    def test_no_hand_value_claims_a_reading(self):
        """Hand-typed values carry the Reconstruction label (docs/EVIDENCE.md), never Derived or Measured."""
        for set_name in ("core",):
            for path, leaf in leaves(self.doc[set_name]):
                src = leaf["$extensions"]["source"]
                self.assertFalse(src.startswith(("Derived", "Measured")), f"{path}: {src}")


if __name__ == "__main__":
    unittest.main()
