"""Xbox tokens resolve and use measured colour forms."""
import json
import pathlib
import unittest

TOKENS = pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


class TokensTest(unittest.TestCase):
    def test_file_parses_and_names_both_themes(self):
        doc = json.loads(TOKENS.read_text())
        self.assertIn("core", doc)
        self.assertIn("light", doc)
        self.assertIn("dark", doc)
        self.assertEqual(doc["light"]["action"]["primary"]["$value"], "{core.color.lime}")
        self.assertEqual(doc["core"]["color"]["lime"]["$value"], "#9bf00b")
        self.assertEqual(doc["core"]["color"]["storeGreen"]["$value"], "#008746")


# ---- every token records where its value came from (docs/EVIDENCE.md)
import json as _json
import pathlib as _pathlib

_TOKENS_FILE = _pathlib.Path(__file__).resolve().parent.parent / "tokens.json"


def _unsourced(node, path=()):
    """Dotted paths of leaves whose $extensions.source is missing or empty."""
    out = []
    for key, child in node.items():
        if key.startswith("$") or not isinstance(child, dict):
            continue
        if "$value" in child:
            source = (child.get("$extensions") or {}).get("source")
            if not source:
                out.append(".".join(path + (key,)))
        else:
            out.extend(_unsourced(child, path + (key,)))
    return out


class EverySourcedTest(unittest.TestCase):
    def test_every_token_has_a_source(self):
        missing = _unsourced(_json.loads(_TOKENS_FILE.read_text()))
        self.assertEqual(missing, [], "tokens with no $extensions.source")

    def test_unsourced_leaf_is_reported(self):
        tree = {"core": {"a": {"$value": "#000", "$extensions": {"source": {}}},
                         "b": {"$value": "#fff", "$extensions": {"source": {"evidence": "Measured"}}}}}
        self.assertEqual(_unsourced(tree), ["core.a"])


# ---- every alias resolves (own set, then core, then the root path)
import json as _json
import pathlib as _pathlib
import re as _re

_ALIAS_TOKENS_FILE = _pathlib.Path(__file__).resolve().parent.parent / "tokens.json"
_ALIAS = _re.compile(r"\{([^{}]+)\}")


def _alias_leaves(tree):
    flat = {}

    def walk(node, path):
        for key, child in node.items():
            if key.startswith("$") or not isinstance(child, dict):
                continue
            if "$value" in child:
                flat[".".join(path + [key])] = child
            else:
                walk(child, path + [key])

    walk(tree, [])
    return flat


def _alias_refs(value):
    if isinstance(value, str):
        return _ALIAS.findall(value)
    if isinstance(value, dict):
        value = list(value.values())
    if isinstance(value, list):
        return [ref for item in value for ref in _alias_refs(item)]
    return []


def _alias_target(flat, path, ref):
    own = path.split(".")[0]
    for candidate in (f"{own}.{ref}", f"core.{ref}", ref):
        if candidate in flat:
            return candidate
    return None


def dead_aliases(tree):
    """Aliases that point at nothing, at themselves, or round a cycle. Every reference inside a
    target's value (a string, or any string in a list or object) is followed, with the chain of
    token paths walked so far, so a cycle through a list or composite value is found too."""
    flat = _alias_leaves(tree)
    bad = []

    def walk(start, ref, cur_path, chain):
        target = _alias_target(flat, cur_path, ref)
        if target is None:
            return f"{start}: {{{ref}}} points at nothing"
        if target in chain:
            return f"{start}: {{{ref}}} loops back on itself"
        for nxt in _alias_refs(flat[target]["$value"]):
            err = walk(start, nxt, target, chain | {target})
            if err:
                return err
        return None

    for path, node in flat.items():
        for ref in _alias_refs(node["$value"]):
            err = walk(path, ref, path, {path})
            if err:
                bad.append(err)
    return bad


class AliasesResolveTest(unittest.TestCase):
    def test_every_alias_resolves(self):
        tree = _json.loads(_ALIAS_TOKENS_FILE.read_text())
        self.assertEqual(dead_aliases(tree), [])

    def test_dead_top_level_alias_fails(self):
        tree = {"core": {"a": {"$value": "#000000", "$type": "color"}},
                "light": {"page": {"$value": "{color.nope}", "$type": "color"}}}
        self.assertEqual(len(dead_aliases(tree)), 1)

    def test_dead_alias_inside_typography_fails(self):
        tree = {"core": {"a": {"$value": "#000000", "$type": "color"}},
                "light": {"body": {"$type": "typography",
                                   "$value": {"fontFamily": "{font.nope}", "fontSize": "16px"}}}}
        self.assertEqual(len(dead_aliases(tree)), 1)

    def test_self_reference_and_cycle_fail(self):
        tree = {"core": {"a": {"$value": "{a}", "$type": "color"},
                         "b": {"$value": "{c}", "$type": "color"},
                         "c": {"$value": "{b}", "$type": "color"}}}
        self.assertEqual(len(dead_aliases(tree)), 3)

    def test_cycle_through_list_values_fails(self):
        tree = {"core": {"a": {"$value": ["{b}"], "$type": "fontFamily"},
                         "b": {"$value": ["{a}"], "$type": "fontFamily"}}}
        self.assertEqual(len(dead_aliases(tree)), 2)

    def test_alias_resolves_in_own_set_then_core_then_root(self):
        tree = {"core": {"x": {"$value": "#111111", "$type": "color"}},
                "light": {"x": {"$value": "#222222", "$type": "color"},
                          "p": {"$value": "{x}", "$type": "color"},
                          "q": {"$value": "{core.x}", "$type": "color"}}}
        self.assertEqual(dead_aliases(tree), [])
        self.assertEqual(_alias_target(_alias_leaves(tree), "light.p", "x"), "light.x")


if __name__ == "__main__":
    unittest.main()
