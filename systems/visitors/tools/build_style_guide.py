#!/usr/bin/env python3
"""Render a self-contained style-guide.html from tokens.json.

The kit template expects Claude-shaped component tokens. Visitors does not
have those, so this builder writes its own page from the measured sets.
"""
import json, pathlib, html

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


def swatch(path, token):
    value = token["$value"]
    if token["$type"] != "color":
        return ""
    label = html.escape(path)
    shown = html.escape(str(value))
    return (
        f'<div class="swatch"><i style="background:{html.escape(str(value))}"></i>'
        f'<span>{label}</span><code>{shown}</code></div>'
    )


def theme_block(name):
    bits = [swatch(path, token) for path, token in flat(T[name])]
    return f'<section data-theme="{name}"><h2>{name}</h2><div class="grid">{"".join(bits)}</div></section>'


ramps = []
for hue, steps in T["core"]["palette"].items():
    if hue.endswith("-alpha"):
        continue
    cells = []
    for step, token in steps.items():
        cells.append(
            f'<i title="{hue}-{step} {token["$value"]}" style="background:{token["$value"]}"></i>'
        )
    ramps.append(f'<div class="ramp"><b>{hue}</b>{"".join(cells)}</div>')

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Visitors style guide</title>
<style>
  :root {{ color-scheme: light; }}
  body {{ margin: 0; font: 16px/1.5 "Open Runde", Inter, sans-serif; background: #fff; color: #181925; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 20px 80px; }}
  h1 {{ font-size: 36px; letter-spacing: -0.04em; margin: 0 0 8px; }}
  p.note {{ color: #666; max-width: 62ch; }}
  h2 {{ font-size: 20px; margin: 32px 0 12px; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 8px; }}
  .swatch {{ display: grid; grid-template-columns: 28px 1fr; gap: 2px 8px; align-items: center; font-size: 12px; }}
  .swatch i {{ width: 28px; height: 28px; border-radius: 8px; grid-row: span 2; box-shadow: inset 0 0 0 1px #00000014; }}
  .swatch code {{ color: #666; }}
  .ramp {{ display: flex; align-items: center; gap: 4px; margin: 6px 0; }}
  .ramp b {{ width: 72px; font-size: 13px; }}
  .ramp i {{ width: 48px; height: 28px; border-radius: 6px; box-shadow: inset 0 0 0 1px #00000014; }}
  .mock {{ display: flex; gap: 12px; align-items: center; margin-top: 12px; }}
  .pill {{ background: #918df6; color: #fff; border: 0; border-radius: 999px; height: 44px; padding: 0 20px; font: 500 16px/1 "Open Runde", Inter, sans-serif; }}
  .quiet {{ background: #00000008; color: #666; border: 0; border-radius: 999px; height: 44px; padding: 0 20px; font: 500 16px/1 "Open Runde", Inter, sans-serif; }}
  .field {{ background: #f5f5f5; border: 0; border-radius: 12px; height: 40px; padding: 0 16px; width: 240px; font: 500 16px/1 "Open Runde", Inter, sans-serif; }}
  [data-theme="dark"] {{ background: #14141f; color: #eaeaeb; padding: 16px; border-radius: 16px; }}
</style>
</head>
<body>
<main>
  <h1>Visitors</h1>
  <p class="note">Values come from the live stylesheet on visitors.now, read 2026-11-21. Light is what the public pages rendered. Dark is the <code>.dark</code> block in that file. It was not applied on any public page.</p>
  <h2>Controls, from computed styles on /login and /</h2>
  <div class="mock">
    <button class="pill">Start 14 day free trial</button>
    <button class="quiet">See demo</button>
    <input class="field" placeholder="Email address" readonly>
  </div>
  <h2>Ramps (:root)</h2>
  {''.join(ramps)}
  {theme_block('light')}
  {theme_block('dark')}
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("wrote style-guide.html", len(page))
