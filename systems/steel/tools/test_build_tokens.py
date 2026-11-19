"""Steel tokens keep the measured marketing page, accent, and focus ring."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_dark_page_and_accent(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["dark"]["surface"]["page"]["$value"], "#141414")
        self.assertEqual(data["dark"]["accent"]["$value"], "#eeeeec")
        self.assertEqual(data["dark"]["text"]["primary"]["$value"], "#eeeeec")
        self.assertEqual(data["dark"]["text"]["secondary"]["$value"], "#b4b3ad")
        self.assertEqual(data["dark"]["status"]["focus"]["$value"], "#05a5ff")
        self.assertEqual(data["light"]["surface"]["page"]["$value"], "#ffffff")
        self.assertEqual(data["light"]["text"]["primary"]["$value"], "#21201c")
        self.assertEqual(data["core"]["radius"]["button"]["$value"], "6px")
        self.assertEqual(data["core"]["motion"]["duration"]["default"]["$value"], "150ms")


if __name__ == "__main__":
    unittest.main()
