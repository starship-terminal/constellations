"""Rebuild checks for the Dona builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots and crops by name only),
so nothing committed is rewritten.
"""
import json
import pathlib
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

    def style(self, comp, state="default"):
        return self.C[comp]["states"][state]["style"]

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)
        self.assertEqual((PKG / "components.md").read_text(), self.md)

    def test_dimensions_are_px_or_rem(self):
        for path, leaf in self.tok.items():
            if leaf["$type"] == "dimension" and not str(leaf["$value"]).startswith("{"):
                self.assertRegex(leaf["$value"], r"^-?\d*\.?\d+(px|rem)$", path)
        kept = {e["name"]: e["value"] for e in self.built["core"]["$extensions"]["notTokenised"]}
        self.assertEqual(kept["radius.round"], self.style("modal-close")["borderTopLeftRadius"])
        self.assertEqual(kept["radius.swoosh"], self.C["newsletter"]["states"]["default"]["::before"]["borderRadius"])

    def test_probe_values_without_a_reading_say_so(self):
        for p in ("core.layout.container", "core.layout.gutter", "core.layout.grid-gap"):
            self.assertTrue(self.tok[p]["$extensions"]["source"].startswith("Reconstruction:"), p)
        self.assertEqual(self.tok["core.layout.content"]["$value"], self.style("header")["width"])
        self.assertIn("recapture needed", self.tok["core.shadow.banner-mobile"]["$extensions"]["source"])

    def test_literals_are_read(self):
        self.assertIn("try-cta default", self.tok["light.text.inverse"]["$extensions"]["source"])
        self.assertEqual(self.tok["core.easing.standard"]["$value"],
                         [0.25, 0.1, 0.25, 1] if self.style("cookie-accept")["transitionTimingFunction"].startswith("ease,") else None)

    def test_failed_focus_is_listed_not_measured(self):
        self.assertIn("Focus could not be captured on 2 more", self.md)
        self.assertIn("`logo`, `team-card`", self.md)


if __name__ == "__main__":
    unittest.main()
