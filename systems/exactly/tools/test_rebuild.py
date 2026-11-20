"""Rebuild checks for the exactly.ai builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/, so nothing committed is rewritten.
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
MEASURED = re.compile(r"^measured computed style of (\S+) (\S+) \(raw/components-computed\.json\) · ([\w ]+?)(?:;.*)?$")


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
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        cls.core = dict(flat(cls.built["core"]))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    @staticmethod
    def B_norm(v):
        """rgb()/rgba() as build_tokens.py writes it (#rrggbb when opaque)."""
        m = re.fullmatch(r"rgba?\((\d+), (\d+), (\d+)(?:, ([\d.]+))?\)", v.strip())
        if not m:
            return v.lower()
        r, g, b, a = m.groups()
        return "#%02x%02x%02x" % (int(r), int(g), int(b)) if a is None or float(a) == 1 else f"rgba({r}, {g}, {b}, {a})"

    def resolve(self, v):
        while isinstance(v, str) and v.startswith("{"):
            v = self.core[v[1:-1]]["$value"]
        return v

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_every_measured_leaf_equals_its_reading(self):
        """Every leaf whose source names a computed style carries that reading, so a recapture can
        never leave a typed literal behind a "measured" label."""
        n = 0
        for path, leaf in flat({k: self.built[k] for k in ("core", "light")}):
            m = MEASURED.match(leaf["$extensions"]["source"])
            if not m:
                continue
            comp, state, prop = m.groups()
            st = self.C[comp]["states"][state]
            if prop.startswith("rect "):
                want = ("%g" % round(st["rect"]["h" if "height" in prop else "w"], 2)) + "px"
            else:
                text = st.get("textStyle") or {}
                font = prop in ("fontFamily", "fontSize", "lineHeight", "fontWeight", "letterSpacing", "color")
                want = (text.get(prop) if font else None) or st["style"][prop]
            got = leaf["$value"]
            if leaf["$type"] == "duration" and want.endswith("s") and not want.endswith("ms"):
                want = "%gms" % (float(want[:-1]) * 1000)
            if leaf["$type"] == "fontWeight":
                want = int(want)
            if leaf["$type"] == "color":
                got, want = got.lower(), self.B_norm(want)
            self.assertEqual(got, want, path)
            n += 1
        self.assertGreater(n, 60)

    def test_focus_rings_are_labelled_as_the_browsers(self):
        for k in ("ring", "ring-mobile"):
            self.assertIn("so the browser chose it, not the site", self.built["light"]["focus"][k]["$extensions"]["source"])

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
        """A newer capture records a failed focus as {skipped, via} with no style; components.md
        still has to say focus could not be captured on that component."""
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
            block = md.split(f"Read as `{k}`", 1)[1].split("\n#### ", 1)[0]
            self.assertIn("Focus not capturable", block)

    def test_docs_cite_only_existing_tokens(self):
        names = set()
        for theme in ("core", "light", "dark"):
            names |= {f"{theme}.{n}" for n, _ in flat(self.built.get(theme, {}))}
        for doc in ("patterns.md", "components.md"):
            for m in set(re.findall(r"`((?:core|light|dark)\.[A-Za-z0-9._-]+)`", (PKG / doc).read_text())):
                self.assertTrue(m in names or any(n.startswith(m + ".") for n in names), f"{doc} cites {m}")


if __name__ == "__main__":
    unittest.main()
