#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Clearful paints one light theme. The header toggle is present and disabled in
the copy, because there is no dark set to switch to. Every swatch is a custom
property generated from tokens.json.
"""
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


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v = t["$value"]
    if t["$type"] == "typography":
        return f'{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} {alias(v["fontFamily"])}'
    return alias(v)


props = "\n".join(
    f"  {cssname(n)}: {css_val(t)};" for setname in ("core", "light") for n, t in flat(T[setname])
)

swatches = []
for name, token in flat(T["light"]):
    if token["$type"] != "color":
        continue
    swatches.append(
        f'<div class="sw"><i style="background:{css_val(token)}"></i>'
        f'<div><b>{name}</b><code>{token["$value"]}</code></div></div>'
    )
ramps = []
for name, token in flat(T["core"]):
    if token["$type"] != "color":
        continue
    ramps.append(
        f'<div class="chip" style="background:{css_val(token)}" title="{name}">{name.split("-")[-1]}</div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Clearful style guide</title>
<style>
:root {{
{props}
  --sg-sans: Manrope, ui-sans-serif, system-ui, sans-serif;
  --sg-display: Literatatt, "Iowan Old Style", Palatino, serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px var(--sg-sans); }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 24px; border-bottom: 1px solid var(--border); }}
header h1 {{ margin: 0; font: 700 20px/28px var(--sg-display); }}
header span {{ color: var(--muted); font-size: 14px; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 24px 64px; }}
h2 {{ font: 700 32px/40px var(--sg-display); margin: 40px 0 12px; }}
.grid {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.sw {{ display: flex; gap: 10px; align-items: center; width: 240px; }}
.sw i {{ width: 44px; height: 44px; border-radius: 8px; border: 1px solid var(--border); display: block; }}
.sw b {{ display: block; font-size: 13px; }}
.sw code {{ font-size: 12px; color: var(--muted); }}
.ramps {{ display: flex; flex-wrap: wrap; gap: 4px; }}
.chip {{ width: 72px; height: 48px; border-radius: 6px; font-size: 10px; display: flex; align-items: flex-end; padding: 4px; color: #fff; text-shadow: 0 1px 1px rgba(0,0,0,.4); }}
.btn {{ display: inline-flex; align-items: center; height: var(--component-button-height); padding: 12px 20px; border-radius: var(--component-button-radius); background: var(--accent); color: var(--on-accent); font-weight: 600; text-decoration: none; }}
.btn.ghost {{ background: transparent; color: var(--text); border: 1px solid var(--border); }}
.field {{ display: block; width: 320px; height: var(--component-field-height); border: 1px solid var(--border); border-radius: var(--component-field-radius); padding: 16px 12px; font: inherit; }}
.card {{ background: var(--surface); border-radius: var(--radius-large); padding: 20px; max-width: 420px; }}
</style>
</head>
<body>
<header>
  <h1>Clearful</h1>
  <span>One theme. Light only. Values from tokens.json.</span>
</header>
<main>
  <h2>Colour roles</h2>
  <div class="grid">{''.join(swatches)}</div>
  <h2>Ramps</h2>
  <div class="ramps">{''.join(ramps)}</div>
  <h2>Type</h2>
  <p style="font: var(--typography-display); margin: 0;">Be a more thoughtful you</p>
  <p style="font: var(--typography-body); color: var(--muted);">Manrope carries the UI. Literatatt carries the display line.</p>
  <h2>Controls</h2>
  <p><a class="btn" href="#">Start a journal</a></p>
  <p><a class="btn ghost" href="#">Log In</a></p>
  <p><input class="field" placeholder="Enter your name..." readonly></p>
  <div class="card"><b>Guided journal</b><p style="color: var(--muted); margin: 8px 0 0;">A card sits on the secondary surface, not a new colour.</p></div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
