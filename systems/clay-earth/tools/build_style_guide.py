#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Clay has no icons/ directory."""
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


def block(setname):
    if setname not in T:
        return ""
    return "\n".join(f"  {cssname(n)}: {alias(t['$value'])};" for n, t in flat(T[setname]))


def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"v": node["$value"], "t": node["$type"], "s": node["$extensions"]["source"]}
    return {k: slim(v) for k, v in node.items() if not k.startswith("$")}


data = json.dumps({k: slim(T[k]) if k in T else {} for k in ("core", "light", "dark")},
                  ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
tpl = (HERE / "tools" / "style-guide.template.html").read_text()
html = (tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", block("dark"))
        .replace("/*TOKENS*/null", data))
html = re.sub(r"<!--icon:[^>]*-->", "", html)
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
