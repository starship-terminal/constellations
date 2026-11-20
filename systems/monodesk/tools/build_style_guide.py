#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Dark-only package."""
import json, pathlib, re

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


def css_val(name, t):
    v, ty = t["$value"], t["$type"]
    if ty == "typography":
        return f'{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} {v["fontFamily"]}'
    if ty == "fontFamily":
        return v
    return alias(v)


def block(setname):
    if setname not in T:
        return ""
    return "\n".join(f"  {cssname(n)}: {css_val(n, t)};" for n, t in flat(T[setname]))


tpl = (HERE / "tools" / "style-guide.template.html").read_text()
html = tpl.replace("/*CORE*/", block("core")).replace("/*DARK*/", block("dark"))
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
