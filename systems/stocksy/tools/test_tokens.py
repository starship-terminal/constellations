"""The Stocksy tokens resolve, and the measured brand green is the accent."""
import json
import unittest
from pathlib import Path

TOKENS = Path(__file__).resolve().parents[1] / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_accent_is_the_measured_green(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["color"]["action"]["fill"]["$value"], "#0ae47c")
        self.assertEqual(data["dark"]["color"]["bg"]["page"]["$value"], "#000000")
        self.assertEqual(data["core"]["font"]["family"]["brand"]["$value"][0], "Poppins")

    def test_component_aliases_point_at_a_real_token(self):
        data = json.loads(TOKENS.read_text())

        def walk(node, path, found):
            if isinstance(node, dict):
                if "$value" in node and isinstance(node["$value"], str) and node["$value"].startswith("{"):
                    found.append((path, node["$value"].strip("{}")))
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, path + [key], found)

        refs = []
        walk(data, [], refs)
        flat = set()

        def flatten(node, path):
            if isinstance(node, dict) and "$value" in node:
                flat.add(".".join(path))
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        flatten(child, path + [key])

        flatten(data, [])
        missing = [ref for _, ref in refs if ref not in flat]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
