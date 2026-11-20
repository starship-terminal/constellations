"""The committed tokens.json matches a fresh build, and every token has a source."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"


def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value)


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_rebuild(self):
        # Built in memory; importing the builder writes nothing.
        import build_tokens
        self.assertEqual(TOKENS.read_text(), build_tokens.render())

    def test_link_is_the_product_link_reading(self):
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())
        self.assertEqual(raw["controls"]["login"]["productLink"]["color"], "rgb(17, 17, 13)")
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["light"]["text"]["link"]["$value"], "#11110d")

    def test_style_guide_aliases_name_emitted_properties(self):
        # Every var(--x) the builder writes for an alias must be a property it declares.
        import re
        html = (PKG / "style-guide.html").read_text()
        declared = set(re.findall(r"(--[A-Za-z0-9-]+):", html))
        for used in set(re.findall(r"var\((--[A-Za-z0-9-]+)", html)):
            self.assertIn(used, declared)

    def test_every_token_has_a_source(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)
        for token in walk(doc):
            source = token.get("$extensions", {}).get("source")
            self.assertTrue(source, token)


if __name__ == "__main__":
    unittest.main()
