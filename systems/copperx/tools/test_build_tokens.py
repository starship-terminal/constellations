#!/usr/bin/env python3
"""The committed tokens.json is what build_tokens.py builds from raw/, built in memory (nothing is written)."""
import importlib
import json
import pathlib
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))


class BuildTokens(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.built = importlib.import_module("build_tokens").build()
        cls.committed = json.loads((ROOT / "tokens.json").read_text())

    def test_committed_file_matches_a_fresh_build(self):
        self.assertEqual(self.committed, self.built)

    def test_values_come_from_the_readings(self):
        f = json.loads((ROOT / "raw" / "foundations.json").read_text())
        self.assertEqual(self.built["core"]["color"]["indigo"]["$value"], "#4c63ed")
        self.assertEqual(f["heroAccent"]["color"], "rgb(76, 99, 237)")
        self.assertEqual(self.built["light"]["action"]["primary"]["$value"], "{color.black}")
        self.assertIn("light", self.built["$themes"][0]["selectedTokenSets"])

    def test_motion_group_is_committed(self):
        # motion.build returns (group, notTokenised); the group must land in core.motion.
        self.assertIn("duration", self.built["core"]["motion"])

    def test_hand_entered_values_say_so(self):
        for path in (("color", "body"), ("typography", "title"), ("radius", "panel")):
            leaf = self.built["core"]
            for k in path:
                leaf = leaf[k]
            self.assertTrue(leaf["$extensions"]["source"].startswith("Reconstruction:"), path)


if __name__ == "__main__":
    unittest.main()
