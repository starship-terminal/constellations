#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light theme only."""
import json, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())

def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")

def css_name(path):
    return "--" + path.replace(".", "-")

def css_value(token):
    val = token["$value"]
    if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
        return "var(" + css_name(val[1:-1]) + ")"
    if token["$type"] == "cubicBezier":
        return "cubic-bezier(" + ", ".join(str(x) for x in val) + ")"
    if isinstance(val, list):
        return ", ".join(str(x) for x in val)
    return str(val)

lines = [":root {"]
for path, token in flat(T["core"]):
    lines.append(f"  {css_name('core.' + path)}: {css_value(token)};")
for path, token in flat(T["light"]):
    lines.append(f"  {css_name('light.' + path)}: {css_value(token)};")
lines.append("}")
vars_css = "\n".join(lines)

swatches = []
for path, token in list(flat(T["core"]["palette"])):
    swatches.append(f'<div class="sw"><i style="background:{css_value(token)}"></i><span>{path}</span><code>{token["$value"]}</code></div>')

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sharewillow style guide</title>
<style>
{vars_css}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--light-background-page); color: var(--light-text-primary); font: 400 16px/1.5 var(--core-font-family-sans); }}
header {{ padding: 28px 32px; border-bottom: 1px solid var(--light-border-default); display: flex; justify-content: space-between; align-items: baseline; }}
h1 {{ font-family: var(--core-font-family-display); font-weight: 500; font-size: 40px; margin: 0; letter-spacing: -0.025em; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px; }}
h2 {{ font-size: 13px; letter-spacing: 0.05em; text-transform: none; color: var(--light-text-muted); font-weight: 500; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
.sw i {{ display: block; height: 64px; border-radius: 12px; border: 1px solid var(--light-border-default); }}
.sw span {{ display: block; margin-top: 6px; font-size: 13px; }}
.sw code {{ font-size: 11px; color: var(--light-text-muted); }}
.row {{ display: flex; gap: 16px; align-items: center; flex-wrap: wrap; margin: 16px 0 32px; }}
.btn {{ display: inline-flex; align-items: center; height: var(--light-component-button-height); padding: 0 22px; border-radius: 999px; background: var(--light-component-button-background); color: var(--light-component-button-text); text-decoration: none; font-weight: 500; }}
.quiet {{ color: var(--light-text-link); text-decoration: none; font-weight: 500; }}
.field {{ height: var(--light-component-field-height); border-radius: var(--light-component-field-radius); border: 1px solid var(--light-border-strong); background: var(--light-component-field-background); padding: 0 14px; width: 280px; color: var(--light-text-primary); }}
.badge {{ background: var(--light-accent-default); color: var(--light-text-onAccent); border-radius: 999px; padding: 2px 8px; font-size: 11px; font-weight: 600; }}
.hero {{ background: var(--light-background-hero); color: var(--light-text-hero); border-radius: 24px; padding: 28px; }}
.note {{ color: var(--light-text-muted); font-size: 14px; }}
</style>
</head>
<body>
<header>
  <h1>Sharewillow</h1>
  <span class="note">Public marketing site, light only</span>
</header>
<main>
  <h2>Palette</h2>
  <div class="grid">{''.join(swatches)}</div>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn" href="#components">Book a demo</a>
    <a class="quiet" href="#components">See the app</a>
    <span class="badge">Coming soon</span>
  </div>
  <div class="row">
    <input class="field" placeholder="Company name" aria-label="Sample field">
  </div>
  <h2>Hero section</h2>
  <div class="hero">
    <p style="font-family:var(--core-font-family-display);font-size:36px;margin:0 0 8px">Show your techs the money.</p>
    <p style="color:var(--light-text-heroMuted);margin:0">Dark section inside the light page. Not a second theme.</p>
  </div>
  <p class="note">Matter and Mackinac are proprietary. This page falls back to the stacks in the tokens. Values come from tokens.json.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
