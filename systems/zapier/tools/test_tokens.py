"""Zapier token file checks. Run from systems/zapier/tools."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


class TokenTest(unittest.TestCase):
    def test_checker_passes_and_catches_a_self_alias(self):
        import sys
        sys.path.insert(0, str(TOKENS.parent / "tools"))
        import build_tokens
        data = json.loads(TOKENS.read_text())
        self.assertEqual(build_tokens.problems(data), [])
        # The committed file once held light.color.status.danger = {color.status.danger}, which
        # resolves set-first to itself.
        data["light"]["color"]["status"]["danger"]["$value"] = "{color.status.danger}"
        self.assertTrue(any("alias cycle" in p for p in build_tokens.problems(data)))

    def test_checker_follows_aliases_inside_composite_values(self):
        import sys
        sys.path.insert(0, str(TOKENS.parent / "tools"))
        import build_tokens
        data = json.loads(TOKENS.read_text())
        data["core"]["typography"]["display"]["$value"]["fontSize"] = "{font.size.missing}"
        self.assertIn("core.typography.display: alias {font.size.missing} points at nothing",
                      build_tokens.problems(data))

    def test_every_token_has_a_source(self):
        data = json.loads(TOKENS.read_text())
        missing = [path for path, token in walk(data) if "source" not in token.get("$extensions", {})]
        self.assertEqual(missing, [])

    def test_light_only(self):
        data = json.loads(TOKENS.read_text())
        self.assertIn("light", data)
        self.assertNotIn("dark", data)
        self.assertEqual(data["light"]["color"]["action"]["fill"]["$value"], "{color.brand.orange}")
        self.assertEqual(data["core"]["color"]["brand"]["orange"]["$value"], "#ff4f00")


if __name__ == "__main__":
    unittest.main()
