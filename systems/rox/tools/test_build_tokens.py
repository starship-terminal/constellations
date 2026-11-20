"""Tests for build_tokens.check. Run: python3 -m unittest discover -s tools (from this package).

The fixture below is the smallest token file check() reads, so these tests hold for any product's
mapping. test_committed_tokens_pass runs the check on the package's own tokens.json."""
import copy
import json
import pathlib
import sys
import unittest

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_tokens  # noqa: E402

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
SRC = {"$extensions": {"source": {"evidence": "Sampled", "capture": "dark/01-home"}}}


def tok(type_, value):
    return {"$type": type_, "$value": value, **copy.deepcopy(SRC)}


def theme(page):
    return {"color": {"bg": {"page": tok("color", page)}, "text": {"primary": tok("color", "{color.neutral.0}")}}}


FIXTURE = {
    "core": {
        "color": {"neutral": {"0": tok("color", "#FFFFFF")}},
        "fontWeight": {"regular": tok("fontWeight", 400)},
        "typography": {"body": tok("typography", {"fontWeight": "{fontWeight.regular}", "fontSize": "17px"})},
    },
    "light": theme("#FCFCFC"),
    "dark": theme("#141414"),
}


class CheckTest(unittest.TestCase):
    @unittest.skipUnless(TOKENS.exists(), "no tokens.json yet (kit copy)")
    def test_committed_tokens_pass(self):
        build_tokens.check(json.loads(TOKENS.read_text()))

    def test_fixture_passes(self):
        build_tokens.check(copy.deepcopy(FIXTURE))

    def test_one_theme_passes(self):
        doc = copy.deepcopy(FIXTURE)
        del doc["dark"]
        build_tokens.check(doc)

    def test_missing_alias_inside_a_typography_style_fails(self):
        doc = copy.deepcopy(FIXTURE)
        doc["core"]["typography"]["body"]["$value"]["fontWeight"] = "{fontWeight.doesNotExist}"
        with self.assertRaisesRegex(AssertionError, "doesNotExist"):
            build_tokens.check(doc)

    def test_missing_top_level_alias_fails(self):
        doc = copy.deepcopy(FIXTURE)
        doc["light"]["color"]["text"]["primary"]["$value"] = "{color.accent.nothing}"
        with self.assertRaisesRegex(AssertionError, "nothing"):
            build_tokens.check(doc)

    def test_theme_keys_must_match(self):
        doc = copy.deepcopy(FIXTURE)
        doc["dark"]["color"]["bg"]["sheet"] = tok("color", "#1E1E1E")
        with self.assertRaisesRegex(AssertionError, "keys differ"):
            build_tokens.check(doc)

    def test_the_check_still_runs_under_python_O(self):
        # `assert` is stripped by -O; check() must reject a bad file either way.
        import subprocess
        code = ("import sys, build_tokens; doc = {'core': {'c': {'$type': 'color', '$value': '#fff'}}}\n"
                "try:\n build_tokens.check(doc)\nexcept build_tokens.CheckError as e:\n print(e); sys.exit(3)")
        done = subprocess.run([sys.executable, "-O", "-c", code], cwd=pathlib.Path(__file__).resolve().parent,
                              capture_output=True, text=True)
        self.assertEqual(done.returncode, 3, done.stderr)
        self.assertIn("no source", done.stdout)



class Provenance(unittest.TestCase):
    def test_committed_tokens_match_build(self):
        self.assertEqual(json.loads(TOKENS.read_text()), json.loads(json.dumps(build_tokens.build())))

    def test_unread_colours_say_reconstruction(self):
        color = json.loads(TOKENS.read_text())["core"]["color"]
        for name in ("blue", "green", "red", "orange"):
            self.assertTrue(color[name]["$extensions"]["source"].startswith("Reconstruction"), name)

if __name__ == "__main__":
    unittest.main()
