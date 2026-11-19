#!/usr/bin/env python3
"""The token builder must keep the colours that were read off the page."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

import build_tokens

ROOT = Path(__file__).resolve().parents[1]


class BuildTokens(unittest.TestCase):
    def test_writes_measured_blue_and_page(self):
        build_tokens.main()
        doc = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(doc["core"]["color"]["blue"]["$value"], "#0988f0")
        self.assertEqual(doc["marketing"]["background"]["page"]["$value"], "#9a9a9a")
        self.assertEqual(doc["marketing"]["background"]["action"]["$value"], "#379def")
        self.assertEqual(doc["docs-dark"]["background"]["action"]["$value"], "#008847")
        self.assertEqual(doc["docs-light"]["text"]["primary"]["$value"], "#161a18")
        self.assertEqual(doc["sign-in"]["background"]["action"]["$value"], "#0989f1")
        self.assertIn("getComputedStyle", doc["marketing"]["text"]["primary"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
