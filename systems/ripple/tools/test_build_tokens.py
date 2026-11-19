"""tokens.json has a source on every token and resolves."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"

def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v)

class TokensTest(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(TOKENS.is_file())

    def test_every_token_has_a_source(self):
        doc = json.loads(TOKENS.read_text())
        for name in ("core", "light"):
            for tok in walk(doc[name]):
                src = tok.get("$extensions", {}).get("source", {})
                self.assertTrue(src.get("evidence"), tok)
                self.assertTrue(src.get("capture"), tok)

    def test_accent_is_measured_blue(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["light"]["accent"]["$value"], "#006aff")
