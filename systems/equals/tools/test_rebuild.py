"""Rebuild checks for the Equals builders. Run from this folder, or via tools/package_tests.py.

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
COMPUTED = re.compile(r"^computed (\w+) of (\S+) (\S+) \(raw/components-computed\.json\)")


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    MOTION_FROM = "hero-cta"  # the reading core.motion.control is built from

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
        spec = importlib.util.spec_from_file_location("equals_bct", root / "tools" / "build_component_tokens.py")
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

    def test_computed_colour_leaves_equal_the_reading(self):
        n = 0
        for theme in ("light", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = COMPUTED.match(leaf["$extensions"]["source"])
                if not m or leaf["$type"] != "color":
                    continue
                prop, comp, state = m.groups()
                raw = self.C[comp]["states"][state]["style"][prop]
                self.assertEqual(self.resolve(leaf["$value"]), self.B.css_color(raw), f"{theme}.{path}")
                n += 1
        self.assertGreater(n, 20)

    def test_no_surface_is_transparent(self):
        for theme in ("light", "dark"):
            for path, leaf in flat(self.built[theme]):
                if leaf["$type"] == "color":
                    self.assertFalse(self.B.transparent(self.resolve(leaf["$value"])), f"{theme}.{path}")
        gaps = {g["token"] for g in self.spec["_gaps"]}
        for t in ("light.signin.card", "light.marketing.focus"):
            self.assertIn(t, gaps)

    def test_focus_rings_are_painted_rings(self):
        # the docs search draws a 1px auto outline in the product primary: that colour is painted
        for theme, comp in (("light", "docs-search"), ("dark", "d-docs-search")):
            sty = self.C[comp]["states"]["focus-visible"]["style"]
            self.assertEqual(self.resolve(self.built[theme]["docs"]["focus"]["$value"]), self.B.css_color(sty["outlineColor"]))
        # the marketing links draw the browser's default ring, so no product colour is published
        self.assertNotIn("focus", self.built["light"]["marketing"])

    def test_transition_pairs_each_property_with_its_timing(self):
        t = self.B.transition
        # one timing for several properties: it repeats to every property
        self.assertEqual(t({"transitionProperty": "color, background-color", "transitionDuration": "0.15s",
                            "transitionTimingFunction": "ease-out"}),
                         "color 0.15s ease-out, background-color 0.15s ease-out")
        # per-property timings pair by index
        self.assertEqual(t({"transitionProperty": "opacity, transform", "transitionDuration": "0.1s, 0.3s",
                            "transitionTimingFunction": "linear, cubic-bezier(0.2, 0, 0, 1)"}),
                         "opacity 0.1s linear, transform 0.3s cubic-bezier(0.2, 0, 0, 1)")
        # shorter timing lists repeat from the start, as CSS repeats them
        self.assertEqual(t({"transitionProperty": "a, b, c", "transitionDuration": "1s, 2s",
                            "transitionTimingFunction": "ease"}),
                         "a 1s ease, b 2s ease, c 1s ease")
        # and the committed token is that pairing of its own reading
        comp = self.MOTION_FROM
        self.assertEqual(self.core["motion.control"]["$value"], t(self.C[comp]["states"]["default"]["style"]))

    def test_font_sizes_are_dimensions(self):
        for path, leaf in flat(self.built["core"]["font"]["size"]):
            self.assertEqual(leaf["$type"], "dimension", path)

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
            names |= {f"{theme}.{n}" for n, _ in flat(self.built[theme])}
        for doc in ("patterns.md", "components.md"):
            for m in set(re.findall(r"`((?:core|light|dark)\.[A-Za-z0-9._-]+)`", (PKG / doc).read_text())):
                self.assertTrue(m in names or any(n.startswith(m + ".") for n in names), f"{doc} cites {m}")


if __name__ == "__main__":
    unittest.main()
