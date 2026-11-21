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
    ("text", "light.color.text"),
    ("accent", "light.color.accent"),
    ("on accent", "light.color.accent-on"),
    ("soft", "light.color.accent-soft"),
    ("soft text", "light.color.accent-soft-text"),
    ("link", "light.color.link"),
    ("login accent", "light.color.login-accent"),
]
swatches = "\n".join(
    f'<div class="swatch"><i style="background:{val(p)}"></i><span>{name}<br><code>{val(p)}</code></span></div>'
    for name, p in colors
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Notion style guide</title>
<style>
body {{ font: 16px/1.5 Inter, Helvetica, sans-serif; margin: 32px; color: {val('light.color.text')}; background: {val('light.color.page')}; }}
h1 {{ font-weight: 600; letter-spacing: -1.2px; font-size: 48px; }}
.swatches {{ display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }}
.swatch {{ display: flex; gap: 8px; align-items: center; }}
.swatch i {{ width: 48px; height: 48px; border: 1px solid #ccc; display: block; }}
code {{ font-family: ui-monospace, monospace; font-size: 12px; }}
.btn {{ display: inline-block; padding: 4px 14px; border-radius: 8px; background: {val('light.color.accent')}; color: {val('light.color.accent-on')}; font-weight: 500; text-decoration: none; }}
.soft {{ display: inline-block; margin-left: 8px; padding: 4px 14px; border-radius: 8px; background: {val('light.color.accent-soft')}; color: {val('light.color.accent-soft-text')}; font-weight: 500; text-decoration: none; }}
</style>
</head>
<body>
<h1>Notion</h1>
<p>Public marketing site, light only. Values from tokens.json, measured 2026-11-21 on www.notion.com. NotionInter is not loaded here.</p>
<div class="swatches">{swatches}</div>
<p style="margin-top:24px"><a class="btn" href="#get">Get Notion free</a><a class="soft" href="#soft">Sign up</a></p>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
