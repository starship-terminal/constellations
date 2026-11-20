#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Dark-only: the dark set sits on :root."""
import html as _html
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


def esc(value):
    """Escapes a value for text and a double-quoted attribute: a font stack with quotes cannot close style=\"\"."""
    return _html.escape(str(value), quote=True)


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def css_val(t):
    return str(t["$value"])


props = []
for setname in ("core", "dark"):
    for name, tok in flat(T.get(setname, {})):
        props.append(f"  {cssname(name)}: {css_val(tok)};")

swatches = []
for name, tok in flat(T.get("dark", {})):
    if tok["$type"] != "color":
        continue
    swatches.append(
        f'<div class="swatch"><i style="background:{esc(tok["$value"])}"></i><span>{esc(name)}</span><code>{esc(tok["$value"])}</code></div>'
    )

ramps = []
for hue, steps in sorted((T.get("core", {}).get("color") or {}).items()):
    if not isinstance(steps, dict):
        continue
    chips = []
    for step, tok in steps.items():
        if not isinstance(tok, dict) or "$value" not in tok or tok.get("$type") != "color":
            continue
        chips.append(f'<i title="{esc(hue)} {esc(step)}" style="background:{esc(tok["$value"])}"></i>')
    if chips:
        ramps.append(f'<div class="ramp"><b>{esc(hue)}</b>{"".join(chips)}</div>')

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>MasterClass style guide</title>
<style>
:root {{
{chr(10).join(props)}
}}
body {{ margin: 0; background: var(--page-default, #0d0d0e); color: var(--text-primary, #fff); font: 16px/1.5 Sohne, Helvetica, Arial, sans-serif; }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 20px 80px; }}
h1 {{ font-weight: 600; letter-spacing: 0.02em; }}
.swatches, .ramps {{ display: grid; gap: 8px; }}
.swatch {{ display: grid; grid-template-columns: 48px 1fr auto; gap: 12px; align-items: center; background: #191c21; border-radius: 8px; padding: 8px 12px; }}
.swatch i {{ width: 48px; height: 32px; border-radius: 4px; border: 1px solid #303136; }}
.ramp {{ display: flex; gap: 4px; align-items: center; }}
.ramp b {{ width: 88px; font-weight: 600; font-size: 13px; color: #d4d5d9; }}
.ramp i {{ width: 28px; height: 28px; border-radius: 4px; }}
.specimen {{ margin-top: 28px; }}
.btn {{ display: inline-block; background: var(--accent-default, #e32652); color: #fff; border-radius: 8px; padding: 12px 16px; font-weight: 600; }}
.field {{ display: block; margin-top: 12px; background: #191c21; color: #fff; border: 1px solid #272c33; border-radius: 8px; padding: 12px; width: 280px; }}
</style>
</head>
<body>
<main>
<h1>MasterClass</h1>
<p>Signed-out public surface. One dark theme. Values are the custom properties read on :root.</p>
<h2>Roles</h2>
<div class="swatches">{''.join(swatches)}</div>
<h2>Ramps</h2>
<div class="ramps">{''.join(ramps)}</div>
<div class="specimen">
  <a class="btn" href="#roles">Get MasterClass</a>
  <input class="field" placeholder="Email" readonly>
</div>
</main>
</body>
</html>
"""
if __name__ == "__main__":
    (HERE / "style-guide.html").write_text(html)
    print("style-guide.html", len(html))
