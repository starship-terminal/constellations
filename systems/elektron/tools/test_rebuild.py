"""Rebuild checks for the Elektron builders. Run from this folder, or via tools/package_tests.py.

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

    def _rebuild_with(self, edit):
        """Rebuild a second temp copy after edit(components) changes its raw readings."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name) / "pkg"
        shutil.copytree(self.root, root)
        raw = root / "raw" / "components-computed.json"
        J = json.loads(raw.read_text())
        edit(J["components"])
        raw.write_text(json.dumps(J))
        r = subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")],
                           cwd=root, capture_output=True, text=True)
        return r, (json.loads((root / "raw" / "component-tokens.json").read_text()) if r.returncode == 0 else None)

    def test_focus_ring_colours_follow_the_reading(self):
        # 13-11: neutral.white and dark.focus-outline were typed; they must follow nav-link focus-visible.
        def edit(C):
            s = C["nav-link"]["states"]["focus-visible"]["style"]
            s["boxShadow"] = "rgb(1, 2, 3) 0px 0px 0px 2px"
            s["outlineColor"] = "rgb(4, 5, 6)"
        r, spec = self._rebuild_with(edit)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(spec["core"]["color"]["neutral"]["white"]["value"], "#010203")
        self.assertEqual(spec["dark"]["focus-outline"]["value"], "#040506")

    def test_focus_white_is_the_spread_ring_layer(self):
        # Review: with a drop shadow before the ring, the first layer is not the ring.
        def edit(C):
            C["nav-link"]["states"]["focus-visible"]["style"]["boxShadow"] = \
                "rgb(1, 2, 3) 0px 4px 8px 0px, rgb(255, 255, 255) 0px 0px 0px 2px"
        r, spec = self._rebuild_with(edit)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(spec["core"]["color"]["neutral"]["white"]["value"], "#ffffff")

    def test_easing_must_be_read(self):
        # 13-12: the easing loop published its typed curve even when the cited reading lacked it.
        def edit(C):
            C["header"]["states"]["default"]["style"]["transitionTimingFunction"] = "ease"
        r, _ = self._rebuild_with(edit)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("easing standard", r.stderr)

    def test_shadow_layer_it_cannot_read_stops_the_build(self):
        # 13-18: a single-layer fullmatch dropped multi-layer or inset shadows silently.
        def edit(C):
            C["nav-link"]["states"]["focus-visible"]["style"]["boxShadow"] = "rgb(255, 255, 255) 0px 0px 0px 2px, color(srgb 0 0 0) 0px 1px 2px"
        r, _ = self._rebuild_with(edit)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("shadow layer not understood", r.stderr)


if __name__ == "__main__":
    unittest.main()
