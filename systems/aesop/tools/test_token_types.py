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


def first_typography_node(node):
    if isinstance(node, dict):
        for ty, val in (("$type", "$value"), ("type", "value")):
            if node.get(ty) == "typography" and isinstance(node.get(val), dict):
                return node
        for v in node.values():
            hit = first_typography_node(v)
            if hit:
                return hit
    return None


def first_path(node, want, prefix=""):
    """The dotted path of the first leaf of type `want` in a spec tree."""
    if isinstance(node, dict):
        if (node.get("$type") or node.get("type")) == want and ("$value" in node or "value" in node):
            return prefix
        for k, v in node.items():
            if k.startswith("_") or k.startswith("$"):
                continue
            hit = first_path(v, want, f"{prefix}.{k}" if prefix else k)
            if hit:
                return hit
    return None


class TokenTypesTest(unittest.TestCase):
    def build(self, mutate=None):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__", "screenshots", "components"))
            # Remove the committed output from the copy first, so a builder that
            # writes nothing cannot pass by leaving the committed file in place.
            (copy / "tokens.json").unlink()
            if mutate:
                spec_path = copy / "raw" / "component-tokens.json"
                spec = json.loads(spec_path.read_text())
                mutate(spec)
                spec_path.write_text(json.dumps(spec))
            run = subprocess.run([sys.executable, str(copy / "tools" / "build_tokens.py")], capture_output=True, text=True)
            built = (copy / "tokens.json").read_text() if run.returncode == 0 and (copy / "tokens.json").exists() else None
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


    def test_font_family_must_be_names(self):
        def mutate(spec):
            first_typography(spec)["fontFamily"] = 42
        run, _ = self.build(mutate)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("fontFamily", run.stderr)

    def test_whole_value_alias_must_match_type(self):
        # a typography token whose whole value aliases a colour is refused
        def mutate(spec):
            colour = first_path(spec["core"], "color")
            node = first_typography_node(spec)
            node["$value" if "$value" in node else "value"] = "{" + colour + "}"
        run, _ = self.build(mutate)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("is a color", run.stderr)

    def test_bad_line_height_is_refused(self):
        def mutate(spec):
            first_typography(spec)["lineHeight"] = "big"
        run, _ = self.build(mutate)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("lineHeight", run.stderr)

    def test_line_height_alias_must_be_a_number_or_dimension(self):
        def mutate(spec):
            first_typography(spec)["lineHeight"] = "{" + first_path(spec["core"], "color") + "}"
        run, _ = self.build(mutate)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("lineHeight", run.stderr)
        self.assertIn("is a color", run.stderr)

    def test_line_height_forms_are_accepted(self):
        for good in (1.5, "150%", "24px"):
            with self.subTest(lineHeight=good):
                def mutate(spec, good=good):
                    first_typography(spec)["lineHeight"] = good
                run, built = self.build(mutate)
                self.assertEqual(run.returncode, 0, run.stderr)


if __name__ == "__main__":
    unittest.main()
