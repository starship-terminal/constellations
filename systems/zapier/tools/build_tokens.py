#!/usr/bin/env python3
"""Zapier tokens are written from live readings, not rebuilt by this kit copy.

The committed tokens.json is the source. This file stays so the kit layout is
present. It checks that every token has a source and that every alias resolves, set first and
then core, without pointing at itself, to a hex colour where the token is a colour.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            yield from walk(child, f"{path}.{key}" if path else key)


def resolve(flat, path, depth=0):
    """Follow an alias the way tools/catalog.py's Resolver does: the token's own set, then core,
    then the root. Returns the final value, or raises on a dangling alias or a cycle."""
    if depth > 12:
        raise ValueError(f"{path}: alias cycle")
    value = flat[path]["$value"]
    match = re.fullmatch(r"\{([^{}]+)\}", value.strip()) if isinstance(value, str) else None
    if not match:
        return value
    ref, own = match.group(1), path.split(".")[0]
    for candidate in (f"{own}.{ref}", f"core.{ref}", ref):
        if candidate in flat:  # a self-reference loops here, as it does in the Resolver
            return resolve(flat, candidate, depth + 1)
    raise ValueError(f"{path}: alias {{{ref}}} points at nothing")


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, dict):
        for v in value.values():
            yield from strings(v)
    elif isinstance(value, list):
        for v in value:
            yield from strings(v)


def resolve_nested(flat, path, value):
    """Follow every alias inside an object or list value (a typography's fontSize, a shadow's
    colour) from the token's own set, the same way resolve() follows a whole-value alias."""
    own = path.split(".")[0]
    for text in strings(value):
        for ref in re.findall(r"\{([^{}]+)\}", text):
            for candidate in (f"{own}.{ref}", f"core.{ref}", ref):
                if candidate in flat:
                    inner = resolve(flat, candidate)
                    if isinstance(inner, (dict, list)):
                        resolve_nested(flat, candidate, inner)
                    break
            else:
                raise ValueError(f"{path}: alias {{{ref}}} points at nothing")


def problems(data):
    out = []
    flat = {path: token for path, token in walk(data)}
    for path, token in flat.items():
        if "source" not in token.get("$extensions", {}):
            out.append(f"{path}: no $extensions.source")
        try:
            value = resolve(flat, path)
            if isinstance(value, (dict, list)):
                resolve_nested(flat, path, value)
        except ValueError as err:
            out.append(str(err))
            continue
        if token["$type"] == "color" and not re.fullmatch(r"#[0-9a-fA-F]{6}([0-9a-fA-F]{2})?", str(value)):
            out.append(f"{path}: colour {value!r} is not hex")
    return out


def check():
    data = json.loads(TOKENS.read_text())
    bad = problems(data)
    if bad:
        raise SystemExit("\n".join(bad))
    print(f"{len(list(walk(data)))} tokens, each with a source, every alias resolving to a hex colour or value")


if __name__ == "__main__":
    check()
    sys.exit(0)
