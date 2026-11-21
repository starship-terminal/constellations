"""Lyft token file keeps a source on every token."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent

def walk(node):
    if isinstance(node, dict) and "$value" in node:
        yield node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value)

class TokenFileTest(unittest.TestCase):
    def test_every_token_has_a_measured_source(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        missing = [t for t in walk(tokens) if "source" not in t.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_accent_is_the_measured_purple(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["surface"]["interactive"]["$value"], "#820076")


if __name__ == "__main__":
    unittest.main()
