"""The token builder writes the colours and lengths that were measured.

build_tokens.build() runs in memory; nothing here writes tokens.json."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = json.loads((ROOT / "tokens.json").read_text())
COMP = json.loads((ROOT / "raw" / "components.json").read_text())


class Tokens(unittest.TestCase):
    def test_committed_file_is_what_the_builder_makes(self):
        self.assertEqual(TOKENS, build_tokens.build())

    def test_action_and_type_match_the_readings(self):
        self.assertEqual(TOKENS["light"]["background"]["action"]["$value"], "#6307f8")
        self.assertEqual(TOKENS["light"]["text"]["primary"]["$value"], "#15002c")
        self.assertEqual(TOKENS["core"]["typography"]["display"]["$value"]["fontSize"], "45px")
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "9999px")
        self.assertEqual(TOKENS["light"]["background"]["login-action"]["$value"], "#131316")

    def test_type_styles_carry_the_raw_readings(self):
        typo = TOKENS["core"]["typography"]
        self.assertEqual(typo["heading"]["$value"]["fontSize"], COMP["h2"]["fontSize"])
        self.assertEqual(typo["heading"]["$value"]["lineHeight"], COMP["h2"]["lineHeight"])
        self.assertEqual(typo["login-label"]["$value"]["fontSize"], COMP["login"]["label"]["fontSize"])

    def test_a_line_height_raw_does_not_hold_is_not_measured(self):
        for key in ("title", "price", "feature", "faq", "footer", "login-heading", "login-label"):
            self.assertTrue(TOKENS["core"]["typography"][key]["$extensions"]["source"].startswith("Reconstruction"), key)

    def test_every_token_is_typed_and_sourced(self):
        def leaves(node, path=""):
            if isinstance(node, dict) and "$value" in node:
                yield path, node
            elif isinstance(node, dict):
                for k, v in node.items():
                    if not k.startswith("$"):
                        yield from leaves(v, f"{path}.{k}")

        for path, t in leaves({"core": TOKENS["core"], "light": TOKENS["light"]}):
            self.assertIn("$type", t, path)
            self.assertTrue(t["$extensions"]["source"], path)
        self.assertEqual(TOKENS["core"]["motion"]["easing"]["standard"]["$value"], [0.4, 0, 0.2, 1])


if __name__ == "__main__":
    unittest.main()
