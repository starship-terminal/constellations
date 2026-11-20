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

    def test_card_shadow_matches_both_layers_of_the_reading(self):
        """Each token layer equals the matching layer of the saved computed box-shadow, read here
        independently of the builder: colour as #rrggbbaa, then x, y, blur and spread."""
        import re
        layers = []
        for m in re.finditer(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\) ([^ ,]+) ([^ ,]+) ([^ ,]+) ([^ ,]+)",
                             R["signin"]["card"]["boxShadow"]):
            r, g, b, a, x, y, blur, spread = m.groups()
            alpha = float(a) if a is not None else 1.0
            colour = "#%02x%02x%02x" % (int(r), int(g), int(b)) + ("%02x" % int(alpha * 255 + 0.5) if alpha < 1 else "")
            layers.append({"color": colour, "offsetX": x, "offsetY": y, "blur": blur, "spread": spread})
        self.assertEqual(len(layers), 2)
        self.assertEqual(T["light"]["shadow"]["card"]["$value"], layers)

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
