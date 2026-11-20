"""Checks for the Luma token builders. Run from this folder, or via tools/package_tests.py.

Both builders run in a scratch package that copies the readings, so a fresh build is compared
with the committed raw/component-tokens.json and tokens.json without rewriting either.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
READINGS = ("css-vars.json", "components-computed.json", "component-tokens.json")


class TokenBuilders(unittest.TestCase):
    def setUp(self):
        self.root = pathlib.Path(tempfile.mkdtemp())
        (self.root / "tools").mkdir()
        (self.root / "raw").mkdir()
        for name in ("build_component_tokens.py", "build_tokens.py"):
            shutil.copy(PKG / "tools" / name, self.root / "tools" / name)
        for name in READINGS:
            shutil.copy(PKG / "raw" / name, self.root / "raw" / name)

    def tearDown(self):
        shutil.rmtree(self.root, ignore_errors=True)

    def run_builder(self, name):
        return subprocess.run([sys.executable, str(self.root / "tools" / name)], capture_output=True, text=True)

    def test_both_builds_match_the_committed_files(self):
        for name in ("build_component_tokens.py", "build_tokens.py"):
            proc = self.run_builder(name)
            self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertEqual((self.root / "raw" / "component-tokens.json").read_text(), (PKG / "raw" / "component-tokens.json").read_text())
        self.assertEqual((self.root / "tokens.json").read_text(), (PKG / "tokens.json").read_text())

    def test_the_modal_inset_edge_stays_inset(self):
        modal = json.loads((PKG / "tokens.json").read_text())["core"]["shadow"]["modal"]["$value"]
        self.assertEqual([layer.get("inset", False) for layer in modal], [False] * 5 + [True])
        self.assertEqual(modal[-1]["offsetY"], "-4px")

    def test_every_declared_layer_is_kept(self):
        raw = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]["light"]
        tokens = json.loads((PKG / "tokens.json").read_text())["core"]["shadow"]
        for key, name in (("modal", "--shadow-modal"), ("lg", "--shadow-lg"), ("card-hover", "--card-hover-shadow")):
            self.assertEqual(len(tokens[key]["$value"]), raw[name]["value"].count("rgba("), key)

    def test_a_layer_it_cannot_read_fails(self):
        path = self.root / "raw" / "css-vars.json"
        v = json.loads(path.read_text())
        v["resolved"]["light"]["--shadow-modal"]["value"] += ", 0px 1px var(--x)"
        path.write_text(json.dumps(v))
        proc = self.run_builder("build_component_tokens.py")
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("shadow layer not understood", proc.stderr)


if __name__ == "__main__":
    unittest.main()
