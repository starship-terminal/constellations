"""tokens.json loads, every token records Measured evidence with a where, and the page, accent and text colours hold."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_file_loads(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("core", doc)
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)

    def test_every_token_has_measured_evidence(self):
        doc = json.loads(TOKENS.read_text())

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source", {})
                self.assertEqual(source.get("evidence"), "Measured", path)
                self.assertTrue(source.get("where"), path)
                return
            if isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, f"{path}.{key}" if path else key)

        walk(doc, "")

    def test_page_and_accent_match_the_reading(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["light"]["color"]["page"]["$value"], "#FAF9F5")
        self.assertEqual(doc["light"]["color"]["accent"]["$value"], "#0D0D0D")
        self.assertEqual(doc["light"]["color"]["text"]["$value"], "#0D0D0D")


if __name__ == "__main__":
    unittest.main()
