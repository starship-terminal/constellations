"""tokens.json and style-guide.html are what the builders write; labels say how values were read."""
import json
import pathlib
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import build_tokens  # noqa: E402  (writes only when run as a script)


class Tokens(unittest.TestCase):
    def test_committed_file_matches_builder(self):
        self.assertEqual((ROOT / "tokens.json").read_text(), build_tokens.TEXT)

    def test_durations_are_durations(self):
        for name, tok in json.loads(build_tokens.TEXT)["core"]["motion"]["duration"].items():
            self.assertEqual(tok["$type"], "duration", name)
            self.assertRegex(tok["$value"], r"^\d+ms$")

    def test_screenshot_and_stand_in_values_are_not_measured(self):
        doc = json.loads(build_tokens.TEXT)
        self.assertTrue(doc["light"]["color"]["border"]["$extensions"]["source"].startswith("Observed."))
        self.assertTrue(doc["core"]["radius"]["pill"]["$extensions"]["source"].startswith("Reconstruction."))


class StyleGuide(unittest.TestCase):
    def test_hostile_names_and_values_stay_escaped(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            pkg = pathlib.Path(tmp) / "pkg"
            shutil.copytree(ROOT, pkg, ignore=shutil.ignore_patterns("screenshots", "components", "boards", "raw"))
            doc = json.loads((pkg / "tokens.json").read_text())
            doc["light"]["color"]['x"<b>&'] = {"$type": "color", "$value": '#000000" onclick="x', "$extensions": {"source": "test"}}
            doc["core"]["spacing"]["evil"] = {"$type": "dimension", "$value": '1px"><script>', "$extensions": {"source": "test"}}
            (pkg / "tokens.json").write_text(json.dumps(doc))
            subprocess.run([sys.executable, str(pkg / "tools" / "build_style_guide.py")], check=True, capture_output=True)
            html = (pkg / "style-guide.html").read_text()
            for raw in ('x"<b>&', '" onclick="x', '"><script>'):
                self.assertNotIn(raw, html)
            self.assertIn("x&quot;&lt;b&gt;&amp;", html)
            self.assertIn("#000000&quot; onclick=&quot;x", html)

    def test_committed_guide_matches_builder(self):
        with tempfile.TemporaryDirectory() as tmp:
            pkg = pathlib.Path(tmp) / "pkg"
            shutil.copytree(ROOT, pkg, ignore=shutil.ignore_patterns("screenshots", "components", "boards", "raw"))
            subprocess.run([sys.executable, str(pkg / "tools" / "build_style_guide.py")], check=True, capture_output=True)
            self.assertEqual((pkg / "style-guide.html").read_text(), (ROOT / "style-guide.html").read_text())


if __name__ == "__main__":
    unittest.main()
