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
        self.assertEqual(tokens["light"]["page"]["$value"], "#ffffff")
        self.assertEqual(tokens["light"]["text"]["$value"], "#171717")
        self.assertEqual(tokens["light"]["accent"]["$value"], "#3b82f6")
        self.assertEqual(tokens["core"]["color"]["marketing"]["cyan"]["$value"], "#00a8f5")
        self.assertEqual(tokens["core"]["radius"]["claim"]["$value"], "26px")
        self.assertEqual(tokens["core"]["typography"]["display"]["$value"]["fontSize"], "51px")
        self.assertIn("duration", tokens["core"]["motion"])


if __name__ == "__main__":
    unittest.main()
