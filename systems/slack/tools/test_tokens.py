"""Slack token file keeps the measured marketing accent and Slack Kit aubergine."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_light_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["light"]["color"]["bg"]["page"]["$value"], "#ffffff")
        self.assertEqual(data["light"]["color"]["accent"]["$value"], "#730394")
        self.assertEqual(data["light"]["color"]["text"]["primary"]["$value"], "#1d1c1d")
        self.assertEqual(data["light"]["color"]["text"]["secondary"]["$value"], "#454447")
        self.assertEqual(data["core"]["color"]["brand"]["aubergine"]["$value"], "#4a154b")
        self.assertEqual(data["core"]["radius"]["base"]["$value"], "4px")
        self.assertEqual(data["core"]["radius"]["xlarge"]["$value"], "12px")
        self.assertNotIn("dark", data)


if __name__ == "__main__":
    unittest.main()
