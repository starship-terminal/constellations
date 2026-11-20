"""tokens.json is what the builder writes, and motion values DTCG cannot carry are listed."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_untokenised_easings_are_listed(self):
        listed = json.loads(build_tokens.TEXT)["core"]["$extensions"]["notTokenised"]
        values = {x["value"] for x in listed}
        self.assertIn("steps(12, end)", values)


if __name__ == "__main__":
    unittest.main()
