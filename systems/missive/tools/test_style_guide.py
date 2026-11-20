"""The style guide's script handles a colour token that sits straight under core.color."""
import json
import pathlib
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


class StyleGuide(unittest.TestCase):
    def test_flat_recurses_into_objects_only(self):
        # Without the guard, core.color.white recursed through its value string until a RangeError,
        # which stopped the palette and left space, radius and layout empty.
        tpl = (PKG / "tools" / "style-guide.template.html").read_text()
        self.assertIn('typeof v === "object" ? flat(v', tpl)

    def test_single_colours_exist_to_be_drawn(self):
        color = json.loads((PKG / "tokens.json").read_text())["core"]["color"]
        singles = [k for k, v in color.items() if isinstance(v, dict) and "$value" in v]
        self.assertTrue(singles)  # white, black, brand
        self.assertIn('node && node.t ? [["", node]]', (PKG / "tools" / "style-guide.template.html").read_text())


    def test_committed_guide_matches_builder(self):
        import subprocess, sys, tempfile, shutil
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(PKG, copy, ignore=shutil.ignore_patterns("raw", "screenshots", "components", "boards"))
            subprocess.run([sys.executable, str(copy / "tools" / "build_style_guide.py")], check=True, capture_output=True)
            self.assertEqual((copy / "style-guide.html").read_text(), (PKG / "style-guide.html").read_text())


if __name__ == "__main__":
    unittest.main()
