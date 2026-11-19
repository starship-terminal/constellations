"""tokens.json matches raw/foundations.json. Run from this tools/ folder."""
import json
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent


class BuildTokensTest(unittest.TestCase):
    def test_coral_matches_raw(self):
        raw = json.loads((HERE / "raw" / "foundations.json").read_text())
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["coral"]["$value"], raw["colors"]["coral"])
        self.assertEqual(tokens["light"]["component"]["button"]["bg"]["$value"], "#ff4143")
        self.assertEqual(tokens["light"]["surface"]["hero"]["$value"], "#42022e")
        self.assertIn("source", tokens["core"]["color"]["coral"]["$extensions"])


if __name__ == "__main__":
    unittest.main()
