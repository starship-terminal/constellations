#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

DailyArt Magazine has one light theme and no icon set in this package, so the
guide is generated here rather than from the Claude template. Every colour and
type style is a custom property from tokens.json. Deterministic.
"""
import json, pathlib, re

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
    v, ty = t["$value"], t["$type"]
    if ty == "typography":
        lh = alias(v.get("lineHeight", v["fontSize"]))
        ls = v.get("letterSpacing")
        extra = f" letter-spacing:{alias(ls)};" if ls else ""
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{lh} {alias(v["fontFamily"])}', extra
    return alias(v), ""


lines = []
for name, tok in list(flat(T["core"])) + list(flat(T["light"])):
    val, _ = css_val(tok)
    lines.append(f"  {cssname(name)}: {val};")
css = "\n".join(lines)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>DailyArt Magazine style guide</title>
<style>
:root {{
{css}
  color-scheme: light;
  --sg-sans: "Basier", ui-sans-serif, system-ui, sans-serif;
  --sg-display: "RoslindaleCondensed", "Iowan Old Style", Palatino, serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--text); font: 400 16px/24px var(--sg-sans); }}
header {{ background: var(--header); color: var(--text-on-dark); padding: 16px 24px; display: flex; gap: 24px; align-items: center; }}
header strong {{ font-family: var(--sg-display); font-weight: 500; font-size: 22px; letter-spacing: 0; }}
header span {{ font-size: 14px; font-weight: 600; }}
main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px 64px; }}
h2 {{ font: 500 32px/40px var(--sg-display); margin: 32px 0 12px; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
.swatch {{ width: 140px; }}
.swatch i {{ display: block; height: 64px; border: 1px solid var(--border); }}
.swatch code {{ font-size: 11px; color: var(--text-secondary); }}
.btn {{ display: inline-block; background: var(--button); color: var(--button-text); font: 600 14px/17px var(--sg-sans); padding: 10.5px 20px; border-radius: var(--radius-control); border: 0; }}
.btn.ghost {{ background: transparent; color: var(--text); box-shadow: inset 0 0 0 1px var(--text); }}
.badge {{ display: inline-block; background: var(--accent); color: var(--text-on-dark); font: 700 10px/12px var(--sg-sans); padding: 4px; border-radius: var(--radius-control); letter-spacing: 0.04em; text-transform: uppercase; }}
a.sample {{ color: var(--link); font-weight: 700; font-size: 12px; text-decoration: none; }}
input, textarea {{ font: 400 14px/18px var(--sg-sans); border: 1px solid var(--border); border-radius: var(--radius-field); padding: 10px; width: 320px; }}
.card {{ background: var(--header); color: var(--text-on-dark); padding: 24px; margin-top: 16px; }}
.card h3 {{ font: 500 40px/48px var(--sg-display); margin: 8px 0; }}
.note {{ color: var(--text-muted); font-size: 14px; }}
</style>
</head>
<body>
<header>
  <strong>DailyArt Magazine</strong>
  <span>Stories</span><span>Shop</span><span>Courses</span>
  <span style="margin-left:auto;box-shadow:inset 0 0 0 1px #fff;padding:8px 16px;border-radius:3px">Search</span>
</header>
<main>
  <h2>Colour</h2>
  <div class="swatches">
    <div class="swatch"><i style="background:var(--page)"></i><code>page</code></div>
    <div class="swatch"><i style="background:var(--header)"></i><code>header</code></div>
    <div class="swatch"><i style="background:var(--accent)"></i><code>accent</code></div>
    <div class="swatch"><i style="background:var(--text)"></i><code>text</code></div>
    <div class="swatch"><i style="background:var(--text-muted)"></i><code>text muted</code></div>
    <div class="swatch"><i style="background:var(--border)"></i><code>border</code></div>
  </div>
  <h2>Type</h2>
  <p style="font:var(--typography-display);font:500 56px/60px var(--sg-display)">Article title</p>
  <p style="font:500 32px/40px var(--sg-display)">Section heading</p>
  <p style="font:400 18px/24px var(--sg-sans);color:var(--text-muted)">Article body in Basier, 18 on 24, slate.</p>
  <h2>Controls</h2>
  <p><span class="badge">Renaissance</span></p>
  <p><span class="btn">Search</span> <span class="btn ghost">Subscribe</span></p>
  <p><a class="sample" href="#">About Us</a></p>
  <p><input placeholder="Your name" readonly></p>
  <div class="card">
    <span class="badge">Featured story</span>
    <h3>African Art Highlights</h3>
    <p style="color:#fff;opacity:.8">Featured band on the header ink.</p>
  </div>
  <p class="note">One light theme. Basier and Roslindale are licensed and are not loaded here. Values come from tokens.json.</p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
