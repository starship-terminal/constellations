"""Both builders' OKLab/OKLCh converters give the sRGB values browsers do.

Loads only each builder's imports and functions (not its top-level build), so the
test needs no raw files and writes nothing."""
import ast
import pathlib
import unittest

HERE = pathlib.Path(__file__).resolve().parent


def load(name):
    mod = ast.parse((HERE / name).read_text())
    ns = {}
    body = [n for n in mod.body if isinstance(n, (ast.FunctionDef, ast.Import, ast.ImportFrom))]
    exec(compile(ast.Module(body=body, type_ignores=[]), name, "exec"), ns)
    return ns["oklab_srgb"]


CASES = [
    ("oklab(0.627955 0.224863 0.125846)", "#ff0000"),   # sRGB red
    ("oklch(0.627955 0.257683 29.2339)", "#ff0000"),
    ("oklch(62.8% 0.2577 29.23)", "#ff0000"),           # percent lightness
    ("oklch(1 0 0)", "#ffffff"),
    ("oklch(0.5 0 0)", "#636363"),
    ("oklab(0 0 0 / 0.5)", "rgba(0, 0, 0, 0.5)"),       # alpha
    ("oklch(0.5 0 0 / 50%)", "rgba(99, 99, 99, 0.5)"),  # percent alpha
]


class Converters(unittest.TestCase):
    def test_both_copies(self):
        for name in ("build_component_tokens.py", "build_tokens.py"):
            conv = load(name)
            for css, want in CASES:
                self.assertEqual(conv(css), want, f"{name}: {css}")


if __name__ == "__main__":
    unittest.main()
