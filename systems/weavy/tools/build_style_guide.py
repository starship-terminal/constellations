#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light only: the public site has one theme."""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


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


def alias(value):
    return re.sub(r"\{([^{}]+)\}", lambda match: f"var({cssname(match.group(1))})", str(value))


def css_val(token):
    value, kind = token["$value"], token["$type"]
    if kind == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(item) for item in value)
    if kind == "shadow":
        return ", ".join(
            f'{item["offsetX"]} {item["offsetY"]} {item["blur"]} {item["spread"]} {alias(item["color"])}'
            for item in value)
    if kind == "typography":
        return f'{alias(value["fontWeight"])} {alias(value["fontSize"])}/{alias(value["lineHeight"])} {alias(value["fontFamily"])}'
    return alias(value)


props = "\n".join(
    f"  {cssname(name)}: {css_val(token)};"
    for set_name in ("core", "light")
    for name, token in flat(T[set_name])
)

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Figma Weave style guide</title>
<style>
:root {{
{props}
  color-scheme: light;
  --sg-sans: "Figma Sans Regular", Arial, sans-serif;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--color-page); color: var(--color-text); font: 400 14.4px/20px var(--sg-sans); }}
header {{ padding: 20px 28px; display: flex; justify-content: space-between; align-items: center; background: var(--color-inverse); color: var(--color-text-on-inverse); }}
header h1 {{ margin: 0; font-size: 20px; font-weight: 400; }}
.cta {{ background: var(--color-accent); color: var(--color-ink); padding: 10px 16px; font-size: 28px; line-height: 1; text-decoration: none; }}
main {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 64px; }}
h2 {{ font-size: 28px; font-weight: 400; letter-spacing: -0.8px; margin: 36px 0 12px; }}
.row {{ display: flex; flex-wrap: wrap; gap: 16px; }}
.sw {{ width: 180px; }}
.sw i {{ display: block; height: 56px; border: 1px solid var(--color-border); }}
.sw b, .sw span {{ display: block; font-size: 12px; line-height: 16px; }}
.sw span {{ color: var(--color-muted); }}
.card {{ background: var(--color-surface); border: 1px solid var(--color-border); border-radius: var(--radius-card); padding: 21px; width: 280px; }}
.card h3 {{ margin: 0 0 8px; font-size: 22px; font-weight: 400; }}
.btn {{ display: inline-block; background: var(--color-button); color: var(--color-text-on-inverse); border-radius: var(--radius-control); padding: 10.8px 21.6px; text-decoration: none; }}
.badge {{ background: var(--color-accent); color: rgba(0,0,0,.9); border-radius: var(--radius-badge); padding: 2px 6px; font-family: Dmsans, Arial, sans-serif; font-size: 13px; }}
.tab {{ background: var(--color-tab-selected); color: white; border-radius: var(--radius-control); padding: 8px 16px; }}
.note {{ color: var(--color-muted); max-width: 68ch; }}
.type-display {{ font-size: var(--fontSize-display); line-height: var(--lineHeight-display); letter-spacing: -4.32px; color: var(--color-ink); }}
</style>
</head>
<body>
<header>
  <h1>Figma Weave</h1>
  <a class="cta" href="#components">Start Now</a>
</header>
<main>
  <p class="note">Public marketing surface of weavy.ai, captured 2026-11-21. One theme. Values come from tokens.json. Figma Sans is not loaded here, so the page falls back to Arial.</p>
  <h2>Colour</h2>
  <div class="row" id="swatches"></div>
  <h2>Type</h2>
  <p class="type-display">Figma Weave</p>
  <p>Body at 14.4px. Nav labels are 12px uppercase.</p>
  <h2 id="components">Components</h2>
  <div class="row">
    <div class="card">
      <span class="badge">Save 30%</span>
      <h3>Free</h3>
      <p>Explore Figma Weave's possibilities</p>
      <a class="btn" href="#components">Start free</a>
    </div>
    <div>
      <span class="tab">Individuals</span>
      <p class="note">The plan button hover fill is #eaf297. The nav Start Now hover fill is #252525 with #f4f4f4 text.</p>
    </div>
  </div>
</main>
<script>
const roles = [
  ["page", "--color-page"], ["surface", "--color-surface"], ["inverse", "--color-inverse"],
  ["text", "--color-text"], ["ink", "--color-ink"], ["muted", "--color-muted"],
  ["accent", "--color-accent"], ["button", "--color-button"], ["border", "--color-border"]
];
const root = document.getElementById("swatches");
for (const [name, prop] of roles) {{
  const el = document.createElement("div");
  el.className = "sw";
  el.innerHTML = `<i style="background:var(${{prop}})"></i><b>${{name}}</b><span>${{getComputedStyle(document.documentElement).getPropertyValue(prop)}}</span>`;
  root.append(el);
}}
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
