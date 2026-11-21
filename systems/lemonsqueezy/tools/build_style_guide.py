#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: the public site has no dark theme."""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(token):
    v, ty = token["$value"], token["$type"]
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    return alias(v)


def block(setname):
    return "\n".join(f"  {cssname(n)}: {css_val(t)};" for n, t in flat(T[setname]))


swatches = []
for name, token in flat(T["core"]["palette"]):
    if token["$type"] != "color":
        continue
    swatches.append(
        f'<div class="sw"><i style="background:{html.escape(token["$value"])}"></i>'
        f'<div><div class="nm">{html.escape(name)}</div><div class="vl">{html.escape(token["$value"])}</div></div></div>'
    )

roles = []
for name, token in flat(T["light"]):
    if token["$type"] != "color":
        continue
    roles.append(
        f'<div class="sw"><i style="background:{html.escape(str(token["$value"]))}"></i>'
        f'<div><div class="nm">light.{html.escape(name)}</div><div class="vl">{html.escape(str(token["$value"]))}</div></div></div>'
    )

type_rows = []
for name, token in flat(T["core"]["typography"]):
    type_rows.append(
        f'<div class="typerow"><div class="k">{html.escape(name)}</div>'
        f'<div class="sample" style="font:{css_val(token)}">Sell digital products globally</div></div>'
    )

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lemon Squeezy style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--light-surface); color: var(--light-text); font: 400 16px/24px Inter, ui-sans-serif, system-ui, sans-serif; }}
header {{ background: var(--light-page); color: var(--light-text-on-accent); padding: 28px 32px; }}
header p {{ color: var(--light-muted); max-width: 62ch; }}
.banner {{ background: var(--light-banner); color: var(--light-text); padding: 12px 32px; font-size: 15px; }}
main {{ padding: 32px; max-width: 1100px; }}
h2 {{ font-size: 28px; font-weight: 500; margin: 36px 0 12px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 44px; height: 44px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--light-border); display: block; }}
.nm {{ font: 600 12px/1.3 ui-monospace, monospace; }}
.vl {{ font-size: 12px; color: var(--light-muted-ink); }}
.typerow {{ display: grid; grid-template-columns: 160px 1fr; gap: 16px; padding: 12px 0; border-bottom: 1px solid var(--light-border); align-items: baseline; }}
.k {{ font: 600 12px/1.4 ui-monospace, monospace; }}
.row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
.btn {{ display: inline-flex; align-items: center; height: var(--size-button-height); padding: 8px 20px; border-radius: var(--radius-pill); background: var(--light-surface); color: var(--light-text); font-weight: 500; font-size: 15px; text-decoration: none; }}
.btn-auth {{ display: inline-flex; align-items: center; height: var(--size-auth-button-height); padding: 10px 16px; border-radius: var(--radius-control); background: var(--light-accent-auth); color: white; font-weight: 500; }}
.field {{ height: var(--size-field-height); border: 1px solid var(--light-border); border-radius: var(--radius-control); padding: 8px 16px; width: 280px; }}
.card {{ background: var(--core-palette-pink-100); border-radius: var(--radius-control); padding: 24px; max-width: 420px; }}
</style>
</head>
<body>
<div class="banner">Lemon Squeezy is no longer accepting new sign-ups and will shut down on March 31, 2027</div>
<header>
  <h1>Lemon Squeezy</h1>
  <p>Public marketing and account-entry tokens, read on 2026-11-21. One theme. The signed-in app was not entered.</p>
</header>
<main>
  <h2>Roles</h2>
  <div class="grid">{''.join(roles)}</div>
  <h2>Palette</h2>
  <div class="grid">{''.join(swatches)}</div>
  <h2>Type</h2>
  {''.join(type_rows)}
  <h2>Controls</h2>
  <div class="row"><a class="btn">Start with Managed Payments</a><span class="btn-auth">Sign in</span></div>
  <div class="row"><input class="field" placeholder="Email address" readonly></div>
  <div class="card"><strong>5% + 50¢</strong><p>Pricing comparison column uses the pink-100 fill.</p></div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(doc)
print("wrote style-guide.html", len(doc))
