"""The Sonarworks token file matches the values read on 2026-11-19."""
import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_page_and_nav(self):
        self.assertEqual(TOKENS["light"]["background"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["light"]["background"]["inverse"]["$value"], "#000000")
        self.assertEqual(TOKENS["light"]["text"]["secondary"]["$value"], "#96999c")

    def test_display_and_pill(self):
        display = TOKENS["core"]["typography"]["display"]["$value"]
        self.assertEqual(display["fontSize"], "44px")
        self.assertEqual(display["letterSpacing"], "-1.5px")
        self.assertEqual(TOKENS["core"]["radius"]["full"]["$value"], "9999px")

    def test_disabled_and_sale(self):
        self.assertEqual(TOKENS["light"]["background"]["disabled"]["$value"], "#d8d9da")
        self.assertEqual(TOKENS["light"]["status"]["sale"]["$value"], "#ffe701")
        self.assertEqual(TOKENS["light"]["action"]["trial"]["$value"], "#68befd")


    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not (node.get("$extensions") or {}).get("source"):
                    missing.append(path)
                return
            if isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v, f"{path}.{k}" if path else k)

        walk(TOKENS, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
