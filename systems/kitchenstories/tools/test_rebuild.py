"""The Kitchen Stories builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared with the committed file. Run from this folder, or via
tools/package_tests.py kitchenstories.
"""
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

PKG = Path(__file__).resolve().parent.parent
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_components_md.py", "build_style_guide.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "components.md", "style-guide.html"]


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

    @unittest.skipUnless(shutil.which("node"), "needs Node.js for build-measurements.mjs")
    def test_measurements_match_committed(self):
        res = subprocess.run(["node", str(self.dst / "tools" / "capture" / "public" / "build-measurements.mjs")],
                             cwd=self.dst, capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual((self.dst / "raw" / "measurements.md").read_text(), (PKG / "raw" / "measurements.md").read_text())

    def test_every_wpds_colour_is_a_token(self):
        """Each resolved --wpds-color-* is a token (68 state colours were once nested inside a parent leaf)."""
        resolved = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]["light"]
        cited = {leaf["$extensions"]["source"].split()[1] for _, leaf in leaves(self.tokens["light"]["wpds"])}
        missing = {n for n, v in resolved.items() if n.startswith("--wpds-color-") and (v.get("value", v.get("raw")) if isinstance(v, dict) else v)} - cited
        self.assertEqual(missing, set())

    def test_unconverted_colour_forms_are_refused(self):
        """lab(), oklch(), color() and color-mix() fail the build instead of shipping as colours nothing can check."""
        src = (PKG / "tools" / "build_tokens.py").read_text().split("\ncore = build(")[0]  # the helpers, nothing written
        ns = {"__file__": str(PKG / "tools" / "build_tokens.py")}
        exec(compile(src, "build_tokens.py", "exec"), ns)
        norm = ns["norm_color"]
        self.assertEqual(norm("#ABC"), "#aabbcc")
        self.assertEqual(norm("rgba(0, 0, 0, 0.5)"), "rgba(0, 0, 0, 0.5)")
        for v in ("lab(50% 20 30)", "oklch(0.6 0.1 30)", "color(srgb 1 0 0)", "color-mix(in srgb, red, blue)"):
            with self.subTest(v), self.assertRaises(ValueError):
                norm(v)

    def test_no_token_holds_tokens(self):
        for set_name in ("core", "light"):
            for path, leaf in leaves(self.tokens[set_name]):
                self.assertEqual([k for k in leaf if not k.startswith("$")], [], f"{set_name}.{path}")


if __name__ == "__main__":
    unittest.main()
