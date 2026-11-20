"""The Parallel package records attached-browser measurements, not invented values."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class MeasuredRecord(unittest.TestCase):
    def test_measured_json_names_the_attached_browser(self):
        data = json.loads((ROOT / "raw" / "measured.json").read_text())
        self.assertIn("Attached T3 preview browser", data["method"])
        self.assertEqual(data["pages"]["home"]["loginButton"]["backgroundColor"], "rgb(251, 99, 27)")
        self.assertIn("screenshot frames", data["screenshotGap"])

    def test_brand_token_matches_the_login_button(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        brand = tokens["core"]["color"]["brand"]
        self.assertEqual(brand["$value"], "#fb631b")
        self.assertIn("LOG IN", brand["$extensions"]["source"])
        self.assertNotIn("#ff590a", brand["$value"])

    def test_login_was_not_submitted(self):
        data = json.loads((ROOT / "raw" / "measured.json").read_text())
        joined = " ".join(data["notEntered"])
        self.assertIn("email form", joined)
        self.assertIn("useparallel.com", joined)


if __name__ == "__main__":
    unittest.main()
