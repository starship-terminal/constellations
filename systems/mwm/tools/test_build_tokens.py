"""The token builder is deterministic and keeps the measured orange."""
import json
import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent


class BuildTokens(unittest.TestCase):
    def test_orange_is_measured(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["dark"]["color"]["orange"]["$value"], "#ff5301")
        self.assertEqual(tokens["dark"]["color"]["page"]["$value"], "#0c0c0c")
        self.assertEqual(tokens["core"]["font"]["size"]["display"]["$value"], "72px")
        self.assertEqual(tokens["light"], {})

    def test_rebuild_is_stable(self):
        before = (PKG / "tokens.json").read_text()
        subprocess.run([sys.executable, str(HERE / "build_tokens.py")], check=True, cwd=PKG)
        self.assertEqual((PKG / "tokens.json").read_text(), before)


if __name__ == "__main__":
    unittest.main()
