"""Rebuild checks for the Excalidraw builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/, so nothing committed is rewritten.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
ALIAS_SRC = re.compile(r"css-var (--\S+) \(declared as var\((--[^)]+)\) and kept as an alias\)")


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def declared(V, var, theme):
    """The theme's own declaration of var: the dark override when there is one, else .excalidraw's."""
    rules = {r["selector"]: r["properties"][var].strip() for r in V["theme"]
             if r["selector"] in (".excalidraw", ".excalidraw.theme--dark") and not r["context"] and var in r["properties"]}
    return rules.get(".excalidraw.theme--dark") if theme == "dark" and ".excalidraw.theme--dark" in rules else rules.get(".excalidraw")


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.V = json.loads((PKG / "raw" / "css-vars.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_every_alias_is_the_themes_own_declaration(self):
        for theme in ("light", "dark"):
            for path, leaf in flat(self.built[theme]):
                m = ALIAS_SRC.fullmatch(leaf["$extensions"]["source"])
                if not m:
                    continue
                var, target = m.groups()
                self.assertEqual(declared(self.V, var, theme), f"var({target})", f"{theme}.{path}")
                self.assertIn(target, self.V["resolved"][theme], f"{theme}.{path} names a variable raw/ does not hold")

    def test_dark_scrollbar_carries_the_dark_declaration(self):
        bar = self.built["dark"]["control"]["scrollbar"]
        RD = self.V["resolved"]["dark"]
        self.assertEqual(bar["thumb"]["$value"], RD["--scrollbar-thumb"]["value"])
        self.assertEqual(bar["thumb-hover"]["$value"], RD["--scrollbar-thumb-hover"]["value"])
        self.assertEqual(bar["thumb"]["$value"], "#343a40")

    def test_display_family_is_the_computed_stack(self):
        fam = self.built["core"]["font"]["family"]
        self.assertEqual(fam["display"]["$value"], self.C["welcome-logo"]["states"]["default"]["style"]["fontFamily"])
        self.assertTrue(fam["mono"]["$extensions"]["source"].startswith("Reconstruction:"))

    def test_failed_focus_is_not_published_as_a_reading(self):
        md = (PKG / "raw" / "measurements.md").read_text()
        failed = [k for k, c in self.C.items() if (c["states"].get("focus-visible") or {}).get("via") == "focus failed"]
        self.assertTrue(failed)
        for k in failed:
            block = md.split(f"#### {k}\n", 1)[1].split("\n#### ", 1)[0]
            self.assertIn("| Skipped |", block, k)


if __name__ == "__main__":
    unittest.main()
