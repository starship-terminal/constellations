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
        problems = []

        def lookup(set_name, ref):
            # set-first, then core, then the document root ({core.color...})
            for root in (data[set_name], data["core"], data):
                node = root
                for part in ref.strip("{}").split("."):
                    node = node.get(part) if isinstance(node, dict) else None
                if isinstance(node, dict) and "$value" in node:
                    return node
            return None

        def refs(value):
            if isinstance(value, str) and value.startswith("{"):
                yield value
            elif isinstance(value, dict):
                for v in value.values():
                    yield from refs(v)
            elif isinstance(value, list):
                for v in value:
                    yield from refs(v)

        def follow(set_name, ref, trail):
            if ref in trail:
                problems.append("alias loop: " + " -> ".join(trail + [ref]))
                return
            node = lookup(set_name, ref)
            if node is None:
                problems.append(" -> ".join(trail + [ref]) + " resolves to nothing")
                return
            for nxt in refs(node["$value"]):
                follow(set_name, nxt, trail + [ref])

        def walk(node, set_name, path):
            if isinstance(node, dict) and "$value" in node:
                source = node.get("$extensions", {}).get("source")
                if not (isinstance(source, dict) and source.get("evidence")):
                    problems.append(f"{path} has no source with an evidence label")
                for ref in refs(node["$value"]):
                    follow(set_name, ref, ["{" + path.split(".", 1)[1] + "}"])
                return
            if isinstance(node, dict):
                for key, child in node.items():
                    if not key.startswith("$"):
                        walk(child, set_name, f"{path}.{key}")

        walk(data["core"], "core", "core")
        walk(data["light"], "light", "light")
        self.assertEqual(problems, [])


if __name__ == "__main__":
    unittest.main()
