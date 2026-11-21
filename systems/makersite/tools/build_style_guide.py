#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light only. No catalog required."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())


def val(path):
    node = tokens
    for part in path.split("."):
        node = node[part]
    return node["$value"]


colors = [
    ("page", "light.color.page"),
    ("surface", "light.color.surface"),
    ("text", "light.color.text"),
    ("text on accent", "light.color.text-on-accent"),
    ("accent", "light.color.accent"),
    ("announce", "light.color.announce"),
    ("button fill", "light.color.button-fill"),
    ("focus", "light.color.focus"),
]
swatches = "\n".join(
    f'<div class="swatch"><i style="background:{val(p)}"></i><span>{name}<br><code>{val(p)}</code></span></div>'
    for name, p in colors
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Makersite style guide</title>
<style>
body {{ font: 16px/1.5 Georgia, serif; margin: 32px; color: {val('light.color.text')}; background: {val('light.color.page')}; }}
h1 {{ font-weight: 500; color: {val('light.color.accent')}; }}
.swatches {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
.swatch {{ display: flex; gap: 8px; align-items: center; }}
.swatch i {{ width: 48px; height: 48px; border: 1px solid #ccc; display: block; }}
code {{ font-family: ui-monospace, monospace; font-size: 12px; }}
.btn {{ display: inline-block; padding: 16px 32px; border: 1px solid {val('light.color.surface')}; background: {val('light.color.button-fill')}; color: {val('light.color.accent')}; font-weight: 700; text-decoration: none; }}
.hero {{ background: {val('light.color.surface')}; color: white; padding: 32px; margin-top: 24px; }}
</style>
</head>
<body>
<h1>Makersite</h1>
<p>Public marketing site, light only. Values from tokens.json, measured 2026-11-21 on makersite.io. Arboria is not loaded here.</p>
<div class="swatches">{swatches}</div>
<p class="hero">Hero surface {val('light.color.surface')}. <a class="btn" href="#book">Book a Demo</a></p>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
