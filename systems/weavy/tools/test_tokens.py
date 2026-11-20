"""Weavy tokens stay tied to the readings."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
R = json.loads((HERE / "raw" / "readings.json").read_text())


class TokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        import sys
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens
        self.assertEqual(T, build_tokens.build())  # built in memory, nothing written

    def test_check_refuses_a_broken_file(self):
        import copy
        import sys
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens
        bad = copy.deepcopy(T)
        bad["dark"]["color"]["app"]["page"]["$value"] = "rgb(44, 44, 44)"
        with self.assertRaises(SystemExit):
            build_tokens.check(bad)

    def test_card_shadow_keeps_both_layers(self):
        self.assertEqual(len(T["light"]["shadow"]["card"]["$value"]), 2)
        self.assertIn("0px 0px 0.5px 0px", R["signin"]["card"]["boxShadow"])

    def test_lemon_is_the_measured_fill(self):
        self.assertEqual(T["light"]["color"]["marketing"]["lemon"]["$value"], "#f7ff9e")
        self.assertEqual(R["marketing"]["rootCustomProperties"]["--brand--lemon"], "#f7ff9e")

    def test_signin_text_is_the_computed_role(self):
        self.assertEqual(T["light"]["color"]["app"]["text"]["$value"], "#000000e5")

    def test_dark_page_is_the_declared_ramp(self):
        self.assertEqual(T["dark"]["color"]["app"]["page"]["$value"], "#2c2c2c")

    def test_every_token_has_a_source(self):
        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                src = node.get("$extensions", {}).get("source", "")
                self.assertTrue(src, path)
            elif isinstance(node, dict):
                for key, value in node.items():
                    if key.startswith("$"):
                        continue
                    walk(value, path + "." + key)

        walk(T["core"], "core")
        walk(T["light"], "light")
        walk(T["dark"], "dark")

    def test_display_size_matches_the_1440_heading(self):
        self.assertEqual(T["core"]["typography"]["display"]["$value"]["fontSize"], "94px")


if __name__ == "__main__":
    unittest.main()
