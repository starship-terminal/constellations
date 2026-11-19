"""The committed tokens.json still matches raw/readings.json."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class TokensTest(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        import build_tokens  # noqa: F401  (writes tokens.json)

        committed = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(committed["light"]["color"]["text"]["primary"]["$value"], "#171717")
        self.assertEqual(committed["light"]["color"]["background"]["page"]["$value"], "#ffffff")
        self.assertIn("source", committed["core"]["fontSize"]["display"]["$extensions"])


if __name__ == "__main__":
    unittest.main()
