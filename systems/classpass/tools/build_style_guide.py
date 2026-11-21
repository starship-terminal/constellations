#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light only. No external fonts."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    out = []
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            out.append((prefix + k, v))
        elif isinstance(v, dict):
            out.extend(flat(v, prefix + k + "."))
    return out


def css_name(path):
    return "--" + path.replace(".", "-")


def css_val(token):
    v = token["$value"]
    if isinstance(v, dict):
        return f'{v.get("fontWeight", "400")} {v.get("fontSize", "16px")}/{v.get("lineHeight", "24px")} norms, sans-serif'
    return str(v)


lines = []
for set_name in ("core", "light"):
    for path, token in flat(T[set_name]):
        lines.append(f"  {css_name(path)}: {css_val(token)};")

swatches = []
for path, token in flat(T["light"]):
    if token["$type"] != "color":
        continue
    swatches.append(
        f'<div class="sw"><i style="background:{token["$value"]}"></i><div><code>{path}</code><span>{token["$value"]}</span></div></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ClassPass style guide</title>
<style>
:root {{
{chr(10).join(lines)}
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 16px/24px norms, ui-sans-serif, system-ui, sans-serif; }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: 400 48px/56px norms, sans-serif; margin: 0 0 8px; }}
h2 {{ font: 500 20px/28px norms, sans-serif; margin: 40px 0 12px; }}
p {{ color: #333; max-width: 68ch; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 48px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 48px; height: 48px; border-radius: 8px; box-shadow: inset 0 0 0 1px #e7e7e7; display: block; }}
.sw code {{ display: block; font-size: 12px; }}
.sw span {{ font-size: 12px; color: #555; }}
.row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; margin: 12px 0; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; height: var(--component-button-primary-height); padding: 0 20px; border-radius: var(--component-button-primary-radius); background: var(--component-button-primary-background); color: var(--component-button-primary-text); border: 0; font: 500 16px/24px norms, sans-serif; }}
.sso {{ display: inline-flex; align-items: center; justify-content: center; height: 48px; padding: 0 20px; border-radius: var(--component-button-sso-radius); background: var(--component-button-sso-background); color: var(--component-button-sso-text); border: 1px solid #d6d6d6; font: 500 16px/24px norms, sans-serif; }}
.field {{ height: var(--component-field-height); border-radius: var(--component-field-radius); border: var(--component-field-border-width) solid var(--border-default); padding: 0 12px; font: 400 18px/24px norms, sans-serif; width: 280px; }}
.field:focus {{ outline: none; border-color: var(--border-focus); }}
.chip {{ height: 32px; padding: 0 12px; border-radius: var(--radius-chip); border: 1px solid #d6d6d6; background: #fff; color: var(--component-chip-text); font: 500 14px/20px norms, sans-serif; }}
.header {{ height: var(--size-header); display: flex; align-items: center; gap: 16px; background: var(--component-header-background); box-shadow: var(--component-header-shadow); padding: 0 16px; margin: 16px -24px; }}
.nav {{ font: 500 14px/20px norms, sans-serif; }}
.display {{ font: var(--typography-display); }}
note {{ display: block; font-size: 13px; color: #555; }}
</style>
</head>
<body>
<main>
<h1>ClassPass</h1>
<p>Public site tokens, light only. TT Norms is not loaded here, so the page falls back to the system sans. Values come from tokens.json.</p>
<h2>Colour</h2>
<div class="swatches">
{''.join(swatches)}
</div>
<h2>Type</h2>
<p class="display">Choose how much to spend</p>
<p class="nav">Search, Plans, How it works</p>
<h2>Controls</h2>
<div class="header"><strong>classpass</strong><span class="nav">Search</span><span class="nav">Plans</span><span class="btn" style="height:36px;margin-left:auto">Get 14 days free</span></div>
<div class="row">
  <button class="btn">Log in</button>
  <button class="sso">Sign in with Apple</button>
  <button class="chip">Fitness</button>
</div>
<div class="row">
  <input class="field" placeholder="Email address" aria-label="Email address">
</div>
<p>Header shadow, pill radius and the blue accent are the measured values. Hover, pressed, disabled and dark are not in this guide because they were not captured.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
