"""Rebuild checks for the Expedia builders. Run from this folder, or via tools/package_tests.py.

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


def flat(tree, path=""):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        p = f"{path}.{k}" if path else k
        if isinstance(v, dict) and "$value" in v:
            yield p, v
        elif isinstance(v, dict):
            yield from flat(v, p)


class RebuildTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        root = pathlib.Path(cls.tmp.name)
        shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
        shutil.copytree(PKG / "raw", root / "raw")
        for b in ("build_component_tokens.py", "build_tokens.py"):
            subprocess.run([sys.executable, str(root / "tools" / b)], cwd=root, check=True, capture_output=True)
        # the components builder lists screenshots and counts crops by file name: mirror the names
        for d in ("screenshots", "components/crops"):
            (root / d).mkdir(parents=True)
            for f in (PKG / d).glob("*.png"):
                (root / d / f.name).touch()
        subprocess.run([sys.executable, str(root / "tools" / "build_components_md.public.py")], cwd=root, check=True, capture_output=True)
        cls.root = root
        cls.built = json.loads((root / "tokens.json").read_text())
        cls.spec = json.loads((root / "raw" / "component-tokens.json").read_text())
        cls.C = json.loads((PKG / "raw" / "components-computed.json").read_text())["components"]

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_committed_output_matches_rebuild(self):
        self.assertEqual(json.loads((PKG / "tokens.json").read_text()), self.built)
        self.assertEqual(json.loads((PKG / "raw" / "component-tokens.json").read_text()), self.spec)

    def test_components_md_matches_rebuild(self):
        self.assertEqual((PKG / "components.md").read_text(), (self.root / "components.md").read_text())

    def test_measured_leaves_name_a_real_reading(self):
        n = 0
        for path, leaf in flat(self.built["core"]["measured"]):
            m = re.match(r"measured (\S+) (\S+) \(", leaf["$extensions"]["source"])
            self.assertTrue(m, path)
            comp, state = m.groups()
            self.assertIn(state, self.C[comp]["states"], f"{path}: {comp} has no {state} reading")
            n += 1
        self.assertGreater(n, 15)

    def test_browser_default_focus_ring_is_not_published(self):
        sty = self.C["search-submit"]["states"]["focus-visible"]["style"]
        self.assertEqual((sty["outlineStyle"], sty["outlineColor"]), ("auto", "rgb(16, 16, 16)"))
        self.assertNotIn("outlineColor", self.built["core"]["measured"]["focus"])
        self.assertIn("core.measured.focus.outlineColor", {g["token"] for g in self.spec["_gaps"]})

    def _build_with(self, edit):
        """Run build_component_tokens.py on a temp copy whose readings `edit` changed."""
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            shutil.copytree(PKG / "tools", root / "tools", ignore=shutil.ignore_patterns("capture", "__pycache__"))
            shutil.copytree(PKG / "raw", root / "raw")
            raw = json.loads((root / "raw" / "components-computed.json").read_text())
            edit(raw["components"])
            (root / "raw" / "components-computed.json").write_text(json.dumps(raw))
            return subprocess.run([sys.executable, str(root / "tools" / "build_component_tokens.py")], cwd=root, capture_output=True, text=True)

    def test_builder_stops_when_a_cited_state_is_missing(self):
        r = self._build_with(lambda c: c["search-submit"]["states"].pop("focus-visible"))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("search-submit focus-visible", r.stderr)

    def test_builder_stops_on_a_component_flagged_missing(self):
        # a subset capture that did not find search-submit keeps its old states and flags it
        r = self._build_with(lambda c: c["search-submit"].update(missing=True))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("flagged missing", r.stderr)

    def test_builder_stops_on_a_missing_colour(self):
        r = self._build_with(lambda c: c["search-submit"]["states"]["default"]["style"].pop("color"))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("core.measured.button.search.text", r.stderr)

    def test_marketing_band_labels_from_its_own_palette(self):
        md = (PKG / "components.md").read_text()
        block = md.split("Read as `marketing-band`", 1)[1].split("\n#### ", 1)[0]
        labels = re.findall(r"`(color\.palette\.[a-zA-Z0-9]+)\.", block)
        self.assertTrue(labels)
        self.assertEqual(set(labels), {"color.palette.marketing3"})

    def test_style_guide_fetches_nothing(self):
        html = (PKG / "style-guide.html").read_text()
        self.assertNotIn("fonts.googleapis.com", html)
        self.assertNotIn("fonts.gstatic.com", html)


if __name__ == "__main__":
    unittest.main()
