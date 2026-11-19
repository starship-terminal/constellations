"""Package tests for the Microsoft Copilot capture. Run from tools/ via package_tests.py."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class Tokens(unittest.TestCase):
    def test_measured_dark_page_and_button(self):
        tokens = json.loads((ROOT / "tokens.json").read_text())
        self.assertEqual(tokens["dark"]["background"]["page"]["$value"], "#1f1f1f")
        self.assertEqual(tokens["dark"]["component"]["button"]["bg"]["$value"], "#ffffff")
        self.assertEqual(tokens["dark"]["component"]["button"]["radius"]["$value"], "16px")
        self.assertEqual(tokens["core"]["radius"]["card"]["$value"], "24px")
        for name, tok in walk(tokens["dark"]):
            self.assertIn("source", tok.get("$extensions", {}), name)

    def test_screenshots_exist(self):
        shots = ROOT / "screenshots"
        for name in ("home-dark-default.png", "home-dark-mobile.png", "login-light-default.png"):
            self.assertTrue((shots / name).is_file(), name)
            side = json.loads((shots / (name + ".capture.json")).read_text())
            self.assertIn("innerWidth", side.get("measured", {}))


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}{key}"
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path + ".")


if __name__ == "__main__":
    unittest.main()
