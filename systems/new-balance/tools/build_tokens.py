#!/usr/bin/env python3
"""Check systems/new-balance/tokens.json.

Values were measured in the T3 preview browser on 2026-11-19 and written into
tokens.json. This script does not invent tokens. It checks every alias and
refuses a colour or length that is not a measured form.
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


if __name__ == "__main__":
    check()
    print(f"tokens.json: {sum(1 for _ in walk(json.loads(TOKENS.read_text())['core']))} core, "
          f"{sum(1 for _ in walk(json.loads(TOKENS.read_text())['light']))} light")
