"""The public Shopify readings survive in tokens.json."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


class Tokens(unittest.TestCase):
    def test_marketing_page_is_black(self):
        self.assertEqual(TOKENS["dark"]["page"]["$value"], "#000000")
        self.assertEqual(TOKENS["dark"]["text"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["dark"]["accent"]["$value"], "#5433eb")

    def test_login_form_text_and_link(self):
        self.assertEqual(TOKENS["light"]["text"]["$value"], "#303030")
        self.assertEqual(TOKENS["light"]["accent"]["$value"], "#005bd3")
        self.assertEqual(TOKENS["light"]["field"]["bg"]["$value"], "#f3f3f3")

    def test_pill_and_login_radius(self):
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "9999px")
        self.assertEqual(TOKENS["light"]["button"]["radius"]["$value"], "8px")
        self.assertEqual(TOKENS["light"]["button"]["height"]["$value"], "44px")

    def test_login_page_is_recorded_on_dark(self):
        self.assertEqual(TOKENS["dark"]["login-page"]["$value"], "#0a1314")

    def test_every_token_names_its_source(self):
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                src = node.get("$extensions", {}).get("source")
                if not src:
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if key.startswith("$"):
                        continue
                    walk(child, path + "." + key)

        walk(TOKENS["core"], "core")
        walk(TOKENS["light"], "light")
        walk(TOKENS["dark"], "dark")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
