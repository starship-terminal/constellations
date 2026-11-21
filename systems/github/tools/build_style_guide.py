#!/usr/bin/env python3
"""Rebuild style-guide.html from tokens.json. Deterministic."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())

def val(path):
    node = tokens
    for part in path.split("."):
        node = node[part]
    return node["$value"]

roles = [
    ("page", "light.color.bg.canvas", "dark.color.bg.canvas"),
    ("surface", "light.color.bg.default", "dark.color.bg.default"),
    ("muted", "light.color.bg.muted", "dark.color.bg.muted"),
    ("text", "light.color.fg.default", "dark.color.fg.default"),
    ("muted text", "light.color.fg.muted", "dark.color.fg.muted"),
    ("accent", "light.color.accent.fg", "dark.color.accent.fg"),
    ("success", "light.color.success.emphasis", "dark.color.success.emphasis"),
    ("danger", "light.color.danger.emphasis", "dark.color.danger.emphasis"),
    ("attention", "light.color.attention.emphasis", "dark.color.attention.emphasis"),
    ("border", "light.color.border.default", "dark.color.border.default"),
]
rows = []
for name, light, dark in roles:
    rows.append(
        f'<div class="swatch"><span class="chip" style="background:{val(light)}"></span>'
        f'<span class="chip" style="background:{val(dark)}"></span>'
        f'<div><strong>{name}</strong><div class="meta">{val(light)} / {val(dark)}</div></div></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>GitHub public tokens</title>
<style>
  :root {{ color-scheme: light; }}
  body {{ margin: 0; font: 14px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; background: #fff; color: #1f2328; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-size: 32px; font-weight: 440; letter-spacing: -0.02em; margin: 0 0 8px; }}
  p {{ color: #59636e; }}
  .swatches {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; margin: 24px 0; }}
  .swatch {{ display: flex; gap: 10px; align-items: center; border: 1px solid #d1d9e0; border-radius: 6px; padding: 10px 12px; }}
  .chip {{ width: 28px; height: 28px; border-radius: 6px; border: 1px solid #d1d9e0; }}
  .meta {{ color: #59636e; font-size: 12px; }}
  .hero {{ background: #fff; border: 1px solid #d1d9e0; border-radius: 12px; padding: 32px; margin-top: 24px; }}
  .hero h2 {{ margin: 0 0 16px; font-size: 28px; font-weight: 440; }}
  .row {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; }}
  .field {{ background: #f6f8fa; color: #59636e; border-radius: 8px; padding: 12px 16px; min-width: 180px; }}
  .green {{ background: {val("light.color.button.hero")}; color: #fff; border: 0; border-radius: 6px; padding: 10px 16px; }}
  .quiet {{ background: rgba(0,0,0,0.06); border: 1px solid #d2d9d4; border-radius: 6px; padding: 10px 16px; }}
  .black {{ background: #000; color: #fff; border-radius: 6px; padding: 6px 12px; }}
  .note {{ margin-top: 24px; font-size: 13px; color: #59636e; }}
</style>
</head>
<body>
<main>
  <h1>GitHub public surface</h1>
  <p>Light chips first, dark chips second. Values are the Primer custom properties resolved on github.com on 2026-11-22. Mona Sans is not shipped; this page uses the system sans.</p>
  <div class="swatches">
    {''.join(rows)}
  </div>
  <div class="hero">
    <h2>Software still starts with you</h2>
    <div class="row">
      <div class="field">Enter your email</div>
      <button class="green">Sign up for GitHub</button>
      <button class="quiet">Download GitHub Copilot app</button>
      <span class="black">Sign up</span>
    </div>
  </div>
  <p class="note">The green hero button is sampled (#08792b). Primer's primary button token is {val("light.color.success.emphasis")}. The header Sign up pill is black. Login is a separate dark card.</p>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
