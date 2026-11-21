#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One light theme. Deterministic."""
import html
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


def esc(s):
    return html.escape(str(s))


rows = []
for path, leaf in walk(T["light"]):
    val = leaf["$value"]
    if leaf.get("$type") == "color":
        rows.append(
            f'<div class="sw"><i style="background:{esc(val)}"></i>'
            f'<div><div class="nm">light.{esc(path)}</div><div class="vl">{esc(val)}</div></div></div>'
        )

ramps = []
colors = T["core"].get("color", {}).get("color", {})
for family, steps in colors.items():
    if not isinstance(steps, dict):
        continue
    chips = []
    for step, leaf in steps.items():
        if isinstance(leaf, dict) and leaf.get("$type") == "color":
            chips.append(f'<i title="{esc(family)} {esc(step)} {esc(leaf["$value"])}" style="background:{esc(leaf["$value"])}"></i>')
    if chips:
        ramps.append(f'<div class="ramp"><span>{esc(family)}</span><div class="chips">{"".join(chips)}</div></div>')

sizes = []
size_node = T["core"]["typography"]["size"]["text"]
for step, leaf in size_node.items():
    if not isinstance(leaf, dict) or "$value" not in leaf:
        continue
    px = leaf["$value"]
    sizes.append(
        f'<div class="ty"><code>text.{esc(step)}</code> <span style="font-size:{esc(px)}">{esc(px)} Column</span></div>'
    )

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Column style guide</title>
<style>
  :root {{ color-scheme: light; }}
  body {{ margin: 0; background: #fff; color: #12161e; font: 400 15px/1.45 ui-sans-serif, system-ui, sans-serif; }}
  main {{ max-width: 980px; margin: 0 auto; padding: 32px 20px 80px; }}
  h1 {{ font-size: 32px; font-weight: 500; letter-spacing: -0.03em; margin: 0 0 8px; }}
  h2 {{ font-size: 18px; margin: 36px 0 12px; }}
  p {{ color: #575a64; max-width: 68ch; }}
  .roles {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; }}
  .sw i {{ width: 36px; height: 36px; border-radius: 8px; box-shadow: inset 0 0 0 1px #e3e4e8; display: block; }}
  .nm {{ font: 600 12px/1.3 ui-monospace, monospace; }}
  .vl {{ font-size: 12px; color: #7c7f88; }}
  .ramp {{ display: grid; grid-template-columns: 88px 1fr; gap: 8px; align-items: center; margin: 4px 0; }}
  .chips {{ display: flex; gap: 2px; }}
  .chips i {{ flex: 1; height: 28px; border-radius: 3px; }}
  .ty {{ display: flex; gap: 16px; align-items: baseline; border-bottom: 1px solid #eeeff2; padding: 8px 0; }}
  .ty code {{ width: 88px; color: #7c7f88; font-size: 12px; }}
  button.demo {{ background: #111a4a; color: #fff; border: 0; border-radius: 8px; padding: 10px 16px; font: 500 14px/1 sans-serif; }}
  button.ghost {{ background: #fff; color: #232730; border: 1px solid #e3e4e8; border-radius: 8px; padding: 10px 16px; font: 500 14px/1 sans-serif; }}
  .row {{ display: flex; gap: 12px; align-items: center; }}
</style>
</head>
<body>
<main>
  <h1>Column</h1>
  <p>Public marketing tokens read from column.com on 2026-11-21. One light theme. Suisse Intl is not loaded here; the page uses the system sans.</p>
  <h2>Roles</h2>
  <div class="roles">{''.join(rows)}</div>
  <h2>Buttons</h2>
  <div class="row"><button class="demo">Get started</button><button class="ghost">Sign in</button></div>
  <h2>Type sizes</h2>
  {''.join(sizes)}
  <h2>Ramps</h2>
  {''.join(ramps)}
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("wrote style-guide.html", len(page))
