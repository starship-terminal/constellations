#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Relume-specific template."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

def css(token):
    return token["$value"]

html = f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Relume style guide</title>
<style>
  :root {{
    color-scheme: light;
    --page: {css(T['light']['page'])};
    --surface: {css(T['light']['surface'])};
    --text: {css(T['light']['text'])};
    --muted: {css(T['light']['muted'])};
    --accent: {css(T['light']['accent'])};
    --border: {css(T['light']['border'])};
    --on-accent: {css(T['light']['component']['button']['text'])};
    --radius: {css(T['core']['radius']['sm'])};
  }}
  html[data-theme="dark"] {{
    color-scheme: dark;
    --page: {css(T['dark']['page'])};
    --surface: {css(T['dark']['surface'])};
    --text: {css(T['dark']['text'])};
    --muted: {css(T['dark']['muted'])};
    --accent: {css(T['dark']['accent'])};
    --border: {css(T['dark']['border'])};
    --on-accent: {css(T['dark']['component']['button']['text'])};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 14px/1.45 "Geist Variable", Arial, sans-serif; }}
  main {{ max-width: 960px; margin: 0 auto; padding: 32px 20px 80px; }}
  h1 {{ font-weight: 400; font-size: 40px; letter-spacing: -0.03em; margin: 0 0 8px; }}
  h2 {{ font-size: 13px; font-weight: 500; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); margin: 36px 0 10px; }}
  p {{ max-width: 62ch; color: var(--muted); }}
  button.theme {{ background: var(--surface); color: var(--text); border: 1px solid var(--border); border-radius: var(--radius); padding: 6px 12px; }}
  .row {{ display: flex; flex-wrap: wrap; gap: 8px; }}
  .sw {{ width: 140px; }}
  .sw i {{ display: block; height: 48px; border-radius: var(--radius); border: 1px solid var(--border); }}
  .sw b, .sw span {{ display: block; font-size: 12px; }}
  .sw span {{ color: var(--muted); }}
  .cta {{ display: inline-block; background: var(--accent); color: var(--on-accent); border-radius: var(--radius); padding: 6px 12px; font-weight: 500; text-decoration: none; }}
  .card {{ background: var(--surface); border: 1px solid var(--border); border-radius: 12px; padding: 16px; max-width: 280px; }}
  table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
  td, th {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--border); }}
</style>
</head>
<body>
<main>
  <button class="theme" type="button" onclick="document.documentElement.dataset.theme = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark'">Switch theme</button>
  <h1>Relume</h1>
  <p>Public marketing system, measured from relume.ai on 2026-11-21. Geist Variable, warm paper, magenta accent. Values come from tokens.json.</p>
  <h2>Roles</h2>
  <div class="row" id="roles"></div>
  <h2>Button</h2>
  <a class="cta" href="#">Start for free</a>
  <h2>Card</h2>
  <div class="card"><b>Publish</b><p>Take your project live and grow it.</p></div>
  <h2>Radius</h2>
  <table id="radius"></table>
  <h2>Spacing</h2>
  <table id="space"></table>
</main>
<script>
const roles = [
  ["page", getComputedStyle(document.documentElement).getPropertyValue("--page")],
  ["surface", getComputedStyle(document.documentElement).getPropertyValue("--surface")],
  ["text", getComputedStyle(document.documentElement).getPropertyValue("--text")],
  ["muted", getComputedStyle(document.documentElement).getPropertyValue("--muted")],
  ["accent", getComputedStyle(document.documentElement).getPropertyValue("--accent")],
  ["border", getComputedStyle(document.documentElement).getPropertyValue("--border")],
];
document.getElementById("roles").innerHTML = roles.map(([n, v]) =>
  `<div class="sw"><i style="background:${{v.trim()}}"></i><b>${{n}}</b><span>${{v.trim()}}</span></div>`).join("");
const radius = {json.dumps({k: t["$value"] for k, t in T["core"]["radius"].items()})};
const space = {json.dumps({k: t["$value"] for k, t in T["core"]["spacing"].items()})};
document.getElementById("radius").innerHTML = Object.entries(radius).map(([k,v]) => `<tr><td>${{k}}</td><td>${{v}}</td></tr>`).join("");
document.getElementById("space").innerHTML = Object.entries(space).map(([k,v]) => `<tr><td>${{k}}</td><td>${{v}}</td></tr>`).join("");
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
