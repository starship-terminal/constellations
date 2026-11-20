#!/usr/bin/env python3
"""The Metaview token file still matches the raw readings, and the measured roles resolve."""
import json
import pathlib
import re
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
MARK = (HERE / "raw" / "marketing-root.css").read_text()
APP = json.loads((HERE / "raw" / "app-vars.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


class Tokens(unittest.TestCase):
    def test_marketing_page_colour_is_the_declared_one(self):
        declared = re.search(r"--mv-color-background:([^;]+)", MARK).group(1)
        self.assertEqual(TOKENS["core"]["color"]["marketing"]["background"]["$value"], declared)

    def test_app_dark_page_matches_the_dark_sheet(self):
        self.assertEqual(APP["dark"]["--mv-ui1"], "#050606")
        self.assertEqual(TOKENS["dark"]["color"]["ui"]["1"]["$value"], "#050606")

    def test_every_token_names_a_source(self):
        missing = [name for name, token in flat(TOKENS) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_radius_pill_is_a_length(self):
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$value"], "999px")
        self.assertEqual(TOKENS["core"]["radius"]["pill"]["$type"], "dimension")


class Builder(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        sys.path.insert(0, str(HERE / "tools"))
        import build_tokens  # writes only when run as a script
        self.assertEqual((HERE / "tokens.json").read_text(), build_tokens.text)

    def test_unread_app_values_are_not_measured(self):
        for role in ("appHeading", "appControl", "appField"):
            self.assertTrue(TOKENS["core"]["typography"][role]["$extensions"]["source"].startswith("Reconstruction"), role)


if __name__ == "__main__":
    unittest.main()
