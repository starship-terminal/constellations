#!/usr/bin/env python3
"""Check systems/mymind/tokens.json.

The public site does not publish a token file. tokens.json was written by hand
from computed styles in raw/computed.json, read on 2026-11-19. This script does
not rebuild those values. It refuses a token with no source, an alias that
points at nothing or at itself (resolved set first, then core), a dimension
that is not one px length, and a measured colour no reading holds.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TOKENS = HERE.parent / "tokens.json"
LENGTH = re.compile(r"^-?\d+(\.\d+)?px$")


def walk(node, path, found):
    if isinstance(node, dict) and "$value" in node:
        found.append((path, node))
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            walk(child, f"{path}.{key}" if path else key, found)


def resolve(value, sets, order, seen=frozenset()):
    """Resolve aliases the way tools/catalog.py's Resolver and Tokens Studio do: the token's own set
    first, then core. An alias inside light that names a light token resolves to that light token,
    so light.color.link = {color.link} pointed at itself."""
    if isinstance(value, dict):
        return {key: resolve(child, sets, order, seen) for key, child in value.items()}
    if isinstance(value, list):
        return [resolve(child, sets, order, seen) for child in value]
    if not isinstance(value, str) or not (value.startswith("{") and value.endswith("}")):
        return value
    ref = value[1:-1]
    for name in order:
        node = sets[name].get(ref)
        if node is not None:
            key = (name, ref)
            if key in seen:
                raise ValueError(f"alias cycle at {name}.{ref}")
            # Continue from the referenced token's own set, as the catalog Resolver does: an alias that
            # led into core resolves its next step in core, not back in light.
            return resolve(node["$value"], sets, ORDER[name], seen | {key})
    raise ValueError(f"alias {value} points at nothing in {' or '.join(order)}")


ORDER = {"core": ("core",), "light": ("light", "core")}
RAW = HERE.parent / "raw" / "computed.json"


def raw_colours():
    """Every rgb()/rgba() colour in raw/computed.json, as lowercase hex (alpha only when not 1)."""
    text = RAW.read_text()
    out = set()
    for m in re.finditer(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", text):
        hx = "#%02x%02x%02x" % tuple(int(m.group(i)) for i in (1, 2, 3))
        if m.group(4) is not None and float(m.group(4)) < 1:
            hx += "%02x" % round(float(m.group(4)) * 255)
        out.add(hx)
    return out


def check(data, colours=None):
    """Refuse a token with no evidence or capture, an alias that points at nothing or at itself, a
    dimension that is not one px length, a colour that is not hex, and a literal Measured colour that
    no reading in raw/computed.json holds (tokens.json is hand-written, so this is its drift check)."""
    colours = raw_colours() if colours is None else colours
    sets = {}
    for group in ("core", "light"):
        if group not in data:
            raise ValueError(f"missing {group} set")
        found = []
        walk(data[group], "", found)
        sets[group] = dict(found)
    problems = []
    count = 0
    for group, order in (("core", ("core",)), ("light", ("light", "core"))):
        for path, node in sets[group].items():
            count += 1
            where = f"{group}.{path}"
            source = (node.get("$extensions") or {}).get("source") or {}
            if source.get("evidence") not in ("Measured", "Derived"):
                problems.append(f"{where}: missing evidence")
            if not source.get("capture"):
                problems.append(f"{where}: missing capture")
            try:
                value = resolve(node["$value"], sets, order, frozenset({(group, path)}))
            except ValueError as e:
                problems.append(f"{where}: {e}")
                continue
            if node.get("$type") == "dimension" and not LENGTH.match(str(value)):
                problems.append(f"{where}: dimension {value!r} is not one px length")
            if node.get("$type") == "color" and not re.fullmatch(r"#[0-9a-fA-F]{6,8}", str(value)):
                problems.append(f"{where}: colour {value!r} is not hex")
            literal = node["$value"]
            if (node.get("$type") == "color" and isinstance(literal, str) and literal.startswith("#")
                    and source.get("evidence") == "Measured" and literal.lower() not in colours):
                problems.append(f"{where}: measured colour {literal} is in no reading in raw/computed.json")
    if problems:
        raise ValueError("\n".join(problems))
    return count


def main():
    data = json.loads(TOKENS.read_text())
    count = check(data)
    print(f"tokens.json: {count} tokens, sources resolve")
    return 0


if __name__ == "__main__":
    sys.exit(main())
