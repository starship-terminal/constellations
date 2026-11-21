#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

FlutterFlow's public site names roles as --ff-color-* and scales as
--ff-radius-*, --ff-space-*, --ff-text-*. The guide paints those as CSS
custom properties. Light roles sit on :root; dark roles sit on
[data-theme="dark"], the same attribute the site uses.

Deterministic: same tokens.json, byte-identical HTML.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def css_val(tok):
    v, ty = tok["$value"], tok["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if isinstance(v, (int, float)) and ty == "number":
        return str(v)
    return str(v)


def block(mapping):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in mapping)


core = list(flat(T["core"]))
light = list(flat(T["light"]))
dark = list(flat(T["dark"]))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{css_val(t)}"></i><div><b>{n}</b><span>{css_val(t)}</span></div></div>'
    for n, t in light
    if t["$type"] == "color"
)
type_rows = "\n".join(
    f'<div class="ty"><code>{n}</code><p style="font:{css_val(t)};margin:0">Build an app by describing it</p></div>'
    for n, t in core
    if t["$type"] == "typography"
)
radius_rows = "\n".join(
    f'<div class="sw"><i style="border-radius:{css_val(t)};background:var(--accent)"></i><div><b>{n}</b><span>{css_val(t)}</span></div></div>'
    for n, t in core
    if t["$type"] == "radius" or n.startswith("radius-")
)

html = f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>FlutterFlow style guide</title>
<style>
:root {{
  color-scheme: light;
{block(core)}
{block(light)}
  --sg-sans: var(--fontFamily-sans, Inter, system-ui, sans-serif);
  --sg-mono: var(--fontFamily-mono, ui-monospace, monospace);
}}
[data-theme="dark"] {{
  color-scheme: dark;
{block(dark)}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 15px/1.5 var(--sg-sans); }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border); position: sticky; top: 0; background: var(--page); }}
header h1 {{ font-size: 16px; font-weight: 600; margin: 0; }}
button.theme {{ margin-left: auto; border: 1px solid var(--border); background: var(--surface); color: var(--text); border-radius: 999px; padding: 6px 12px; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h2 {{ font-size: 22px; font-weight: 560; letter-spacing: -0.02em; margin: 40px 0 12px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 10px; box-shadow: inset 0 0 0 1px var(--border); display: block; }}
.sw b {{ display: block; font: 600 12px/1.3 var(--sg-mono); }}
.sw span {{ color: var(--muted); font-size: 12px; }}
.ty {{ display: grid; grid-template-columns: 180px 1fr; gap: 16px; padding: 10px 0; border-bottom: 1px solid var(--border); align-items: baseline; }}
.ty code {{ font: 12px var(--sg-mono); color: var(--muted); }}
.btn {{ display: inline-flex; align-items: center; height: 32px; padding: 0 14px; border-radius: 999px; background: var(--button); color: var(--buttonInk); font-size: 13px; font-weight: 510; text-decoration: none; }}
.ghost {{ color: var(--muted); background: transparent; }}
.card {{ background: var(--surface); border-radius: 20px; padding: 20px; box-shadow: var(--shadow-resting, 0 0 0 1px var(--border)); max-width: 360px; }}
p.note {{ color: var(--muted); max-width: 68ch; }}
</style>
</head>
<body>
<header>
  <h1>FlutterFlow</h1>
  <span>Public site tokens</span>
  <button class="theme" type="button" onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'">Toggle theme</button>
</header>
<main>
  <p class="note">Rendered from tokens.json. Values were read from www.flutterflow.io on 2026-11-21. Dark paints when data-theme is dark, the same switch the site uses. The signed-in app was not captured.</p>
  <h2>Colour roles</h2>
  <div class="grid">{swatches}</div>
  <h2>Type</h2>
  {type_rows}
  <h2>Radius</h2>
  <div class="grid">{radius_rows}</div>
  <h2>Controls</h2>
  <p><a class="btn" href="#build">Start building</a></p>
  <div class="card"><strong>Card</strong><p class="note">Surface is --ff-color-card. Accent is the blue used on send and links, not the near-black primary button.</p></div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
