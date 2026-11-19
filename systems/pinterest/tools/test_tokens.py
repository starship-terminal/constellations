"""Pinterest token file holds the values measured on the public homepage."""
import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_primary_red(self):
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"], "#e60023")

    def test_page_is_white(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#ffffff")

    def test_button_radius(self):
        self.assertEqual(TOKENS["light"]["component"]["button"]["radius"]["$value"], "16px")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
