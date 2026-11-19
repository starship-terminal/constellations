"""Zapier token file checks. Run from systems/zapier/tools."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


class TokenTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        data = json.loads(TOKENS.read_text())
        missing = [path for path, token in walk(data) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_light_only(self):
        data = json.loads(TOKENS.read_text())
        self.assertIn("light", data)
        self.assertNotIn("dark", data)
        self.assertEqual(data["light"]["color"]["action"]["fill"]["$value"], "{color.brand.orange}")
        self.assertEqual(data["core"]["color"]["brand"]["orange"]["$value"], "#ff4f00")


if __name__ == "__main__":
    unittest.main()
