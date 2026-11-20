"""Rebuild checks for the Dock builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots and crops by name only),
so nothing committed is rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
HAND = "el.focus() — a real ring painted; document.activeElement read the shadow host (check fixed in kbFocus)"


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
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

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)
        self.assertEqual((PKG / "components.md").read_text(), self.md)

    def test_no_token_reads_an_unconfirmed_focus(self):
        for path, leaf in self.tok.items():
            for comp, state in re.findall(r"of ([\w-]+) ([\w-]+) \(raw/components-computed\.json\)", leaf["$extensions"]["source"]):
                via = self.C[comp]["states"][state].get("via")
                self.assertNotIn(via, ("focus failed", HAND), f"{path} cites {comp} {state}")

    def test_band_roles_are_the_readings(self):
        self.assertEqual(self.tok["dark.action.ghost.default"]["$value"], "rgba(0, 0, 0, 0)")
        self.assertEqual(self.C["hero-demo"]["states"]["default"]["style"]["backgroundColor"], "rgba(0, 0, 0, 0)")
        self.assertIn("hero-cta focus-visible", self.tok["dark.focus.ring"]["$extensions"]["source"])
        self.assertIn("nav-cta default", self.tok["light.text.on.action"]["$extensions"]["source"])
        self.assertIn("mcp-copy focus-visible", self.tok["light.focus.ring.default"]["$extensions"]["source"])

    def test_typed_and_stale_values_say_so(self):
        self.assertTrue(self.tok["dark.surface.pane"]["$extensions"]["source"].startswith("Reconstruction:"))
        self.assertNotIn("hero-lede", self.tok["core.color.brand.blue-deep"]["$extensions"]["source"])
        for p in ("core.font.size.menu", "core.font.lineHeight.menu", "core.radius.menu-item", "light.component.menurow.height"):
            self.assertIn("recaptureMissed", self.tok[p]["$extensions"]["source"], p)

    def test_hand_relabelled_focus_is_not_a_ring(self):
        tally = re.search(r"\*\*Focus\.\*\* .*", self.md).group(0)
        rings = tally.split(" draw an outline ring: ")[1].split(". ")[0]
        for k in ("nav-trigger", "nav-cta", "footer-link", "m-nav-item"):
            self.assertNotIn(f"`{k}`", rings)
        self.assertIn("Focus could not be captured on 9 more", tally)

    def test_colours_labelled_once(self):
        self.assertIsNone(re.search(r"`([^`]+)` `\1`", self.md))

    def test_wrong_elements_flagged(self):
        for k in ("hero-lede", "signup-submit", "m-hero"):
            entry = self.md.split(f"Read as `{k}`")[1].split("####")[0]
            self.assertIn("Known wrong; recapture needed.", entry, k)


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
        entry = built.split("#### nav-trigger\n")[1].split("\n#### ")[0]
        self.assertIn("| Skipped |", entry)

if __name__ == "__main__":
    unittest.main()
