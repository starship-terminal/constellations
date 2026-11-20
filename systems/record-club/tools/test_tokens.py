"""Record Club token checks. Run from the package tools folder."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(TOKENS.read_text())

    def test_sets(self):
        self.assertEqual(set(self.doc) - {"$themes"}, {"core", "light", "dark"})

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source")
                if not source or "evidence" not in source:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, path + "." + key)

        for name, body in self.doc.items():
            if name.startswith("$"):
                continue
            walk(body, name)
        self.assertEqual(missing, [])

    def test_brand_is_the_computed_pair(self):
        self.assertEqual(self.doc["light"]["color"]["action"]["brand"]["$value"], "#6e36ff")
        self.assertEqual(self.doc["dark"]["color"]["action"]["brand"]["$value"], "#ab68ff")

    def test_primary_flips_between_themes(self):
        self.assertEqual(self.doc["light"]["color"]["action"]["fill"]["$value"], "#121212")
        self.assertEqual(self.doc["dark"]["color"]["action"]["fill"]["$value"], "#ffffff")


if __name__ == "__main__":
    unittest.main()
