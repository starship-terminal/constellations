"""Rebuild checks for the Eleven Music builders. Run from this folder, or via tools/package_tests.py.

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

    def test_dimensions_are_px_or_rem(self):
        # 15-16: the em tracking steps were typed dimension; they are listed under notTokenised.
        for path, v in flat(self.built):
            if v.get("$type") == "dimension" and not str(v["$value"]).startswith("{"):
                self.assertRegex(v["$value"], r"^-?\d*\.?\d+(px|rem)$", path)
        skipped = {e["name"]: e["value"] for e in self.built["core"]["$extensions"]["notTokenised"]}
        self.assertEqual(skipped, {"font.tracking.tight": "-0.025em", "font.tracking.wide": "0.025em",
                                   "font.tracking.wider": "0.05em", "font.tracking.widest": "0.1em"})

    def test_colour_helper_keeps_alpha(self):
        # 14-23 / 18-18: #rrggbbaa lost its alpha and a % alpha was not read.
        src = (PKG / "tools" / "build_component_tokens.py").read_text()
        ns = {"re": __import__("re")}
        exec(src[src.index("def norm_color"):src.index("def have(")], ns)
        self.assertEqual(ns["norm_color"]("#0000001a"), "rgba(0, 0, 0, 0.102)")
        self.assertEqual(ns["norm_color"]("rgba(10, 20, 30, 50%)"), "rgba(10, 20, 30, 0.5)")
        self.assertEqual(ns["norm_color"]("#ffffffff"), "#ffffff")

    def test_faq_answer_is_marked(self):
        md = (PKG / "components.md").read_text()
        self.assertIn("**Read in the wrong state.**", md.split("Read as `faq-answer`", 1)[1].split("\n#### ", 1)[0])


if __name__ == "__main__":
    unittest.main()
