#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and tools/style-guide.template.html."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "typography":
        return f'{v.get("fontWeight", 400)} {v.get("fontSize", "16px")}/{v.get("lineHeight", "1.4")} {v.get("fontFamily", "sans-serif")}'
    if ty == "shadow" and isinstance(v, str):
        return v
    return alias(v)


def block(setname):
    if setname not in T:
        return ""
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"v": node["$value"], "t": node["$type"]}
    if isinstance(node, dict):
        return {k: slim(v) for k, v in node.items() if not k.startswith("$")}
    return node


data = json.dumps({k: slim(T[k]) for k in ("core", "light", "dark") if k in T}, separators=(",", ":")).replace("<", "\\u003c")
tpl = (HERE / "tools" / "style-guide.template.html").read_text()
html = (tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", block("dark")).replace("/*TOKENS*/null", data))
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html", "bytes", len(html))
