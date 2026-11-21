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
    ("text", light["text"]["$value"]),
    ("muted", light["muted"]["$value"]),
    ("link", light["link"]["$value"]),
    ("brand", light["brand"]["$value"]),
    ("brand soft", light["brandSoft"]["$value"]),
    ("accent", light["accent"]["$value"]),
    ("accent hover", light["accentHover"]["$value"]),
    ("buy", light["buy"]["$value"]),
    ("search scope", light["searchScope"]["$value"]),
    ("on accent", light["onAccent"]["$value"]),
]
chips = "\n".join(
    f'<div class="swatch"><i style="background:{value}"></i><span>{name}</span><code>{value}</code></div>'
    for name, value in swatches
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Amazon tokens</title>
<style>
  :root {{
    --page: {light["page"]["$value"]};
    --surface: {light["surface"]["$value"]};
    --text: {light["text"]["$value"]};
    --muted: {light["muted"]["$value"]};
    --accent: {light["accent"]["$value"]};
    --on-accent: {light["onAccent"]["$value"]};
    --brand: {light["brand"]["$value"]};
    --buy: {light["buy"]["$value"]};
    --link: {light["link"]["$value"]};
    --radius: {core["radius"]["control"]["$value"]};
    --sans: {core["font"]["family"]["sans"]["$value"]};
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 14px/20px var(--sans); }}
  header {{ background: var(--brand); color: #fff; height: 60px; display: flex; align-items: center; padding: 0 16px; font-weight: 700; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-weight: 400; font-size: 28px; line-height: 36px; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
  .swatch {{ background: var(--surface); border: 1px solid #e6e6e6; border-radius: 8px; padding: 12px; }}
  .swatch i {{ display: block; height: 48px; border-radius: 6px; border: 1px solid #e6e6e6; }}
  .swatch span, .swatch code {{ display: block; font-size: 13px; color: var(--muted); }}
  button {{ background: var(--accent); color: var(--on-accent); border: 1px solid var(--accent); border-radius: var(--radius); height: 32px; padding: 0 16px; font: 14px/20px var(--sans); }}
  button.buy {{ background: var(--buy); border-color: var(--buy); }}
  a {{ color: var(--link); }}
  p.note {{ color: var(--muted); }}
</style>
</head>
<body>
<header>amazon</header>
<main>
  <h1>Amazon</h1>
  <p class="note">Public storefront tokens measured on amazon.com, 2026-11-22. Light theme only. Signed out.</p>
  <p><button type="button">Add to cart</button> <button class="buy" type="button">Buy Now</button></p>
  <p><a href="#tokens">Conditions of Use</a></p>
  <div class="swatches" id="tokens">
    {chips}
  </div>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
