"""Rebuild checks for the Docusign builders. Run from this folder, or via tools/package_tests.py.

The builders run on a temporary copy of tools/ and raw/ (screenshots and crops by name only),
so nothing committed is rewritten.
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


def flat(tree, path=""):
    for k, v in tree.items():
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


def hexof(c):
    r, g, b, *a = (float(x) for x in re.findall(r"[\d.]+", c))
    return "#%02x%02x%02x" % (int(r), int(g), int(b)) if not a or a[0] == 1 else "rgba(%d, %d, %d, %g)" % (r, g, b, a[0])


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

    def reading(self, key, state, prop):
        return self.C[key]["states"][state]["style"][prop]

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)
        self.assertEqual((PKG / "components.md").read_text(), self.md)

    def test_no_unsupported_error_colour(self):
        self.assertNotIn("core.color.error", self.tok)

    def test_measured_sources_name_the_reading_they_hold(self):
        # Every leaf sourced "measured components-computed.json: <key> <state> <prop>" equals that reading.
        checked = 0
        for path, leaf in self.tok.items():
            src = leaf["$extensions"]["source"]
            v = leaf["$value"]
            if not src.startswith("measured components-computed.json: ") or not isinstance(v, str) or v.startswith("{"):
                continue
            for ref in src.split(": ", 1)[1].split("; "):
                parts = ref.split(" ")
                if len(parts) != 3 or parts[0] not in self.C:
                    continue
                raw = self.reading(*parts)
                want = hexof(raw) if leaf["$type"] == "color" else raw
                if leaf["$type"] == "duration":
                    want = "%gms" % (float(raw[:-1]) * 1000)
                self.assertEqual(v, want, f"{path} cites {ref}")
                checked += 1
        self.assertGreater(checked, 60)

    def test_recited_values(self):
        self.assertEqual(self.tok["core.color.ink-70"]["$value"], hexof(self.reading("ec-billing-monthly", "default", "color")))
        self.assertEqual(self.tok["core.color.violet-30"]["$value"], hexof(self.reading("sg-clear", "default", "color")))
        self.assertEqual(self.tok["core.color.violet-50"]["$value"], hexof(self.reading("sg-download", "default", "color")))
        self.assertEqual(self.tok["core.duration.panel"]["$value"], "300ms")
        self.assertEqual(self.reading("sg-download", "default", "transitionDuration"), "0.3s")
        self.assertEqual(self.tok["core.font.size.label"]["$value"], self.reading("nav-search", "default", "fontSize"))
        self.assertEqual(self.tok["core.font.lineHeight.body"]["$value"], self.reading("nav-dropdown", "default", "lineHeight"))

    def test_typed_values_say_so(self):
        for p in ("core.font.size.h4", "core.font.lineHeight.h4", "core.font.tracking.h4", "core.font.tracking.eyebrow"):
            self.assertTrue(self.tok[p]["$extensions"]["source"].startswith("Reconstruction:"), p)
        self.assertIn("focus failed", self.tok["core.color.focus-green"]["$extensions"]["source"])

    def test_shadows_keep_inset(self):
        self.assertTrue(self.tok["core.shadow.field-focus"]["$value"][0].get("inset"))
        self.assertTrue(self.tok["core.shadow.hairline-inset"]["$value"][0].get("inset"))
        self.assertFalse(any(l.get("inset") for l in self.tok["core.shadow.ring-double"]["$value"]))

    def test_transparent_outline_is_not_a_ring(self):
        ring = re.search(r"(\d+) draw an outline ring: (.*?)\. \d+ draw a focus ring as a shadow instead: ([^.]*)\.", self.md)
        self.assertIsNotNone(ring)
        self.assertNotIn("`buy-now`", ring.group(2))
        self.assertIn("`buy-now`", ring.group(3))
        self.assertNotIn("transparent", ring.group(2))

    def test_failed_focus_is_listed_not_measured(self):
        self.assertIn("Focus could not be captured on 3 more", self.md)
        self.assertIn("(the marketing .dark islands appear inside light shots)", self.md)


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
        entry = built.split("#### sg-download\n")[1].split("\n#### ")[0]
        self.assertIn("| Skipped |", entry)

if __name__ == "__main__":
    unittest.main()
