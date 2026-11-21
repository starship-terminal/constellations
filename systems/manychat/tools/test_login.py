"""The signed-in notes name real screenshots and do not claim a submitted create."""
import json
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class LoginReview(unittest.TestCase):
    def setUp(self):
        self.review = json.loads((PKG / "login-review.json").read_text())

    def test_screens_exist(self):
        self.assertGreaterEqual(len(self.review["screens"]), 2)
        for row in self.review["screens"]:
            self.assertTrue((PKG / row["file"]).is_file(), row["file"])

    def test_create_was_offered_and_not_reached(self):
        create = self.review["offered"]["create"]
        self.assertIn("+ Add New Account", create["items"])
        self.assertEqual(create["reached"], [])
        self.assertIn("Add New Account", self.review["not_submitted"])

    def test_signed_in_flag(self):
        self.assertTrue(self.review["signed_in"])
        self.assertEqual(self.review["viewports"]["desktop"]["innerWidth"], 1440)
        self.assertEqual(self.review["viewports"]["phone"]["innerWidth"], 390)


if __name__ == "__main__":
    unittest.main()
