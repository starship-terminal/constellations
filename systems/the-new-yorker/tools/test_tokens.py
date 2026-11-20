"""The New Yorker package: measured tokens stay tied to the readings file."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.tokens = json.loads((ROOT / "tokens.json").read_text())
        self.raw = json.loads((ROOT / "raw" / "readings.json").read_text())

    def test_accent_matches_subscribe(self):
        self.assertEqual(self.tokens["light"]["accent"]["$value"], "#0879bf")
        self.assertIn("8, 121, 191", self.raw["computed"]["homeSubscribe"]["bg"])

    def test_body_size(self):
        body = self.tokens["core"]["typography"]["body"]["$value"]
        self.assertEqual(body["fontSize"], "21px")
        self.assertEqual(self.raw["computed"]["articleBody"]["size"], "21px")

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = (node.get("$extensions") or {}).get("source")
                if not source:
                    missing.append(path)
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, f"{path}.{key}" if path else key)

        walk(self.tokens["core"], "core")
        walk(self.tokens["light"], "light")
        self.assertEqual(missing, [])

    def test_screenshot_gap_is_recorded(self):
        note = (ROOT / "screenshots" / "README.md").read_text()
        self.assertIn("not producing screenshot frames", note)


if __name__ == "__main__":
    unittest.main()
