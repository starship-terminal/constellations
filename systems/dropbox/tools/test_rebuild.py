"""Rebuild checks for the Dropbox builders. Run from this folder, or via tools/package_tests.py.

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
        # The copy starts without the outputs, so each comparison reads a freshly written file.
        cls.expected = [rel for rel in OUTPUTS + ("raw/measurements.md",) if (PKG / rel).exists()]
        for rel in cls.expected:
            (root / rel).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        if NODE and MEASUREMENTS.exists():
            subprocess.run([NODE, str(root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                           cwd=root, check=True, capture_output=True)
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        for rel in self.expected:
            if rel == "raw/measurements.md" and not NODE:
                continue
            self.assertTrue((self.root / rel).exists(), f"{rel} was not rebuilt")
            self.assertEqual((PKG / rel).read_text(), (self.root / rel).read_text(), rel)

    @unittest.skipUnless(NODE and MEASUREMENTS.exists(), "needs node")
    def test_measurements_match_rebuild(self):
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

    def test_measured_sizes_on_the_ramp_alias_it(self):
        # 13-22: the de-dupe compared against "value", which var leaves lack, so a measured size
        # equal to a ramp step was published as "outside the declared ramp".
        sizes = self.built["core"]["font"]["size"]
        for key in ("measured-section-h2", "measured-price"):
            self.assertEqual(sizes[key]["$value"], "{font.size.text-xlarge}", key)
        self.assertEqual(sizes["text-xlarge"]["$value"], "20px")
        for key, v in sizes.items():
            if key.startswith("measured-") and not str(v["$value"]).startswith("{"):
                ramp = {x["$value"] for k, x in sizes.items() if isinstance(x, dict) and not k.startswith("measured-")}
                self.assertNotIn(v["$value"], ramp, key)

    def _tokens_with_shadow(self, value):
        """Rebuild a temp copy whose floating shadow var resolves to `value`."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name) / "pkg"
        shutil.copytree(self.root, root)
        raw = root / "raw" / "css-vars.json"
        V = json.loads(raw.read_text())
        V["resolved"]["light"]["--dig-utilities__boxshadow__floating"]["value"] = value
        raw.write_text(json.dumps(V))
        r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, capture_output=True, text=True)
        spec = json.loads((root / "raw" / "component-tokens.json").read_text()) if r.returncode == 0 else None
        return r, spec

    def test_unreadable_shadow_layer_stops_the_build(self):
        # 13-18: findall skipped a layer it could not read; the build must stop instead.
        r, _ = self._tokens_with_shadow("rgba(0, 0, 0, 0.04) 0px 10px 40px 20px, color(srgb 0 0 0) 0px 1px 2px")
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("shadow layer not understood", r.stderr)

    def test_inset_is_read_before_or_after_the_colour(self):
        r, spec = self._tokens_with_shadow("inset rgb(1, 2, 3) 0px 1px 2px 0px, rgb(4, 5, 6) 0px 2px 4px 0px inset")
        self.assertEqual(r.returncode, 0, r.stderr)
        layers = spec["light"]["shadow"]["floating"]["value"]
        self.assertEqual([(l["color"], l["inset"]) for l in layers], [("#010203", True), ("#040506", True)])

    def test_social_icon_is_marked_wrong(self):
        md = (PKG / "components.md").read_text()
        self.assertIn("**Wrong element.**", md.split("Read as `social-icon`", 1)[1].split("\n#### ", 1)[0])


if __name__ == "__main__":
    unittest.main()
