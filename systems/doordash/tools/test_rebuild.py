"""Rebuild checks for the DoorDash builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots and crops by name only),
so nothing committed is rewritten.
"""
import json
import pathlib
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict) and not k.startswith("$"):
            yield from flat(v, p)


def hexof(rgb):
    r, g, b = (int(x) for x in rgb[rgb.index("(") + 1:rgb.index(")")].split(",")[:3])
    return "#%02x%02x%02x" % (r, g, b)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for d in ("screenshots", "components/crops"):
            (root / d).mkdir(parents=True)
            for f in (PKG / d).glob("*.png"):
                (root / d / f.name).touch()
        for b in ("build_component_tokens.py", "build_tokens.py", "build_components_md.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.md = (root / "components.md").read_text()
        cls.tok = dict(flat(cls.built))
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)
        self.assertEqual((PKG / "components.md").read_text(), self.md)

    def test_text_tokens_are_the_first_text_node(self):
        for key, comp in (("offerBadge", "offer-badge"), ("heroBand", "hero-band"), ("footer", "footer")):
            want = self.C[comp]["states"]["default"]["textStyle"]["color"]
            self.assertEqual(self.tok[f"light.component.{key}.text"]["$value"], hexof(want), key)
        self.assertNotEqual(self.tok["light.component.offerBadge.text"]["$value"], "#0000ee")
        self.assertIn("not confirmed", self.tok["light.component.menuItem.text"]["$extensions"]["source"])

    def test_shadows_are_dtcg_layers(self):
        for path, leaf in self.tok.items():
            if leaf["$type"] == "shadow" and not str(leaf["$value"]).startswith("{"):
                self.assertIsInstance(leaf["$value"], list, path)
        self.assertEqual(self.tok["core.elevation.none"]["$value"][0]["color"], "rgba(25, 25, 25, 0)")

    def test_shadow_parser_keeps_inset_and_refuses_what_it_cannot_read(self):
        # the temp copy's build_tokens.py, run as a module (it rewrites only the temp tokens.json)
        ns = runpy.run_path(str(pathlib.Path(self.tmp.name) / "tools" / "build_tokens.py"))
        layers = ns["parse_shadow"]("t", "rgba(0, 0, 0, 0.2) 0px 1px 2px 0px inset, inset 0 0 0 1px #fff")
        self.assertEqual([l.get("inset") for l in layers], [True, True])
        self.assertEqual(layers[1]["spread"], "1px")
        self.assertEqual(ns["parse_shadow"]("t", "0px 6px 6px -3px rgb(0, 0, 0)")[0]["spread"], "-3px")
        with self.assertRaises(ValueError):
            ns["parse_shadow"]("t", "rgba(0, 0, 0, 0.2) 0px 1px 2px, var(--x)")
        with self.assertRaises(ValueError):
            ns["parse_shadow"]("t", "none")

    def test_browser_defaults_are_labelled(self):
        self.assertIn("browser default (Times 16/normal 400, #000000)", self.md)
        self.assertNotIn("Times 16/normal 400, #000000 `color.black`", self.md)
        self.assertIn("Focus could not be captured on 6 more", self.md)


    def test_measurements_rebuild_matches(self):
        node = shutil.which("node")
        if not node:
            self.skipTest("node is not installed")
        root = pathlib.Path(self.tmp.name)
        (root / "tools" / "capture" / "public").mkdir(parents=True, exist_ok=True)
        shutil.copy(PKG / "tools" / "capture" / "css-colour.mjs", root / "tools" / "capture")
        shutil.copy(PKG / "tools" / "capture" / "public" / "build-measurements.mjs", root / "tools" / "capture" / "public")
        subprocess.run([node, str(root / "tools" / "capture" / "public" / "build-measurements.mjs")], cwd=root, check=True, capture_output=True)
        built = (root / "raw" / "measurements.md").read_text()
        self.assertEqual((PKG / "raw" / "measurements.md").read_text(), built)
        # a failed keyboard focus reads Skipped, never the element at rest
        entry = built.split("#### tab-selected\n")[1].split("\n#### ")[0]
        self.assertIn("| Skipped |", entry)

if __name__ == "__main__":
    unittest.main()
