#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and the template."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
template = (HERE / "tools" / "style-guide.template.html").read_text()
# Compact token tree for the page script. Drop descriptions so the file stays small.
def slim(node):
    if isinstance(node, dict) and "$value" in node:
        return {"$value": node["$value"], "$type": node["$type"]}
    if isinstance(node, dict):
        return {k: slim(v) for k, v in node.items() if not k.startswith("$")}
    return node

blob = json.dumps({"core": slim(tokens["core"]), "light": slim(tokens["light"])}, separators=(",", ":"))
html = template.replace("/*TOKENS*/null", blob)
css_lines = []
def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = prefix + k
        if isinstance(v, dict) and "$value" in v:
            yield path, v["$value"]
        elif isinstance(v, dict):
            yield from flat(v, path + "-")

def css_val(value):
    if not isinstance(value, str):
        return None
    return value.replace("{", "var(--").replace("}", ")").replace(".", "-")

block = []
for path, value in list(flat(tokens["core"])) + list(flat(tokens["light"])):
    name = "--" + path
    # template uses short names without core-/light- for the painted roles
    short = "--" + path.split("-", 1)[-1] if path.startswith("light-") or path.startswith("core-") else "--" + path
    rendered = css_val(value)
    if rendered:
        block.append(f"  {short}: {rendered};")
css = ":root {\n" + "\n".join(block) + "\n}\n"
html = html.replace("/*CORE*/", css)
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
