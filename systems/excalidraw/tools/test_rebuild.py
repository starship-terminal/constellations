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
        # raw/measurements.md comes from the capture folder's build-measurements.mjs; copy only it
        # and the colour helper it imports, and run it on the temp copy.
        cls.measurements = None
        if shutil.which("node"):
            (root / "tools" / "capture" / "public").mkdir(parents=True)
            shutil.copy(PKG / "tools" / "capture" / "css-colour.mjs", root / "tools" / "capture")
            shutil.copy(PKG / "tools" / "capture" / "public" / "build-measurements.mjs", root / "tools" / "capture" / "public")
            subprocess.run(["node", str(root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                           cwd=root, check=True, capture_output=True)
            cls.measurements = (root / "raw" / "measurements.md").read_text()
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
        """An older capture saved a failed keyboard focus as the element at rest with via 'focus
        failed'; build-measurements.mjs must show it as Skipped, with no values. The record is made
        here on a temp copy, so the test does not depend on what the committed capture holds."""
        if self.measurements is None:
            self.skipTest("node is not installed")
        self.assertEqual((PKG / "raw" / "measurements.md").read_text(), self.measurements)
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(pathlib.Path(self.tmp.name) / "tools", root / "tools")
            shutil.copytree(PKG / "raw", root / "raw")
            raw = json.loads((root / "raw" / "components-computed.json").read_text())
            k = next(k for k, c in raw["components"].items() if "style" in (c["states"].get("focus-visible") or {}))
            st = raw["components"][k]["states"]["focus-visible"]
            raw["components"][k]["states"]["focus-visible"] = {**st, "via": "focus failed"}
            (root / "raw" / "components-computed.json").write_text(json.dumps(raw))
            subprocess.run(["node", str(root / "tools" / "capture" / "public" / "build-measurements.mjs")],
                           cwd=root, check=True, capture_output=True)
            md = (root / "raw" / "measurements.md").read_text()
        block = md.split(f"#### {k}\n", 1)[1].split("\n#### ", 1)[0]
        cells = lambda r: [c.strip() for c in r.strip().strip("|").split("|")]  # noqa: E731
        table = [cells(r) for r in block.splitlines() if r.startswith("| ") and not r.startswith("|---")]
        col = table[0].index("focus-visible")
        self.assertIn("Skipped", [row[0] for row in table[1:]])
        for row in table[1:]:
            if row[0] == "Skipped":
                self.assertTrue(row[col].startswith("focus failed"), k)
            else:
                # "-" (no value), or "=" where the first state has no value either
                self.assertIn(row[col], ("-", "=") if row[1] == "-" else ("-",), f"{k}: {row}")

    def test_skipped_focus_keeps_its_note(self):
        """A newer capture records a failed focus as {skipped, via} with no style; components.md
        still has to say focus could not be captured on that component."""
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(pathlib.Path(self.tmp.name) / "tools", root / "tools", ignore=shutil.ignore_patterns("capture"))
            shutil.copytree(PKG / "raw", root / "raw")
            shutil.copy(PKG / "tokens.json", root / "tokens.json")
            raw = json.loads((root / "raw" / "components-computed.json").read_text())
            k = next(k for k, c in raw["components"].items() if "style" in (c["states"].get("focus-visible") or {}))
            raw["components"][k]["states"]["focus-visible"] = {
                "skipped": "focus failed: keyboard focus did not reach the element", "via": "focus failed"}
            (root / "raw" / "components-computed.json").write_text(json.dumps(raw))
            subprocess.run([sys.executable, str(root / "tools" / "build_components_md.py")], cwd=root, check=True, capture_output=True)
            md = (root / "components.md").read_text()
            block = md.split(f"Read as `{k}`", 1)[1].split("\n#### ", 1)[0]
            self.assertIn("Focus not capturable", block)

    def test_docs_cite_only_existing_tokens(self):
        names = set()
        for theme in ("core", "light", "dark"):
            names |= {f"{theme}.{n}" for n, _ in flat(self.built[theme])}
        for doc in ("patterns.md", "components.md"):
            for m in set(re.findall(r"`((?:core|light|dark)\.[A-Za-z0-9._-]+)`", (PKG / doc).read_text())):
                self.assertTrue(m in names or any(n.startswith(m + ".") for n in names), f"{doc} cites {m}")


if __name__ == "__main__":
    unittest.main()
