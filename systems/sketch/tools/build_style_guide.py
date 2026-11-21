#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light theme only."""
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
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path)


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(t):
    v, ty = t["$value"], t["$type"]
    if ty == "typography":
        fam = alias(v["fontFamily"])
        return f'{v["fontWeight"]} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {fam}'
    return alias(v)


lines = []
for prefix, tree in (("core", T["core"]), ("light", T["light"])):
    for name, tok in flat(tree):
        if tok["$type"] == "typography":
            continue
        lines.append(f"  {cssname(prefix + '-' + name)}: {css_val(tok)};")

css = "\n".join(lines)
swatches = []
for role in ("page", "surface", "text", "muted", "accent", "on-accent", "link", "border", "field", "card", "disabled"):
    swatches.append(
        f'<div class="sw"><i style="background:var(--light-{role})"></i><span>{role}</span><code>var(--light-{role})</code></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sketch public style guide</title>
<style>
:root {{
{css}
  --sg-sans: var(--core-font-family-ui);
  --sg-display: var(--core-font-family-display);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--light-page); color: var(--light-text); font: 400 16px/1.4 var(--sg-sans); }}
header, main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px; }}
h1 {{ font-family: var(--sg-display); font-weight: 500; font-size: 48px; line-height: 1; letter-spacing: -1px; margin: 0 0 8px; }}
h2 {{ font-size: 13px; letter-spacing: 0.08em; text-transform: none; margin: 32px 0 12px; }}
p.note {{ color: var(--light-muted); max-width: 62ch; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(140px, 1fr)); gap: 12px; }}
.sw {{ background: var(--light-surface); border-radius: var(--core-radius-promo); padding: 10px; }}
.sw i {{ display: block; height: 48px; border-radius: 12px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.08); }}
.sw span {{ display: block; margin-top: 8px; font-weight: 600; }}
.sw code {{ font-size: 11px; color: var(--light-muted); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.btn {{ display: inline-flex; align-items: center; height: var(--light-component-button-height); padding: 0 24px; border-radius: var(--core-radius-control); background: var(--light-accent); color: var(--light-on-accent); font-weight: 600; text-decoration: none; }}
.field {{ height: var(--light-component-field-height); border: 0; border-radius: var(--core-radius-field); background: var(--light-field); padding: 0 14px; font: inherit; min-width: 240px; }}
.card {{ background: var(--light-card); border-radius: var(--core-radius-card); padding: 24px; max-width: 280px; }}
a.link {{ color: var(--light-link); font-weight: 600; }}
</style>
</head>
<body>
<header>
  <h1>Sketch</h1>
  <p class="note">Public marketing site, light theme, measured 2026-11-21. Reckless is not loaded here, so the display falls back to a serif. Values come from tokens.json.</p>
</header>
<main>
  <h2>Colour roles</h2>
  <div class="swatches">{''.join(swatches)}</div>
  <h2>Controls</h2>
  <div class="row">
    <a class="btn" href="#">Get started</a>
    <input class="field" placeholder="Email" readonly>
    <a class="link" href="#">Create an account</a>
  </div>
  <h2>Plan card</h2>
  <div class="card">
    <strong>Standard</strong>
    <p class="note">Radius and fill from the measured pricing card. Prices are not tokens.</p>
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
