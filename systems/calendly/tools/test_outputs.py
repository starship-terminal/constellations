"""Committed outputs describe calendly.com, not the sibling the builders were copied from."""
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class Outputs(unittest.TestCase):
    def test_measurements_prose_names_this_product(self):
        head = (PKG / "raw" / "measurements.md").read_text().split("## Components")[0]
        self.assertIn("calendly.com", head)
        for wrong in ("butter.video", "/explore", "iubenda"):
            self.assertNotIn(wrong, head)


if __name__ == "__main__":
    unittest.main()
