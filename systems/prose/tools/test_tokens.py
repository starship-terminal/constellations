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

    def test_every_token_has_a_source_and_every_alias_resolves(self):
        data = json.loads(TOKENS.read_text())
        missing = []

        def walk(node, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source")
                if not source or (isinstance(source, dict) and not source.get("evidence")):
                    missing.append(path)
                value = node["$value"]
                if isinstance(value, str) and value.startswith("{"):
                    # set-first, then core, then the document root ({core.color...})
                    ref = value[1:-1].split(".")
                    hit = None
                    for root in (data[path.split(".")[0]], data["core"], data):
                        hit = root
                        for part in ref:
                            hit = hit.get(part) if isinstance(hit, dict) else None
                        if isinstance(hit, dict) and "$value" in hit:
                            break
                        hit = None
                    if hit is None:
                        missing.append(f"{path} -> {value} resolves to nothing")
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, f"{path}.{key}" if path else key)

        walk(data["core"], "core")
        walk(data["light"], "light")
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
