"""The Coolors package records a Cloudflare block and does not invent product values."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class BlockRecord(unittest.TestCase):
    def test_block_json_says_blocked(self):
        data = json.loads((ROOT / "raw" / "block.json").read_text())
        self.assertEqual(data["verdict"], "blocked")
        self.assertTrue(data["curlProbes"])
        self.assertTrue(all(p["status"] == 403 for p in data["curlProbes"]))
        self.assertTrue(all(p["cfMitigated"] == "challenge" for p in data["curlProbes"]))
        self.assertIn("Just a moment", data["playwrightProbe"]["title"])

    def test_block_record_is_still_on_disk(self):
        data = json.loads((ROOT / "raw" / "block.json").read_text())
        self.assertEqual(data["verdict"], "blocked")
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["primary"]["$value"], "#2563eb")

    def test_screenshot_exists(self):
        self.assertTrue((ROOT / "screenshots" / "home-blocked-challenge.png").is_file())


if __name__ == "__main__":
    unittest.main()
