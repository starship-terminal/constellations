#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Does not edit catalog.json."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
dark = tokens["dark"]["color"]
core = tokens["core"]

swatches = [
    ("page", dark["page"]["$value"]),
    ("header", dark["header"]["$value"]),
    ("text", dark["text"]["$value"]),
    ("muted", dark["muted"]["$value"]),
    ("accent", dark["accent"]["$value"]),
    ("on accent", dark["onAccent"]["$value"]),
    ("border", dark["border"]["$value"]),
]
chips = "\n".join(
    f'<div class="swatch"><i style="background:{value}"></i><span>{name}</span><code>{value}</code></div>'
    for name, value in swatches
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Apple TV tokens</title>
<style>
  :root {{
    --page: {dark["page"]["$value"]};
    --header: {dark["header"]["$value"]};
    --text: {dark["text"]["$value"]};
    --muted: {dark["muted"]["$value"]};
    --accent: {dark["accent"]["$value"]};
    --on-accent: {dark["onAccent"]["$value"]};
    --border: {dark["border"]["$value"]};
    --radius: {core["radius"]["control"]["$value"]};
    --sans: {core["font"]["family"]["sans"]["$value"]};
  }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 13px/1.23 var(--sans); }}
  header {{ background: var(--header); color: var(--text); height: 52px; display: flex; align-items: center; justify-content: space-between; padding: 0 16px; }}
  header strong {{ font-weight: 600; font-size: 16px; }}
  header button {{ background: var(--accent); color: var(--on-accent); border: 0; border-radius: var(--radius); height: 28px; padding: 0 12px; font: 600 13px/1 var(--sans); }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-weight: 600; font-size: 48px; line-height: 1.08; }}
  .swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
  .swatch {{ background: #000; border: 1px solid var(--border); border-radius: 8px; padding: 12px; }}
  .swatch i {{ display: block; height: 48px; border-radius: 6px; border: 1px solid var(--border); }}
  .swatch span, .swatch code {{ display: block; font-size: 13px; color: var(--muted); }}
  p.note {{ color: var(--muted); }}
</style>
</head>
<body>
<header><strong>Apple TV</strong><button type="button">Sign In</button></header>
<main>
  <h1>Apple TV</h1>
  <p class="note">Public browse tokens measured on tv.apple.com, 2026-11-22. Dark theme only. Signed out.</p>
  <div class="swatches" id="tokens">
    {chips}
  </div>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
