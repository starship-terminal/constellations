#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: dark was not painted."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
template = (HERE / "tools" / "style-guide.template.html").read_text()


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v and v.get("$type") == "color":
            yield prefix + k, v["$value"]
        elif isinstance(v, dict) and "$value" not in v:
            yield from flat(v, prefix + k + "-")


lines = []
for name, value in flat(T["light"]):
    lines.append("  %s: %s;" % (cssname(name), value))
css = "\n".join(lines)
html = template.replace("/*LIGHT*/", css)
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
