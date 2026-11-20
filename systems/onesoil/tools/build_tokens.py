#!/usr/bin/env python3
"""Check systems/onesoil/tokens.json.

The marketing tokens were written from live computed styles on 2026-11-19.
This script does not invent values. It checks the committed file and exits
0 when every token has a source, every alias resolves, and every token
labelled Measured carries a colour, px length and duration that a raw/ reading
holds (check_against_raw). tokens.json is written by hand, so that last check
is what ties it to the readings.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
PKG = HERE.parent
TOKENS = PKG / "tokens.json"


class CheckError(Exception):
    pass


def walk(node, prefix=()):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = prefix + (key,)
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def aliases(value):
    if isinstance(value, str):
        return re.findall(r"\{([^{}]+)\}", value)
    if isinstance(value, dict):
        found = []
        for item in value.values():
            found.extend(aliases(item))
        return found
    if isinstance(value, list):
        found = []
        for item in value:
            found.extend(aliases(item))
        return found
    return []


def check(doc):
    sets = [name for name in ("core", "light", "dark") if name in doc]
    paths = {".".join(path) for name in sets for path, _ in walk(doc[name])}
    for name in sets:
        for path, token in walk(doc[name]):
            where = name + "." + ".".join(path)
            src = token.get("$extensions", {}).get("source", {})
            if not src.get("evidence") or not src.get("capture"):
                raise CheckError(f"{where}: no source")
            for alias in aliases(token["$value"]):
                if alias not in paths:
                    raise CheckError(f"{where}: alias {{{alias}}} points at nothing")
            value = token["$value"]
            if isinstance(value, str) and value.startswith("{"):
                continue
            if token["$type"] == "color" and not re.fullmatch(r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?", value):
                raise CheckError(f"{where}: bad colour {value}")
            if token["$type"] == "dimension" and not re.fullmatch(r"-?\d+(\.\d+)?px", value):
                raise CheckError(f"{where}: bad dimension {value}")
    if "light" in doc and "dark" in doc:
        light = sorted(".".join(path) for path, _ in walk(doc["light"]))
        dark = sorted(".".join(path) for path, _ in walk(doc["dark"]))
        if light != dark:
            raise CheckError("light and dark keys differ")


def raw_values():
    """The colours (#rrggbb), px lengths and durations raw/ holds."""
    text = "\n".join(p.read_text() for p in sorted((PKG / "raw").glob("*.json")))
    colours = {"#%02x%02x%02x" % tuple(int(x) for x in m) for m in re.findall(r"rgba?\((\d+),\s*(\d+),\s*(\d+)", text)}
    for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text):
        colours.add("#" + (h if len(h) == 6 else "".join(c * 2 for c in h)).lower())
    lengths = set(re.findall(r"-?\d+(?:\.\d+)?px", text)) | {f"{n}px" for n in re.findall(r'": (\d+)[,}\s]', text)}
    times = set(re.findall(r"\d*\.?\d+m?s\b", text))
    return colours, lengths, times


def check_against_raw(doc):
    """Refuse a token labelled Measured whose literal colour, px length or duration is in no raw/ reading."""
    colours, lengths, times = raw_values()
    for name in [n for n in ("core", "light", "dark") if n in doc]:
        for path, token in walk(doc[name]):
            if token["$extensions"]["source"].get("evidence") != "Measured":
                continue
            where = name + "." + ".".join(path)
            value = token["$value"]
            for item in (value.values() if isinstance(value, dict) else [value]):
                item = str(item)
                if re.fullmatch(r"#[0-9A-Fa-f]{6}([0-9A-Fa-f]{2})?", item) and item[:7].lower() not in colours:
                    raise CheckError(f"{where}: Measured colour {item} is in no raw/ reading")
                if re.fullmatch(r"-?\d+(\.\d+)?px", item) and item not in lengths:
                    raise CheckError(f"{where}: Measured length {item} is in no raw/ reading")
                ms = re.fullmatch(r"(\d+(?:\.\d+)?)ms", item)
                if ms and not ({item, f"{float(ms.group(1)) / 1000:g}s", f"{float(ms.group(1)) / 1000:g}s".lstrip("0")} & times):
                    raise CheckError(f"{where}: Measured duration {item} is in no raw/ reading")


def main():
    doc = json.loads(TOKENS.read_text())
    check(doc)
    check_against_raw(doc)
    count = sum(1 for name in ("core", "light", "dark") if name in doc for _ in walk(doc[name]))
    print(f"tokens.json: {count} tokens ok")


if __name__ == "__main__":
    try:
        main()
    except CheckError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)
