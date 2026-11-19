"""The committed tokens resolve, and the measured Prose ink is the value that was read."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def resolve(data, value, seen=None):
    seen = seen or set()
    if not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    ref = value[1:-1]
    if ref in seen:
        raise AssertionError("alias cycle: %s" % ref)
    seen.add(ref)
    node = data
    for part in ref.split("."):
        node = node[part]
    return resolve(data, node["$value"], seen)


class TokensTest(unittest.TestCase):
    def test_primary_ink_is_measured(self):
        data = json.loads(TOKENS.read_text())
        self.assertEqual(data["core"]["color"]["primary"]["400"]["$value"], "#323429")
        self.assertEqual(resolve(data, data["light"]["bg"]["action"]["$value"]), "#323429")
        self.assertEqual(data["light"]["focus"]["ring"]["$value"], "#e59700")
        self.assertIn("light", data)
        self.assertNotIn("dark", data)


if __name__ == "__main__":
    unittest.main()
