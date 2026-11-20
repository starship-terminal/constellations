#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One theme."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
tokens = json.loads((ROOT / "tokens.json").read_text())
template = (HERE / "style-guide.template.html").read_text()

def hex_of(node):
    v = node["$value"]
    return v

core = tokens["core"]["color"]
css = []
for name, node in core.items():
    css.append(f"  --{name}: {hex_of(node)};")
css.append(f"  --page: {core['page']['$value']};")
css.append(f"  --ink: {core['ink']['$value']};")
css.append(f"  --surface: {core['paper']['$value']};")
css.append(f"  --muted: {core['muted']['$value']};")
css.append(f"  --field: {core['field']['$value']};")
html = template.replace("/*CORE*/", "\n".join(css))
swatch_html = []
for name, node in core.items():
    val = node["$value"]
    swatch_html.append(
        f'<div class="sw"><i style="background:{val}"></i><b>{name}</b><span>{val}</span></div>'
    )
html = html.replace('<div class="row" id="swatches"></div>', '<div class="row" id="swatches">' + "".join(swatch_html) + "</div>")
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
