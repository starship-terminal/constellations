#!/usr/bin/env python3
"""Check tokens.json. This capture writes tokens from raw/readings.json by hand.

The script does not regenerate tokens.json. It refuses a token with no source,
an alias that points at nothing, and a Measured colour that is not in raw/.
"""
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
RAW = "\n".join(p.read_text(errors="replace") for p in (HERE / "raw").rglob("*") if p.is_file())


def walk(node, path=""):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for key, value in node.items():
            if key.startswith("$"):
                continue
            yield from walk(value, f"{path}.{key}" if path else key)


def check():
    problems = []
    names = {path for path, _ in walk(TOKENS)}
    for path, token in walk(TOKENS):
        source = (token.get("$extensions") or {}).get("source")
        if not isinstance(source, dict) or not source.get("evidence") or not source.get("capture"):
            problems.append(f"{path}: missing source")
        value = token["$value"]
        if isinstance(value, str):
            for alias in re.findall(r"\{([^{}]+)\}", value):
                if alias not in names and f"core.{alias}" not in names:
                    # aliases are written without the set prefix and resolve inside core or the same set
                    if alias not in names:
                        problems.append(f"{path}: alias {{{alias}}} does not resolve")
        if source and source.get("evidence") == "Measured" and token.get("$type") == "color" and isinstance(value, str) and value.startswith("#"):
            if value.lower() not in RAW.lower() and value.upper() not in RAW:
                problems.append(f"{path}: Measured colour {value} is not in raw/")
    return problems


def main():
    problems = check()
    if problems:
        print("\n".join(problems))
        return 1
    print(f"tokens ok: {sum(1 for _ in walk(TOKENS))} tokens")
    return 0


if __name__ == "__main__":
    sys.exit(main())
