#!/usr/bin/env python3
"""Check tokens.json against the readings in raw/.

The token file is the capture record. This script does not invent values.
It fails when a semantic colour in tokens.json is absent from raw/css-vars.json, and it refuses:
  - a token whose source is missing or does not start with an evidence label;
  - a literal colour that no file under raw/ holds (hex, rgb() or rgba(), compared as
    lower-case #rrggbb or #rrggbbaa, alpha rounded half up);
  - an alias that does not resolve (in its own set, then core, then the root) or that loops.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = HERE / "raw"
CSS = json.loads((RAW / "css-vars.json").read_text())
# The evidence labels of docs/EVIDENCE.md, plus this package's own words for them:
# "Computed" is a computed-style reading (Measured), "Alias" a token that points at another.
# A reading entered by hand that no raw/ file holds says so at the start of its source; the colour
# check passes it, because the source already says it is not backed by raw/.
BY_HAND = "Reconstruction: entered by hand at capture time; no raw/ file holds this reading"
LABELS = ("Measured", "Derived", "Sampled", "Observed", "Reconstruction", "Not captured", "Computed", "Alias")
RESOLVED = CSS["home"]["resolved"]

EXPECTED = {
    "dark.accent": ("#ff5e3e", "--semantic-primary"),
    "dark.surface": ("#171717", "--semantic-background"),
    "dark.text-muted": ("#ffffff80", "--semantic-muted-foreground"),
    "dark.focus": ("#3773f5", "--semantic-focus-ring"),
    "dark.success": ("#17f455", "--semantic-success"),
    "dark.destructive": ("#ef4444", "--semantic-destructive"),
    "dark.muted": ("#ffffff1a", "--semantic-muted"),
    "dark.surface-card": ("#1b1b1b", "--semantic-surface-card"),
}


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
    out = list(source_problems(tokens))
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
        by_hand = str((tok.get("$extensions") or {}).get("source", "")).startswith(BY_HAND)
        if tok.get("$type") == "color" and isinstance(v, str) and not v.startswith("{") and not by_hand:
            if not colours_in(v) <= seen or not colours_in(v):
                out.append(f"{path}: {v} is in no file under raw/")
    return out


def source_problems(tokens):
    for path, tok in tokens_in(tokens):
        src = (tok.get("$extensions") or {}).get("source")
        if not isinstance(src, str) or not src.strip():
            yield f"{path}: missing $extensions.source"
        elif not src.startswith(LABELS):
            yield f"{path}: source does not start with an evidence label"


def load_raw():
    return [json.loads(p.read_text()) for p in sorted(RAW.glob("*.json"))]


def value(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return node["$value"]


def main():
    failed = False
    for path, (want, var) in EXPECTED.items():
        got = value(path)
        declared = RESOLVED.get(var, "")
        if got != want or declared.lower() != want:
            print(f"{path}: token {got} reading {var}={declared} expected {want}", file=sys.stderr)
            failed = True
    if "--font-tertiary" not in RESOLVED or "Phonic" not in RESOLVED["--font-tertiary"]:
        print("missing Phonic in --font-tertiary", file=sys.stderr)
        failed = True
    for line in problems(TOKENS, load_raw()):
        print(line, file=sys.stderr)
        failed = True
    if failed:
        return 1
    print("tokens match raw/css-vars.json and every colour, alias and source checks out")
    return 0


if __name__ == "__main__":
    sys.exit(main())
