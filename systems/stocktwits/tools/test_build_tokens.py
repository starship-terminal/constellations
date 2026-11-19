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

    def test_measured_roles(self):
        tokens = json.loads((PKG / "tokens.json").read_text())
        self.assertEqual(tokens["core"]["color"]["blue5"]["$value"], "#1b66e7")
        self.assertEqual(tokens["light"]["page"]["$value"], "{color.white}")
        self.assertEqual(tokens["dark"]["page"]["$value"], "{color.stDarkGrey6}")
        self.assertEqual(tokens["light"]["positive"]["$value"], "{color.greenLight}")
        self.assertEqual(tokens["dark"]["negative"]["$value"], "{color.redDark}")
        self.assertEqual(tokens["core"]["radius"]["full"]["$value"], "9999px")


if __name__ == "__main__":
    unittest.main()
