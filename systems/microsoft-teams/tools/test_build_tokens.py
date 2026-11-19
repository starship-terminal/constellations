#!/usr/bin/env python3
"""The token builder writes the painted button colour and the measured hero size."""
import json
import subprocess
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


class BuildTokensTest(unittest.TestCase):
    def test_painted_action_and_hero(self):
        subprocess.check_call(["python3", str(HERE / "build_tokens.py")], cwd=ROOT)
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["light"]["background"]["action"]["$value"], "#5d5bd4")
        self.assertEqual(tokens["light"]["background"]["action-hover"]["$value"], "#5553c1")
        self.assertEqual(tokens["core"]["typography"]["hero"]["$value"]["fontSize"], "62px")
        self.assertEqual(tokens["core"]["radius"]["control"]["$value"], "8px")
        self.assertTrue(tokens["light"]["text"]["heading"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
