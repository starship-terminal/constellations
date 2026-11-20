#!/usr/bin/env python3
"""Check systems/new-balance/tokens.json.

Values were measured in the T3 preview browser on 2026-11-19 and written into
tokens.json by hand. This script does not invent tokens. It checks every alias,
refuses a colour that is not #rrggbb, and (check_against_raw) refuses a token
labelled Measured whose colour, px length or font stack is in no raw/ reading.
"""
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
TOKENS = HERE / "tokens.json"


class CheckError(ValueError):
    pass


def walk(node, prefix=""):
    for key, value in node.items():
        if str(key).startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def check(doc=None):
    doc = doc or json.loads(TOKENS.read_text())
    names = {path for path, _ in walk(doc.get("core", {}))}
    names |= {path for path, _ in walk(doc.get("light", {}))}
    for group in ("core", "light"):
        if group not in doc:
            continue
        for path, token in walk(doc[group]):
            source = token.get("$extensions", {}).get("source", "")
            if not source:
                raise CheckError(f"{group}.{path}: no source")
            value = token["$value"]
            blobs = [value] if isinstance(value, str) else (
                list(value.values()) if isinstance(value, dict) else []
            )
            for blob in blobs:
                if not isinstance(blob, str):
                    continue
                for alias in re.findall(r"\{([^{}]+)\}", blob):
                    if alias not in names:
                        raise CheckError(f"{group}.{path}: alias {{{alias}}} points at nothing")
            if token["$type"] == "color" and isinstance(value, str) and not value.startswith("{"):
                if not re.fullmatch(r"#[0-9a-fA-F]{6}", value):
                    raise CheckError(f"{group}.{path}: colour {value!r} is not #rrggbb")
    return doc


RAW = HERE / "raw"


def raw_values():
    """Every colour (as #rrggbb) and length (as Npx) that raw/ holds, plus its text, for check_against_raw."""
    text = "\n".join(p.read_text() for p in sorted(RAW.glob("*.json")))
    colours = {"#%02x%02x%02x" % tuple(int(x) for x in m) for m in re.findall(r"rgba?\((\d+),\s*(\d+),\s*(\d+)", text)}
    for h in re.findall(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b", text):
        colours.add("#" + (h if len(h) == 6 else "".join(c * 2 for c in h)).lower())
    lengths = set(re.findall(r"-?\d+(?:\.\d+)?px", text)) | {f"{n}px" for n in re.findall(r'"(?:height|width|top)": (\d+)', text)}
    return colours, lengths, text.replace('\\"', '"')


def check_against_raw(doc=None):
    """A token labelled Measured must carry a value raw/ holds: each literal colour and px length in it
    (also inside a typography value) and each font stack is looked up in the readings. A value typed in by
    hand must say so with a non-Measured label instead (finding 16-5: tokens.json is written by hand)."""
    doc = doc or json.loads(TOKENS.read_text())
    colours, lengths, text = raw_values()
    for group in ("core", "light"):
        for path, token in walk(doc.get(group, {})):
            if not str(token.get("$extensions", {}).get("source", "")).startswith("Measured"):
                continue
            value = token["$value"]
            members = value.items() if isinstance(value, dict) else [(None, value)]
            for member, item in members:
                item = str(item)
                if item.startswith("{"):
                    continue
                if re.fullmatch(r"#[0-9a-fA-F]{6}", item) and item.lower() not in colours:
                    raise CheckError(f"{group}.{path}: Measured colour {item} is in no raw/ reading")
                if re.fullmatch(r"-?\d+(?:\.\d+)?px", item) and item not in lengths:
                    raise CheckError(f"{group}.{path}: Measured length {item} is in no raw/ reading")
                if (token["$type"] == "fontFamily" or member == "fontFamily") and item not in text:
                    raise CheckError(f"{group}.{path}: Measured font stack is in no raw/ reading")
    return doc


if __name__ == "__main__":
    check()
    check_against_raw()
    print(f"tokens.json: {sum(1 for _ in walk(json.loads(TOKENS.read_text())['core']))} core, "
          f"{sum(1 for _ in walk(json.loads(TOKENS.read_text())['light']))} light")
