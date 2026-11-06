"""core() must stop with a named error when a list reading holds too few positions, instead of
falling back to a fixed value or an IndexError. Run: python3 -m unittest discover -s tools."""
import copy
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402


@unittest.skipUnless(build_tokens.READ, "no raw/readings.json")
class CountTest(unittest.TestCase):
    def setUp(self):
        self.saved = copy.deepcopy(build_tokens.READ)

    def tearDown(self):
        build_tokens.READ.clear()
        build_tokens.READ.update(self.saved)

    def test_committed_readings_build(self):
        build_tokens.core()

    def test_too_few_settings_dividers_fails(self):
        build_tokens.READ["rows.settings"]["dark"]["value"] = build_tokens.READ["rows.settings"]["dark"]["value"][:3]
        with self.assertRaisesRegex(ValueError, "rows.settings: 3 positions"):
            build_tokens.core()

if __name__ == "__main__":
    unittest.main()
