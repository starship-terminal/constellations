"""The Missive token file stays a valid DTCG document the builder can rebuild."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_sets_and_brand(self):
        doc = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(set(doc), {"core", "light", "dark", "$themes", "$metadata"})
        self.assertEqual(doc["core"]["color"]["brand"]["$value"], "#2266ed")
        self.assertEqual(doc["light"]["accent"]["$value"], "{color.brand}")
        self.assertEqual(doc["dark"]["page"]["$value"], "#1d1e1f")
        self.assertIn("motion", doc["core"])

    def test_dimensions_are_lengths(self):
        doc = json.loads((ROOT / "tokens.json").read_text())

        def walk(node):
            for k, v in node.items():
                if k.startswith("$"):
                    continue
                if isinstance(v, dict) and "$value" in v:
                    yield k, v
                elif isinstance(v, dict):
                    yield from walk(v)

        for name, tok in walk(doc["core"]):
            if tok.get("$type") == "dimension":
                self.assertRegex(tok["$value"], r"^-?\d+(\.\d+)?(px|rem)$", name)


if __name__ == "__main__":
    unittest.main()
