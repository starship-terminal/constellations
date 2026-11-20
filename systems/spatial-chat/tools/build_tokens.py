#!/usr/bin/env python3
"""Check SpatialChat's hand-written tokens.json against raw/readings.json.

The kit builder expects a css-vars dump this capture does not have, so tokens.json was written
by hand from raw/readings.json and is the source of truth. This script does not rebuild it; it
refuses a token file that:
  - has a token whose source does not start with "Measured" or "Derived";
  - has a literal colour that no reading in raw/readings.json holds (hex, rgb() or rgba(),
    compared as lower-case #rrggbb or #rrggbbaa);
  - has an alias ({a.b}) that does not resolve in its own set, then core, then the root, or
    that loops back on itself.
"""
import json, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve().parent.parent
KEYWORDS = {"black": "#000000", "white": "#ffffff", "transparent": "#00000000"}


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if k.startswith("$"):
                continue
            yield from walk(v, f"{path}.{k}" if path else k)


def norm(h):
    """#abc, #abcd, #aabbcc, #aabbccdd -> lower-case #rrggbb[aa]; an opaque alpha is dropped."""
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 8 and h.endswith("ff"):
        h = h[:6]
    return "#" + h


def colours_in(text):
    out = set()
    for m in re.finditer(r"#([0-9a-fA-F]{3,8})\b", text):
        if len(m.group(1)) in (3, 4, 6, 8):
            out.add(norm(m.group(1)))
    for m in re.finditer(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", text):
        h = "#%02x%02x%02x" % tuple(int(x) for x in m.groups()[:3])
        a = m.group(4)
        if a is not None:
            alpha = float(a[:-1]) / 100 if a.endswith("%") else float(a)
            if alpha < 1:
                h += "%02x" % int(alpha * 255 + 0.5)
        out.add(h)
    for word, h in KEYWORDS.items():
        if re.search(r"\b%s\b" % word, text):
            out.add(h)
    return out


def strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for k, v in node.items():
            yield k
            yield from strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from strings(v)


def lookup(tree, dotted):
    node = tree
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node if isinstance(node, dict) and "$value" in node else None


def resolve(tokens, setname, ref, seen):
    """None when the alias reaches a literal, else the reason it does not. A name resolves in its own
    set, then core, then the root (a set-qualified name such as core.palette.white); the next hop
    resolves from the set the target was found in, and loops are tracked by (set, path)."""
    candidates = [(setname, ref), ("core", ref)]
    if "." in ref:
        candidates.append(tuple(ref.split(".", 1)))
    for found_set, found_path in candidates:
        tok = lookup(tokens.get(found_set, {}), found_path)
        if tok is None:
            continue
        if (found_set, found_path) in seen:
            return f"alias cycle at {{{ref}}}"
        v = tok["$value"]
        inner = re.fullmatch(r"\{([^{}]+)\}", v) if isinstance(v, str) else None
        return resolve(tokens, found_set, inner.group(1), seen | {(found_set, found_path)}) if inner else None
    return f"dead alias {{{ref}}}"


def problems(tokens, readings):
    seen = set()
    for s in strings(readings):
        seen |= colours_in(s)
    out = []
    for path, tok in walk(tokens):
        src = (tok.get("$extensions") or {}).get("source", "")
        if not src.startswith(("Measured", "Derived")):
            out.append(f"{path}: source is not Measured or Derived")
        setname = path.split(".", 1)[0]
        v = tok["$value"]
        values = v.values() if isinstance(v, dict) else v if isinstance(v, list) else [v]
        for item in values:
            if not isinstance(item, str):
                continue
            for ref in re.findall(r"\{([^{}]+)\}", item):
                err = resolve(tokens, setname, ref, set())
                if err:
                    out.append(f"{path}: {err}")
        for literal in literal_colours(tok):
            if colour_form(literal) not in seen:
                out.append(f"{path}: {literal} is in no reading in raw/readings.json")
    return out


def colour_form(value):
    """A token's literal colour (hex, rgb() or rgba()) in the same form colours_in() gives readings."""
    v = value.strip().lower()
    if v.startswith("#"):
        return norm(v)
    if v in KEYWORDS:
        return KEYWORDS[v]
    m = re.fullmatch(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+%?))?\s*\)", v)
    if not m:
        return v
    h = "#%02x%02x%02x" % tuple(int(x) for x in m.groups()[:3])
    a = m.group(4)
    if a is not None:
        alpha = float(a[:-1]) / 100 if a.endswith("%") else float(a)
        if alpha < 1:
            h += "%02x" % int(alpha * 255 + 0.5)
    return h


def literal_colours(tok):
    """The non-alias colour strings a token holds: a colour's value, or each layer's colour in a shadow."""
    v = tok["$value"]
    if tok.get("$type") == "color":
        layers = [v]
    elif tok.get("$type") == "shadow":
        layers = [layer.get("color") for layer in (v if isinstance(v, list) else [v]) if isinstance(layer, dict)]
    else:
        layers = []
    return [c for c in layers if isinstance(c, str) and not c.strip().startswith("{")]


def main():
    tokens = json.loads((HERE / "tokens.json").read_text())
    readings = json.loads((HERE / "raw" / "readings.json").read_text())
    bad = problems(tokens, readings)
    if bad:
        sys.exit("tokens.json fails its checks:\n  " + "\n  ".join(bad))
    print(f"spatial-chat: {sum(1 for _ in walk(tokens))} tokens checked against raw/readings.json")


if __name__ == "__main__":
    main()
