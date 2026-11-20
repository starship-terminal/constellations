#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and tools/style-guide.template.html.

The template paints only token custom properties. TT Commons and TT Talent are
not loaded. There is no dark set, so the page stays on the light tokens.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
template = (HERE / "tools" / "style-guide.template.html").read_text()


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}-{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from flat(value, path)


def css_name(path):
    return "--" + path


def css_value(token):
    value, kind = token["$value"], token["$type"]
    if kind in ("typography", "shadow"):
        return None
    if isinstance(value, str):
        return value
    return None


core = "\n".join(
    f"  {css_name(name)}: {css_value(token)};"
    for name, token in flat(tokens["core"])
    if css_value(token) is not None
)
light = "\n".join(
    f"  {css_name(name)}: {css_value(token)};"
    for name, token in flat(tokens["light"])
    if css_value(token) is not None
)
html = template.replace("/*CORE*/", core).replace("/*LIGHT*/", light)
# "<" as \u003c keeps a value holding "</script>" from ending the inlined script (the kit's escape).
html = html.replace("/*TOKENS*/null", json.dumps(tokens, separators=(",", ":")).replace("<", "\\u003c"))
(HERE / "style-guide.html").write_text(html)
print(f"wrote style-guide.html ({len(html)} bytes)")
