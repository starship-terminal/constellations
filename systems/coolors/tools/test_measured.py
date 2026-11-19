"""The Coolors package records attached-browser measurements, not invented values."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class MeasuredRecord(unittest.TestCase):
    def test_measured_json_names_the_attached_browser(self):
        data = json.loads((ROOT / "raw" / "measured.json").read_text())
        self.assertIn("Attached T3 preview browser", data["method"])
        self.assertTrue(data["pages"])
        self.assertEqual(data["home"]["primaryButton"]["backgroundColor"], "rgb(37, 99, 235)")

    def test_primary_token_matches_the_button(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        primary = tokens["core"]["color"]["primary"]
        self.assertEqual(primary["$value"], "#2563eb")
        self.assertIn("Start the Generator", primary["$extensions"]["source"])
        self.assertNotIn("Not captured", tokens["light"]["page"]["$extensions"]["source"])

    def test_generator_screenshot_exists(self):
        self.assertTrue((ROOT / "screenshots" / "generate-light-desktop.png").is_file())


if __name__ == "__main__":
    unittest.main()
