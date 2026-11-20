#!/usr/bin/env python3
"""Skillshare tokens: every literal colour is a raw/ reading."""
import json, pathlib, re, unittest

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def raw_colours(package):
    """Every colour a raw/ file holds, as lower-case #rrggbb or #rrggbbaa (hex, rgb() and rgba())."""
    seen = set()
    for f in sorted((package / "raw").rglob("*")):
        if not f.is_file() or f.suffix not in (".json", ".md", ".txt", ".css"):
            continue
        text = f.read_text(errors="replace").lower()
        for h in re.findall(r"#([0-9a-f]{8}|[0-9a-f]{6}|[0-9a-f]{3,4})\b", text):
            h = "".join(c * 2 for c in h) if len(h) in (3, 4) else h
            seen.add("#" + (h[:6] if len(h) == 8 and h.endswith("ff") else h))
        for m in re.finditer(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", text):
            h = "#%02x%02x%02x" % tuple(int(x) for x in m.groups()[:3])
            if m.group(4) and float(m.group(4)) < 1:
                h += "%02x" % int(float(m.group(4)) * 255 + 0.5)
            seen.add(h)
    return seen


def colour_form(value):
    """A literal colour (hex, rgb() or rgba()) in the form raw_colours() uses; anything else as written."""
    v = value.strip().lower()
    if v.startswith("#"):
        h = v[1:]
        h = "".join(c * 2 for c in h) if len(h) in (3, 4) else h
        return "#" + (h[:6] if len(h) == 8 and h.endswith("ff") else h)
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", v)
    if not m:
        return v
    h = "#%02x%02x%02x" % tuple(int(x) for x in m.groups()[:3])
    if m.group(4) and float(m.group(4)) < 1:
        h += "%02x" % int(float(m.group(4)) * 255 + 0.5)
    return h


def literal_colours(node, path=""):
    """(path, value, source) for every colour token with a literal (non-alias) value, in every set
    and group; hex, rgb() and rgba() all come back in raw_colours()'s form."""
    if isinstance(node, dict) and "$value" in node:
        v = node["$value"]
        if node.get("$type") == "color" and isinstance(v, str) and not v.strip().startswith("{"):
            yield path, colour_form(v), (node.get("$extensions") or {}).get("source", "")
        return
    if isinstance(node, dict):
        for k, child in node.items():
            if not k.startswith("$"):
                yield from literal_colours(child, f"{path}.{k}" if path else k)



class Tokens(unittest.TestCase):
    def test_light_only(self):
        self.assertEqual([t["id"] for t in T["$themes"]], ["light"])
        self.assertNotIn("dark", T)

    def test_accent_is_measured_mint(self):
        self.assertEqual(T["light"]["color"]["accent"]["$value"], "#55da9b")
        self.assertEqual(T["light"]["color"]["link"]["$value"], "#5620c1")

    def test_unrecorded_rgba_colour_is_caught(self):
        tree = {"core": {"zz": {"$type": "color", "$value": "rgba(1, 2, 3, 0.5)",
                                "$extensions": {"source": "Measured: test"}}}}
        found = list(literal_colours(tree))
        self.assertEqual(found[0][1], "#01020380")
        self.assertNotIn(found[0][1], raw_colours(HERE))

    def test_literal_colours_are_in_raw(self):
        """Every literal colour, in every set and nested group, is a colour some raw/ file holds,
        unless its source says it was entered by hand (Reconstruction)."""
        seen = raw_colours(HERE)
        found = list(literal_colours(T))
        self.assertTrue(found, "no colour tokens")
        for path, value, source in found:
            if source.startswith("Reconstruction"):
                continue
            with self.subTest(token=path):
                short = value[:7] if len(value) == 9 and value.endswith("ff") else value
                self.assertIn(short, seen, value)

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
