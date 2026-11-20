#!/usr/bin/env python3
"""Check The New York Times' hand-written tokens.json against the captured readings.

The package writes tokens.json by hand from raw/computed.json and raw/tokens-resolved.json. This
script does not rebuild it. It refuses a token file that:
  - has a token with no source or with an evidence label docs/EVIDENCE.md does not use
    ("Declared", this package's word for a declared custom property, is accepted too);
  - has a literal colour that no raw/ file holds (hex, rgb() or rgba(), compared as lower-case
    #rrggbb or #rrggbbaa), unless the token is labelled Reconstruction;
  - has an alias ({a.b}), at any depth of a value, that does not resolve in its own set, then
    core, then the root, or that loops;
  - has drifted from the painted masthead, ink, accent and login readings it was written from.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LABELS = {"Measured", "Derived", "Sampled", "Observed", "Reconstruction", "Not captured", "Declared"}


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, f"{path}.{k}" if path else k)


def norm(h):
    h = h.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 8 and h.endswith("ff"):
        h = h[:6]
    return "#" + h


def colour(text):
    """A hex, rgb() or rgba() value in the one form raw_colours() uses; anything else lower-cased."""
    t = text.strip().lower()
    if t.startswith("#"):
        return norm(t)
    found = raw_colours([t])
    return found.pop() if len(found) == 1 else t


def raw_colours(raw_texts):
    seen = set()
    for text in raw_texts:
        for m in re.finditer(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b", text):
            seen.add(norm(m.group(1)))
        for m in re.finditer(r"rgba?\(\s*(\d+)[,\s]+(\d+)[,\s]+(\d+)(?:\s*[,/]\s*([\d.]+))?\s*\)", text):
            h = "#%02x%02x%02x" % tuple(int(x) for x in m.groups()[:3])
            if m.group(4) is not None and float(m.group(4)) < 1:
                h += "%02x" % int(float(m.group(4)) * 255 + 0.5)
            seen.add(h)
    return seen


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)


def lookup(tree, dotted):
    node = tree
    for part in dotted.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node if isinstance(node, dict) and "$value" in node else None


def find(tokens, setname, ref):
    """The full path a reference resolves to: its own set, then core, then the root (the
    Resolver's order), or None."""
    for prefix in (f"{setname}.", "core.", ""):
        full = prefix + ref
        if lookup(tokens, full) is not None:
            return full
    return None


def follow(tokens, path, ref, chain):
    """Follow ref from the token at full path `path`; each hop resolves from the target's own set
    and the chain holds full paths, so only a true loop is a cycle."""
    full = find(tokens, path.split(".", 1)[0], ref)
    if full is None:
        return f"dead alias {{{ref}}}"
    if full in chain:
        return f"alias cycle at {{{ref}}}"
    for text in strings(lookup(tokens, full)["$value"]):
        for nxt in re.findall(r"\{([^{}]+)\}", text):
            err = follow(tokens, full, nxt, chain | {full})
            if err:
                return err
    return None


def problems(tokens, raw_texts):
    seen = raw_colours(raw_texts)
    out = []
    for path, tok in walk(tokens):
        source = (tok.get("$extensions") or {}).get("source")
        label = source.get("evidence") if isinstance(source, dict) else None
        if not source:
            out.append(f"{path}: no source")
        elif label not in LABELS:
            out.append(f"{path}: evidence label {label!r} is not one docs/EVIDENCE.md uses")
        for text in strings(tok["$value"]):
            for ref in re.findall(r"\{([^{}]+)\}", text):
                err = follow(tokens, path, ref, {path})
                if err:
                    out.append(f"{path}: {err}")
        v = tok["$value"]
        if (tok.get("$type") == "color" and isinstance(v, str) and not v.startswith("{")
                and label != "Reconstruction" and colour(v) not in seen):
            out.append(f"{path}: {v} is in no raw/ reading")
    return out


def drift(tokens, computed):
    checks = {
        "core.color.ink": (tokens["core"]["color"]["ink"]["$value"], "#121212"),
        "core.color.masthead": (tokens["core"]["color"]["masthead"]["$value"], "#567b95"),
        "core.color.accent": (tokens["core"]["color"]["accent"]["$value"], "#346eb7"),
        "subscribe bg": (computed["home"]["subscribe"]["backgroundColor"], "rgb(86, 123, 149)"),
        "login continue": (computed["login"]["continue"]["backgroundColor"], "rgb(18, 18, 18)"),
        "login radius": (computed["login"]["continue"]["borderRadius"], "3px"),
    }
    return [f"drift: {name}" for name, (got, want) in checks.items() if got != want]


def main() -> int:
    tokens = json.loads((ROOT / "tokens.json").read_text())
    computed = json.loads((ROOT / "raw" / "computed.json").read_text())
    raw_texts = [p.read_text() for p in sorted((ROOT / "raw").glob("*.json"))]
    bad = problems(tokens, raw_texts) + drift(tokens, computed)
    if bad:
        print("\n".join(bad), file=sys.stderr)
        return 1
    print(f"{sum(1 for _ in walk(tokens))} tokens checked against raw/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
