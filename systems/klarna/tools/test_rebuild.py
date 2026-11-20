"""The Klarna builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py klarna.
"""
import json
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

    def test_no_token_holds_tokens(self):
        """catalog.py's flatten stops at $value, so a token nested in another is invisible (24 were)."""
        for set_name in ("core", "light", "dark"):
            for path, leaf in leaves(self.tokens[set_name]):
                kids = [k for k in leaf if not k.startswith("$")]
                self.assertEqual(kids, [], f"{set_name}.{path} holds child tokens {kids}")

    def test_every_colour_var_is_a_token(self):
        resolved = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]["light"]
        names = {n for n in resolved if n.startswith("--colors-")}
        for set_name in ("light", "dark"):
            cited = {leaf["$extensions"]["source"].split()[1].rstrip(",") for _, leaf in leaves(self.tokens[set_name]["color"])}
            self.assertEqual(names - cited, set(), f"{set_name}: colour vars with no token")


if __name__ == "__main__":
    unittest.main()
