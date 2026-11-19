#!/usr/bin/env python3
"""The Peerlist token builder writes the measured green and the light page."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


class BuildTokensTest(unittest.TestCase):
    def test_measured_green_and_page(self):
        subprocess.check_call([sys.executable, str(HERE / "build_tokens.py")], cwd=HERE)
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["green"]["$value"], "rgb(0 170 69)")
        self.assertEqual(tokens["light"]["page"]["$value"], "{color.gray.00}")
        self.assertEqual(tokens["core"]["radius"]["button"]["$value"], "12px")
        self.assertIn("source", tokens["light"]["accent"]["$extensions"])


if __name__ == "__main__":
    unittest.main()
