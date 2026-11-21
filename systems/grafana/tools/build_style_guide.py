#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Does not edit catalog.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
light = tokens["light"]["color"]
core = tokens["core"]

def hex_of(group, name):
    return light[group][name]["$value"] if group in light and isinstance(light.get(group), dict) else light[name]["$value"]

swatches = [
    ("page", light["page"]["$value"]),
    ("surface", light["surface"]["$value"]),
    ("text", light["text"]["$value"]),
    ("muted", light["muted"]["$value"]),
    ("accent", light["accent"]["$value"]),
    ("accent hover", light["accentHover"]["$value"]),
    ("brand", light["brand"]["$value"]),
    ("success", light["success"]["$value"]),
    ("danger", light["danger"]["$value"]),
    ("warning", light["warning"]["$value"]),
]
chips = "\n".join(
    f'<div class="swatch"><i style="background:{value}"></i><span>{name}</span><code>{value}</code></div>'
    for name, value in swatches
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Grafana tokens</title>
<style>
  :root {{
    --page: {light["page"]["$value"]};
    --surface: {light["surface"]["$value"]};
    --text: {light["text"]["$value"]};
    --muted: {light["muted"]["$value"]};
    --accent: {light["accent"]["$value"]};
    --on-accent: {light["onAccent"]["$value"]};
    --brand: {light["brand"]["$value"]};
    --radius: {core["radius"]["control"]["$value"]};
    --sans: {core["font"]["family"]["sans"]["$value"]};
    --heading: {core["font"]["family"]["heading"]["$value"]};
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 16px/1.5 var(--sans); }}
  main {{ max-width: 960px; margin: 0 auto; padding: 48px 24px; }}
  h1 {{ font-family: var(--heading); font-weight: 600; letter-spacing: -1px; font-size: 40px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
  .swatch {{ background: var(--surface); border-radius: var(--radius); padding: 12px; }}
  .swatch i {{ display: block; height: 48px; border-radius: 6px; border: 1px solid #e6e6ea; }}
  .swatch span, .swatch code {{ display: block; font-size: 13px; color: var(--muted); }}
  button {{ background: var(--accent); color: var(--on-accent); border: 0; border-radius: var(--radius); height: 36px; padding: 0 14px; font: 500 14px/20px var(--sans); }}
  p.note {{ color: var(--muted); }}
</style>
</head>
<body>
<main>
  <h1>Grafana</h1>
  <p class="note">Public marketing tokens measured on grafana.com, 2026-11-22. Light theme only.</p>
  <p><button type="button">Sign up</button></p>
  <div class="swatches">
    {chips}
  </div>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
