#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One light theme."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

def walk(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        path = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict) and "$value" in v:
            yield path, v
        elif isinstance(v, dict):
            yield from walk(v, path)

rows = []
for path, leaf in walk(T["core"]):
    val = leaf["$value"]
    if isinstance(val, dict):
        val = " ".join(f"{k} {val[k]}" for k in ("offsetX", "offsetY", "blur", "spread", "color"))
    rows.append((path, leaf.get("$type", ""), str(val), leaf["$extensions"]["source"]))

swatches = [
    ("page", T["light"]["page"]["$value"]),
    ("surface", T["light"]["surface"]["$value"]),
    ("text", T["light"]["text"]["$value"]),
    ("muted", T["light"]["muted"]["$value"]),
    ("accent", T["light"]["accent"]["$value"]),
    ("border", T["light"]["border"]["$value"]),
]

def css_of(alias):
    # {core.color.page} -> look up
    if isinstance(alias, str) and alias.startswith("{") and alias.endswith("}"):
        parts = alias[1:-1].split(".")
        node = T
        for p in parts:
            node = node[p]
        return node["$value"]
    return alias

html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>LottieFiles style guide</title>
<style>
  :root { color-scheme: light; }
  body { margin: 0; background: #fff; color: #111; font: 400 15px/1.45 "Inter", ui-sans-serif, system-ui, sans-serif; }
  main { max-width: 960px; margin: 0 auto; padding: 32px 20px 80px; }
  h1 { font: 500 40px/1.05 "DM Sans", "Inter", sans-serif; letter-spacing: -0.04em; margin: 0 0 8px; }
  h2 { margin: 36px 0 12px; font-size: 18px; }
  p { max-width: 68ch; color: #444; }
  .swatches { display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }
  .sw { border: 1px solid #e6e6e8; border-radius: 12px; overflow: hidden; }
  .sw i { display: block; height: 64px; }
  .sw span { display: block; padding: 8px 10px; font-size: 12px; }
  .btn { display: inline-flex; align-items: center; height: 48px; padding: 0 24px; border-radius: 12px; background: #28aca2; color: #fafafa; font-weight: 500; text-decoration: none; }
  .quiet { display: inline-flex; align-items: center; height: 48px; padding: 0 24px; border-radius: 12px; background: #fff; color: #20272c; border: 1px solid #e4e4e7; font-weight: 500; margin-left: 8px; }
  table { border-collapse: collapse; width: 100%; font-size: 13px; }
  td, th { text-align: left; padding: 6px 8px; border-bottom: 1px solid #eee; vertical-align: top; }
  code { font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 12px; }
</style>
</head>
<body>
<main>
<h1>LottieFiles</h1>
<p>Public marketing site, one light theme. Values come from tokens.json. The teal chip below uses the sampled sRGB of the primary button so a browser that does not paint oklch still shows the control.</p>
<h2>Roles</h2>
<div class="swatches">
"""
for name, alias in swatches:
    val = css_of(alias)
    paint = "#28aca2" if name == "accent" else val
    html += f'<div class="sw"><i style="background:{paint}"></i><span><code>{name}</code><br>{val}</span></div>\n'
html += """</div>
<h2>Controls</h2>
<p><a class="btn" href="#roles">Get started for free</a><span class="quiet">Get in touch</span></p>
<p>Hero buttons are 48px tall, 12px radius, Inter LF 16/500. Header Sign up is 36px tall, 6px radius, 14/500.</p>
<h2>Tokens</h2>
<table>
<tr><th>Token</th><th>Value</th><th>Source</th></tr>
"""
for path, ty, val, src in rows:
    html += f"<tr><td><code>{path}</code></td><td><code>{val}</code></td><td>{src}</td></tr>\n"
html += "</table></main></body></html>\n"
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
