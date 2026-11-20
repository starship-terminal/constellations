"""Lint for the kit's own scripts (tools/kit/): checks that must hold whatever the product. Run with `make test`."""
import ast
import unittest
from pathlib import Path

KIT = Path(__file__).resolve().parent / "kit"


class ChecksSurviveOptimisation(unittest.TestCase):
    def test_no_kit_script_checks_with_assert(self):
        # python3 -O drops assert statements, so a builder's check written as one silently passes there;
        # the kit's builders raise instead (native/build_tokens.py's CheckError and require()).
        bad = []
        for f in sorted(KIT.rglob("*.py")):
            if f.name.startswith("test_"):
                continue
            bad += [f"{f.relative_to(KIT)}:{n.lineno}" for n in ast.walk(ast.parse(f.read_text())) if isinstance(n, ast.Assert)]
        self.assertEqual(bad, [])


if __name__ == "__main__":
    unittest.main()
