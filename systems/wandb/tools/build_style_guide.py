#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and tools/style-guide.template.html."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if not isinstance(value, dict) or key.startswith("$"):
            continue
        if "$value" in value:
            yield prefix + key, value
        else:
            yield from flat(value, prefix + key + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(value):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(value))


def css_val(token):
    value, kind = token["$value"], token["$type"]
    if kind == "typography":
        return f'{alias(value["fontWeight"])} {alias(value["fontSize"])}/{alias(value["lineHeight"])} {alias(value["fontFamily"])}'
    return alias(value)


def block(name):
    if name not in T:
        return ""
    return "\n".join(f"  {cssname(path)}: {css_val(token)};" for path, token in flat(T[name]))


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"v": node["$value"], "t": node["$type"], "s": node["$extensions"]["source"]}
    return {key: slim(value) for key, value in node.items() if not str(key).startswith("$")}


data = json.dumps({key: slim(T[key]) for key in ("core", "dark", "light") if key in T}, separators=(",", ":")).replace("<", "\\u003c")
html = (HERE / "tools" / "style-guide.template.html").read_text()
html = html.replace("/*CORE*/", block("core")).replace("/*DARK*/", block("dark")).replace("/*LIGHT*/", block("light"))
html = html.replace("/*TOKENS*/null", data)
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
