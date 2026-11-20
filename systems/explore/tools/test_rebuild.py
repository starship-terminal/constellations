"""Rebuild checks for the Explore builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/, so nothing committed is rewritten.
"""
import contextlib
import importlib.util
import io
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
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        # raw/measurements.md comes from the capture folder's build-measurements.mjs; copy only it
        # and the colour helper it imports, and run it on the temp copy.
        cls.measurements = None
        if shutil.which("node"):
            (root / "tools" / "capture" / "public").mkdir(parents=True)
            shutil.copy(PKG / "tools" / "capture" / "css-colour.mjs", root / "tools" / "capture")
            shutil.copy(PKG / "tools" / "capture" / "public" / "build-measurements.mjs", root / "tools" / "capture" / "public")
            subprocess.run(["node", str(root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                           cwd=root, check=True, capture_output=True)
            cls.measurements = (root / "raw" / "measurements.md").read_text()
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        spec = importlib.util.spec_from_file_location("explore_bct", root / "tools" / "build_component_tokens.py")
        cls.B = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(cls.B)  # re-runs the builder inside the temp copy
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        cls.core = dict(flat(cls.built["core"]))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def resolve(self, v):
        while isinstance(v, str) and v.startswith("{"):
            v = self.core[v[1:-1]]["$value"]
        return v

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_every_leaf_names_raw_evidence(self):
        """Each colour picked from the sheet is still declared there, each measured geometry leaf
        equals its rect, and the hand-entered ones say so."""
        decl = json.loads((PKG / "raw" / "css-declarations.json").read_text())
        values = {v for d in decl["declarations"] for v in d["properties"].values()}
        n = 0
        for path, leaf in flat({k: self.built[k] for k in ("core", "light")}):
            src, val = leaf["$extensions"]["source"], leaf["$value"]
            m = re.match(r"measured (\S+) (\S+) rect\.([wh]) \(raw/components-computed\.json\)", src)
            if m:
                comp, state, k = m.groups()
                self.assertEqual(val, "%gpx" % self.C[comp]["states"][state]["rect"][k], path)
                n += 1
            elif src.startswith("stylesheet declaration") and leaf["$type"] == "color" and not str(val).startswith("{"):
                form = self.B.cssom(self.spec_value(path), "color")
                self.assertTrue(any(form in v for v in values), path)
                n += 1
        self.assertGreater(n, 40)
        self.assertTrue(self.built["core"]["zIndex"]["modal"]["$extensions"]["source"].startswith("Reconstruction:"))
        self.assertEqual(self.built["core"]["font"]["lineHeight"]["tight"]["$value"], 41 / 40)

    def spec_value(self, path):
        node = self.spec
        for part in path.split("."):
            node = node[part]
        return node["value"]

    def test_builder_stops_on_a_value_the_sheet_no_longer_declares(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            decl = json.loads((root / "raw" / "css-declarations.json").read_text())
            for d in decl["declarations"]:
                for p, v in d["properties"].items():
                    d["properties"][p] = v.replace("rgb(255, 198, 10)", "rgb(1, 2, 3)")  # the brand yellow
            (root / "raw" / "css-declarations.json").write_text(json.dumps(decl))
            r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("#ffc60a", r.stderr)

    def test_failed_focus_is_not_published_as_a_reading(self):
        """An older capture saved a failed keyboard focus as the element at rest with via 'focus
        failed'; build-measurements.mjs must show it as Skipped, with no values. The record is made
        here on a temp copy, so the test does not depend on what the committed capture holds."""
        if self.measurements is None:
            self.skipTest("node is not installed")
        self.assertEqual((PKG / "raw" / "measurements.md").read_text(), self.measurements)
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(pathlib.Path(self.tmp.name) / "tools", root / "tools")
            shutil.copytree(PKG / "raw", root / "raw")
            raw = json.loads((root / "raw" / "components-computed.json").read_text())
            k = next(k for k, c in raw["components"].items() if "style" in (c["states"].get("focus-visible") or {}))
            st = raw["components"][k]["states"]["focus-visible"]
            raw["components"][k]["states"]["focus-visible"] = {**st, "via": "focus failed"}
            (root / "raw" / "components-computed.json").write_text(json.dumps(raw))
            subprocess.run(["node", str(root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                           cwd=root, check=True, capture_output=True)
            md = (root / "raw" / "measurements.md").read_text()
        block = md.split(f"#### {k}\n", 1)[1].split("\n#### ", 1)[0]
        cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]  # noqa: E731
        table = [cells(r) for r in block.splitlines() if r.startswith("| ") and not r.startswith("|---")]
        col = table[0].index("focus-visible")
        self.assertIn("Skipped", [row[0] for row in table[1:]])
        for row in table[1:]:
            if row[0] == "Skipped":
                self.assertTrue(row[col].startswith("focus failed"), k)
            else:
                # "-" (no value), or "=" where the first state has no value either
                self.assertIn(row[col], ("-", "=") if row[1] == "-" else ("-",), f"{k}: {row}")

    def test_skipped_focus_keeps_its_note(self):
        """A newer capture records a failed focus as {skipped, via} with no style; components.md still
        lists it among the controls focus could not be moved onto, and leaves it out of the tables."""
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(pathlib.Path(self.tmp.name) / "tools", root / "tools", ignore=shutil.ignore_patterns("capture"))
            shutil.copytree(PKG / "raw", root / "raw")
            shutil.copy(PKG / "tokens.json", root / "tokens.json")
            raw = json.loads((root / "raw" / "components-computed.json").read_text())
            k = next(k for k, c in raw["components"].items() if "style" in (c["states"].get("focus-visible") or {}))
            raw["components"][k]["states"]["focus-visible"] = {
                "skipped": "focus failed: keyboard focus did not reach the element", "via": "focus failed"}
            (root / "raw" / "components-computed.json").write_text(json.dumps(raw))
            subprocess.run([sys.executable, str(root / "tools" / "build_components_md.py")], cwd=root, check=True, capture_output=True)
            md = (root / "components.md").read_text()
            focus = next(line for line in md.splitlines() if line.startswith("**Focus.**"))
            self.assertIn(f"`{k}`", focus.split("Focus could not be moved onto", 1)[1])
        committed = (PKG / "components.md").read_text()
        for k, c in self.C.items():
            if (c["states"].get("focus-visible") or {}).get("via") == "focus failed":
                block = committed.split(f"Read as `{k}`", 1)[1].split("\n#### ", 1)[0]
                self.assertNotIn("focus-visible", block, k)

    def test_an_error_only_focus_record_does_not_break_the_build(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(pathlib.Path(self.tmp.name) / "tools", root / "tools", ignore=shutil.ignore_patterns("capture"))
            shutil.copytree(PKG / "raw", root / "raw")
            shutil.copy(PKG / "tokens.json", root / "tokens.json")
            raw = json.loads((root / "raw" / "components-computed.json").read_text())
            k = next(k for k, c in raw["components"].items() if "style" in (c["states"].get("focus-visible") or {}))
            raw["components"][k]["states"]["focus-visible"] = {"error": "focus attempt threw"}
            (root / "raw" / "components-computed.json").write_text(json.dumps(raw))
            r = subprocess.run([sys.executable, str(root / "tools" / "build_components_md.py")], cwd=root, capture_output=True, text=True)
            self.assertEqual(r.returncode, 0, r.stderr[-400:])

    def test_docs_cite_only_existing_tokens(self):
        names = set()
        for theme in ("core", "light", "dark"):
            names |= {f"{theme}.{n}" for n, _ in flat(self.built.get(theme, {}))}
        for doc in ("patterns.md", "components.md"):
            for m in set(re.findall(r"`((?:core|light|dark)\.[A-Za-z0-9._-]+)`", (PKG / doc).read_text())):
                self.assertTrue(m in names or any(n.startswith(m + ".") for n in names), f"{doc} cites {m}")


if __name__ == "__main__":
    unittest.main()
