"""Package smoke test. Confirms tokens.json parses and names both painted themes."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_themes_present(self):
        data = json.loads(TOKENS.read_text())
        self.assertIn("light", data)
        self.assertIn("dark", data)
        self.assertEqual(data["light"]["color"]["bg"]["action"]["$value"], "{color.marketing.primary-purple}")
        self.assertEqual(data["dark"]["color"]["bg"]["page"]["$value"], "{color.studio.secondary.c1100}")


if __name__ == "__main__":
    unittest.main()
