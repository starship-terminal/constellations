#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

The page defaults to the dark token set from the 2026-11-19 readings. The light set is the 2026-11-21 Explore page.
Colours, radii, and type come from tokens.json. Proprietary TikTok fonts are not loaded.
"""
from __future__ import annotations

import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def resolve(value, seen=None):
    if not isinstance(value, str) or not value.startswith("{") or not value.endswith("}"):
        return value
    seen = seen or set()
    path = value[1:-1]
    if path in seen:
        raise SystemExit(f"alias loop: {path}")
    node = T["core"]
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"], seen | {path})


def color(path):
    node = T
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"])


C = {
    "page": color("core.color.page"),
    "text": color("core.color.text"),
    "strong": color("core.color.text-strong"),
    "nav": color("core.color.text-nav"),
    "muted": color("core.color.text-muted"),
    "action": color("core.color.razzmatazz"),
    "primary": color("core.color.primary"),
    "splash": color("core.color.splash"),
    "cyan": color("core.color.cyan"),
    "positive": color("core.color.positive"),
    "negative": color("core.color.negative"),
    "sheet": color("core.color.sheet"),
    "channel": color("core.color.channel"),
    "mask": color("core.color.mask"),
    "ink": color("core.color.ink"),
    "yellow": color("core.color.yellow"),
}

html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>TikTok style guide</title>
<style>
  :root {{
    color-scheme: dark;
    --page: {C['page']};
    --text: {C['text']};
    --strong: {C['strong']};
    --nav: {C['nav']};
    --muted: {C['muted']};
    --action: {C['action']};
    --primary: {C['primary']};
    --splash: {C['splash']};
    --sheet: {C['sheet']};
    --channel: {C['channel']};
    --negative: {C['negative']};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 400 14px/21px Arial, Tahoma, PingFangSC, sans-serif; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 32px 24px 64px; }}
  h1 {{ font-size: 33px; line-height: 49.5px; font-weight: 700; margin: 0 0 8px; color: var(--strong); }}
  h2 {{ font-size: 16px; font-weight: 500; letter-spacing: 0.15px; margin: 32px 0 12px; }}
  p {{ max-width: 68ch; }}
  .row {{ display: flex; gap: 12px; flex-wrap: wrap; }}
  .swatch {{ width: 96px; }}
  .swatch i {{ display: block; height: 48px; border-radius: 6px; box-shadow: inset 0 0 0 1px rgba(255,255,255,0.12); }}
  .swatch span {{ display: block; margin-top: 6px; font-size: 12px; color: var(--muted); }}
  button.login {{ background: var(--action); color: #fff; border: 0; border-radius: 6px; height: 40px; padding: 1px 16px; font: 500 16px/21px Arial, sans-serif; letter-spacing: 0.15px; }}
  button.nav {{ background: transparent; color: var(--nav); border: 0; border-radius: 6px; height: 40px; padding: 0 16px; font: 500 16px/21px Arial, sans-serif; }}
  button.nav.on {{ color: var(--primary); }}
  .search {{ display: inline-flex; align-items: center; height: 40px; padding: 6px 16px; border-radius: 999px; background: var(--channel); color: var(--nav); }}
  .sheet {{ background: var(--sheet); border-radius: 24px; padding: 24px; max-width: 428px; }}
  .channel {{ display: flex; align-items: center; height: 48px; border-radius: 24px; background: var(--channel); padding: 0 14px 0 10px; margin-top: 8px; font-weight: 600; }}
  .focus {{ outline: 2px solid var(--negative); }}
  a.signup {{ color: var(--primary); font-size: 11px; font-weight: 600; text-decoration: none; }}
  code {{ font-family: ui-monospace, Menlo, Consolas, monospace; font-size: 12px; }}
</style>
</head>
<body>
<main>
  <h1>TikTok</h1>
  <p>Signed-out chrome. This page renders the dark token set from the 2026-11-19 readings. The light set in tokens.json is the 2026-11-21 Explore page. TikTokFont and TikTokDisplayFont are not loaded here.</p>
  <h2>Colour</h2>
  <div class="row">
    <div class="swatch"><i style="background:{C['page']}"></i><span>page {C['page']}</span></div>
    <div class="swatch"><i style="background:{C['sheet']}"></i><span>sheet {C['sheet']}</span></div>
    <div class="swatch"><i style="background:{C['action']}"></i><span>action {C['action']}</span></div>
    <div class="swatch"><i style="background:{C['primary']}"></i><span>primary {C['primary']}</span></div>
    <div class="swatch"><i style="background:{C['splash']}"></i><span>splash {C['splash']}</span></div>
    <div class="swatch"><i style="background:{C['channel']}"></i><span>channel {C['channel']}</span></div>
    <div class="swatch"><i style="background:{C['negative']}"></i><span>focus {C['negative']}</span></div>
    <div class="swatch"><i style="background:{C['cyan']}"></i><span>cyan {C['cyan']}</span></div>
    <div class="swatch"><i style="background:{C['positive']}"></i><span>positive {C['positive']}</span></div>
  </div>
  <h2>Controls</h2>
  <div class="row">
    <button class="login">Log in</button>
    <button class="nav on">For You</button>
    <button class="nav">Explore</button>
    <span class="search">Search</span>
  </div>
  <h2>Login sheet</h2>
  <div class="sheet">
    <div style="font-size:33px;line-height:49.5px;font-weight:700;color:#fff">Log in to TikTok</div>
    <div class="channel">Use QR code</div>
    <div class="channel">Use phone or email</div>
    <p style="font-size:15px">Don't have an account? <a class="signup" href="#signup">Sign up</a></p>
    <button class="login focus">Focus ring</button>
  </div>
  <p>The focus ring is the declared <code>button:focus-visible</code> outline, {C['negative']} at 2px. It was not painted during capture.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html", len(html))
