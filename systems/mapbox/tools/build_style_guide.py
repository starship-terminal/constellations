#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and the template."""
import json, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
TEMPLATE = (HERE / "tools" / "style-guide.template.html").read_text()


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


def block(setname):
    if setname not in T:
        return ""
    return "\n".join(f"  {cssname(n)}: {alias(t['$value'])};" for n, t in flat(T[setname]))


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"v": node["$value"], "t": node["$type"]}
    if isinstance(node, dict):
        return {k: slim(v) for k, v in node.items() if not k.startswith("$")}
    return node


html = TEMPLATE.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", "")
# "<" as \u003c keeps a value holding "</script>" from ending the inlined script (the kit's escape).
html = html.replace("/*TOKENS*/null", json.dumps(slim(T), ensure_ascii=False).replace("<", "\\u003c"))
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
