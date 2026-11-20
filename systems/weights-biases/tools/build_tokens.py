#!/usr/bin/env python3
"""Check tokens.json for Weights & Biases against its rules and its readings.

tokens.json was written by hand at capture time from raw/computed.json and raw/css-vars.json; this
file does not regenerate it. It was installed from the native kit (grokbot), whose readings-to-roles
mapping never applied to a web capture, so that dead mapping was removed and only the checks kept:

    python3 tools/build_tokens.py

check() refuses a token without a source, an alias that points at nothing, a colour that is not
#RRGGBB(AA), a dimension that is not one px length, and a light and dark set whose keys differ.
check_readings() refuses a literal colour labelled Measured that no file in raw/ holds (as a hex or
as an rgb()/rgba() reading). Standard library only.
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent


def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    """Every {alias} in a value, including those inside a composite (a typography style)."""
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []


class CheckError(AssertionError):
    """A tokens file check() rejects. Raised explicitly, not by `assert`, so the
    check still runs under `python3 -O`; an AssertionError for older callers."""


def require(ok, message):
    if not ok:
        raise CheckError(message)


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            require(src.get("evidence") and src.get("capture"), f"{where}: no source")
            v = t["$value"]
            for a in aliases(v):
                require(a in paths, f"{where}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                require(re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v), f"{where}: bad colour {v}")
            elif t["$type"] == "dimension":
                require(re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}")
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        require(keys("light") == keys("dark"), "light and dark keys differ")


def raw_colours(raw_dir=PKG / "raw"):
    """Every colour a raw/ file holds, as upper-case #RRGGBB and, for a translucent rgba(), #RRGGBBAA."""
    seen = set()
    for f in sorted(pathlib.Path(raw_dir).glob("*.json")):
        text = f.read_text()
        for h in re.findall(r"#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})\b", text):
            if len(h) in (3, 4):
                h = "".join(c * 2 for c in h)
            seen.add("#" + h.upper())
            if len(h) == 8 and h[6:].upper() == "FF":
                seen.add("#" + h[:6].upper())
        for body in re.findall(r"rgba?\(([^)]*)\)", text):
            parts = [x for x in re.split(r"[\s,/]+", body.strip()) if x]
            try:
                r, g, b = (round(float(x)) for x in parts[:3])
                a = float(parts[3].rstrip("%")) / (100 if parts[3].endswith("%") else 1) if len(parts) > 3 else 1.0
            except (ValueError, IndexError):
                continue
            hx = "#%02X%02X%02X" % (r, g, b)
            seen.add(hx if a >= 1 else hx + "%02X" % round(a * 255))
    return seen


def check_readings(doc, seen=None):
    seen = raw_colours() if seen is None else seen
    for name in ("core", "light", "dark"):
        for p, t in walk(doc.get(name, {})):
            v, src = t["$value"], t["$extensions"]["source"]
            if t["$type"] == "color" and src.get("evidence") == "Measured" and isinstance(v, str) and v.startswith("#"):
                require(v.upper() in seen, f"{name}.{'.'.join(p)}: Measured {v} is in no raw/ reading")


if __name__ == "__main__":
    doc = json.loads((PKG / "tokens.json").read_text())
    check(doc)
    check_readings(doc)
    n = sum(1 for s in ("core", "light", "dark") if s in doc for _ in walk(doc[s]))
    print(f"ok {n} tokens")
