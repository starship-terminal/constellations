"""Rebuild checks for the Dub builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of the package (images replaced by empty files of the same
name, capture scripts left out except build-measurements.mjs), so nothing committed is rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = [b for b in ("build_component_tokens.py", "build_tokens.py", "build_style_guide.py", "build_components_md.py")
            if (PKG / "tools" / b).exists()]
OUTPUTS = ("raw/component-tokens.json", "tokens.json", "style-guide.html", "components.md")
MEASUREMENTS = PKG / "tools" / "capture" / "public" / "build-measurements.mjs"
NODE = shutil.which("node")


def _copy(src, dst):
    if src.endswith((".png", ".jpg", ".jpeg", ".webp", ".gif")):
        pathlib.Path(dst).touch()  # the builders only list image names
    else:
        shutil.copy2(src, dst)


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def leaf(tree, path):
    for part in path.split("."):
        tree = tree[part]
    return tree


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.root = root = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, root, copy_function=_copy,
                        ignore=shutil.ignore_patterns("capture", "__pycache__", "full"))
        if MEASUREMENTS.exists():
            cap = root / "tools" / "capture"
            (cap / "public").mkdir(parents=True)
            shutil.copy2(PKG / "tools" / "capture" / "css-colour.mjs", cap / "css-colour.mjs")
            shutil.copy2(MEASUREMENTS, cap / "public" / "build-measurements.mjs")
        # The copy starts without the outputs, so each comparison reads a freshly written file
        # and a builder that stops writing fails the test instead of passing on the committed copy.
        for rel in OUTPUTS + ("raw/measurements.md",):
            if (root / rel).exists():
                (root / rel).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for rel in OUTPUTS:
            if (PKG / rel).exists():
                self.assertTrue((self.root / rel).exists(), f"{rel} was not rebuilt")
                self.assertEqual((PKG / rel).read_text(), (self.root / rel).read_text(), rel)

    @unittest.skipUnless(NODE and MEASUREMENTS.exists(), "needs node")
    def test_measurements_match_rebuild(self):
        subprocess.run([NODE, str(self.root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                       cwd=self.root, check=True, capture_output=True)
        rel = "raw/measurements.md"
        self.assertEqual((PKG / rel).read_text(), (self.root / rel).read_text(), rel)

    def test_failed_focus_is_not_a_reading(self):
        failed = [k for k, c in self.C.items()
                  if (c.get("states") or {}).get("focus-visible", {}).get("via") == "focus failed"]
        md = (PKG / "raw" / "measurements.md").read_text()
        for k in failed:
            block = md.split(f"#### {k}\n", 1)[1].split("\n#### ", 1)[0]
            self.assertIn("focus failed: keyboard focus did not reach the element", block, k)
        for path, v in flat(self.built):
            src = (v.get("$extensions") or {}).get("source", "")
            for k in failed:
                self.assertNotIn(f"of {k} focus-visible", src, path)

    def test_no_css_color4_value_left_unconverted(self):
        # 15-10: oklab washes are converted to sRGB, the computed string kept in $extensions.authored.
        for path, v in flat(self.built):
            if v.get("$type") == "color" and isinstance(v["$value"], str):
                self.assertRegex(v["$value"], r"^(#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\)|\{.+\})$", path)
        wash = self.built["core"]["color"]["wash"]
        self.assertEqual(wash["primary-10"]["$value"], "rgba(21, 93, 252, 0.1)")  # the docs #155dfc at 10%
        self.assertTrue(wash["primary-10"]["$extensions"]["authored"].startswith("oklab("))

    def test_dimensions_are_px_or_rem(self):
        # 15-16: em tracking and currentColor go to notTokenised, not into typed tokens.
        for path, v in flat(self.built):
            if v.get("$type") == "dimension" and not str(v["$value"]).startswith("{"):
                self.assertRegex(v["$value"], r"^-?\d*\.?\d+(px|rem)$", path)
        skipped = {e["name"] for e in self.built["core"]["$extensions"]["notTokenised"]}
        self.assertEqual(skipped, {"font.tracking.tighter", "font.tracking.tight"})

    def test_unconvertible_colour_stops_the_build(self):
        # A colour function the builder cannot convert must fail, not vanish from the export.
        spec_path = self.root / "raw" / "component-tokens.json"
        saved = spec_path.read_text()
        spec = json.loads(saved)
        spec["core"]["color"]["wash"]["primary-10"]["value"] = "lab(50% 20 -30 / 0.1)"
        try:
            spec_path.write_text(json.dumps(spec))
            r = subprocess.run([sys.executable, str(self.root / "tools" / "build_tokens.py")],
                               cwd=self.root, capture_output=True, text=True)
        finally:
            spec_path.write_text(saved)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("lab(50% 20 -30 / 0.1)", r.stderr)

    def test_flagged_and_wrong_readings_say_so(self):
        # 13-7 and 11d-10: a kept or wrong-element reading names itself in the source.
        core = self.built["core"]
        self.assertIn("recaptureMissed", core["layout"]["docs-sidebar"]["$extensions"]["source"])
        self.assertIn("recapture needed", core["font"]["tracking"]["price-tight"]["$extensions"]["source"])
        self.assertIn("recapture needed",
                      self.built["light"]["component"]["nav-dropdown"]["width"]["$extensions"]["source"])

    def test_transparent_outline_is_not_a_ring(self):
        # 18-5: nav-login's focus-visible outline is 2px solid transparent.
        focus = next(l for l in (PKG / "components.md").read_text().splitlines() if l.startswith("**Focus.**"))
        ring = focus.split("draw an outline ring:", 1)[1].split(". ", 1)[0]
        self.assertNotIn("`nav-login`", ring)
        self.assertNotIn("transparent", ring)


if __name__ == "__main__":
    unittest.main()
