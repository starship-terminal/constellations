"""Checks for the Unsplash token file."""
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokenCheck(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_missing_source_fails(self):
        doc = {"core": {"color": {"ink": {"$type": "color", "$value": "#111111"}}}}
        with self.assertRaises(build_tokens.CheckError):
            build_tokens.check(doc)

    def test_unread_measured_colour_fails(self):
        doc = json.loads(TOKENS.read_text())
        doc["core"]["color"]["black"]["$value"] = "#123456"
        with self.assertRaisesRegex(build_tokens.CheckError, "in no raw"):
            build_tokens.check(doc)

    def test_alias_that_resolves_nowhere_fails(self):
        doc = json.loads(TOKENS.read_text())
        doc["dark"]["color"]["text"]["primary"]["$value"] = "{color.nowhere}"
        with self.assertRaisesRegex(build_tokens.CheckError, "missing alias color.nowhere"):
            build_tokens.check(doc)


    def test_alpha_only_change_fails(self):
        doc = json.loads(TOKENS.read_text())
        doc["core"]["color"]["borderOpacity"]["$value"] = "#00000080"  # raw holds #0000001f
        with self.assertRaisesRegex(build_tokens.CheckError, "in no raw"):
            build_tokens.check(doc)

    def test_core_alias_to_a_theme_only_name_fails(self):
        # Core resolves in core, then the root; a name only the themes hold is not reachable from it.
        doc = json.loads(TOKENS.read_text())
        doc["core"]["color"]["black"]["$value"] = "{color.text.primary}"
        with self.assertRaisesRegex(build_tokens.CheckError, "missing alias color.text.primary"):
            build_tokens.check(doc)

if __name__ == "__main__":
    unittest.main()
