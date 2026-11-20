"""The Krea builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py krea.
"""
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_components_md.py", "build_style_guide.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "components.md", "style-guide.html"]

sys.path.insert(0, str(Path(__file__).resolve().parent))
from oklab import oklab_or_oklch  # noqa: E402


def leaves(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from leaves(v, f"{path}.{k}" if path else k)


class Rebuild(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.dst = Path(cls.tmp.name) / PKG.name
        # Images only need to exist (the builders list and count them), so they are copied empty.
        shutil.copytree(PKG, cls.dst, ignore=shutil.ignore_patterns("*.png"))
        for png in PKG.rglob("*.png"):
            (cls.dst / png.relative_to(PKG)).parent.mkdir(parents=True, exist_ok=True)
            (cls.dst / png.relative_to(PKG)).touch()
        for b in BUILDERS:
            res = subprocess.run([sys.executable, str(cls.dst / "tools" / b)], cwd=cls.dst,
                                 capture_output=True, text=True, timeout=120)
            if res.returncode:
                raise AssertionError(f"{b} failed:\n{res.stderr}")
        cls.tokens = json.loads((PKG / "tokens.json").read_text())

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for rel in OUTPUTS:
            with self.subTest(rel):
                self.assertEqual((self.dst / rel).read_text(), (PKG / rel).read_text(),
                                 f"{rel}: the builders no longer reproduce the committed file")

    def test_colours_are_srgb(self):
        """Contrast checks and DESIGN.md parse hex and rgba only (14-18: oklch strings were committed)."""
        for set_name in ("core", "dark"):
            for path, leaf in leaves(self.tokens[set_name]):
                if leaf["$type"] == "color" and not str(leaf["$value"]).startswith("{"):
                    self.assertRegex(leaf["$value"], r"^(#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\))$", f"{set_name}.{path}")

    def test_oklab_conversion(self):
        self.assertEqual(oklab_or_oklch("oklch(0.985 0 0)"), "#fafafa")
        self.assertEqual(oklab_or_oklch("oklab(0.579 -0.0558729 -0.243369 / 0.15)"), "rgba(0, 110, 255, 0.15)")
        self.assertEqual(oklab_or_oklch("oklab(0 0 0 / 0.1)"), "rgba(0, 0, 0, 0.1)")
        self.assertIsNone(oklab_or_oklch("#ffffff"))

    def test_focus_ring_is_what_is_painted(self):
        """nav-signin's outline is none, so its ring is the box-shadow spread, not the unpainted outlineColor."""
        comps = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        sty = comps["nav-signin"]["states"]["focus-visible"]["style"]
        focus = self.tokens["dark"]["component"]["focus"]
        self.assertEqual(sty["outlineStyle"], "none")
        self.assertNotIn("outline", focus)
        layers = re.findall(r"((?:rgba?|oklab)\([^)]*\)) 0px 0px 0px (\d+)px", sty["boxShadow"])
        painted = [(c, w) for c, w in layers if int(w) > 0]
        self.assertEqual(focus["ring-width"]["$value"], painted[-1][1] + "px")
        self.assertEqual(focus["ring"]["$value"], oklab_or_oklch(painted[-1][0]) or painted[-1][0])


if __name__ == "__main__":
    unittest.main()
