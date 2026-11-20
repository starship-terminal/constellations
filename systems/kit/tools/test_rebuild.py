"""The kit.com builders reproduce the committed files.

Each builder runs in a scratch copy of the package, so nothing committed is rewritten, and its
output is compared byte for byte with the committed file. Run from this folder, or via
tools/package_tests.py kit.
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

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for rel in OUTPUTS:
            with self.subTest(rel):
                self.assertEqual((self.dst / rel).read_text(), (PKG / rel).read_text(),
                                 f"{rel}: the builders no longer reproduce the committed file")

    @unittest.skipUnless(shutil.which("node"), "needs Node.js for tools/capture/public/build-measurements.mjs")
    def test_measurements_match_committed(self):
        """raw/measurements.md comes from the JavaScript builder; its focus filter and crop notes are checked here."""
        res = subprocess.run(["node", str(self.dst / "tools" / "capture" / "public" / "build-measurements.mjs")],
                             cwd=self.dst, capture_output=True, text=True, timeout=120)
        self.assertEqual(res.returncode, 0, res.stderr)
        self.assertEqual((self.dst / "raw" / "measurements.md").read_text(), (PKG / "raw" / "measurements.md").read_text(),
                         "raw/measurements.md: build-measurements.mjs no longer reproduces the committed file")

    def test_hover_is_the_measured_fill(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        comps = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        fill = comps["nav-trial"]["states"]["hover"]["style"]["backgroundColor"]
        r, g, b = (int(x) for x in fill[fill.index("(") + 1:fill.index(")")].split(",")[:3])
        self.assertEqual(tokens["light"]["action"]["hover"]["$value"], "#%02x%02x%02x" % (r, g, b))

    def test_no_token_holds_tokens(self):
        """A leaf that also holds child tokens hides them from every reader (catalog flatten stops at $value)."""
        tokens = json.loads((PKG / "tokens.json").read_text())
        for set_name in ("core", "light", "dark"):
            for path, leaf in leaves(tokens[set_name]):
                kids = [k for k in leaf if not k.startswith("$")]
                self.assertEqual(kids, [], f"{set_name}.{path} holds child tokens {kids}")

    def test_every_declared_colour_is_a_token(self):
        """Every resolved --color-* hex becomes a core.color token (warm-white-100 was once lost)."""
        tokens = json.loads((PKG / "tokens.json").read_text())
        sources = {leaf["$extensions"]["source"].split()[1] for _, leaf in leaves(tokens["core"]["color"])}
        resolved = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]["light"]
        for name, v in resolved.items():
            value = v.get("value", v.get("raw")) if isinstance(v, dict) else v
            if name.startswith("--color-") and str(value).startswith("#"):
                self.assertIn(name, sources)

    def test_failed_focus_is_not_published(self):
        """A focus-visible reading taken where keyboard focus never landed is left out of the tables."""
        md = (PKG / "components.md").read_text()
        self.assertNotIn("hero-secondary-focus-visible.png", md)
        self.assertIn("**Focus not capturable.**", md)
        self.assertNotIn("hero-secondary-focus-visible.png", (PKG / "raw" / "measurements.md").read_text())


if __name__ == "__main__":
    unittest.main()
