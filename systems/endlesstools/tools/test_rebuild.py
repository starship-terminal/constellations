"""Rebuild checks for the Endless Tools builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ (without capture/) and raw/, with
empty stand-ins for the screenshot and crop files (only their names are read),
so nothing committed is rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def flat(tree, path=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def builder_fn(name, end, first=None):
    """A helper from the token builder, loaded without running the build
    (the source from `def first` or `def name` up to `end`)."""
    src = (PKG / "tools" / "build_component_tokens.py").read_text()
    start = src.index(f"def {first or name}(")
    ns = {"re": re}
    exec(src[start:src.index(end, start)], ns)
    return ns[name]


norm = builder_fn("norm_color", "\ndef have(")


def tok_norm(v):
    """build_tokens.py's colour normaliser (converts oklab/oklch)."""
    src = (PKG / "tools" / "build_tokens.py").read_text()
    ns = {"re": re}
    exec(src[src.index("def _lin("):src.index("\nDIM = ")], ns)
    return ns["norm_color"](v)
MEASURED = re.compile(r"^(computed|measured) (\w+) of ([\w-]+) ([\w-]+)[ ;(]")


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components/crops"):
            (root / d).mkdir(parents=True)
            for f in (PKG / d).glob("*.png"):
                (root / d / f.name).touch()
        for b in ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.root = root
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def resolve(self, theme, v):
        while isinstance(v, str) and v.startswith("{"):
            node = None
            for s in (theme, "core"):
                node = self.built[s]
                for part in v[1:-1].split("."):
                    node = node.get(part) if isinstance(node, dict) else None
                if node:
                    break
            v = node["$value"]
        return v

    def test_committed_output_matches_rebuild(self):
        for f in ("tokens.json", "raw/component-tokens.json", "components.md", "style-guide.html"):
            self.assertEqual((PKG / f).read_text(), (self.root / f).read_text(), f)

    def test_measured_leaves_equal_their_reading(self):
        checked = 0
        for theme in ("core", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = MEASURED.match((leaf.get("$extensions") or {}).get("source", ""))
                if not m or m.group(2) == "transition":
                    continue
                kind, prop, comp, state = m.groups()
                if comp not in self.C:
                    continue  # "of every measured component": the builder checks there is one stack
                rd = self.C[comp]["states"][state]
                if kind == "measured":
                    raw = "%gpx" % rd["rect"][prop]
                else:
                    # The builder reads the first text node only where the source says so.
                    first = "first text node" in leaf["$extensions"]["source"]
                    raw = ((rd.get("textStyle") or {}).get(prop) if first else None) or rd["style"][prop]
                got = self.resolve(theme, leaf["$value"])
                if leaf["$type"] == "color":
                    self.assertEqual(got, tok_norm(raw), path)
                elif prop == "fontWeight":
                    self.assertEqual(got, int(float(raw)), path)
                elif str(got).endswith("px") and raw.endswith("px"):
                    self.assertAlmostEqual(float(str(got)[:-2]), float(raw[:-2]), places=2, msg=path)
                else:
                    self.assertEqual(str(got), raw, path)
                checked += 1
        self.assertGreater(checked, 35)

    def test_no_colour_is_left_in_oklab(self):
        authored = 0
        for theme in ("core", "dark"):
            for path, leaf in flat(self.built[theme]):
                if leaf["$type"] == "color":
                    self.assertNotRegex(str(leaf["$value"]), r"^(ok)?l(ab|ch)\(", path)
                    authored += "authored" in leaf["$extensions"]
        self.assertEqual(authored, 6)
        self.assertEqual(self.built["core"]["color"]["neutral"]["alpha"]["black-50"]["$value"], "rgba(10, 10, 10, 0.5)")

    def test_painted_literals_are_read_from_their_components(self):
        n = self.built["core"]["color"]["neutral"]
        self.assertEqual(n["ring"]["$value"], "#222222")
        self.assertIn("rgb(34, 34, 34) 0px 0px 0px 1px inset", self.C["plan-card"]["states"]["default"]["style"]["boxShadow"])
        body = next(a["bg"] for a in self.C["header"]["states"]["default"]["ancestors"] if a["node"].startswith("body"))
        self.assertEqual(n["page"]["$value"], tok_norm(body))
        self.assertEqual(n["alpha"]["placeholder-50"]["$value"], tok_norm(self.C["news-field"]["states"]["default"]["placeholder"]["color"]))
        sheets = json.loads((PKG / "raw" / "components-computed.json").read_text())["_meta"]["sheets"]
        spin = next(r for r in sheets["login"] if r["selector"] == ".animate-spin")
        self.assertEqual(self.built["core"]["motion"]["animation"]["spin"]["$value"], spin["animation"])

    def test_values_without_a_reading_say_so(self):
        self.assertTrue(self.built["core"]["gradient"]["overlay"]["$extensions"]["source"].startswith("entered by hand"))
        self.assertIn("outline-style auto", self.built["core"]["color"]["accent"]["focus"]["$extensions"]["source"])

    def test_focus_summary_counts_only_real_rings(self):
        md = (PKG / "components.md").read_text()
        focus = next(l for l in md.splitlines() if l.startswith("**Focus.**"))
        self.assertNotIn("draw an outline ring", focus)  # every 2px outline is transparent
        self.assertIn("Focus could not be captured on `billing-yearly`", focus)
        self.assertNotIn("`billing-yearly`", focus.split("Focus could not be captured", 1)[0])
        entry = md.split("Read as `billing-yearly`", 1)[1].split("\n#### ", 1)[0]
        self.assertNotIn("focus-visible", entry.split("**Focus not capturable.**", 1)[0])

    def run_on_changed_copy(self, change):
        """Run the token builder on a temp copy whose raw files `change` edits;
        return the result and whether the spec file was left as it was."""
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            change(root / "raw")
            before = (root / "raw" / "component-tokens.json").read_text()
            r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, capture_output=True, text=True)
            return r, (root / "raw" / "component-tokens.json").read_text() == before

    @staticmethod
    def edit(path, fn):
        j = json.loads(path.read_text())
        fn(j)
        path.write_text(json.dumps(j))

    def test_missing_reading_stops_the_build(self):
        drop_var = lambda raw: self.edit(raw / "css-vars.json", lambda j: j["resolved"]["dark"].pop("--radius-base"))
        drop_comp = lambda raw: self.edit(raw / "components-computed.json", lambda j: j["components"].pop("asset-thumb"))
        for name, change in (("declared var", drop_var), ("component", drop_comp)):
            r, kept = self.run_on_changed_copy(change)
            self.assertNotEqual(r.returncode, 0, name)
            self.assertIn("missing readings", r.stderr, name)
            self.assertTrue(kept, name)

    def test_disagreeing_readings_stop_the_build(self):
        def change(raw):
            self.edit(raw / "components-computed.json",
                      lambda j: j["components"]["edu-cta"]["states"]["default"]["style"].update(backgroundColor="rgb(1, 2, 3)"))
        r, kept = self.run_on_changed_copy(change)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("disagree", r.stderr)
        self.assertTrue(kept)

    def test_no_named_row_was_dropped(self):
        self.assertNotIn("_gaps", self.spec)


if __name__ == "__main__":
    unittest.main()
