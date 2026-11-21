#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())
CORE = TOKENS["core"]["color"]

def hex_of(token):
    return token["$value"]

rows = []
for group, items in CORE.items():
    for name, token in items.items():
        rows.append((f"{group}.{name}", hex_of(token)))

swatches = "\n".join(
    f'<div class="sw"><i style="background:{v}"></i><span>{n}</span><code>{v}</code></div>'
    for n, v in rows
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>fal style guide</title>
<style>
body {{ margin: 0; font: 16px/1.4 Arial, sans-serif; background: #fff; color: #111; }}
header {{ padding: 24px; background: #403700; color: #99edff; }}
main {{ padding: 24px; display: grid; gap: 16px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 8px; }}
.sw {{ display: flex; gap: 8px; align-items: center; border: 1px solid #eee; padding: 8px; }}
.sw i {{ width: 36px; height: 36px; border-radius: 4px; border: 1px solid #ddd; }}
code {{ font-size: 12px; color: #444; }}
.btn {{ display: inline-block; padding: 10px 16px; border-radius: 4px; margin-right: 8px; text-decoration: none; font-weight: 600; }}
</style>
</head>
<body>
<header>
  <h1>fal public tokens</h1>
  <p>Marketing bronze and neon, plus the signed-out app shell. Values from tokens.json.</p>
</header>
<main>
  <section>
    <a class="btn" style="background:#adff00;color:#000">Get Started</a>
    <a class="btn" style="background:#e5ece7;color:#000">Contact Sales</a>
    <a class="btn" style="background:#000;color:#fff">Header start</a>
  </section>
  <section class="grid">
    {swatches}
  </section>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
