"""tokens.json must rebuild from raw/component-tokens.json, and the builder must refuse a composite
token (one passed through as a ready $value) whose parts are not their DTCG type. The builder runs
on a temporary copy of the package, so nothing committed is rewritten."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def first_typography(node):
    """The value dict of the first typography composite, in either spec form."""
    if isinstance(node, dict):
        for ty, val in (("$type", "$value"), ("type", "value")):
            if node.get(ty) == "typography" and isinstance(node.get(val), dict):
                return node[val]
        for v in node.values():
            hit = first_typography(v)
            if hit:
                return hit
    return None


class TokenTypesTest(unittest.TestCase):
    def build(self, mutate=None):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__", "screenshots", "components"))
            if mutate:
                spec_path = copy / "raw" / "component-tokens.json"
                spec = json.loads(spec_path.read_text())
                mutate(spec)
                spec_path.write_text(json.dumps(spec))
            run = subprocess.run([sys.executable, str(copy / "tools" / "build_tokens.py")], capture_output=True, text=True)
            built = (copy / "tokens.json").read_text() if run.returncode == 0 else None
            return run, built

    def test_tokens_match_committed(self):
        run, built = self.build()
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(built, (PKG / "tokens.json").read_text())

    def test_bad_composite_part_is_refused(self):
        def mutate(spec):
            first_typography(spec)["fontSize"] = "big"
        run, _ = self.build(mutate)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("fontSize", run.stderr)


if __name__ == "__main__":
    unittest.main()
