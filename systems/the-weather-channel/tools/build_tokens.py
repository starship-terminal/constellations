#!/usr/bin/env python3
"""Check tokens.json for The Weather Channel against raw/.

Values were read from the live public page and written by hand into tokens.json, which is
the source of truth. This script does not invent tokens. It refuses:
  - a token whose source is missing or carries no evidence label;
  - a colour that is not a hex or rgba value, and a dimension that is not a px length;
  - a literal colour that no file under raw/ holds (hex, rgb() or rgba(), compared as
    lower-case #rrggbb or #rrggbbaa, alpha rounded half up);
  - an alias that does not resolve (in its own set, then core, then the root) or that loops.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"
RAW = HERE / "raw"
COLOR = re.compile(r"^(#[0-9a-fA-F]{6}|rgba?\([^)]+\))$")
DIM = re.compile(r"^\d+(\.\d+)?px$")
EVIDENCE = {"Measured", "Derived", "Sampled", "Observed", "Reconstruction", "Not captured"}


def walk(node, path, errors):
    if not isinstance(node, dict):
        return
    if "$value" in node:
        if "$extensions" not in node or "source" not in node.get("$extensions", {}):
            errors.append(f"{path}: missing $extensions.source")
        else:
            label = node["$extensions"]["source"].get("evidence")
            if label not in EVIDENCE:
                errors.append(f"{path}: evidence {label!r} is not a known label")
            if not node["$extensions"]["source"].get("where"):
                errors.append(f"{path}: source has no where")
        kind = node.get("$type")
        value = node["$value"]
        if kind == "color" and not (isinstance(value, str) and COLOR.match(value)):
            errors.append(f"{path}: colour {value!r} is not hex or rgb")
        if kind == "dimension" and not (isinstance(value, str) and DIM.match(value)):
            errors.append(f"{path}: dimension {value!r} is not a px length")
        if kind == "cubicBezier":
            if not (isinstance(value, list) and len(value) == 4):
                errors.append(f"{path}: easing is not four numbers")
        return
    for key, child in node.items():
        if key.startswith("$"):
            continue
        walk(child, f"{path}.{key}" if path else key, errors)


def check(data):
    errors = []
    for group in ("core", "light"):
        if group not in data:
            errors.append(f"missing {group} set")
        else:
            walk(data[group], group, errors)
    if "dark" in data:
        errors.append("dark set is present; the public page had no dark theme")
    return errors


KEYWORDS = {"black": "#000000", "white": "#ffffff", "transparent": "#00000000"}


def norm(h):
    """#abc, #abcd, #aabbcc, #aabbccdd -> lower-case #rrggbb[aa]; an opaque alpha is dropped."""
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 8 and h.endswith("ff"):
        h = h[:6]
    return "#" + h


def colours_in(text, words=True):
    """Every colour a string holds, as lower-case #rrggbb[aa]. Alpha rounds half up."""
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
    for word, h in (KEYWORDS.items() if words else ()):
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


def tokens_in(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from tokens_in(v, f"{path}.{k}" if path else k)


def lookup(tree, dotted):
    node = tree
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node if isinstance(node, dict) and "$value" in node else None


def resolve(tokens, setname, ref, seen):
    """None when the alias reaches a literal, else the reason it does not."""
    # Own set, then core, then the root, as tools/catalog.py's Resolver does. The next hop resolves
    # from the set the token was found in, and loops are tracked by (set, path within it).
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


def problems(tokens, raw):
    """Everything wrong with tokens against the readings in raw (a parsed raw/ file)."""
    out = list(check(tokens))
    seen = set()
    for s in strings(raw):
        seen |= colours_in(s, words=False)
    for path, tok in tokens_in(tokens):
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
        if tok.get("$type") == "color" and isinstance(v, str) and not v.startswith("{"):
            if not colours_in(v) <= seen or not colours_in(v):
                out.append(f"{path}: {v} is in no file under raw/")
    return out


def load_raw():
    return [json.loads(p.read_text()) for p in sorted(RAW.glob("*.json"))]


def main():
    data = json.loads(TOKENS.read_text())
    errors = problems(data, load_raw())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"{TOKENS.name}: ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
