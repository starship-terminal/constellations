"""check() under python3 -O: each of its five rules must still reject a bad tokens.json, since -O
strips assert statements. Run: python3 -m unittest discover -s tools."""
import ast
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
RUN = ("import json, sys, build_tokens\n"
       "try:\n build_tokens.check(json.load(sys.stdin))\n"
       "except build_tokens.CheckError as e:\n print(e); sys.exit(3)")


def first(doc, typ):
    """The first token of `typ` in core or a theme whose value is a literal, not an alias."""
    for name in ("core", "light", "dark"):
        for p, t in build_tokens.walk(doc.get(name, {})):
            if t["$type"] == typ and isinstance(t["$value"], str) and not t["$value"].startswith("{"):
                return t
    raise unittest.SkipTest(f"no literal {typ} token")


def number(doc):
    """The first fontWeight or number token whose value is a literal number."""
    for name in ("core", "light", "dark"):
        for p, t in build_tokens.walk(doc.get(name, {})):
            if t["$type"] in ("number", "fontWeight") and isinstance(t["$value"], (int, float)):
                return t
    raise unittest.SkipTest("no literal number token")


def bad_docs(doc):
    out = {}
    d = copy.deepcopy(doc); first(d, "color")["$extensions"] = {}; out["no source"] = d
    d = copy.deepcopy(doc); first(d, "color")["$value"] = "{color.nothing.here}"; out["points at nothing"] = d
    d = copy.deepcopy(doc); first(d, "color")["$value"] = "#12345"; out["bad colour"] = d
    d = copy.deepcopy(doc); first(d, "dimension")["$value"] = "12pt"; out["bad dimension"] = d
    d = copy.deepcopy(doc); number(d)["$value"] = "bold"; out["is not a number"] = d
    if "light" in doc and "dark" in doc:
        d = copy.deepcopy(doc); t = first(d, "color")
        d["dark"]["extraForTest"] = copy.deepcopy(t); out["keys differ"] = d
    return out


@unittest.skipUnless(TOKENS.exists(), "no tokens.json yet")
class OptimisedCheckTest(unittest.TestCase):
    def test_every_rule_rejects_under_python_O(self):
        doc = json.loads(TOKENS.read_text())
        for message, bad in bad_docs(doc).items():
            done = subprocess.run([sys.executable, "-O", "-c", RUN], cwd=HERE, input=json.dumps(bad),
                                  capture_output=True, text=True)
            self.assertEqual(done.returncode, 3, f"{message}: {done.stderr[-300:]}")
            self.assertIn(message, done.stdout)

    def test_no_assert_statement_guards_the_build(self):
        # python3 -O strips assert, so every check in build_tokens.py (check(), pixel_check() and the
        # rest) must raise CheckError instead.
        tree = ast.parse((HERE / "build_tokens.py").read_text())
        lines = [n.lineno for n in ast.walk(tree) if isinstance(n, ast.Assert)]
        self.assertEqual(lines, [], "assert statements in build_tokens.py")


if __name__ == "__main__":
    unittest.main()
