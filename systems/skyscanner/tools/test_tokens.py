"""tokens.json holds the action, text, type, radius and field values that were measured."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_action_and_type_values(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["background"]["action"]["$value"], "{color.accent}")
        self.assertEqual(tokens["core"]["color"]["accent"]["$value"], "#0062e3")
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "{color.text}")
        self.assertEqual(tokens["core"]["color"]["text"]["$value"], "#161616")
        self.assertEqual(tokens["core"]["typography"]["heading-2"]["$value"]["fontSize"], "32px")
        self.assertEqual(tokens["core"]["radius"]["md"]["$value"], "12px")
        self.assertEqual(tokens["core"]["size"]["field"]["$value"], "72px")
        self.assertEqual(tokens["light"]["background"]["contrast"]["$value"], "{color.ink}")


if __name__ == "__main__":
    unittest.main()
