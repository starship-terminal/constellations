import json
import pathlib
import subprocess
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent

class BuildTokens(unittest.TestCase):
    def test_rebuild_matches(self):
        before = (PKG / "tokens.json").read_text()
        subprocess.run(["python3", str(HERE / "build_tokens.py")], check=True, cwd=PKG)
        after = (PKG / "tokens.json").read_text()
        self.assertEqual(before, after)

    def test_primary_is_measured(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["primary"]["$value"], "#513a06")
        self.assertEqual(tokens["core"]["color"]["primaryLight"]["$value"], "#b4ff6a")
        self.assertEqual(tokens["light"]["page"]["$value"], "{color.backgroundLight}")

if __name__ == "__main__":
    unittest.main()
