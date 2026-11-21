#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. One theme. Edit tokens, not the HTML."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
tokens = json.loads((HERE / "tokens.json").read_text())
core = tokens["core"]


def val(group, *path):
    node = core[group]
    for part in path:
        node = node[part]
    return node["$value"]


page = val("color", "page")
surface = val("color", "surface")
text = val("color", "text")
muted = val("color", "text-tertiary")
accent = val("color", "accent")
border = val("color", "border")
link = val("color", "link")
up = val("color", "up")
down = val("color", "down")
up_wash = val("color", "up-wash")
down_wash = val("color", "down-wash")
field = val("color", "field")
disabled = val("color", "disabled")
font = val("font", "family", "ui").split(",")[0].strip('"')

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Stocktwits style guide</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&display=swap">
<style>
  body {{ margin: 0; background: {page}; color: {text}; font: 400 16px/24px "Source Sans 3", sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-size: 28px; margin: 0 0 8px; }}
  h2 {{ font-size: 20px; margin: 32px 0 12px; }}
  p {{ color: {muted}; max-width: 68ch; }}
  .row {{ display: flex; gap: 16px; flex-wrap: wrap; }}
  .sw {{ width: 140px; }}
  .sw i {{ display: block; height: 56px; border-radius: 8px; border: 1px solid {border}; }}
  .sw span {{ display: block; font-size: 12px; margin-top: 6px; }}
  button, .btn {{ font: 600 15px/1 "Source Sans 3", sans-serif; border-radius: 9999px; height: 40px; padding: 0 20px; border: 1px solid transparent; }}
  .primary {{ background: {accent}; color: #fff; }}
  .secondary {{ background: #fff; color: {text}; border-color: {border}; }}
  .disabled {{ background: {disabled}; color: #fff; }}
  .bull {{ background: {up_wash}; color: {text}; }}
  .bear {{ background: {down_wash}; color: {text}; }}
  input {{ font: 400 16px/24px "Source Sans 3", sans-serif; background: {field}; border: 0; border-radius: 8px; height: 40px; padding: 8px 12px; width: 280px; }}
  a {{ color: {link}; }}
  .up {{ color: {up}; }}
  .down {{ color: {down}; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 14px; }}
  td, th {{ text-align: left; padding: 8px; border-bottom: 1px solid {border}; }}
</style>
</head>
<body>
<main>
  <h1>Stocktwits</h1>
  <p>Rendered from tokens.json. Light only. Source Sans 3 is the measured UI face. Values that were not read are absent.</p>
  <h2>Colour</h2>
  <div class="row">
    <div class="sw"><i style="background:{page}"></i><span>page {page}</span></div>
    <div class="sw"><i style="background:{surface}"></i><span>surface {surface}</span></div>
    <div class="sw"><i style="background:{text}"></i><span>text {text}</span></div>
    <div class="sw"><i style="background:{muted}"></i><span>muted {muted}</span></div>
    <div class="sw"><i style="background:{accent}"></i><span>accent {accent}</span></div>
    <div class="sw"><i style="background:{border}"></i><span>border {border}</span></div>
    <div class="sw"><i style="background:{link}"></i><span>link {link}</span></div>
    <div class="sw"><i style="background:{up}"></i><span>up {up}</span></div>
    <div class="sw"><i style="background:{down}"></i><span>down {down}</span></div>
  </div>
  <h2>Controls</h2>
  <div class="row">
    <button class="primary">Sign Up</button>
    <button class="secondary">Log In</button>
    <button class="disabled" disabled>Log In</button>
    <button class="bull">Bullish</button>
    <button class="bear">Bearish</button>
  </div>
  <h2>Field</h2>
  <input placeholder="Email or Username" readonly>
  <h2>Type</h2>
  <p style="color:{text}; font-size:20px; font-weight:700; line-height:28px">Log In</p>
  <p style="color:{text}">Body at 16px. <a href="#">Inline link</a>. <span class="up">+1.41%</span> <span class="down">-6.41%</span></p>
  <h2>Tokens</h2>
  <table>
    <tr><th>Token</th><th>Value</th></tr>
    <tr><td>core.font.family.ui</td><td>{font}</td></tr>
    <tr><td>core.radius.pill</td><td>9999px</td></tr>
    <tr><td>core.radius.field</td><td>8px</td></tr>
    <tr><td>core.size.button-md</td><td>40px</td></tr>
  </table>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
