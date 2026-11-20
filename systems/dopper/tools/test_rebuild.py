"""Rebuild checks for the Dopper builders. Run from this folder, or via tools/package_tests.py.

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


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict) and not k.startswith("$"):
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

    def test_no_token_reads_an_unconfirmed_focus_or_flagged_entry(self):
        hand = "el.focus() — a real ring painted; document.activeElement read the shadow host (check fixed in kbFocus)"
        for path, leaf in self.tok.items():
            for comp, state in re.findall(r"of ([\w-]+) ([\w-]+)(?:;| \()", leaf["$extensions"]["source"]):
                if comp not in self.C:
                    continue
                self.assertFalse(self.C[comp].get("missing"), f"{path} cites flagged {comp}")
                self.assertNotIn(self.C[comp]["states"][state].get("via"), ("focus failed", hand), f"{path} cites {comp} {state}")

    def test_roles_name_readings_that_hold_them(self):
        self.assertIn("btn-outline focus-visible", self.tok["light.focus.ring.default"]["$extensions"]["source"])
        self.assertNotIn("btn-outline", self.tok["light.border.ink"]["$extensions"]["source"])
        for p in ("light.text.muted", "light.action.warm", "light.surface.menu.default", "light.surface.card"):
            self.assertNotIn("computed", self.tok[p]["$extensions"]["source"], p)

    def test_flagged_entries_reach_no_tally(self):
        focus = re.search(r"\*\*Focus\.\*\* .*", self.md).group(0)
        motion = self.md.split("**Motion.**")[1].split("**Card shapes.**")[0]
        for k in ("flyout-card", "flyout-tab", "m-filter-radio"):
            self.assertNotIn(f"`{k}` (", focus.split("Focus could not be captured")[0])
            self.assertNotIn(k, motion)
        for k in ("nav-link", "m-burger", "m-menu-pill"):
            self.assertNotIn(f"`{k}` (", focus)
        self.assertIn("Focus could not be captured on 5 more", focus)
        self.assertIn("**Known wrong; recapture needed.**", self.md.split("Read as `cart-empty`")[1].split("####")[0])


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
        entry = built.split("#### nav-link\n")[1].split("\n#### ")[0]
        self.assertIn("| Skipped |", entry)

if __name__ == "__main__":
    unittest.main()
