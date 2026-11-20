#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and style-guide.template.html.

Light-only. core and light land on :root. Aliases become var(--name).
"""
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
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "shadow":
        s = v
        return f'{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {alias(s["color"])}'
    if ty == "typography":
        return None
    if isinstance(v, (int, float)) and ty == "number":
        return str(v)
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
    return {k: slim(v) for k, v in node.items() if not str(k).startswith("$")}


data = json.dumps({k: slim(T[k]) for k in ("core", "light") if k in T}, separators=(",", ":")).replace("<", "\\u003c")
tpl = (HERE / "tools" / "style-guide.template.html").read_text()
html = tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", "").replace("/*TOKENS*/null", data)
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html.encode()), "bytes")
