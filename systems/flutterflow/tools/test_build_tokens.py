"""tokens.json provenance comes from the pass that produced each value, the
type roles carry only their own measurement, and components.md converts
lab()/oklab() readings.

Run from the package root: python3 -m unittest discover -s tools
"""
import ast
import json
import pathlib
import re
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
T = json.loads((PKG / "tokens.json").read_text())
RES = json.loads((PKG / "raw" / "css-vars.json").read_text())["resolved"]


def leaves(tree, prefix=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from leaves(v, prefix + k + ".")


class ProvenanceTest(unittest.TestCase):
    def test_declared_comes_from_the_same_pass(self):
        checked = 0
        for theme in ("light", "dark"):
            for n, t in leaves(T[theme]):
                m = re.search(r"(--[\w-]+)", t["$extensions"].get("source", ""))
                declared = t["$extensions"].get("declared")
                if declared is None or not m or m.group(1) not in RES[theme]:
                    continue
                self.assertEqual(declared, RES[theme][m.group(1)]["raw"], f"{theme}.{n}")
                checked += 1
        self.assertGreater(checked, 0)

    def test_heading_does_not_borrow_the_display_measurement(self):
        ty = T["core"]["typography"]
        self.assertIn("measured", ty["display"]["$extensions"])
        self.assertNotIn("measured", ty["heading"]["$extensions"])


class ComponentsMdTest(unittest.TestCase):
    def test_no_raw_lab_readings(self):
        self.assertIsNone(re.search(r"\b(ok)?(lab|lch)\(", (PKG / "components.md").read_text()))

    def test_unlab(self):
        node = next(n for n in ast.parse((HERE / "build_components_md.py").read_text()).body
                    if isinstance(n, ast.FunctionDef) and n.name == "unlab")
        ns = {"re": re}
        exec(compile(ast.Module([node], []), "unlab", "exec"), ns)
        self.assertEqual(ns["unlab"]("oklab(0.561988 -0.023436 -0.238834 / 0.5)"), "rgba(41, 98, 255, 0.5)")
        self.assertEqual(ns["unlab"]("lab(48.7982% 67.6999 48.8037)"), "rgb(220, 38, 38)")


class StyleGuideTest(unittest.TestCase):
    def test_esc_escapes_quotes(self):
        src = (HERE / "style-guide.template.html").read_text()
        self.assertIn("'\"':'&quot;'", src)


if __name__ == "__main__":
    unittest.main()
