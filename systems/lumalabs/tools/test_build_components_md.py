"""Checks for the Luma AI components builder. Run from this folder, or via tools/package_tests.py.

The builder runs in a scratch folder that links the package's inputs, so the committed
components.md is compared with a fresh build without being rewritten.
"""
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

PKG = pathlib.Path(__file__).resolve().parent.parent
BUILDER = PKG / "tools" / "build_components_md.py"


def build(raw_dir=None):
    with tempfile.TemporaryDirectory() as d:
        root = pathlib.Path(d)
        (root / "tools").mkdir()
        shutil.copy(BUILDER, root / "tools" / BUILDER.name)
        for name in ("screenshots", "components", "icons", "tokens.json"):
            if (PKG / name).exists():
                os.symlink(PKG / name, root / name)
        os.symlink(raw_dir or PKG / "raw", root / "raw")
        run = subprocess.run([sys.executable, str(root / "tools" / BUILDER.name)], capture_output=True, text=True)
        out = (root / "components.md").read_text() if (root / "components.md").exists() else None
        return run, out


class ComponentsMdTest(unittest.TestCase):
    def test_committed_components_md_matches_build(self):
        run, out = build()
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(out, (PKG / "components.md").read_text())

    def test_no_rows_from_another_product(self):
        text = (PKG / "components.md").read_text()
        for word in ("Gauth", "Homework", "Atlas", "lesson", "Academy", "Insights page"):
            self.assertNotIn(word, text)

    def test_every_linked_file_exists(self):
        text = (PKG / "components.md").read_text()
        links = re.findall(r"\]\(((?:screenshots|components|raw|icons)/[^)#\s]+)\)", text)
        self.assertTrue(links)
        self.assertEqual([t for t in links if not (PKG / t).exists()], [])

    def test_plan_card_body_reading_is_not_published(self):
        text = (PKG / "components.md").read_text()
        entry = text.split("#### Plan card", 1)[1].split("####", 1)[0]
        self.assertIn("Recapture needed", entry)
        self.assertNotIn("1440 x 18434", text)

    def test_a_failed_focus_is_not_counted_as_a_reading(self):
        import json
        with tempfile.TemporaryDirectory() as d:
            raw = pathlib.Path(d) / "raw"
            shutil.copytree(PKG / "raw", raw)
            v = json.loads((raw / "components-computed.json").read_text())
            v["components"]["nav-product"]["states"]["focus-visible"]["via"] = "focus failed"
            (raw / "components-computed.json").write_text(json.dumps(v))
            run, out = build(raw)
        self.assertEqual(run.returncode, 0, run.stderr)
        focus = out.split("**Focus.**", 1)[1].split("\n", 1)[0]
        self.assertIn("6 components were given a real keyboard focus", focus)
        self.assertIn("Focus could not be captured on 1 more", focus)
        self.assertNotIn("nav-product-focus-visible.png", out)

    def test_a_dead_link_fails_the_build(self):
        with tempfile.TemporaryDirectory() as d:
            raw = pathlib.Path(d) / "raw"
            shutil.copytree(PKG / "raw", raw)
            src = (raw / "components-computed.json").read_text()
            # point one crop at a file that is not in the package
            src = src.replace("components/crops/hero-cta-default.png", "components/crops/no-such-crop.png", 1)
            (raw / "components-computed.json").write_text(src)
            run, _ = build(raw)
        self.assertNotEqual(run.returncode, 0)
        self.assertIn("do not exist", run.stderr)


if __name__ == "__main__":
    unittest.main()
