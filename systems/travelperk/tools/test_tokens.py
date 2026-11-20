"""tokens.json holds the measured action, text, type, radius and login control values."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def resolve(tokens, value):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        node = tokens
        for part in value[1:-1].split("."):
            node = node[part]
        return resolve(tokens, node["$value"])
    return value


class Tokens(unittest.TestCase):
    def test_action_and_type_values(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(resolve(tokens, tokens["light"]["background"]["action"]["$value"]), "#beff50")
        self.assertEqual(resolve(tokens, tokens["light"]["text"]["primary"]["$value"]), "#14140f")
        self.assertEqual(tokens["core"]["typography"]["display"]["$value"]["fontSize"], "80px")
        self.assertEqual(tokens["core"]["radius"]["button"]["$value"], "26px")
        self.assertEqual(resolve(tokens, tokens["light"]["login"]["action"]["$value"]), "#14140f")
        self.assertEqual(tokens["core"]["size"]["loginControl"]["$value"], "44px")


if __name__ == "__main__":
    unittest.main()
