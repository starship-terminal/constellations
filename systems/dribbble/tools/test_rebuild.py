"""Rebuild checks for the Dribbble builders. Run from this folder, or via tools/package_tests.py.

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

    def test_wrong_element_warning_follows_the_reading(self):
        # The warning shows for the bad reading and clears once a recapture reads another element.
        md = (PKG / "components.md").read_text()
        for k in ("designer-name", "m-search"):
            self.assertIn("**Wrong element.**", md.split(f"Read as `{k}`", 1)[1].split("\n#### ", 1)[0], k)
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        root = pathlib.Path(tmp.name) / "pkg"
        shutil.copytree(self.root, root)
        raw = root / "raw" / "components-computed.json"
        J = json.loads(raw.read_text())
        J["components"]["designer-name"]["states"]["default"]["text"] = "Jane Studio"
        raw.write_text(json.dumps(J))
        subprocess.run([sys.executable, str(root / "tools" / "build_components_md.py")], cwd=root, check=True, capture_output=True)
        md = (root / "components.md").read_text()
        self.assertNotIn("**Wrong element.**", md.split("Read as `designer-name`", 1)[1].split("\n#### ", 1)[0])

    def test_dimensions_have_no_exponent(self):
        # 15-16: Chromium's 1e+07px pill radius was committed verbatim.
        for path, v in flat(self.built):
            if v.get("$type") == "dimension":
                self.assertNotIn("e+", str(v["$value"]), path)
        self.assertEqual(self.built["core"]["radius"]["button-pill"]["$value"], "10000000px")

    def test_descriptions_name_the_value(self):
        # 13-22: role and measured descriptions named colours the tokens do not hold.
        hexes = __import__("re").compile(r"#[0-9a-f]{6}|rgba\([^)]*\)")
        measured = self.built["core"]["color"]["measured"]
        for key in ("ink-deep", "border", "promo-surface", "muted"):
            v = measured[key]
            self.assertEqual(hexes.findall(v["$description"]), [v["$value"]], key)
        for key in ("muted", "border", "surface-alt"):
            role = self.built["light"]["color"][key]
            target = role["$value"].strip("{}").split(".")[-1]
            self.assertIn(measured[target]["$value"], role["$description"], key)

    def test_roles_alias_only_readings(self):
        # 13-12 / 13-20: page/surface had typed #ffffff fallbacks and roles could dangle.
        measured = self.built["core"]["color"]["measured"]
        for key in ("page", "surface"):
            self.assertIn("raw/components-computed.json", measured[key]["$extensions"]["source"])
            self.assertTrue(measured[key]["$extensions"]["source"].startswith("computed "), key)


if __name__ == "__main__":
    unittest.main()
