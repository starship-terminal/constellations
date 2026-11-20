"""The Kinhive builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py kinhive.
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
BUILDERS = ["build_tokens.py", "build_style_guide.py"]
OUTPUTS = ["tokens.json", "style-guide.html"]


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
        shutil.copytree(PKG, cls.dst, ignore=shutil.ignore_patterns("*.png", "screenshots", "components"))
        for b in BUILDERS:
            res = subprocess.run([sys.executable, str(cls.dst / "tools" / b)], cwd=cls.dst / "tools",
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

    def test_aliases_name_no_set_and_no_self(self):
        """{core.x} names a set (DTCG readers report it dangling); {x} on x resolves to itself."""
        for set_name in ("core", "light", "dark"):
            for path, leaf in leaves(self.tokens[set_name]):
                for ref in re.findall(r"\{([^{}]+)\}", json.dumps(leaf["$value"])):
                    self.assertFalse(ref.split(".")[0] in ("core", "light", "dark"), f"{set_name}.{path}: {{{ref}}}")
                    self.assertNotEqual(ref, path, f"{set_name}.{path} aliases itself")

    def test_hand_values_are_reconstructions(self):
        """Values with no reading in raw/ say so (docs/EVIDENCE.md), never 'measured' or 'computed'."""
        raw = (PKG / "raw" / "css-vars.json").read_text()
        for key in ("nav-height", "nav-link-size", "cta-height", "cta-radius", "field-height", "hero-size"):
            src = self.tokens["core"]["component"][key]["$extensions"]["source"]
            self.assertTrue(src.startswith("Reconstruction"), f"core.component.{key}: {src}")
        for theme in ("light", "dark"):
            hover = self.tokens[theme]["action"]["fill-hover"]
            self.assertNotIn(hover["$value"].lstrip("#"), raw)
            self.assertTrue(hover["$extensions"]["source"].startswith("Reconstruction"))


if __name__ == "__main__":
    unittest.main()
