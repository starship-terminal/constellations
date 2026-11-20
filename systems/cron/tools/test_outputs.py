"""Checks on cron's committed tokens and measurements prose."""
import json
import pathlib
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())


class Outputs(unittest.TestCase):
    def test_typed_content_width_says_so(self):
        self.assertTrue(T["core"]["spacing"]["content-max"]["$extensions"]["source"].startswith("Reconstruction:"))

    def test_measurements_prose_names_no_other_products_cdn(self):
        self.assertNotIn("cloudfront", (ROOT / "raw" / "measurements.md").read_text())


if __name__ == "__main__":
    unittest.main()
