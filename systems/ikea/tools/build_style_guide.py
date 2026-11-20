#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
template = (HERE / "tools" / "style-guide.template.html").read_text()


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
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "fontFamily":
        return ", ".join(v)
    if ty == "typography":
        return None
    if isinstance(v, (dict, list)):
        return None
    return alias(v)


def block(setname):
    if setname not in T:
        return ""
    lines = []
    for n, t in flat(T[setname]):
        val = css_val(t)
        if val is None:
            continue
        lines.append(f"  {cssname(n)}: {val};")
    return "\n".join(lines)


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"v": node["$value"], "t": node["$type"]}
    if isinstance(node, dict):
        return {k: slim(v) for k, v in node.items() if not k.startswith("$")}
    return node


html = template.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light"))
# Inlined into a <script>: "<" as \u003c keeps a value holding "</script>" from ending it early.
html = html.replace("/*TOKENS*/null", json.dumps(slim(T), separators=(",", ":")).replace("<", "\\u003c"))
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
