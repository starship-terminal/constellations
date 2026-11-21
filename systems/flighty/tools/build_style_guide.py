#!/usr/bin/env python3
"""Render style-guide.html from tokens.json for the Flighty package."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def val(group, key):
    return T[group][key]["$value"]


def css():
    lines = [":root {"]
    for key, token in T["light"].items():
        lines.append(f"  --light-{key}: {token['$value']};")
    for key, token in T["dark"].items():
        lines.append(f"  --dark-{key}: {token['$value']};")
    lines.append("}")
    return "\n".join(lines)


display = T["core"]["typography"]["display"]["$value"]
nav = T["core"]["typography"]["nav"]["$value"]
body = T["core"]["typography"]["body"]["$value"]
button = T["core"]["typography"]["button"]["$value"]
stack = ", ".join(T["core"]["font"]["family"]["ui"]["$value"])

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Flighty style guide</title>
<style>
{css()}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: {stack}; background: var(--light-page); color: var(--light-text); }}
header.banner {{ background: var(--light-banner); color: #fff; height: 39px; display: flex; align-items: center; justify-content: center; font-size: {nav['fontSize']}; font-weight: {nav['fontWeight']}; }}
main {{ max-width: 880px; margin: 0 auto; padding: 32px 24px 64px; }}
h1 {{ font-size: {display['fontSize']}; font-weight: {display['fontWeight']}; line-height: {display['lineHeight']}; letter-spacing: {display['letterSpacing']}; margin: 24px 0 8px; }}
.lede {{ color: var(--light-muted); font-size: {body['fontSize']}; font-weight: {body['fontWeight']}; line-height: {body['lineHeight']}; max-width: 40em; }}
.row {{ display: flex; gap: 12px; align-items: center; margin: 20px 0; flex-wrap: wrap; }}
.pill {{ border-radius: 999px; height: 32px; padding: 0 12px; display: inline-flex; align-items: center; background: #fff; color: #000; border: 1px solid rgba(0,0,0,0.12); font-size: {nav['fontSize']}; font-weight: {nav['fontWeight']}; }}
.btn {{ border-radius: 40px; height: 44px; padding: 12px 20px; display: inline-flex; align-items: center; font-size: {button['fontSize']}; font-weight: {button['fontWeight']}; text-decoration: none; }}
.btn.white {{ background: #fff; color: #000; border: 1px solid rgba(0,0,0,0.12); }}
.btn.black {{ background: #000; color: #fff; border: 0; }}
.btn.pro {{ background: var(--light-accent); color: #fff; border: 0; border-radius: 50px; height: 40px; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; margin-top: 24px; }}
.swatch {{ border-radius: 12px; overflow: hidden; border: 1px solid rgba(0,0,0,0.08); }}
.swatch i {{ display: block; height: 64px; }}
.swatch span {{ display: block; padding: 8px 10px; font-size: 12px; }}
.dark-panel {{ margin-top: 32px; background: var(--dark-page); color: var(--dark-text); border-radius: 16px; padding: 24px; }}
.dark-panel h2 {{ margin: 0 0 8px; font-size: 32px; }}
</style>
</head>
<body>
<header class="banner">NEW! Flighty Airports</header>
<main>
  <p class="lede">Public Flighty, measured 2026-11-21. Values come from tokens.json.</p>
  <h1>Get the truth when you travel</h1>
  <p class="lede">The only app that tells you everything about your flight.</p>
  <div class="row">
    <span class="pill">Get the app</span>
    <a class="btn white">Give Flighty a try</a>
    <a class="btn black">Give Flighty a try</a>
    <a class="btn pro">Try it for free</a>
  </div>
  <div class="swatches">
    <div class="swatch"><i style="background:var(--light-page)"></i><span>page {val('light','page')}</span></div>
    <div class="swatch"><i style="background:var(--light-text)"></i><span>text {val('light','text')}</span></div>
    <div class="swatch"><i style="background:var(--light-muted)"></i><span>muted</span></div>
    <div class="swatch"><i style="background:var(--light-banner)"></i><span>banner {val('light','banner')}</span></div>
    <div class="swatch"><i style="background:var(--light-accent)"></i><span>accent {val('light','accent')}</span></div>
    <div class="swatch"><i style="background:var(--light-ink)"></i><span>ink</span></div>
  </div>
  <section class="dark-panel">
    <h2>Level up with Flighty Pro.</h2>
    <p>Pricing page paint, not a theme toggle. Page {val('dark','page')}.</p>
    <a class="btn pro">Try it for free</a>
  </section>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
