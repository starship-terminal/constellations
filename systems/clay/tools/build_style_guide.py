#!/usr/bin/env python3
"""Render systems/clay/style-guide.html from tokens.json.

ADAPTED_FOR = "Clay"
Hand-written guide. Does not touch catalog.json or DESIGN.md.
"""
ADAPTED_FOR = "Clay"

import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
tokens = json.loads((ROOT / "tokens.json").read_text())

def hex_of(node):
    value = node["$value"]
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        parts = value.strip("{}").split(".")
        cur = tokens
        for part in parts:
            cur = cur[part]
        return hex_of(cur)
    return value

swatches = []
for family, steps in tokens["core"]["color"].items():
    if "$value" in steps:
        swatches.append((family, hex_of(steps)))
        continue
    for step, node in steps.items():
        swatches.append((f"{family}-{step}", hex_of(node)))

chips = "\n".join(
    f'<div class="chip"><i style="background:{value}"></i><span>{name}</span><code>{value}</code></div>'
    for name, value in swatches
)
paper = hex_of(tokens["light"]["color"]["bg"]["page"])
ink = hex_of(tokens["light"]["color"]["text"]["primary"])
fill = hex_of(tokens["light"]["color"]["action"]["fill"])
demo = hex_of(tokens["light"]["color"]["action"]["demo"])
accent = hex_of(tokens["light"]["color"]["action"]["accent"])
hero = hex_of(tokens["light"]["color"]["bg"]["hero"])
on_hero = hex_of(tokens["light"]["color"]["text"]["onHero"])
auth = hex_of(tokens["light"]["color"]["action"]["auth"])

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Clay public tokens</title>
<style>
  :root {{ color-scheme: light; }}
  body {{ margin: 0; background: {paper}; color: {ink}; font: 16px/1.4 Arial, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-size: 48px; line-height: 1; letter-spacing: -0.04em; font-weight: 575; margin: 0 0 12px; }}
  p {{ max-width: 62ch; }}
  .hero {{ background: {hero}; color: {on_hero}; border-radius: 24px; padding: 32px; margin: 24px 0; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; margin-top: 20px; }}
  .btn {{ display: inline-flex; align-items: center; height: 39px; padding: 0 16px; border-radius: 12px; text-decoration: none; font-weight: 500; }}
  .fill {{ background: {fill}; color: #fff; }}
  .demo {{ background: {demo}; color: {ink}; height: 47px; }}
  .auth {{ background: {auth}; color: #fff; }}
  .ghost {{ background: #fff; color: {ink}; border: 1px solid #e6e8ec; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; margin-top: 24px; }}
  .chip {{ background: #fff; border-radius: 12px; padding: 10px; }}
  .chip i {{ display: block; height: 48px; border-radius: 8px; border: 1px solid #e6e8ec; }}
  .chip span, .chip code {{ display: block; margin-top: 6px; font-size: 13px; }}
  .card {{ background: #fff; border-radius: 16px; padding: 16px; }}
  .card .head {{ background: {accent}; color: #fff; border-radius: 12px; padding: 16px; margin: -4px -4px 12px; }}
</style>
</head>
<body>
<main>
  <h1>Clay public tokens</h1>
  <p>Measured from the public marketing site at clay.com on 2026-11-22. One light theme. Login and signup stay empty walls.</p>
  <section class="hero">
    <h2 style="margin:0 0 8px;font-size:32px;letter-spacing:-0.03em">Build systems to grow revenue</h2>
    <div class="row">
      <a class="btn fill" href="#buttons">Start free trial</a>
      <a class="btn demo" href="#buttons">Get a demo</a>
    </div>
  </section>
  <h2>Swatches</h2>
  <div class="grid">{chips}</div>
  <h2 id="buttons">Buttons</h2>
  <div class="row">
    <a class="btn fill">Start free trial</a>
    <a class="btn ghost">Get a demo</a>
    <a class="btn demo">Get a demo</a>
    <a class="btn auth">Continue</a>
  </div>
  <h2>Pricing card</h2>
  <div class="card" style="max-width:280px">
    <div class="head"><strong>Free</strong><div>Start building in Clay for free.</div></div>
    <div>Includes 6,000 actions/year</div>
  </div>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
