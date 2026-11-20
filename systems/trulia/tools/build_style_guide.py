#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: Trulia ships no dark theme."""
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


def css_name(path):
    return "--" + path.replace(".", "-")


colors = [(p, n) for p, n in walk(T["core"]["color"])]
semantic = [(p, n) for p, n in walk(T["light"]["color"])]
spaces = list(walk(T["core"]["space"]))
radii = list(walk(T["core"]["radius"]))
sizes = list(walk(T["core"]["fontSize"]))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{n["$value"]}"></i><span>{p.split(".")[-1]}</span><code>{n["$value"]}</code></div>'
    for p, n in colors
)
sem = "\n".join(
    f'<div class="sw"><i style="background:var({css_name("color."+p)})"></i><span>{p}</span><code>{n["$value"]}</code></div>'
    for p, n in semantic
)
type_rows = "\n".join(
    f'<div style="font-size:{n["$value"]};line-height:1.2">{p} {n["$value"]}</div>'
    for p, n in sizes
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trulia style guide</title>
<style>
:root {{
  --font: Figtree, "Figtree Fallback", Arial, sans-serif;
  --page: #ffffff;
  --surface: #f5f6f7;
  --text: #3b4144;
  --muted: #6b7780;
  --accent: #007882;
  --border: #cdd1d4;
  --search: #d93c23;
{chr(10).join(f'  {css_name(p)}: {n["$value"]};' for p, n in colors)}
{chr(10).join(f'  {css_name("color."+p)}: var({css_name(n["$value"].strip("{{}}"))});' for p, n in semantic)}
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/1.5 var(--font); }}
header {{ padding: 24px 32px; border-bottom: 1px solid var(--border); display: flex; justify-content: space-between; align-items: center; }}
h1 {{ margin: 0; font-size: 24px; font-weight: 900; letter-spacing: -0.1px; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px; }}
h2 {{ font-size: 20px; font-weight: 700; margin: 32px 0 12px; }}
.grid {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ width: 140px; }}
.sw i {{ display: block; height: 56px; border-radius: 8px; border: 1px solid var(--border); }}
.sw span, .sw code {{ display: block; font-size: 12px; color: var(--muted); }}
.row {{ display: flex; gap: 12px; align-items: center; margin: 8px 0; }}
button.login {{ background: #fff; color: var(--text); border: 1px solid var(--border); border-radius: 8px; padding: 8px 16px; font: 700 16px/24px var(--font); }}
button.primary {{ background: var(--accent); color: #fff; border: 0; border-radius: 8px; padding: 8px 16px; font: 700 16px/24px var(--font); }}
button.search {{ background: var(--search); color: #fff; border: 0; border-radius: 0 8px 8px 0; width: 60px; height: 42px; }}
.field {{ border: 1px solid #869099; border-radius: 8px; height: 42px; padding: 0 12px; display: flex; align-items: center; color: var(--muted); width: 280px; }}
.card {{ background: var(--surface); border-radius: 16px; padding: 16px; }}
</style>
</head>
<body>
<header>
  <h1>Trulia</h1>
  <button class="login">Sign up or Log in</button>
</header>
<main>
  <p>Rendered from tokens.json. Light only. Figtree is not bundled; the page falls back to Arial.</p>
  <h2>Semantic roles</h2>
  <div class="grid">{sem}</div>
  <h2>Palette</h2>
  <div class="grid">{swatches}</div>
  <h2>Type scale</h2>
  {type_rows}
  <h2>Controls</h2>
  <div class="row"><button class="login">Sign up or Log in</button><button class="primary">Submit</button><button class="search">Go</button></div>
  <div class="row"><div class="field">Search for City, Neighborhood, Zip</div></div>
  <div class="card">Surface card. Radius large is 16px. Page text is grey.900.</div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
