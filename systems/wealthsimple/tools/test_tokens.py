"""Package checks for the Wealthsimple capture. Run from tools/."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_sets(self):
        self.assertIn("core", TOKENS)
        self.assertIn("light", TOKENS)
        self.assertNotIn("dark", TOKENS)

    def test_every_token_has_a_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if "source" not in node.get("$extensions", {}):
                    missing.append(path)
                return
            if isinstance(node, dict):
                for k, v in node.items():
                    if k.startswith("$"):
                        continue
                    walk(v, f"{path}.{k}" if path else k)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        self.assertEqual(missing, [])

    def test_page_is_off_white(self):
        self.assertEqual(TOKENS["core"]["color"]["greyscale"]["99"]["$value"], "#fcfcfc")

    def test_ink(self):
        self.assertEqual(TOKENS["core"]["color"]["slate"]["10"]["$value"], "#1c1b1b")

    def test_no_private_literals(self):
        blob = (HERE / "tokens.json").read_text() + (HERE / "README.md").read_text() + (HERE / "site-tree.md").read_text()
        self.assertNotRegex(blob, r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


if __name__ == "__main__":
    unittest.main()
