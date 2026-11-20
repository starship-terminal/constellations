#!/usr/bin/env python3
"""The builder writes the colours that were measured, and only those."""
import json
import pathlib
import unittest

import build_tokens

HERE = pathlib.Path(__file__).resolve().parent.parent


class BuildTokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.render())

    def test_durations_are_typed_as_durations(self):
        for name, token in build_tokens.build()["core"]["motion"]["duration"].items():
            self.assertEqual(token["$type"], "duration", name)

    def test_measured_colours(self):
        tokens = build_tokens.build()
        self.assertEqual(tokens["light"]["surface"]["page"]["$value"], "#fdfdfd")
        self.assertEqual(tokens["light"]["surface"]["shell"]["$value"], "#f3f3f3")
        self.assertEqual(tokens["light"]["text"]["primary"]["$value"], "#0a0a0a")
        self.assertEqual(tokens["light"]["accent"]["$value"], "#0a0a0a")
        self.assertEqual(tokens["dark"]["surface"]["page"]["$value"], "#0e0e0e")
        self.assertEqual(tokens["dark"]["accent"]["$value"], "#fdfdfd")
        self.assertEqual(tokens["core"]["color"]["brand"]["$value"], "#3e46ff")
        self.assertEqual(tokens["core"]["radius"]["tile"]["$value"], "16px")
        self.assertEqual(tokens["core"]["font"]["family"]["sans"]["$value"].split(",")[0], "saveeFont")


if __name__ == "__main__":
    unittest.main()
