"""The Raster token file keeps the measured marketing colours."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def setUp(self):
        self.t = json.loads((HERE / "tokens.json").read_text())

    def test_brand_red(self):
        self.assertEqual(self.t["core"]["color"]["brand"]["red"]["$value"], "#ff2f66")

    def test_page_is_black(self):
        self.assertEqual(self.t["dark"]["background"]["page"]["$value"], "{color.black}")
        self.assertEqual(self.t["core"]["color"]["black"]["$value"], "#000000")

    def test_control_radius(self):
        self.assertEqual(self.t["core"]["radius"]["control"]["$value"], "5.25px")

    def test_every_token_has_a_source(self):
        def walk(node):
            if isinstance(node, dict) and "$value" in node:
                self.assertIn("source", node.get("$extensions", {}))
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        walk(v)
        walk(self.t["core"])
        walk(self.t["dark"])
        walk(self.t["docs"])


if __name__ == "__main__":
    unittest.main()
