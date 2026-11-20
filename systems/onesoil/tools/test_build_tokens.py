"""Checks for the OneSoil token file. Run from tools/: python3 -m unittest test_build_tokens."""
import copy
import json
import pathlib
import subprocess
import sys
import unittest

import build_tokens

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


HERE = pathlib.Path(__file__).resolve().parent
DOC = json.loads(TOKENS.read_text())


class CheckTest(unittest.TestCase):
    def test_committed_tokens_pass(self):
        build_tokens.check(copy.deepcopy(DOC))
        build_tokens.check_against_raw(copy.deepcopy(DOC))

    def test_missing_alias_inside_a_typography_style_fails(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["typography"]["display"]["$value"]["fontWeight"] = "{fontWeight.doesNotExist}"
        with self.assertRaisesRegex(build_tokens.CheckError, "doesNotExist"):
            build_tokens.check(doc)

    def test_missing_top_level_alias_fails(self):
        doc = copy.deepcopy(DOC)
        key = next(iter(doc["light"]))
        node = doc["light"][key]
        while "$value" not in node:
            node = node[next(k for k in node if not k.startswith("$"))]
        node["$value"] = "{color.nothing}"
        with self.assertRaisesRegex(build_tokens.CheckError, "nothing"):
            build_tokens.check(doc)

    def test_theme_keys_must_match(self):
        doc = copy.deepcopy(DOC)
        doc["dark"] = copy.deepcopy(doc["light"])
        doc["dark"]["extra"] = {"$type": "color", "$value": "#000000",
                                "$extensions": {"source": {"evidence": "Measured", "capture": "fixture"}}}
        with self.assertRaisesRegex(build_tokens.CheckError, "keys differ"):
            build_tokens.check(doc)

    def test_a_measured_value_raw_does_not_hold_fails(self):
        doc = copy.deepcopy(DOC)
        doc["core"]["typography"]["display"]["$extensions"]["source"]["evidence"] = "Measured"
        with self.assertRaisesRegex(build_tokens.CheckError, "in no raw/ reading"):
            build_tokens.check_against_raw(doc)

    def test_the_check_still_runs_under_python_O(self):
        code = ("import sys, build_tokens\n"
                "doc = {'core': {'c': {'$type': 'color', '$value': '#fff', '$extensions': {}}}}\n"
                "try:\n build_tokens.check(doc)\nexcept build_tokens.CheckError as e:\n print(e); sys.exit(3)")
        done = subprocess.run([sys.executable, "-O", "-c", code], cwd=HERE, capture_output=True, text=True)
        self.assertEqual(done.returncode, 3, done.stderr)
        self.assertIn("no source", done.stdout)

    def test_light_only(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("light", doc)
        self.assertNotIn("dark", doc)

    def test_measured_accent(self):
        doc = json.loads(TOKENS.read_text())
        self.assertEqual(doc["core"]["color"]["accent"]["$value"], "#27AE60")
        self.assertEqual(doc["core"]["color"]["page"]["$value"], "#F6F4EF")
