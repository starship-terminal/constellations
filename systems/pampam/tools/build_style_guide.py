#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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


def css_val(token):
    val = token["$value"]
    ty = token.get("$type")
    if isinstance(val, dict):
        parts = []
        if "fontWeight" in val:
            parts.append(str(val["fontWeight"]))
        if "fontSize" in val:
            parts.append(alias(val["fontSize"]))
        if "lineHeight" in val:
            parts.append("/" + alias(val["lineHeight"]))
        if "fontFamily" in val:
            parts.append(alias(val["fontFamily"]))
        return " ".join(parts)
    if isinstance(val, list):
        return "cubic-bezier(" + ", ".join(str(n) for n in val) + ")"
    return alias(val)


lines = []
for name, token in flat(T["core"]):
    lines.append(f"  {cssname(name)}: {css_val(token)};")
for name, token in flat(T["light"]):
    lines.append(f"  {cssname(name)}: {css_val(token)};")
# font faces as custom props the template uses
lines.append("  --font-sans: " + alias(T["core"]["font"]["sans"]["$value"]) + ";")
lines.append("  --font-display: " + alias(T["core"]["font"]["display"]["$value"]) + ";")
lines.append("  --shadow-button: " + alias(T["core"]["shadow"]["button"]["$value"]) + ";")
lines.append("  --shadow-quiet: " + alias(T["core"]["shadow"]["quiet"]["$value"]) + ";")
lines.append("  --shadow-menu: " + alias(T["core"]["shadow"]["menu"]["$value"]) + ";")

html = TEMPLATE.replace("/*LIGHT*/", "\n".join(lines))
html = html.replace("/*TOKENS*/null", json.dumps({"light": True}))
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
