#!/usr/bin/env python3
"""Skillshare tokens stay inside the measured set."""
import json, pathlib, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

MEASURED = {
    "#ffffff", "#000000", "#0b1215", "#394649", "#dcdce1", "#55da9b",
    "#50cf93", "#5620c1", "#fafafa", "#f4f4f4", "#070c0e", "#002333",
    "#232424",
}


class Tokens(unittest.TestCase):
    def test_light_only(self):
        self.assertEqual([t["id"] for t in T["$themes"]], ["light"])
        self.assertNotIn("dark", T)

    def test_accent_is_measured_mint(self):
        self.assertEqual(T["light"]["color"]["accent"]["$value"], "#55da9b")
        self.assertEqual(T["light"]["color"]["link"]["$value"], "#5620c1")

    def test_hex_colours_were_measured(self):
        for name, tok in T["light"]["color"].items():
            value = tok["$value"]
            if isinstance(value, str) and value.startswith("#"):
                self.assertIn(value, MEASURED, name)

    def test_control_radius(self):
        self.assertEqual(T["core"]["radius"]["control"]["$value"], "4px")


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
    """Aliases that point at nothing, at themselves, or round a cycle."""
    flat = _alias_leaves(tree)
    bad = []
    for path, node in flat.items():
        for ref in _alias_refs(node["$value"]):
            seen, cur_path, cur_ref = {path}, path, ref
            while True:
                target = _alias_target(flat, cur_path, cur_ref)
                if target is None:
                    bad.append(f"{path}: {{{ref}}} points at nothing")
                    break
                if target in seen:
                    bad.append(f"{path}: {{{ref}}} loops back on itself")
                    break
                seen.add(target)
                value = flat[target]["$value"]
                whole = _ALIAS.fullmatch(value) if isinstance(value, str) else None
                if not whole:
                    break
                cur_path, cur_ref = target, whole.group(1)
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

    def test_alias_resolves_in_own_set_then_core_then_root(self):
        tree = {"core": {"x": {"$value": "#111111", "$type": "color"}},
                "light": {"x": {"$value": "#222222", "$type": "color"},
                          "p": {"$value": "{x}", "$type": "color"},
                          "q": {"$value": "{core.x}", "$type": "color"}}}
        self.assertEqual(dead_aliases(tree), [])
        self.assertEqual(_alias_target(_alias_leaves(tree), "light.p", "x"), "light.x")


if __name__ == "__main__":
    unittest.main()
