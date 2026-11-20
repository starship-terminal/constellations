"""Rebuild checks for the Dona builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots and crops by name only),
so nothing committed is rewritten.
"""
import json
import pathlib
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
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from flat(v, p)


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
        for b in ("build_component_tokens.py", "build_tokens.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.md = (root / "components.md").read_text()
        cls.tok = dict(flat(cls.built))
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def style(self, comp, state="default"):
        return self.C[comp]["states"][state]["style"]

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)
        self.assertEqual((PKG / "components.md").read_text(), self.md)

    def test_dimensions_are_px_or_rem(self):
        for path, leaf in self.tok.items():
            if leaf["$type"] == "dimension" and not str(leaf["$value"]).startswith("{"):
                self.assertRegex(leaf["$value"], r"^-?\d*\.?\d+(px|rem)$", path)
        kept = {e["name"]: e["value"] for e in self.built["core"]["$extensions"]["notTokenised"]}
        self.assertEqual(kept["radius.round"], self.style("modal-close")["borderTopLeftRadius"])
        self.assertEqual(kept["radius.swoosh"], self.C["newsletter"]["states"]["default"]["::before"]["borderRadius"])

    def test_probe_values_without_a_reading_say_so(self):
        for p in ("core.layout.container", "core.layout.gutter", "core.layout.grid-gap"):
            self.assertTrue(self.tok[p]["$extensions"]["source"].startswith("Reconstruction:"), p)
        self.assertEqual(self.tok["core.layout.content"]["$value"], self.style("header")["width"])
        self.assertIn("recapture needed", self.tok["core.shadow.banner-mobile"]["$extensions"]["source"])

    def test_literals_are_read(self):
        self.assertIn("try-cta default", self.tok["light.text.inverse"]["$extensions"]["source"])
        self.assertEqual(self.tok["core.easing.standard"]["$value"],
                         [0.25, 0.1, 0.25, 1] if self.style("cookie-accept")["transitionTimingFunction"].startswith("ease,") else None)

    def test_failed_focus_is_listed_not_measured(self):
        self.assertIn("Focus could not be captured on 2 more", self.md)
        self.assertIn("`logo`, `team-card`", self.md)


    def test_measurements_rebuild_matches(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        root = pathlib.Path(self.tmp.name)
        (root / "tools" / "capture" / "public").mkdir(parents=True, exist_ok=True)
        shutil.copy(PKG / "tools" / "capture" / "css-colour.mjs", root / "tools" / "capture")
        shutil.copy(PKG / "tools" / "capture" / "public" / "build-measurements.mjs", root / "tools" / "capture" / "public")
        subprocess.run([node, str(root / "tools" / "capture" / "public" / "build-measurements.mjs")], cwd=root, check=True, capture_output=True)
        built = (root / "raw" / "measurements.md").read_text()
        self.assertEqual((PKG / "raw" / "measurements.md").read_text(), built)
        # a failed keyboard focus reads Skipped, never the element at rest
        entry = built.split("#### logo\n")[1].split("\n#### ")[0]
        self.assertIn("| Skipped |", entry)

    def test_incomplete_capture_still_builds(self):
        # A missing component or a function-valued easing must not stop the rebuild.
        with tempfile.TemporaryDirectory() as d:
            root = pathlib.Path(d)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            f = root / "raw" / "components-computed.json"
            j = json.loads(f.read_text())
            j["components"]["modal-close"] = {"missing": True, "states": {}, "page": "home", "title": "x", "group": "x"}
            j["components"]["cookie-accept"]["states"]["default"]["style"]["transitionTimingFunction"] = "cubic-bezier(0.4, 0, 0.2, 1), cubic-bezier(0.4, 0, 0.2, 1)"
            f.write_text(json.dumps(j))
            for b in ("build_component_tokens.py", "build_tokens.py"):
                subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
            out = json.loads((root / "tokens.json").read_text())
            self.assertEqual(out["core"]["easing"]["standard"]["$value"], [0.4, 0, 0.2, 1])
            self.assertNotIn("radius.round", [e["name"] for e in out["core"]["$extensions"]["notTokenised"]])

if __name__ == "__main__":
    unittest.main()
