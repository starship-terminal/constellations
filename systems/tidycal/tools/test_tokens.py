"""The committed tokens match the colours measured on tidycal.com."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = json.loads((ROOT / "tokens.json").read_text())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


class Tokens(unittest.TestCase):
    def test_painted_primary_is_the_button(self):
        self.assertEqual(TOKENS["core"]["color"]["accent-paint"]["$value"], "#1569ef")
        self.assertEqual(TOKENS["light"]["color"]["accent"]["$value"], "{core.color.accent-paint}")

    def test_link_token_stays_separate_from_the_button(self):
        self.assertEqual(TOKENS["core"]["color"]["accent"]["$value"], "#0053ee")

    def test_page_and_text(self):
        self.assertEqual(TOKENS["light"]["color"]["page"]["$value"], "{core.color.page}")
        self.assertEqual(TOKENS["core"]["color"]["page"]["$value"], "#ffffff")
        self.assertEqual(TOKENS["core"]["color"]["text"]["$value"], "#212529")

    def test_control_radius(self):
        self.assertEqual(TOKENS["core"]["radius"]["control"]["$value"], "8px")
        self.assertEqual(TOKENS["core"]["radius"]["card"]["$value"], "16px")

    def test_every_token_has_a_source(self):
        missing = [path for path, node in walk(TOKENS) if "source" not in node.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_light_only(self):
        self.assertNotIn("dark", TOKENS)
        self.assertEqual([theme["id"] for theme in TOKENS["$themes"]], ["light"])


if __name__ == "__main__":
    unittest.main()
