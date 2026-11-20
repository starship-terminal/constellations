"""Rebuild checks for the ElevenLabs builders. Run from this folder, or via tools/package_tests.py.

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
            if "error" not in self.C[k]["states"]["focus-visible"]:  # an error row is no reading either
                self.assertIn("focus failed: keyboard focus did not reach the element", block, k)
        for path, v in flat(self.built):
            src = (v.get("$extensions") or {}).get("source", "")
            for k in failed:
                self.assertNotIn(f"of {k} focus-visible", src, path)

    def test_neutral_white_is_a_reading(self):
        # 13-12: the white surface came from a typed "#ffffff" fallback for a missing ancestor.
        w = self.built["core"]["color"]["neutral"]["white"]
        self.assertEqual(w["$extensions"]["source"], "computed backgroundColor of signin-card default (raw/components-computed.json)")
        self.assertEqual(self.C["signin-card"]["states"]["default"]["style"]["backgroundColor"], "rgb(255, 255, 255)")

    def test_accent_cites_the_palette_class_it_was_found_in(self):
        # 13-12: `hit is not None or True` published the accent whether or not the palette held it.
        V = json.loads((PKG / "raw" / "css-vars.json").read_text())
        src = self.built["core"]["color"]["brand"]["accent"]["$extensions"]["source"]
        cls = src.split("utility class .", 1)[1].split(" ", 1)[0]
        self.assertIn("rgb(43, 127, 255)", json.dumps(V["palette"][cls]))

    def test_wrong_element_readings_are_marked(self):
        # 11d-10 / 11d-15: entries read from another element say so.
        md = (PKG / "components.md").read_text()
        for k in ("feature-row", "voice-card", "menu-link"):
            self.assertIn("**Wrong element.**", md.split(f"Read as `{k}`", 1)[1].split("\n#### ", 1)[0], k)
        self.assertIn("recapture needed", self.built["core"]["color"]["neutral"]["muted"]["$extensions"]["source"])


if __name__ == "__main__":
    unittest.main()
