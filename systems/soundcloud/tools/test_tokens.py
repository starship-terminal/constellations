#!/usr/bin/env python3
"""SoundCloud tokens: every literal colour is a raw/ reading or labelled hand-entered."""
import json, re, pathlib, unittest

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
    def test_both_themes(self):
        self.assertEqual([t["id"] for t in T["$themes"]], ["dark", "light"])

    def test_page_and_accent(self):
        self.assertEqual(T["dark"]["color"]["page"]["$value"], "#121212")
        self.assertEqual(T["dark"]["color"]["accent"]["$value"], "#ff5500")
        self.assertEqual(T["light"]["color"]["page"]["$value"], "#ffffff")

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

    def test_pill_radius(self):
        self.assertEqual(T["core"]["radius"]["pill"]["$value"], "9999px")


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


if __name__ == "__main__":
    unittest.main()
