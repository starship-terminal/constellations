"""build_tokens.check() runs before tokens.json is written and refuses a broken file (finding 16-6)."""
import copy
import json
import pathlib
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def first_literal_colour(doc):
    for set_name in [k for k in doc if not k.startswith("$") and isinstance(doc[k], dict)]:
        for path, token in build_tokens._token_paths(doc[set_name]):
            if token["$type"] == "color" and not str(token["$value"]).startswith("{"):
                return token


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_rgba_colour_is_refused(self):
        doc = json.loads(TOKENS.read_text())
        first_literal_colour(doc)["$value"] = "rgba(0, 0, 0, 0.5)"
        with self.assertRaisesRegex(SystemExit, "not #rrggbb"):
            build_tokens.check(doc)

    def test_dangling_alias_and_missing_source_are_refused(self):
        doc = json.loads(TOKENS.read_text())
        token = first_literal_colour(doc)
        bad = copy.deepcopy(doc)
        first_literal_colour(bad)["$value"] = "{color.does-not-exist}"
        with self.assertRaisesRegex(SystemExit, "resolves nowhere"):
            build_tokens.check(bad)
        del token["$extensions"]
        with self.assertRaisesRegex(SystemExit, "no source"):
            build_tokens.check(doc)

    def test_committed_file_matches_builder(self):
        # Built in memory; the committed file is never rewritten by the test.
        self.assertEqual(json.loads(TOKENS.read_text()), build_tokens.build())

    def test_unparsed_colour_raises_instead_of_passing_through(self):
        with self.assertRaises(ValueError):
            build_tokens.as_color("var(--tux-colorConstTextInverse)")
        self.assertEqual(build_tokens.as_color("rgba(255, 255, 255, 0.5)"), "#ffffff80")

    def test_close_radius_is_one_length(self):
        self.assertEqual(json.loads(TOKENS.read_text())["core"]["radius"]["close"]["$value"], "16px")


if __name__ == "__main__":
    unittest.main()
