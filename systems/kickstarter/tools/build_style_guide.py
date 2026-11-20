#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One light theme. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


colors = [(n, t) for n, t in flat(T["light"]["color"]) if t.get("$type") == "color"]
radii = list(flat(T["core"]["radius"]))
spaces = list(flat(T["core"]["spacing"]))
types = list(flat(T["core"]["typography"]))
shadows = list(flat(T["core"]["elevation"]))

swatches = []
for name, tok in colors:
    val = tok["$value"]
    swatches.append(
        f'<div class="sw"><i style="background:{val}"></i><div><code>{name}</code><span>{val}</span></div></div>'
    )

type_rows = []
for name, tok in types:
    v = tok["$value"]
    type_rows.append(
        f'<div class="ty" style="font:{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} Inter,sans-serif">{name}<small>{v["fontSize"]} / {v["lineHeight"]} / {v["fontWeight"]}</small></div>'
    )

space_rows = "".join(
    f'<div class="sp"><i style="width:{t["$value"]}"></i><code>{n}</code><span>{t["$value"]}</span></div>'
    for n, t in spaces
)
radius_rows = "".join(
    f'<div class="rd" style="border-radius:{t["$value"]}"><code>{n}</code><span>{t["$value"]}</span></div>'
    for n, t in radii
)

def shadow_css(tok):
    v = tok["$value"]
    if isinstance(v, dict):
        return f'{v["offsetX"]} {v["offsetY"]} {v["blur"]} {v["spread"]} {v["color"]}'
    return "none"

shadow_rows = "".join(
    f'<div class="el" style="box-shadow:{shadow_css(t)}"><code>elevation.{n}</code></div>'
    for n, t in shadows
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kickstarter style guide</title>
<style>
  :root {{
    --page: #ffffff;
    --text: #171717;
    --muted: #4d4d4d;
    --line: #e0e0e0;
    --brand: #05ce78;
    --action: #171717;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 400 15px/1.5 Inter, sans-serif; }}
  header {{ display: flex; align-items: center; gap: 16px; padding: 16px 28px; border-bottom: 1px solid var(--line); position: sticky; top: 0; background: #fff; }}
  header strong {{ color: var(--brand); letter-spacing: 0.04em; }}
  main {{ max-width: 1080px; margin: 0 auto; padding: 28px; }}
  h2 {{ font-size: 22px; font-weight: 500; margin: 36px 0 12px; }}
  p.lead {{ color: var(--muted); max-width: 68ch; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 10px; }}
  .sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
  .sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px #e0e0e0; }}
  .sw code, .ty small, .sp span, .rd span {{ display: block; color: var(--muted); font-size: 12px; }}
  .ty {{ padding: 10px 0; border-bottom: 1px solid var(--line); }}
  .ty small {{ font: 400 12px/1.4 Inter, sans-serif; }}
  .sp {{ display: flex; align-items: center; gap: 12px; margin: 6px 0; }}
  .sp i {{ height: 12px; background: var(--brand); display: block; }}
  .rds {{ display: flex; gap: 12px; flex-wrap: wrap; }}
  .rd {{ width: 88px; height: 64px; border: 1px solid var(--line); display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 12px; }}
  .els {{ display: flex; gap: 16px; flex-wrap: wrap; }}
  .el {{ width: 140px; height: 72px; background: #fff; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 12px; }}
  .specimens {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
  .btn {{ background: #037242; color: #fff; border: 0; border-radius: 4px; padding: 10px 16px; font: 500 14px/20px Inter, sans-serif; }}
  .btn.dark {{ background: #171717; }}
  .btn.ghost {{ background: #fff; color: #171717; border: 1px solid #c9c9c9; }}
  .field {{ border: 1px solid #e0e0e0; border-radius: 4px; padding: 10px 12px; min-width: 220px; color: #636363; }}
  .card {{ width: 220px; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px 0 rgba(0,0,0,.18); }}
  .card .media {{ height: 88px; background: #171717; }}
  .card .body {{ padding: 10px 12px; font-size: 13px; }}
  .bar {{ height: 4px; background: #05ce78; width: 70%; }}
  nav a {{ color: var(--muted); text-decoration: none; margin-right: 14px; font-size: 14px; }}
</style>
</head>
<body>
<header>
  <strong>KICKSTARTER</strong>
  <nav><a href="#color">Colour</a><a href="#type">Type</a><a href="#space">Space</a><a href="#shape">Shape</a><a href="#components">Components</a></nav>
</header>
<main>
  <p class="lead">Kickstarter's public KDS tokens, rendered from tokens.json. One light theme. Captured 2026-11-18, signed out. Inter is named but not loaded: the page fetches nothing, so it renders in a locally installed Inter or the sans-serif fallback; the brand green is #05CE78.</p>
  <h2 id="color">Colour</h2>
  <div class="grid">{''.join(swatches)}</div>
  <h2 id="type">Type</h2>
  {''.join(type_rows)}
  <h2 id="space">Spacing</h2>
  {space_rows}
  <h2 id="shape">Radius and elevation</h2>
  <div class="rds">{radius_rows}</div>
  <div class="els" style="margin-top:16px">{shadow_rows}</div>
  <h2 id="components">Components</h2>
  <div class="specimens">
    <button class="btn">Back this project</button>
    <button class="btn dark">Sign in with Apple</button>
    <button class="btn ghost">For creators</button>
    <div class="field">Search projects, creators, and categories</div>
    <div class="card"><div class="media"></div><div class="bar"></div><div class="body">Project title<br><span style="color:#4d4d4d">16 days left</span></div></div>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(colors), "colours")
