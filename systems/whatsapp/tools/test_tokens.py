#!/usr/bin/env python3
"""The measured WhatsApp tokens stay put."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class Tokens(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(TOKENS.read_text())

    def test_green_is_the_measured_download_fill(self):
        self.assertEqual(self.data["core"]["color"]["green"]["$value"], "#25d366")

    def test_dark_set_stays_empty(self):
        self.assertEqual(self.data["dark"], {})

    def test_display_size_is_the_desktop_h1(self):
        self.assertEqual(self.data["core"]["typography"]["display"]["$value"]["fontSize"], "80px")


if __name__ == "__main__":
    unittest.main()
