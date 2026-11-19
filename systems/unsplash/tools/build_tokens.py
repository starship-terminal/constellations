#!/usr/bin/env python3
"""Check systems/unsplash/tokens.json.

The tokens were written from live computed styles on unsplash.com on 2026-11-19.
This script does not rebuild them. It checks aliases, sources, and matching theme keys.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"


class CheckError(AssertionError):
    pass


def walk(node, prefix=""):
    if isinstance(node, dict) and "$value" in node:
        yield prefix, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, f"{prefix}.{key}" if prefix else key)


def lookup(doc, path):
    node = doc["core"]
    for part in path.split("."):
        if not isinstance(node, dict) or part not in node:
            return None
        node = node[part]
    return node if isinstance(node, dict) and "$value" in node else None


def check(doc):
    if "core" not in doc:
        raise CheckError("no core set")
    themes = [name for name in doc if name not in ("core",) and not name.startswith("$")]
    if not themes:
        raise CheckError("no theme set")
    keys = None
    for theme in themes:
        theme_keys = sorted(path for path, _ in walk(doc[theme]))
        if keys is None:
            keys = theme_keys
        elif theme_keys != keys:
            raise CheckError(f"keys differ: {theme}")
    for path, token in list(walk(doc["core"])) + [item for theme in themes for item in walk(doc[theme])]:
        if "$extensions" not in token or "source" not in token["$extensions"]:
            raise CheckError(f"no source on {path}")
        value = token["$value"]
        if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
            target = value[1:-1]
            if lookup(doc, target) is None and not any(
                lookup({"core": doc[theme]}, target) for theme in themes
            ):
                # Theme aliases may point at the same theme. Resolve against core, then each theme.
                found = lookup(doc, target)
                if found is None:
                    raise CheckError(f"missing alias {target} from {path}")
        if isinstance(value, dict):
            for item in value.values():
                if isinstance(item, str) and item.startswith("{") and item.endswith("}"):
                    target = item[1:-1]
                    if lookup(doc, target) is None:
                        raise CheckError(f"missing alias {target} from {path}")


def main():
    doc = json.loads(TOKENS.read_text())
    check(doc)
    print(f"tokens.json ok: {sum(1 for _ in walk(doc['core']))} core, " + ", ".join(
        f"{sum(1 for _ in walk(doc[name]))} {name}" for name in doc if name not in ('core',) and not name.startswith('$')
    ))


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
