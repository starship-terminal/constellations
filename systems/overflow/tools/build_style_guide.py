#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Overflow is light-only. The guide paints marketing specimens and the
signed-out app specimens from the tokens, and lists the app colour ramps.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty in ("typography", "other"):
        return None
    if ty == "shadow":
        return v if isinstance(v, str) else None
    if ty == "number":
        return str(v)
    return alias(v)


lines = []
for name, tok in flat(T["core"]):
    val = css_val(tok)
    if val is not None:
        lines.append(f"  {cssname(name)}: {val};")
for name, tok in flat(T["light"]):
    val = css_val(tok)
    if val is not None:
        lines.append(f"  {cssname(name)}: {val};")
css = "\n".join(lines)

# ramp swatches from light.app colour tokens
ramps = {}
for name, tok in flat(T["light"]["app"]):
    if tok["$type"] != "color":
        continue
    ramps[name] = tok["$value"]

swatch_html = []
for name in sorted(ramps):
    swatch_html.append(
        f'<div class="sw"><i style="background:{ramps[name]}"></i><code>{name}</code><span>{ramps[name]}</span></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Overflow style guide</title>
<style>
:root {{
{css}
  --sg: Inter, "Helvetica Neue", Arial, "Noto Sans", sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 16px/28px var(--sg); }}
header {{ padding: 32px 40px 16px; border-bottom: 1px solid var(--border-stroke); }}
header h1 {{ margin: 0; font: 800 40px/48px var(--sg); letter-spacing: -0.5px; }}
header p {{ margin: 8px 0 0; color: var(--text-secondary); max-width: 68ch; }}
main {{ padding: 8px 40px 80px; max-width: 1180px; }}
h2 {{ font: 800 28px/34px var(--sg); letter-spacing: -0.4px; margin: 40px 0 12px; }}
h3 {{ font: 700 16px/24px var(--sg); margin: 24px 0 8px; }}
.row {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: flex-end; }}
.chip {{ width: 88px; }}
.chip i {{ display: block; height: 56px; border-radius: 8px; border: 1px solid rgba(0,0,0,.08); }}
.chip span {{ display: block; font-size: 11px; line-height: 14px; margin-top: 4px; color: var(--text-secondary); }}
.sw {{ display: flex; gap: 8px; align-items: center; width: 280px; font-size: 12px; line-height: 16px; }}
.sw i {{ width: 28px; height: 28px; border-radius: 6px; border: 1px solid rgba(0,0,0,.08); flex: none; }}
.grid {{ display: flex; flex-wrap: wrap; gap: 8px 16px; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; background: var(--component-button-primary-background); color: var(--component-button-primary-text); border-radius: var(--component-button-primary-radius); height: var(--component-button-primary-height); padding: 0 var(--component-button-primary-padding); font: 550 16px/16px var(--sg); letter-spacing: 0.2px; border: 1px solid #000; text-decoration: none; }}
.btn-s {{ display: inline-flex; align-items: center; background: var(--component-button-secondary-background); color: var(--component-button-secondary-text); border-radius: var(--component-button-secondary-radius); padding: 8px 12px; font: 550 15px/24px var(--sg); border: 1px solid var(--component-button-secondary-background); }}
.field {{ background: var(--component-text-field-background); color: var(--component-text-field-text); border-radius: var(--component-text-field-radius); height: var(--component-text-field-height); padding: 0 16px; border: 0; width: 293px; font: 400 14px/14px var(--sg); }}
.card {{ background: var(--component-plan-card-background); border-radius: var(--component-plan-card-radius); box-shadow: var(--shadow-plan-card); padding: 40px; width: 320px; }}
.card h3 {{ color: var(--text-link); font-weight: 700; text-align: center; }}
.panel {{ background: var(--background-auth-panel); color: var(--text-navy); padding: 32px; border-radius: 0; width: 280px; min-height: 180px; }}
.app-btn {{ display: inline-flex; align-items: center; justify-content: center; background: var(--component-app-button-background); color: var(--component-app-button-text); border-radius: var(--component-app-button-radius); height: var(--component-app-button-height); padding: 0 12px; font: 600 12px/24px var(--sg); letter-spacing: 0.1px; box-shadow: var(--shadow-app-button); border: 0; }}
.app-field {{ background: var(--component-app-field-background); color: var(--component-app-field-text); border: 1px solid var(--border-app-input); border-radius: var(--component-app-field-radius); height: var(--component-app-field-height); padding: 7px 11px; width: 280px; font: 400 14px/24px var(--sg); }}
.type-display {{ font: 800 56px/63.84px var(--sg); letter-spacing: -1.2px; margin: 0; }}
.type-section {{ font: 800 48px/55.68px var(--sg); letter-spacing: -0.8px; margin: 0; }}
.note {{ color: var(--text-secondary); font-size: 14px; line-height: 22px; max-width: 72ch; }}
a.link {{ color: var(--text-link); font-weight: 500; }}
</style>
</head>
<body>
<header>
  <h1>Overflow</h1>
  <p>Public marketing site and the signed-out app shell, measured 2026-11-19. Light only. Inter is not loaded here; the stack falls back to Helvetica Neue, Arial, Noto Sans.</p>
</header>
<main>
  <h2>Colour roles</h2>
  <div class="row">
    <div class="chip"><i style="background:var(--background-page)"></i><span>page</span></div>
    <div class="chip"><i style="background:var(--background-sunken)"></i><span>sunken</span></div>
    <div class="chip"><i style="background:var(--background-band)"></i><span>band</span></div>
    <div class="chip"><i style="background:var(--background-action)"></i><span>action</span></div>
    <div class="chip"><i style="background:var(--background-action-secondary)"></i><span>secondary</span></div>
    <div class="chip"><i style="background:var(--text-link)"></i><span>link</span></div>
    <div class="chip"><i style="background:var(--text-navy)"></i><span>navy</span></div>
    <div class="chip"><i style="background:var(--background-auth-panel)"></i><span>auth panel</span></div>
    <div class="chip"><i style="background:var(--background-app-action)"></i><span>app action</span></div>
    <div class="chip"><i style="background:var(--color-theme)"></i><span>theme-color</span></div>
    <div class="chip"><i style="background:var(--focus-outline)"></i><span>focus (Chromium's default ring, not Overflow's)</span></div>
  </div>

  <h2>Type</h2>
  <p class="type-display">User flows done right</p>
  <p class="type-section">Simple pricing</p>
  <p>Body is Inter 16/28. Footer links are 14/24.5 at 60% black. The app shell uses Inter var: h1 32/40 weight 600, tracking -0.6px.</p>

  <h2>Marketing controls</h2>
  <div class="row">
    <a class="btn">Download - free trial</a>
    <button class="btn-s">Required only</button>
    <input class="field" placeholder="Your email" aria-label="Your email">
  </div>
  <p class="note">Primary hover lifts 2px and does not change colour. Secondary hover fills #e8e8ea. Focus-visible on the header primary button is a 1px #005fcc outline, offset 1px, with outline-style auto: that is Chromium's default focus ring, drawn by the browser because Overflow sets no focus colour. Do not copy it as a brand colour.</p>

  <h2>Plan card</h2>
  <div class="card">
    <h3>Pro</h3>
    <p style="text-align:center;font-weight:800;font-size:32px;margin:8px 0">$19.95</p>
    <p class="note" style="text-align:center">per user/month</p>
  </div>

  <h2>Signed-out app</h2>
  <div class="row" style="align-items:stretch">
    <div class="panel"><strong>Communicate your designs like never before.</strong></div>
    <div>
      <input class="app-field" placeholder="alex@example.com" aria-label="Email">
      <div style="height:12px"></div>
      <button class="app-btn">Download for free</button>
      <p class="note">Disabled Sign in is #f0f1f3 with #b7bdc5 text. Google hover deepens the shadow and does not change the fill. The blue download button hover fills #0065c5.</p>
    </div>
  </div>

  <h2>App colour tokens</h2>
  <p class="note">Resolved on body at overflow.io/n/signin. These names are the product's own custom properties.</p>
  <div class="grid">
    {''.join(swatch_html)}
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
