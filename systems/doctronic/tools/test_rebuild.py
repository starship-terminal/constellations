"""Rebuild checks for the Doctronic builders. Run from this folder, or via tools/package_tests.py.

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

    def test_shadows_are_normalised_dtcg_layers(self):
        for path, leaf in self.tok.items():
            if leaf["$type"] == "shadow" and isinstance(leaf["$value"], list):
                for layer in leaf["$value"]:
                    self.assertRegex(layer["color"], r"^(#[0-9a-f]{6}|rgba\(\d+, \d+, \d+, [\d.]+\))$", path)
        self.assertEqual(self.tok["light.shadow.focus-ring"]["$value"][0]["color"], "#2463eb")

    def test_shadow_parser_refuses_what_it_cannot_read(self):
        import runpy
        ns = runpy.run_path(str(pathlib.Path(self.tmp.name) / "tools" / "build_component_tokens.py"))
        layers = ns["parse_shadow"]("rgba(0, 0, 0, 0.2) 0px 1px 2px 0px inset, rgb(255, 255, 255) 0 0 0 1px")
        self.assertEqual([l["inset"] for l in layers], [True, False])
        with self.assertRaises(ValueError):
            ns["parse_shadow"]("rgba(0, 0, 0, 0.2) 0px 1px 2px, color-mix(in srgb, red, blue) 0 0 1px")

    def test_wrong_elements_flagged(self):
        for k in ("nav-link", "input-card", "chat-hero", "logo", "feature-card", "signin-dialog", "menu-item"):
            entry = self.md.split(f"Read as `{k}`")[1].split("####")[0]
            self.assertIn("**Known wrong; recapture needed.**", entry, k)
        self.assertIn("recapture needed", self.tok["light.component.dialog.width"]["$extensions"]["source"])

    def test_failed_focus_is_listed_not_measured(self):
        self.assertRegex(self.md, r"Focus could not be captured on \d+ more")
