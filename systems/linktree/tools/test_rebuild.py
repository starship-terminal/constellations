"""The builders reproduce the committed files, and the focus token is a ring the page paints.

Every builder runs on a temporary copy of the package, so the committed files are never rewritten.
"""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ["build_component_tokens.py", "build_tokens.py", "build_components_md.py", "build_style_guide.py"]
OUTPUTS = ["raw/component-tokens.json", "tokens.json", "components.md", "style-guide.html"]


class RebuildTest(unittest.TestCase):
    def test_builders_reproduce_committed_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "linktree"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("__pycache__"))
            for b in BUILDERS:
                subprocess.run([sys.executable, str(copy / "tools" / b)], check=True, capture_output=True, cwd=copy)
            for out in OUTPUTS:
                self.assertEqual((copy / out).read_text(), (PKG / out).read_text(), out)

    def test_focus_token_is_a_painted_ring(self):
        # nav-link's outlineColor (#005fcc) was published as the focus colour, but its outline is
        # none/0px: nothing paints it. The token must be the outer box-shadow ring nav-login draws.
        tokens = json.loads((PKG / "tokens.json").read_text())
        raw = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]
        shadow = raw["nav-login"]["states"]["focus-visible"]["style"]["boxShadow"]
        self.assertIn("rgb(30, 35, 48) 0px 0px 0px 4px", shadow)
        self.assertEqual(tokens["light"]["focus"]["$value"], "#1e2330")
        self.assertIn("nav-login focus-visible", tokens["light"]["focus"]["$extensions"]["source"])

    def test_failed_focus_is_not_a_state_row(self):
        md = (PKG / "components.md").read_text()
        self.assertIn("could not be driven: `login-continue`", md)
        self.assertNotIn("login-continue-focus-visible.png", md)


if __name__ == "__main__":
    unittest.main()
