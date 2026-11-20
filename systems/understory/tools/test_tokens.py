"""Checks the committed Understory tokens stay measurable and internally consistent."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, f"{path}.{key}" if path else key)


class TokenTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        data = json.loads(TOKENS.read_text())
        missing = [path for path, token in walk(data) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_measured_colours_are_present(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["background"]["page"]["$value"], "#f6f4e8")
        self.assertEqual(data["light"]["background"]["action"]["$value"], "#022c12")
        self.assertEqual(data["light"]["text"]["primary"]["$value"], "#022c12")
        self.assertEqual(data["light"]["background"]["app-action"]["$value"], "#d5f285")

    def test_light_theme_is_the_only_theme(self):
        data = json.loads(TOKENS.read_text())
        self.assertNotIn("dark", data)
        self.assertEqual(data["$themes"][0]["id"], "light")


if __name__ == "__main__":
    unittest.main()
