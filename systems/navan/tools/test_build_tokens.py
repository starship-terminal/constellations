"""The token builder writes the colours and lengths that were measured."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_action_and_type_match_the_readings(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["background"]["action"]["$value"], "#6307f8")
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "#15002c")
        self.assertEqual(tokens["core"]["typography"]["display"]["$value"]["fontSize"], "45px")
        self.assertEqual(tokens["core"]["radius"]["pill"]["$value"], "9999px")
        self.assertEqual(tokens["light"]["background"]["login-action"]["$value"], "#131316")


if __name__ == "__main__":
    unittest.main()
