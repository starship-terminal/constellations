"""tokens.json matches a fresh build from raw/readings.json."""
import json
import unittest
from pathlib import Path

import build_tokens

HERE = Path(__file__).resolve().parent.parent


class BuildTokensTest(unittest.TestCase):
    def test_committed_tokens_match_the_builder(self):
        committed = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(committed, build_tokens.document())
        self.assertEqual(committed["light"]["background"]["action"]["$value"], "oklch(61.47% .1986 30.12)")
        self.assertEqual(committed["light"]["brand"]["app-action"]["$value"], "#d33322")
        self.assertTrue(committed["core"]["typography"]["display"]["$extensions"]["source"])

    def test_readings_name_the_pages(self):
        raw = json.loads((HERE / "raw" / "readings.json").read_text())
        self.assertEqual(raw["pages"]["login"]["url"], "https://app.todoist.com/auth/login?locale=en")
        self.assertFalse(raw["pages"]["signup"]["entered"])


if __name__ == "__main__":
    unittest.main()
