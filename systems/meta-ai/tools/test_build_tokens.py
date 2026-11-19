"""Package checks for the Meta AI capture."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_semantic_colours_match_computed_properties(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        raw = json.loads((ROOT / "raw" / "computed-root.json").read_text())["vars"]
        self.assertEqual(tokens["dark"]["surface"]["page"]["$value"], raw["--background-primary"])
        self.assertEqual(tokens["dark"]["text"]["primary"]["$value"], raw["--text-primary"])
        self.assertEqual(tokens["dark"]["accent"]["$value"], raw["--accent-dark"])
        self.assertEqual(tokens["dark"]["text"]["secondary"]["$value"], "#f2f7ff87")

    def test_every_token_has_a_source(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node.get("$extensions", {}), path)
            elif isinstance(node, dict):
                for k, v in node.items():
                    if k.startswith("$"):
                        continue
                    walk(v, path + "." + k)

        for group in ("core", "dark", "light"):
            walk(tokens[group], group)

    def test_readme_names_the_capture_gap(self):
        text = (ROOT / "README.md").read_text()
        self.assertIn("preview_snapshot", text)
        self.assertIn("HTTP 403", text)
        self.assertIn("Do and don't", text)


if __name__ == "__main__":
    unittest.main()
