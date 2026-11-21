#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

ADAPTED_FOR = "lyft"
Light only. The public site has no theme switch, so there is no dark block.
"""
import json
import pathlib
import re

ADAPTED_FOR = "lyft"
HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from flat(value, prefix + key + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def css_val(token):
    value, kind = token["$value"], token["$type"]
    if kind == "typography":
        return None
    if kind == "shadow" and isinstance(value, str):
        return value
    return str(value)


def block(setname):
    lines = []
    for name, token in flat(TOKENS[setname]):
        value = css_val(token)
        if value is None:
            continue
        lines.append(f"  {cssname(name)}: {value};")
    return "\n".join(lines)


swatches = []
for name, token in flat(TOKENS["light"]):
    if token["$type"] != "color":
        continue
    swatches.append(
        f'<div class="sw"><i style="background:{token["$value"]}"></i><b>{name}</b><code>{token["$value"]}</code></div>'
    )
brand = []
for name, token in flat(TOKENS["core"]["color"]["brand"]):
    brand.append(
        f'<div class="sw"><i style="background:{token["$value"]}"></i><b>brand.{name}</b><code>{token["$value"]}</code></div>'
    )

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lyft style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  --sg-sans: "RebelSansText", ui-sans-serif, system-ui, sans-serif;
  --sg-display: "RebelSansDisplay", ui-sans-serif, system-ui, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-primary); color: var(--text-primary); font: 400 16px/22px var(--sg-sans); }}
header {{ padding: 24px 32px; border-bottom: 1px solid var(--stroke-tertiary); display: flex; align-items: center; gap: 16px; }}
header strong {{ font-family: var(--sg-display); font-size: 28px; }}
.wrap {{ max-width: 1080px; margin: 0 auto; padding: 32px; }}
h2 {{ font-family: var(--sg-display); font-weight: 600; font-size: 32px; line-height: 1.1; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.sw {{ border: 1px solid var(--stroke-tertiary); border-radius: 12px; overflow: hidden; background: var(--surface-primary); }}
.sw i {{ display: block; height: 64px; }}
.sw b, .sw code {{ display: block; padding: 4px 10px; font-size: 12px; }}
.btn {{ display: inline-flex; align-items: center; height: var(--button-height); padding: 0 var(--button-x); border-radius: var(--pill); background: var(--surface-interactive); color: var(--text-primary-inverse); text-decoration: none; }}
.card {{ width: 280px; padding: var(--card-y) var(--card-x); border-radius: var(--card); background: var(--surface-primary); box-shadow: var(--level2); }}
.note {{ color: var(--text-secondary); max-width: 62ch; }}
</style>
</head>
<body>
<header><strong>Lyft</strong><span>Public marketing tokens, light only</span></header>
<div class="wrap">
<h2>Controls</h2>
<p class="note">The primary control uses surface.interactive and a 48px pill. Rebel Sans is not shipped here, so the page falls back to the system sans.</p>
<p><a class="btn" href="#roles">Get a ride</a></p>
<div class="card"><b>Wait &amp; Save</b><p class="note">Ride-type cards are 16px radius on a white surface.</p></div>
<h2 id="roles">Colour roles</h2>
<div class="grid">
{''.join(swatches)}
</div>
<h2>Brand</h2>
<div class="grid">
{''.join(brand)}
</div>
</div>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
