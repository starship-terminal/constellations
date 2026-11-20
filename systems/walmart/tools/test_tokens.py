"""The Walmart tokens resolve and match the readings that were committed."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


class Tokens(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = [path for path, node in walk(TOKENS) if "source" not in node.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_header_blue_is_the_measured_value(self):
        self.assertEqual(TOKENS["core"]["color"]["blue"]["100"]["$value"], "#0053e2")

    def test_one_light_theme(self):
        self.assertEqual([t["id"] for t in TOKENS["$themes"]], ["light"])

    def test_readings_exist(self):
        self.assertTrue((ROOT / "raw" / "home.json").exists())
        self.assertTrue((ROOT / "screenshots" / "home-light-default.png").exists())


if __name__ == "__main__":
    unittest.main()
