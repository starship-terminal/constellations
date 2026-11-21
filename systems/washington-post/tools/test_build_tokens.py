"""tokens.json matches the measured WPDS custom properties."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_cta_is_measured_blue(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        raw = json.loads((HERE / "raw" / "css-vars.json").read_text())["root"]
        self.assertEqual(tokens["light"]["accent"]["$value"], "#166dfc")
        self.assertIn("22, 109, 252", raw["--wpds-colors-cta"])
        self.assertIn("Measured", tokens["light"]["accent"]["$extensions"]["source"])
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
