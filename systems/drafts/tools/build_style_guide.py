#!/usr/bin/env python3
"""Write style-guide.html from tokens.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
light = tokens["light"]["color"]
display = tokens["core"]["typography"]["display"]["$value"]

def v(node):
    return node["$value"]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Drafts public tokens</title>
<style>
  body {{ margin: 0; padding: 32px; background: {v(light['page'])}; color: {v(light['ink'])}; font: 17px/27.2px -apple-system, system-ui, sans-serif; }}
  h1 {{ font: {display['fontWeight']} {display['fontSize']}/{display['lineHeight']} -apple-system, system-ui, sans-serif; letter-spacing: {display['letterSpacing']}; margin: 0 0 8px; }}
  p {{ color: {v(light['muted'])}; max-width: 42rem; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 24px 0; }}
  .swatch {{ width: 140px; }}
  .chip {{ height: 72px; border-radius: 6px; border: 1px solid rgba(22,28,45,.12); }}
  .label {{ font: 12px/1.4 ui-monospace, monospace; margin-top: 6px; }}
  .cta {{ display: inline-block; background: {v(light['cta'])}; color: {v(light['on-cta'])}; border-radius: 6px; padding: 9px 16px; font: 600 17px/27.2px -apple-system, system-ui, sans-serif; text-decoration: none; }}
</style>
</head>
<body>
  <h1>How Drafts Works</h1>
  <p>Public Drafts marketing tokens, read from getdrafts.com on 2026-11-22. One painted theme.</p>
  <div class="row">
    <div class="swatch"><div class="chip" style="background:{v(light['page'])}"></div><div class="label">page</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['ink'])}"></div><div class="label">ink</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['muted'])}"></div><div class="label">muted</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['cover'])}"></div><div class="label">cover sample</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['footer'])}"></div><div class="label">footer</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['cta'])}"></div><div class="label">cta</div></div>
  </div>
  <a class="cta" href="#home">Drafts Home</a>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
