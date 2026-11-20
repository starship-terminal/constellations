#!/usr/bin/env python3
"""Check systems/unsplash/tokens.json.

The tokens were written from live computed styles on unsplash.com on 2026-11-19.
This script does not rebuild them. It checks aliases (own set, then core), sources, matching theme
keys, and that every colour labelled Measured is held by a file in raw/.
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


def lookup(doc, path, set_name="core"):
    node = doc[set_name]
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
    seen = raw_colours()
    for set_name in ["core"] + themes:
        for path, token in walk(doc[set_name]):
            if "$extensions" not in token or "source" not in token["$extensions"]:
                raise CheckError(f"no source on {set_name}.{path}")
            value = token["$value"]
            refs = [value] if isinstance(value, str) else list(value.values()) if isinstance(value, dict) else []
            for item in refs:
                if isinstance(item, str) and item.startswith("{") and item.endswith("}"):
                    # Own set first, then core, as tools/catalog.py's Resolver does; never another theme.
                    target = item[1:-1]
                    if lookup(doc, target, set_name) is None and lookup(doc, target) is None:
                        raise CheckError(f"missing alias {target} from {set_name}.{path}")
            if (token["$type"] == "color" and isinstance(value, str) and value.startswith("#")
                    and str(token["$extensions"]["source"]).startswith("Measured") and full_hex(value) not in seen):
                raise CheckError(f"{set_name}.{path}: Measured {value} is in no raw/ reading")


def raw_colours():
    """Every colour raw/ holds, alpha included: hex as written, rgb()/rgba() as #rrggbb or #rrggbbaa."""
    import re
    seen = set()
    for f in sorted((HERE / "raw").glob("*.json")):
        text = f.read_text()
        for h in re.findall(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b", text):
            seen.add(full_hex("#" + h))
        for m in re.finditer(r"rgba?\((\d+),\s*(\d+),\s*(\d+)(?:,\s*([\d.]+))?\)", text):
            h = "#%02x%02x%02x" % tuple(int(c) for c in m.groups()[:3])
            if m.group(4) is not None and float(m.group(4)) < 1:
                h += "%02x" % int(float(m.group(4)) * 255 + 0.5)
            seen.add(h)
    return seen


def full_hex(value):
    """#rgb, #rgba, #rrggbb or #rrggbbaa as lower-case #rrggbb[aa], alpha kept; an opaque ff alpha is dropped."""
    h = value.lower().lstrip("#")
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h)
    if len(h) == 8 and h.endswith("ff"):
        h = h[:6]
    return "#" + h


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
