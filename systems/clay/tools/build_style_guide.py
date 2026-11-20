#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Specimens use only measured tokens."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    return str(v)


def block(setname):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


rows = []
for name, token in flat(T["dark"]):
    if token["$type"] != "color":
        continue
    rows.append(f'<div class="sw"><i style="background:{token["$value"]}"></i><div><b>{name}</b><small>{token["$value"]}</small></div></div>')
light_rows = []
for name, token in flat(T["light"]):
    if token["$type"] != "color":
        continue
    light_rows.append(f'<div class="sw"><i style="background:{token["$value"]}"></i><div><b>{name}</b><small>{token["$value"]}</small></div></div>')

html = f"""<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clay public surface style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-bg-page); color: var(--color-text-body, var(--color-text-primary)); font: 400 16px/1.5 var(--font-family-ui); }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font-family: var(--font-family-display); font-weight: 700; letter-spacing: 0.5px; }}
h2 {{ font-family: var(--font-family-display); font-size: 32px; margin: 40px 0 12px; }}
p.note {{ max-width: 72ch; opacity: 0.8; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 10px; }}
.sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(127,127,127,.35); }}
.sw small {{ display: block; opacity: 0.7; }}
.row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
.hero-cta {{ display: inline-flex; align-items: center; justify-content: center; width: var(--component-heroCta-innerWidth); height: var(--component-heroCta-innerHeight); border-radius: var(--component-heroCta-innerRadius); background: var(--component-heroCta-innerBg); color: #000; font-weight: 600; letter-spacing: 1px; box-shadow: 0 0 0 1px #32c5ff, 0 0 4px 1px rgba(255,255,255,.98); }}
.nav-cta {{ display: inline-flex; align-items: center; height: 32px; padding: 0 12px; border-radius: var(--radius-nav-control); color: var(--color-text-accent, #f2b98b); box-shadow: inset 0 0 0 1px rgba(255,255,255,.24); }}
.plan {{ width: var(--component-planCard-width); border-radius: var(--component-planCard-radius); border: 1px solid var(--color-border-card, #eceae8); background: var(--color-bg-card, rgba(149,149,149,.06)); padding: 22px var(--component-planCard-paddingX); color: var(--color-text-primary, #1f1f1f); }}
.plan button {{ width: 100%; height: 44px; border-radius: var(--radius-plan); border: 1px solid var(--color-border-control, rgba(31,31,31,.4)); background: transparent; color: inherit; font-weight: 600; letter-spacing: 1px; }}
.field {{ width: 272px; height: var(--component-field-height); border-radius: var(--component-field-radius); border: 1px solid var(--color-border-field, rgba(72,73,74,.1)); background: var(--color-bg-field, rgba(72,73,74,.04)); padding: 0 12px; color: var(--color-text-muted, #48494a); }}
.toggle {{ margin-left: auto; }}
</style>
</head>
<body>
<div class="wrap">
<header style="display:flex;align-items:center;gap:16px">
  <h1>Clay public surface</h1>
  <button class="toggle" type="button" onclick="document.documentElement.dataset.mode = document.documentElement.dataset.mode === 'dark' ? 'light' : 'dark'">Toggle theme</button>
</header>
<p class="note">Values are the computed styles read on 2026-11-19 from me.sh, the 301 target of clay.earth, and from the signed-out app.me.sh sign-in card. Verlag and Chronicle are named but not loaded here.</p>
<h2>Dark roles</h2>
<div class="swatches">{''.join(rows)}</div>
<h2>Light roles</h2>
<div class="swatches">{''.join(light_rows)}</div>
<h2>Type</h2>
<p style="font-family:var(--font-family-display);font-size:var(--font-size-display);font-weight:700;line-height:64px;letter-spacing:0.88px;margin:0">Every relationship, remembered.</p>
<p style="font-size:var(--font-size-body);line-height:27px">Body copy at the measured 18px / 27px Verlag stack.</p>
<h2>Controls</h2>
<div class="row">
  <span class="hero-cta">GET MESH FREE</span>
  <span class="nav-cta">GET STARTED</span>
</div>
<div class="plan">
  <div style="font-size:12px;letter-spacing:1px;font-weight:700">PERSONAL</div>
  <div style="font-family:var(--font-family-display);font-size:32px;margin:8px 0">Free</div>
  <button type="button">GET STARTED</button>
</div>
<p class="note">The plan card uses the light tokens. Switch the theme toggle to see them on the cream page ground.</p>
<h2>Sign-in field</h2>
<input class="field" placeholder="Enter your email" readonly>
<p class="note">Measured on the signed-out card. Nothing was typed into the live field.</p>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
