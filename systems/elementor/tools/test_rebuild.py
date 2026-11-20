"""Rebuild checks for the Elementor builders. Run from this folder, or via tools/package_tests.py.

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
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for rel in OUTPUTS:
            if (PKG / rel).exists() and (self.root / rel).exists():
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
            if "error" not in self.C[k]["states"]["focus-visible"]:  # an error row is no reading either
                self.assertIn("focus failed: keyboard focus did not reach the element", block, k)
        for path, v in flat(self.built):
            src = (v.get("$extensions") or {}).get("source", "")
            for k in failed:
                self.assertNotIn(f"of {k} focus-visible", src, path)

    def test_typed_values_are_read_from_raw(self):
        # 13-11: page, textMuted, menuPanel, the dark accents and the motion leaves were literals.
        V = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]
        L, D = self.built["light"], self.built["dark"]
        lit = lambda t: t["$value"] if not str(t["$value"]).startswith("{") else None
        self.assertIn("--Blank-Canvas-White", L["page"]["$extensions"]["source"])
        self.assertIn("nav-dropdown paint[0]", L["menuPanel"]["$extensions"]["source"])
        for key, var in (("accent", "--Kernel-Black"), ("accentOn", "--Blank-Canvas-White"), ("border", "--Grey-700")):
            self.assertIn(var, D[key]["$extensions"]["source"], key)
        spec = json.loads((self.root / "raw" / "component-tokens.json").read_text())
        for key, comp in (("button", "hero-cta"), ("link", "nav-login"), ("panel", "faq-answer")):
            s = self.C[comp]["states"]["default"]["style"]
            self.assertEqual(spec["component"]["motion"][key]["$value"],
                             f"{s['transitionDuration'].split(',')[0]} {s['transitionTimingFunction'].split(',')[0]}")
        self.assertEqual(spec["dark"]["border"]["$value"], V["dark"]["--Grey-700"]["value"])

    def test_type_steps_are_the_text_readings(self):
        # 13-12: planPrice/body/small fell back to typed sizes when a reading was missing.
        spec = json.loads((self.root / "raw" / "component-tokens.json").read_text())["component"]["type"]
        for key, comp in (("planPrice", "plan-price"), ("body", "faq-answer"), ("small", "m-nav-item")):
            self.assertEqual(spec[key]["$value"], self.C[comp]["states"]["default"]["textStyle"]["fontSize"], key)


if __name__ == "__main__":
    unittest.main()
