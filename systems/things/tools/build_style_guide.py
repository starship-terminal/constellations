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
<title>Things public tokens</title>
<style>
  body {{ margin: 0; padding: 32px; background: {v(light['page'])}; color: {v(light['ink'])}; font: 18px/1.4 ui-sans-serif, system-ui, sans-serif; }}
  h1 {{ font: 700 36px/36px ui-sans-serif, system-ui, sans-serif; color: {v(light['heading'])}; margin: 0 0 8px; }}
  p {{ color: {v(light['muted'])}; max-width: 36rem; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; margin: 24px 0; }}
  .swatch {{ width: 140px; }}
  .chip {{ height: 72px; border-radius: 8px; border: 1px solid rgba(48,51,54,.12); }}
  .label {{ font: 12px/1.4 ui-sans-serif, system-ui, sans-serif; margin-top: 6px; color: {v(light['footer'])}; }}
  .cta {{ display: inline-block; background: {v(light['button'])}; color: {v(light['on-button'])}; border-radius: 8px; padding: 7px 17px; font: 700 17px/1.2 ui-sans-serif, system-ui, sans-serif; text-decoration: none; }}
  .link {{ color: {v(light['link'])}; font-weight: 600; margin-left: 16px; }}
</style>
</head>
<body>
  <h1>Simply Powerful</h1>
  <p>Public Things marketing tokens, read from culturedcode.com/things on 2026-11-22. One painted light theme.</p>
  <div class="row">
    <div class="swatch"><div class="chip" style="background:{v(light['page'])}"></div><div class="label">page</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['ink'])}"></div><div class="label">ink</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['link'])}"></div><div class="label">link</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['button'])}"></div><div class="label">button</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['focus'])}"></div><div class="label">focus</div></div>
    <div class="swatch"><div class="chip" style="background:{v(light['page-get'])}"></div><div class="label">get slice</div></div>
  </div>
  <a class="cta" href="#subscribe">Subscribe</a>
  <span class="link">See features</span>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote", ROOT / "style-guide.html")
