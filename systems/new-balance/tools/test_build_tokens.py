"""build_tokens.check() and check_against_raw() pass the committed tokens.json and refuse a broken one.

tokens.json is written by hand for this package, so these checks are what keeps it honest: every alias
resolves, every token names a source, colours are hex, and a token labelled Measured carries a value raw/
holds. Nothing here writes a file."""
import copy
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_tokens  # noqa: E402

TOKENS = HERE.parent / "tokens.json"
DOC = json.loads(TOKENS.read_text())


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(copy.deepcopy(DOC))
        build_tokens.check_against_raw(copy.deepcopy(DOC))

    def test_missing_alias_fails(self):
        doc = copy.deepcopy(DOC)
        doc["light"]["text"]["primary"]["$value"] = "{color.missing}"
        with self.assertRaisesRegex(build_tokens.CheckError, "missing"):
            build_tokens.check(doc)

    def test_missing_alias_inside_a_typography_style_fails(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["typography"]["body"]["$value"]["fontWeight"] = "{fontWeight.doesNotExist}"
        with self.assertRaisesRegex(build_tokens.CheckError, "doesNotExist"):
            build_tokens.check(doc)

    def test_a_token_without_a_source_fails(self):
        doc = copy.deepcopy(DOC)
        doc["light"]["text"]["primary"]["$extensions"] = {}
        with self.assertRaisesRegex(build_tokens.CheckError, "no source"):
            build_tokens.check(doc)

    def test_a_non_hex_colour_fails(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["color"]["ink"]["$value"] = "rgb(21, 20, 21)"
        with self.assertRaisesRegex(build_tokens.CheckError, "not #rrggbb"):
            build_tokens.check(doc)

    def test_a_measured_value_raw_does_not_hold_fails(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["color"]["ink"]["$value"] = "#123456"
        with self.assertRaisesRegex(build_tokens.CheckError, "in no raw/ reading"):
            build_tokens.check_against_raw(doc)

    def test_a_literal_font_inside_a_typography_value_is_checked(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["typography"]["body"]["$value"]["fontFamily"] = "Unrecorded Example Font"
        with self.assertRaisesRegex(build_tokens.CheckError, "font stack"):
            build_tokens.check_against_raw(doc)

    def test_the_field_line_height_is_not_labelled_measured(self):
        # 23px rounds a 22.8576px reading that raw/ does not hold
        doc = copy.deepcopy(DOC)
        self.assertTrue(doc["core"]["typography"]["field"]["$extensions"]["source"].startswith("Reconstruction"))
        doc["core"]["typography"]["field"]["$extensions"]["source"] = "Measured line-height"
        with self.assertRaisesRegex(build_tokens.CheckError, "23px"):
            build_tokens.check_against_raw(doc)

    def test_the_check_still_runs_under_python_O(self):
        code = ("import sys, build_tokens\n"
                "doc = {'core': {'c': {'$type': 'color', '$value': '{nope}', '$extensions': {'source': 'Measured x'}}}, 'light': {}}\n"
                "try:\n build_tokens.check(doc)\nexcept build_tokens.CheckError as e:\n print(e); sys.exit(3)")
        done = subprocess.run([sys.executable, "-O", "-c", code], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(done.returncode, 3, done.stderr)
        self.assertIn("points at nothing", done.stdout)


if __name__ == "__main__":
    unittest.main()
