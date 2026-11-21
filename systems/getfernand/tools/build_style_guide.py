#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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


tpl = (HERE / "tools" / "style-guide.template.html").read_text()
html = tpl.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light")).replace("/*DARK*/", "")
html = html.replace("/*TOKENS*/null", json.dumps({"light": True}))
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
