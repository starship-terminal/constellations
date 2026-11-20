"""The committed outputs must rebuild from the package's inputs.

The builders run on a temporary copy of the package, so nothing committed is rewritten.
"""
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDERS = ['build_component_tokens.py', 'build_tokens.py', 'build_style_guide.py']
OUTPUTS = ['raw/component-tokens.json', 'tokens.json', 'style-guide.html']


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.copy = pathlib.Path(cls.tmp.name) / "pkg"
        shutil.copytree(PKG, cls.copy, ignore=shutil.ignore_patterns("__pycache__"))
        # Remove the committed outputs from the copy first, so a builder that
        # writes nothing cannot pass by leaving the committed file in place.
        for out in OUTPUTS:
            (cls.copy / out).unlink()
        for b in BUILDERS:
            subprocess.run([sys.executable, str(cls.copy / "tools" / b)], check=True, capture_output=True, cwd=cls.copy)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_outputs_match_committed(self):
        for out in OUTPUTS:
            with self.subTest(out=out):
                self.assertTrue((self.copy / out).exists(), f"{out} was not rebuilt")
                self.assertEqual((self.copy / out).read_text(), (PKG / out).read_text())

    def test_accent_is_the_accent_role_in_both_themes(self):
        import json
        t = json.loads((self.copy / "tokens.json").read_text())
        self.assertEqual(t["light"]["accent"]["$extensions"]["source"], "css-var --accent")
        self.assertEqual(t["dark"]["accent"]["$extensions"]["source"], "css-var --accent")
        self.assertEqual(t["light"]["accent-cta"]["$value"], "{color.cta.orange}")


def load_parse_shadow():
    """parse_shadow and the helpers it calls, taken from build_tokens.py without running the build
    (the module writes tokens.json at import): every function, the regex constants, the imports."""
    import ast
    import re as _re
    src = (PKG / "tools" / "build_tokens.py").read_text()
    tree = ast.parse(src)
    keep = [n for n in tree.body
            if isinstance(n, (ast.Import, ast.ImportFrom, ast.FunctionDef))
            or (isinstance(n, ast.Assign) and isinstance(n.value, ast.Call)
                and getattr(n.value.func, "attr", "") == "compile")]
    ns = {"re": _re}
    exec(compile(ast.Module(body=keep, type_ignores=[]), "build_tokens.py", "exec"), ns)
    return ns["parse_shadow"]


class ParseShadowTest(unittest.TestCase):
    parse = staticmethod(load_parse_shadow())

    def test_inset_at_either_end(self):
        for v in ("inset 0px 1px 2px 0px rgba(0, 0, 0, 0.1)", "rgba(0, 0, 0, 0.1) 0px 1px 2px 0px inset"):
            with self.subTest(v=v):
                self.assertEqual(self.parse(v), [{"offsetX": "0px", "offsetY": "1px", "blur": "2px", "spread": "0px",
                                                  "color": "rgba(0, 0, 0, 0.1)", "inset": True}])

    def test_unitless_zero(self):
        self.assertEqual(self.parse("0 1px 2px rgba(15,15,15,.05)")[0]["offsetX"], "0px")

    def test_unreadable_layers_are_refused(self):
        for v in ("0px 1px 2px", "1px rgba(0,0,0,.1)", "0px 1px 2px 3px 4px rgba(0,0,0,.1)", "0px 1px 2px wide rgba(0,0,0,.1)"):
            with self.subTest(v=v):
                with self.assertRaises(ValueError):
                    self.parse(v)


if __name__ == "__main__":
    unittest.main()
