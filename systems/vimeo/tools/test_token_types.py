"""Every dimension token is one px or rem length, and every duration is typed duration (finding 16-11)."""
import json
import pathlib
import re
import unittest

TOKENS = json.loads((pathlib.Path(__file__).resolve().parent.parent / "tokens.json").read_text())


def walk(node, path=""):
    for key, value in node.items():
        if key.startswith("$") or not isinstance(value, dict):
            continue
        if "$value" in value:
            yield f"{path}{key}", value
        else:
            yield from walk(value, f"{path}{key}.")


class TokenTypes(unittest.TestCase):
    def test_dimensions_are_one_length_and_durations_are_durations(self):
        for set_name in [k for k in TOKENS if not k.startswith("$") and isinstance(TOKENS[k], dict)]:
            for path, token in walk(TOKENS[set_name]):
                value = token["$value"]
                if not isinstance(value, str) or value.startswith("{"):
                    continue
                with self.subTest(token=f"{set_name}.{path}"):
                    if token["$type"] == "dimension":
                        self.assertRegex(value, r"^-?\d+(\.\d+)?(px|rem)$")
                    if re.fullmatch(r"\d+(\.\d+)?m?s", value):
                        self.assertEqual(token["$type"], "duration")


if __name__ == "__main__":
    unittest.main()
