#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light theme only."""
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


def css_val(tok):
    v = tok["$value"]
    ty = tok.get("$type")
    if isinstance(v, str) and v.startswith("{"):
        return alias(v)
    if ty == "color":
        return v
    if ty == "dimension":
        return v
    if ty == "fontFamily":
        return v
    if ty == "number":
        return str(v)
    if ty == "duration":
        return v
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "typography":
        return None
    return str(v)


lines = []
for name, tok in list(flat(T["core"])) + list(flat(T["light"], "light-")):
    val = css_val(tok)
    if val:
        lines.append(f"  {cssname(name)}: {val};")

swatches = []
for role in ["page", "surface", "raised", "text", "muted", "link", "border", "accent", "accentHover", "success", "danger"]:
    swatches.append(
        f'<div class="swatch"><i style="background:var({cssname("light-" + role)})"></i><span>{role}</span><code>var({cssname("light-" + role)})</code></div>'
    )

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Programa style guide</title>
<meta name="description" content="Programa public site tokens, rendered from tokens.json. One light theme.">
<style>
:root {{
{chr(10).join(lines)}
  --sg-sans: var(--fontFamily-sans), Inter, system-ui, sans-serif;
  --sg-display: var(--fontFamily-display), Georgia, serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--light-page); color: var(--light-text); font: 400 16px/24px var(--sg-sans); }}
header {{ padding: 28px 32px 8px; border-bottom: 1px solid var(--light-border); }}
h1 {{ font: 300 44px/50px var(--sg-display); margin: 0 0 8px; }}
h2 {{ font: 300 28px/34px var(--sg-display); margin: 40px 0 12px; }}
p.lede {{ color: var(--light-muted); max-width: 640px; }}
main {{ max-width: 1080px; margin: 0 auto; padding: 8px 32px 64px; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.swatch {{ border: 1px solid var(--light-border); border-radius: 12px; overflow: hidden; background: var(--light-surface); }}
.swatch i {{ display: block; height: 64px; }}
.swatch span, .swatch code {{ display: block; padding: 6px 10px; font-size: 12px; }}
.swatch code {{ color: var(--light-muted); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }}
.btn-primary {{ display: inline-flex; align-items: center; height: var(--light-component-buttonPrimary-height); padding: 0 8px; border-radius: var(--light-component-buttonPrimary-radius); background: var(--light-component-buttonPrimary-background); color: var(--light-component-buttonPrimary-text); font-size: 14px; font-weight: 500; text-decoration: none; }}
.btn-dark {{ display: inline-flex; align-items: center; height: var(--light-component-buttonDark-height); padding: 0 12px; border-radius: var(--light-component-buttonDark-radius); background: var(--light-component-buttonDark-background); color: var(--light-component-buttonDark-text); text-decoration: none; }}
.btn-secondary {{ display: inline-flex; align-items: center; height: var(--light-component-buttonSecondary-height); padding: 0 12px; border-radius: var(--light-component-buttonSecondary-radius); background: var(--light-component-buttonSecondary-background); color: var(--light-component-buttonSecondary-text); text-decoration: none; box-shadow: 0 0 0 1px rgba(0,0,0,.08); }}
.badge {{ display: inline-flex; align-items: center; height: 20px; padding: 0 6px; border-radius: var(--light-component-badge-radius); background: var(--light-component-badge-background); color: var(--light-component-badge-text); font-size: 12px; }}
.display {{ font: 300 60px/64px var(--sg-display); margin: 0; }}
.note {{ color: var(--light-muted); font-size: 14px; }}
</style>
</head>
<body>
<header>
  <h1>Programa</h1>
  <p class="lede">Public marketing site, one light theme. Values come from tokens.json, read from programa.design on 2026-11-21. Rhymes Display is not loaded here, so the display face falls back to Georgia.</p>
</header>
<main>
  <h2>Colour roles</h2>
  <div class="swatches">
    {''.join(swatches)}
  </div>
  <h2>Type</h2>
  <p class="display">Freedom, by design</p>
  <p>Body is Inter at 16px. Labels are Inter at 14px. Captions are 12px in the muted role.</p>
  <h2>Buttons</h2>
  <div class="row">
    <a class="btn-primary" href="#buttons">Start free</a>
    <a class="btn-dark" href="#buttons">Get started</a>
    <a class="btn-secondary" href="#buttons">Watch a demo</a>
    <span class="badge">New</span>
  </div>
  <p class="note">The mint header button is measured, not the yellow accent. Yellow is the declared primary token. The New badge uses the green pale and green dark pair.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(html))
