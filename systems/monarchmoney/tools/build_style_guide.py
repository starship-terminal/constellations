#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def css_name(path):
    return "--" + path.replace(".", "-")


swatches = []
for path, token in flat(T["light"]):
    if token["$type"] != "color":
        continue
    swatches.append(
        f'<div class="sw"><i style="background:{html.escape(token["$value"])}"></i>'
        f'<div><b>{html.escape(path)}</b><span>{html.escape(token["$value"])}</span></div></div>'
    )

ramps = []
for hue in ("gray", "orange", "blue", "green", "red", "yellow"):
    cells = []
    for i in range(1, 13):
        token = T["core"]["color"][hue][str(i)]
        cells.append(f'<i title="{hue}-{i} {token["$value"]}" style="background:{token["$value"]}"></i>')
    ramps.append(f'<div class="ramp"><span>{hue}</span>{"".join(cells)}</div>')

type_rows = []
for name, token in T["core"]["typography"].items():
    v = token["$value"]
    type_rows.append(
        f'<div class="ty" style="font-size:{v["fontSize"]};font-weight:{v["fontWeight"]};line-height:{v["lineHeight"]}">'
        f'<code>{html.escape(name)}</code> {html.escape(v["fontSize"])} / {v["lineHeight"]} / {v["fontWeight"]}'
        f'<div class="sample">The modern way to manage money</div></div>'
    )

roles = "".join(
    f"  {css_name(path)}: {token['$value']};\n"
    for path, token in flat(T["light"])
    if token["$type"] == "color"
)

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Monarch Money style guide</title>
<style>
:root {{
{roles}  --sg-sans: "ABC Oracle", ui-sans-serif, system-ui, sans-serif;
  --sg-display: "ABC Otto", Georgia, serif;
  --sg-mono: "Beltram Mono", ui-monospace, monospace;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 350 16px/1.4 var(--sg-sans); }}
main {{ max-width: 1080px; margin: 0 auto; padding: 40px 24px 80px; }}
h1 {{ font-family: var(--sg-display); font-weight: 400; font-size: 48px; line-height: 1.1; margin: 0 0 8px; }}
h2 {{ font-size: 14px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin: 40px 0 12px; }}
.lead {{ max-width: 62ch; color: var(--muted); }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }}
.sw {{ display: flex; gap: 10px; align-items: center; }}
.sw i {{ width: 36px; height: 36px; border-radius: 8px; border: 1px solid var(--border); display: block; }}
.sw b {{ display: block; font: 500 12px/1.3 var(--sg-mono); }}
.sw span {{ color: var(--muted); font: 12px/1.3 var(--sg-mono); }}
.ramp {{ display: grid; grid-template-columns: 72px repeat(12, 1fr); gap: 3px; align-items: center; margin: 4px 0; }}
.ramp span {{ font: 12px/1 var(--sg-mono); color: var(--muted); }}
.ramp i {{ height: 28px; border-radius: 4px; display: block; }}
.ty {{ border-top: 1px solid var(--border); padding: 12px 0; }}
.ty code {{ font: 12px/1 var(--sg-mono); color: var(--muted); margin-right: 8px; }}
.sample {{ font-family: var(--sg-display); }}
.btn {{ display: inline-flex; align-items: center; height: 44px; padding: 0 18px; border-radius: 999px; background: var(--accent); color: var(--onAccent); font-weight: 500; }}
.btn.quiet {{ background: var(--surface); color: var(--text); border: 1px solid var(--border); }}
.card {{ background: var(--surface); border-radius: 16px; padding: 20px; max-width: 360px; box-shadow: 0 8px 24px rgba(34,32,29,.08); }}
.note {{ color: var(--muted); font-size: 13px; max-width: 70ch; }}
</style>
</head>
<body>
<main>
<h1>Monarch Money</h1>
<p class="lead">Public marketing tokens from www.monarch.com, read 2026-11-21. One light theme. Proprietary faces fall back to system fonts. Values come from tokens.json.</p>
<h2>Roles</h2>
<div class="swatches">{''.join(swatches)}</div>
<h2>Ramps</h2>
{''.join(ramps)}
<h2>Type</h2>
{''.join(type_rows)}
<h2>Components</h2>
<p class="note">Button and card geometry is drawn from screenshots. Radii and heights were not declared as custom properties, so they are not tokens.</p>
<p><span class="btn">Sign up</span> <span class="btn quiet">Sign in</span></p>
<div class="card"><strong>Core</strong><p>Budget, save, and stay on track</p><span class="btn">Try Monarch free for 7 days</span></div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("wrote", HERE / "style-guide.html")
