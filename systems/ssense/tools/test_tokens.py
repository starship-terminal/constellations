"""tokens.json has no dark set, keeps the measured action, muted text, radius and chrome size, and every light token names a source."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_light_only_values_and_sources(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertNotIn("dark", tokens)
        self.assertEqual(tokens["light"]["background"]["action"]["$value"], "#000000")
        self.assertEqual(tokens["light"]["text"]["muted"]["$value"], "#888888")
        self.assertEqual(tokens["core"]["radius"]["cta"]["$value"], "10px")
        self.assertEqual(tokens["core"]["typography"]["chrome"]["$value"]["fontSize"], "11px")
        for name, token in self._walk(tokens["light"]):
            self.assertIn("source", token["$extensions"], name)

    def test_colours_are_hex(self):
        import re
        tokens = json.loads((ROOT / "tokens.json").read_text())
        for name, token in self._walk(tokens["light"]):
            if token.get("$type") == "color" and not str(token["$value"]).startswith("{"):
                self.assertRegex(token["$value"], r"^#[0-9a-f]{6}([0-9a-f]{2})?$", name)

    def _walk(self, node, prefix=""):
        for key, value in node.items():
            if str(key).startswith("$"):
                continue
            if isinstance(value, dict) and "$value" in value:
                yield prefix + key, value
            elif isinstance(value, dict):
                yield from self._walk(value, prefix + key + ".")


if __name__ == "__main__":
    unittest.main()
