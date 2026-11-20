"""The Playbook tokens resolve, and the measured colours stay the measured colours."""

import json
import unittest
from pathlib import Path

TOKENS = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())


def resolve(value, seen=None):
    if not isinstance(value, str) or not value.startswith("{") or not value.endswith("}"):
        return value
    seen = seen or set()
    path = value[1:-1]
    if path in seen:
        raise AssertionError(f"alias loop at {path}")
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"], seen | {path})


class Tokens(unittest.TestCase):
    def test_measured_colours(self):
        self.assertEqual(TOKENS["core"]["color"]["page-dark"]["$value"], "#0d0e10")
        self.assertEqual(TOKENS["core"]["color"]["blue"]["$value"], "#599ffe")
        self.assertEqual(TOKENS["core"]["color"]["auth-primary"]["$value"], "#ff5d64")
        self.assertEqual(TOKENS["core"]["color"]["ink"]["$value"], "#1a1a1a")

    def test_aliases_resolve(self):
        self.assertEqual(resolve(TOKENS["light"]["surface"]["page"]["$value"]), "#ffffff")
        self.assertEqual(resolve(TOKENS["dark"]["surface"]["page"]["$value"]), "#0d0e10")
        self.assertEqual(resolve(TOKENS["dark"]["accent"]["$value"]), "#599ffe")
        self.assertEqual(resolve(TOKENS["light"]["accent"]["$value"]), "#1a1a1a")

    def test_themes(self):
        names = [theme["name"] for theme in TOKENS["$themes"]]
        self.assertEqual(names, ["light", "dark"])

    def test_every_token_has_a_source(self):
        # docs/EVIDENCE.md: every value says where it came from.
        doc = json.loads((Path(__file__).resolve().parent.parent / "tokens.json").read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                if not node.get("$extensions", {}).get("source"):
                    missing.append(path)
            elif isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(doc, "")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
