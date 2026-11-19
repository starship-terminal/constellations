#!/usr/bin/env python3
"""The measured Synthesia colours survive a rebuild."""
import json
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_painted_values(self):
        tokens = json.loads((HERE / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["indigo"]["500"]["$value"], "#3e57da")
        self.assertEqual(tokens["core"]["color"]["ink"]["$value"], "#090b22")
        self.assertEqual(tokens["light"]["color"]["bg"]["brand"]["$value"], "{color.indigo.500}")
        self.assertEqual(tokens["core"]["typography"]["hero"]["$value"]["fontSize"], "56px")
        self.assertIn("light", tokens)
        self.assertNotIn("dark", tokens)


if __name__ == "__main__":
    unittest.main()
