"""Rebuild checks for the ElevenReader builders. Run from this folder, or via tools/package_tests.py.

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

    def test_ring_offset_sentence_matches_the_readings(self):
        # 18-12: the hand sentence said every ring sits at 2px offset.
        offs = {}
        for k, c in self.C.items():
            s = (c.get("states") or {}).get("focus-visible", {})
            st = s.get("style")
            if not st or s.get("via") == "focus failed" or st["outlineStyle"] == "none" or st["outlineWidth"] == "0px":
                continue
            offs.setdefault(st["outlineOffset"], []).append(k)
        line = next(l for l in (PKG / "components.md").read_text().splitlines() if l.startswith("- **Hover on nav links**"))
        for off, ks in offs.items():
            self.assertIn(f"{off}", line)
            if len(ks) < max(len(v) for v in offs.values()):
                for k in ks:
                    self.assertIn(f"`{k}`", line)

    def test_token_path_collision_stops_the_build(self):
        # 14-28: --color-mauve-default would land on color.mauve.default, where --color-mauve sits.
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name) / "pkg"
        shutil.copytree(self.root, root)
        raw = root / "raw" / "css-vars.json"
        V = json.loads(raw.read_text())
        V["resolved"]["light"]["--color-mauve-default"] = {"raw": "#000000", "value": "#000000"}
        raw.write_text(json.dumps(V))
        r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")],
                           cwd=root, capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("mauve.default: token path already holds a leaf", r.stderr)

    def test_no_transparent_fill_published(self):
        # 14-8: an rgba(0, 0, 0, 0) reading is never a surface or action colour.
        for path, v in flat(self.built):
            if v.get("$type") == "color":
                self.assertNotEqual(v["$value"], "rgba(0, 0, 0, 0)", path)


if __name__ == "__main__":
    unittest.main()
