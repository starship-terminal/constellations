#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: Copperx publishes one theme."""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tokens.json").read_text())


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


def hex_of(path):
    # path is a token path. light.background.page lives under T["light"].
    # an alias {color.indigo} lives under T["core"]["color"].
    if path.startswith("light.") or path.startswith("core."):
        node = T
        for part in path.split("."):
            node = node[part]
    else:
        node = T["core"]
        for part in path.split("."):
            node = node[part]
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        return hex_of("core." + value[1:-1])
    return value


colors = [(path, hex_of("light." + path), tok) for path, tok in walk(T["light"]) if tok.get("$type") == "color"]
radii = [(path, tok["$value"]) for path, tok in walk(T["core"]["radius"])]
type_styles = list(walk(T["core"]["typography"]))

swatches = "\n".join(
    f'<div class="swatch"><i style="background:{value}"></i><div><b>{path.split(".")[-1]}</b><span>{value}</span><code>{path}</code></div></div>'
    for path, value, _ in colors
)
types = "\n".join(
    f'<p class="type" style="font-size:{tok["$value"]["fontSize"]};font-weight:{tok["$value"]["fontWeight"]};line-height:{tok["$value"]["lineHeight"]};letter-spacing:{tok["$value"]["letterSpacing"]}">'
    f'{path.split(".")[-1]} · {tok["$value"]["fontSize"]} / {tok["$value"]["lineHeight"]}</p>'
    for path, tok in type_styles
)
radius_html = "\n".join(
    f'<div class="radius" style="border-radius:{value}"><span>{path.split(".")[-1]} {value}</span></div>'
    for path, value in radii
)

page = hex_of("light.background.page")
text = hex_of("light.text.primary")
muted = hex_of("light.text.muted")
accent = hex_of("light.accent.default")
ink = hex_of("light.action.primary")
paper = hex_of("light.background.wash")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Copperx style guide</title>
<style>
  :root {{ color-scheme: light; }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: {page}; color: {text}; font: 400 16px/24px "Euclid Circular A", ui-sans-serif, system-ui, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-size: 48px; line-height: 52px; font-weight: 500; letter-spacing: -1.2px; margin: 0 0 8px; }}
  h2 {{ font-size: 16px; line-height: 24px; font-weight: 500; margin: 40px 0 12px; }}
  p.lede {{ color: {muted}; max-width: 46em; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
  .swatch {{ display: flex; gap: 12px; align-items: center; }}
  .swatch i {{ width: 48px; height: 48px; border-radius: 8px; border: 1px solid rgba(0,0,0,.12); display: block; }}
  .swatch b {{ display: block; font-size: 14px; font-weight: 500; }}
  .swatch span, .swatch code {{ display: block; color: {muted}; font-size: 12px; }}
  .type {{ margin: 8px 0; }}
  .radius {{ height: 48px; border: 1px solid rgba(106,115,133,.3); display: inline-flex; align-items: center; padding: 0 16px; margin-right: 12px; }}
  .btns {{ display: flex; gap: 12px; align-items: center; }}
  button, .btn {{ height: 36px; padding: 8px 12px; border-radius: 8px; border: 0; font: 500 14px/20px inherit; box-shadow: 0 1px 2px rgba(0,0,0,.06), 0 0 0 1px rgba(106,115,133,.16); }}
  .primary {{ background: {ink}; color: #fff; }}
  .secondary {{ background: #fff; color: #13171f; }}
  .link {{ color: {accent}; font-weight: 500; font-size: 14px; }}
  .note {{ color: {muted}; font-size: 14px; }}
</style>
</head>
<body>
<main>
  <h1>Copperx</h1>
  <p class="lede">Signed-out marketing tokens, measured on copperx.io. One light theme. Euclid Circular A is the product face and is not loaded here.</p>
  <h2>Colour</h2>
  <div class="swatches">{swatches}</div>
  <h2>Type</h2>
  {types}
  <h2>Radius</h2>
  {radius_html}
  <h2>Controls</h2>
  <div class="btns">
    <button class="primary">Get Started</button>
    <button class="secondary">Log in</button>
    <span class="link">Stablecoin Checkout</span>
  </div>
  <p class="note">Primary hover is {hex_of("light.action.primary-hover")}. Secondary hover is {paper}. Focus outline is the browser default {hex_of("light.border.focus")}.</p>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote", ROOT / "style-guide.html")
