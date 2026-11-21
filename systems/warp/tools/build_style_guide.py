#!/usr/bin/env python3
"""Write style-guide.html from tokens.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())
light = tokens["light"]["color"]

def v(node):
    return node["$value"]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Warp public tokens</title>
<style>
  body {{ margin: 0; padding: 32px; background: {v(light['page'])}; color: {v(light['ink'])}; font: 16px/24px Matter, system-ui, sans-serif; }}
  h1 {{ font: 400 40px/1.18 ui-monospace, monospace; margin: 0 0 8px; }}
  p {{ color: {v(light['muted'])}; max-width: 42rem; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 24px 0; }}
  .swatch {{ width: 140px; }}
  .chip {{ height: 72px; border-radius: 4px; border: 1px solid rgba(26,21,34,.12); }}
  .label {{ font: 12px/1.4 ui-monospace, monospace; margin-top: 6px; }}
  .cta {{ display: inline-block; background: {v(light['cta'])}; color: {v(light['on-cta'])}; border-radius: 4px; padding: 6px 16px; font: 500 13px/1.4 ui-monospace, monospace; text-decoration: none; }}
  .demo {{ display: inline-block; background: {v(light['demo'])}; color: {v(light['on-demo'])}; border-radius: 999px; padding: 6px 16px; font: 500 12px/1.4 ui-monospace, monospace; text-decoration: none; margin-left: 8px; }}
</style>
</head>
<body>
  <h1>The software factory infrastructure platform</h1>
  <p>Public Warp marketing tokens, read from warp.dev on 2026-11-22. One painted theme.</p>
  <div class="row">
    <div class="swatch"><div class="chip" style="background:{v(light['page'])}"></div><div class="label">page</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['ink'])}"></div><div class="label">ink</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['cta'])}"></div><div class="label">cta</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['demo'])}"></div><div class="label">demo</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['banner'])}"></div><div class="label">banner</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['accent-declared'])}"></div><div class="label">accent declared</div></div>
  </div>
  <a class="cta" href="#cta">request early access</a>
  <a class="demo" href="#demo">BOOK A DEMO</a>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
