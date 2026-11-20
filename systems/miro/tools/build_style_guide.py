#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and tools/style-guide.template.html."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())
TEMPLATE = (HERE / "tools" / "style-guide.template.html").read_text()


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from flat(value, prefix + key + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(value):
    return re.sub(r"\{([^{}]+)\}", lambda match: f"var({cssname(match.group(1))})", str(value))


def css_val(token):
    value, kind = token["$value"], token["$type"]
    if kind == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(part) for part in value)
    if kind == "shadow":
        return alias(value)
    if kind in ("transition", "animation"):
        return None
    return alias(value)


def block(name):
    if name not in T:
        return ""
    lines = []
    for path, token in flat(T[name]):
        value = css_val(token)
        if value is None:
            continue
        lines.append(f"  {cssname(path)}: {value};")
    return "\n".join(lines)


# The guide's JS reads light roles and the two ramps. Keep the payload small.
slim = {
    "light": {key: {"$value": value["$value"]} for key, value in T["light"].items()},
    "core": {"color": {
        ramp: {step: {"$value": token["$value"]} for step, token in T["core"]["color"][ramp].items()}
        for ramp in ("blue", "gray")
    }},
}
html = TEMPLATE.replace("/*CORE*/", block("core")).replace("/*LIGHT*/", block("light"))
# Inlined into a <script>: "<" as \u003c keeps a value holding "</script>" from ending it early.
html = html.replace("/*TOKENS*/null", json.dumps(slim, separators=(",", ":")).replace("<", "\\u003c"))
if __name__ == "__main__":
    (HERE / "style-guide.html").write_text(html)
    print("wrote", HERE / "style-guide.html")
