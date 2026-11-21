#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
import json
import pathlib
import re

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
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def alias(v):
    if isinstance(v, dict):
        return v
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def block(group, prefix):
    lines = []
    for name, tok in flat(T[group]):
        val = tok["$value"]
        if isinstance(val, dict):
            continue
        lines.append(f"  {cssname(prefix + name)}: {alias(val)};")
    return "\n".join(lines)


core_css = block("core", "")
light_css = block("light", "")

# swatch rows
ramps = []
for hue in ["brand", "accent", "neutral", "gray", "green", "red", "yellow"]:
    cells = []
    for step, tok in T["core"]["color"][hue].items():
        cells.append(f'<i style="background:{tok["$value"]}" title="{hue}-{step} {tok["$value"]}"></i>')
    ramps.append(f'<div class="ramp"><span>{hue}</span><div class="cells">{"".join(cells)}</div></div>')

type_rows = []
for name, tok in T["core"]["typography"].items():
    v = tok["$value"]
    type_rows.append(
        f'<div class="typerow"><div class="k">{name}<small>{v["fontSize"]} / {v["fontWeight"]}</small></div>'
        f'<div class="sample" style="font-size:{v["fontSize"]};font-weight:{v["fontWeight"]};line-height:{v["lineHeight"]}">Make automations</div></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Make style guide</title>
<style>
:root {{
{core_css}
{light_css}
  color-scheme: light;
  --sg-sans: Satoshi, Arial, "Helvetica Neue", Helvetica, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.5 var(--sg-sans); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-weight: 500; font-size: 40px; letter-spacing: -0.02em; margin: 0 0 8px; }}
h2 {{ font-weight: 500; font-size: 24px; margin: 40px 0 12px; }}
p.lead {{ color: var(--muted); max-width: 68ch; }}
.swatches {{ display: grid; gap: 8px; }}
.ramp {{ display: grid; grid-template-columns: 80px 1fr; align-items: center; gap: 8px; }}
.ramp span {{ font-size: 13px; color: var(--muted); }}
.cells {{ display: flex; gap: 3px; }}
.cells i {{ flex: 1; height: 36px; border-radius: 4px; box-shadow: inset 0 0 0 1px rgba(52,34,55,.08); }}
.roles {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.role {{ border: 1px solid var(--border); border-radius: 8px; padding: 12px; }}
.role i {{ display: block; height: 36px; border-radius: 6px; margin-bottom: 8px; box-shadow: inset 0 0 0 1px rgba(52,34,55,.08); }}
.role b {{ display: block; font-size: 13px; }}
.role span {{ font-size: 12px; color: var(--muted); }}
.typerow {{ display: grid; grid-template-columns: 180px 1fr; gap: 16px; padding: 10px 0; border-bottom: 1px solid var(--border); align-items: baseline; }}
.typerow .k {{ font-size: 12px; }}
.typerow small {{ display: block; color: var(--muted); }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; height: 47px; padding: 10px 18px; border-radius: var(--radius-small); font: 400 16px/1 var(--sg-sans); text-decoration: none; border: 1px solid transparent; }}
.btn-primary {{ background: var(--accent); color: var(--onAccent); border-color: var(--accent); }}
.btn-secondary {{ background: var(--surface); color: var(--text); border-color: var(--border); }}
.field {{ height: 40px; border: 1px solid var(--border); border-radius: var(--radius-small); padding: 0 12px; width: 280px; font: 400 16px var(--sg-sans); }}
.card {{ background: var(--surface); border-radius: var(--radius-main); box-shadow: var(--shadow-cardHover); padding: 20px; max-width: 320px; }}
.badge {{ display: inline-flex; border-radius: 999px; background: #dcfce7; color: #15803d; font-size: 12px; padding: 2px 8px; }}
.note {{ font-size: 13px; color: var(--muted); }}
</style>
</head>
<body>
<div class="wrap">
<h1>Make</h1>
<p class="lead">Public marketing site, one light theme. Values from tokens.json. Satoshi is proprietary and is not loaded here, so the page falls back to Arial.</p>
<h2>Colour ramps</h2>
<div class="swatches">{''.join(ramps)}</div>
<h2>Roles</h2>
<div class="roles">
  <div class="role"><i style="background:var(--page)"></i><b>page</b><span>var(--page)</span></div>
  <div class="role"><i style="background:var(--surface)"></i><b>surface</b><span>var(--surface)</span></div>
  <div class="role"><i style="background:var(--text)"></i><b>text</b><span>var(--text)</span></div>
  <div class="role"><i style="background:var(--muted)"></i><b>muted</b><span>var(--muted)</span></div>
  <div class="role"><i style="background:var(--accent)"></i><b>accent</b><span>var(--accent)</span></div>
  <div class="role"><i style="background:var(--accentHover)"></i><b>accent hover</b><span>var(--accentHover)</span></div>
  <div class="role"><i style="background:var(--link)"></i><b>link</b><span>var(--link)</span></div>
  <div class="role"><i style="background:var(--border)"></i><b>border</b><span>var(--border)</span></div>
  <div class="role"><i style="background:var(--success)"></i><b>success</b><span>var(--success)</span></div>
  <div class="role"><i style="background:var(--danger)"></i><b>danger</b><span>var(--danger)</span></div>
  <div class="role"><i style="background:var(--warning)"></i><b>warning</b><span>var(--warning)</span></div>
  <div class="role"><i style="background:var(--info)"></i><b>info</b><span>var(--info)</span></div>
</div>
<h2>Type</h2>
{''.join(type_rows)}
<p class="note">Desktop ends of Make's fluid clamps. Phone sizes are the clamp minimums in raw/css-vars.json.</p>
<h2>Components</h2>
<p><a class="btn btn-primary" href="#">Try it free</a> <a class="btn btn-secondary" href="#">Talk to sales</a></p>
<p><input class="field" placeholder="Search integrations..." aria-label="Search"></p>
<div class="card"><span class="badge">Save 15%</span><p>Pro plan card, radius main, card hover shadow.</p></div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
