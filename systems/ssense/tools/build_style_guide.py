#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: no dark set was measured."""
import html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
T = json.loads((ROOT / "tokens.json").read_text())


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
    if ty == "typography":
        return f'{v["fontWeight"]} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    if ty == "other":
        return None
    return alias(v)


vars_css = []
for setname in ("core", "light"):
    for name, token in flat(T[setname]):
        val = css_val(token)
        if val is None:
            continue
        vars_css.append(f"  {cssname(name)}: {val};")

swatches = []
for name, token in flat(T["light"]):
    if token["$type"] != "color":
        continue
    swatches.append(
        f'<div class="swatch"><i style="background:{token["$value"]}"></i>'
        f'<span>{name}</span><code>{token["$value"]}</code></div>'
    )

FALLBACK = "Helvetica, Arial, sans-serif"  # the body's fallback, which the note promises
type_rows = []
for name, token in flat(T["core"]):
    if token["$type"] != "typography":
        continue
    v = token["$value"]
    type_rows.append(
        # The family is an alias ({font.family.favorit}): resolve it to its custom property.
        # The proprietary faces are not loaded here, so the guide's own fallback follows the token's family.
        f'<p class="type" style="font: {alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}, {FALLBACK};'
        f'letter-spacing:{alias(v["letterSpacing"])}">{name} · SSENSE</p>'
    )

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<title>SSENSE style guide</title>
<style>
:root {{
{chr(10).join(vars_css)}
}}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 11px/15px "Favorit SSENSE Inter", Helvetica, Arial, sans-serif; }}
main {{ max-width: 960px; margin: 0 auto; padding: 55px 20px 40px; }}
h1 {{ font-size: 15px; font-weight: 400; line-height: 20px; letter-spacing: 0.09px; text-transform: uppercase; }}
h2 {{ font-size: 13px; font-weight: 700; line-height: 20px; margin-top: 32px; }}
p.note {{ color: rgb(136, 136, 136); max-width: 62em; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.swatch {{ width: 140px; }}
.swatch i {{ display: block; height: 48px; border: 1px solid rgb(182, 182, 182); }}
.swatch span, .swatch code {{ display: block; font-size: 11px; line-height: 15px; }}
.type {{ margin: 10px 0; color: rgb(51, 51, 51); }}
.row {{ display: flex; gap: 10px; align-items: center; margin: 12px 0; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; min-height: 35px; padding: 0 18px; background: var(--background-action); color: var(--text-on-action); border: 1px solid rgb(0, 0, 0); text-transform: uppercase; }}
.cta {{ display: inline-flex; align-items: center; height: 36px; padding: 0 18px; border: 1px solid var(--border-editorial); border-radius: var(--radius-cta); color: var(--text-secondary); text-transform: uppercase; }}
.field {{ display: block; width: 380px; max-width: 100%; height: 30px; box-sizing: border-box; border: 1px solid var(--border-strong); padding: 0 6px; background: transparent; color: var(--text-primary); font: inherit; }}
.was {{ color: var(--text-muted); text-decoration: line-through; margin-left: 5px; }}
</style>
</head>
<body>
<main>
  <h1>SSENSE</h1>
  <p class="note">Measured signed out on ssense.com/en-sg, 2026-11-19, viewport 1169 by 731. Light only. Proprietary fonts fall back to Helvetica in this file.</p>
  <h2>Colour</h2>
  <div class="swatches">
    {''.join(swatches)}
  </div>
  <h2>Type</h2>
  {''.join(type_rows)}
  <h2>Controls</h2>
  <div class="row"><button class="btn" type="button">Add to bag</button><button class="cta" type="button">Shop menswear</button></div>
  <label>Email address</label>
  <input class="field" type="email" aria-label="Email address">
  <p>$645 <span class="was">$885</span></p>
</main>
</body>
</html>
"""
(ROOT / "style-guide.html").write_text(html)
print("wrote style-guide.html")
