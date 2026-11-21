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
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "other":
        return None
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "typography":
        return None
    if isinstance(v, dict):
        return None
    return alias(v)


lines = []
for name, tok in list(flat(T["core"])) + list(flat(T["light"])):
    val = css_val(tok)
    if val:
        lines.append(f"  {cssname(name)}: {val};")

swatches = []
for name, tok in flat(T["core"], ""):
    if tok["$type"] == "color" and isinstance(tok["$value"], str) and tok["$value"].startswith("#"):
        swatches.append(f'<div class="sw"><i style="background:{tok["$value"]}"></i><span>{name}<br>{tok["$value"]}</span></div>')

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Scape style guide</title>
<style>
:root {{
{chr(10).join(lines)}
  --sg-sans: Arial, sans-serif;
  --sg-display: "Arial Narrow", Arial, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 16px/24px var(--sg-sans); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 64px; }}
h1 {{ font: 700 48px/1 var(--sg-display); text-transform: uppercase; margin: 0 0 8px; }}
h2 {{ font: 700 28px/1 var(--sg-display); text-transform: uppercase; margin: 40px 0 12px; }}
p {{ max-width: 68ch; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 64px; border-radius: 4px; border: 1px solid var(--border-default); }}
.sw span {{ display: block; font-size: 12px; line-height: 16px; margin-top: 4px; }}
.btn {{ display: inline-flex; align-items: center; height: var(--size-button); padding: 10px 14px; border-radius: var(--radius-pill); border: 1px solid transparent; font-size: 14px; line-height: 14px; text-transform: uppercase; text-decoration: none; }}
.btn-fill {{ background: var(--action-primary-background); color: var(--action-primary-text); }}
.btn-line {{ background: transparent; color: var(--action-secondary-text); border-color: var(--border-strong); background: var(--action-secondary-background); }}
.chip {{ display: inline-flex; height: 26px; align-items: center; padding: 6px 12px 4px; border-radius: var(--radius-tab); border: 1px solid var(--border-default); font-size: 14px; }}
.card {{ background: var(--background-surface); box-shadow: var(--shadow-card); padding: 16px; max-width: 280px; }}
.field {{ display: block; width: 280px; padding: 12px 20px; border-radius: var(--radius-field); border: 1px solid var(--border-default); background: var(--background-page); color: var(--text-primary); font: inherit; }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
</style>
</head>
<body>
<div class="wrap">
<h1>Scape</h1>
<p>Rendered from tokens.json. Visuelt and Grotzec Condensed are proprietary, so this page uses Arial. One light theme.</p>
<h2>Colour</h2>
<div class="swatches">
{chr(10).join(swatches)}
</div>
<h2>Type</h2>
<p style="font: 700 64px/0.84 var(--sg-display); text-transform: uppercase; margin: 0;">Student living</p>
<p>Body is 16px / 24px. Labels are 14px, uppercase on buttons.</p>
<h2>Controls</h2>
<div class="row">
<a class="btn btn-fill" href="#">Find a room</a>
<a class="btn btn-line" href="#">Book</a>
<span class="chip">Location</span>
</div>
<h2>Field and card</h2>
<input class="field" placeholder="Search" aria-label="Example field">
<div class="card" style="margin-top:16px"><strong>Wembley</strong><p>Room card surface.</p></div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
