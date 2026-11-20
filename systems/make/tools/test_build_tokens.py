"""tokens.json and components.md are what the builders write from raw/, built in memory."""
import json
import pathlib
import subprocess
import sys
import tempfile
import shutil
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_capture_viewports_are_not_measured(self):
        layout = json.loads(build_tokens.TEXT)["core"]["layout"]
        for name in ("desktop", "phone"):
            self.assertTrue(layout[name]["$extensions"]["source"].startswith("Reconstruction"), name)


class Components(unittest.TestCase):
    def build(self):
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "pkg"
            shutil.copytree(ROOT, copy, ignore=shutil.ignore_patterns("screenshots", "components", "icons", "boards"))
            subprocess.run([sys.executable, str(copy / "tools" / "build_components_md.py")], check=True, capture_output=True)
            return (copy / "components.md").read_text()

    def test_committed_file_matches_builder(self):
        self.assertEqual(self.build(), (ROOT / "components.md").read_text())

    def test_transparent_fill_is_not_black(self):
        text = self.build()
        nav = text.split("## Nav primary action", 1)[1].split("\n## ", 1)[0]
        self.assertIn("| transparent |", nav)
        self.assertNotIn("#000000", nav)


if __name__ == "__main__":
    unittest.main()
