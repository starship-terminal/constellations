#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Does not edit catalog.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
light = tokens["light"]["color"]
core = tokens["core"]

swatches = [
    ("page", light["page"]["$value"]),
    ("surface", light["surface"]["$value"]),
    ("footer", light["footer"]["$value"]),
    ("text", light["text"]["$value"]),
    ("muted", light["muted"]["$value"]),
    ("header", light["header"]["$value"]),
    ("accent", light["accent"]["$value"]),
    ("on accent", light["onAccent"]["$value"]),
    ("yellow", light["yellow"]["$value"]),
    ("link", light["link"]["$value"]),
]
chips = "\n".join(
    f'<div class="swatch"><i style="background:{value}"></i><span>{name}</span><code>{value}</code></div>'
    for name, value in swatches
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Booking.com tokens</title>
<style>
  :root {{
    --page: {light["page"]["$value"]};
    --surface: {light["surface"]["$value"]};
    --text: {light["text"]["$value"]};
    --muted: {light["muted"]["$value"]};
    --header: {light["header"]["$value"]};
    --accent: {light["accent"]["$value"]};
    --on-accent: {light["onAccent"]["$value"]};
    --yellow: {light["yellow"]["$value"]};
    --radius: {core["radius"]["control"]["$value"]};
    --sans: {core["font"]["family"]["sans"]["$value"]}, system-ui, sans-serif;
    --heading: {core["font"]["family"]["heading"]["$value"]}, system-ui, sans-serif;
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 14px/20px var(--sans); }}
  header {{ background: var(--header); color: white; padding: 16px 24px; font-weight: 700; font-size: 20px; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 48px 24px; }}
  h1 {{ font-family: var(--heading); font-weight: 700; font-size: 24px; line-height: 32px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
  .swatch {{ background: var(--surface); border-radius: var(--radius); padding: 12px; border: 1px solid #e7e7e7; }}
  .swatch i {{ display: block; height: 48px; border-radius: 6px; border: 1px solid #e7e7e7; }}
  .swatch span, .swatch code {{ display: block; font-size: 13px; color: var(--muted); }}
  button {{ background: var(--accent); color: var(--on-accent); border: 0; border-radius: var(--radius); height: 48px; padding: 0 24px; font: 500 16px/24px var(--sans); }}
  .frame {{ display: inline-block; background: var(--yellow); border-radius: 8px; padding: 4px; }}
  p.note {{ color: var(--muted); }}
</style>
</head>
<body>
<header>Booking.com</header>
<main>
  <h1>Booking.com</h1>
  <p class="note">Public marketing tokens measured on booking.com, 2026-11-22. Light theme only. Font stacks fall back to system-ui.</p>
  <p class="frame"><button type="button">Search</button></p>
  <div class="swatches">
    {chips}
  </div>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
