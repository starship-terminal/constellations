#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Kinhive's core and semantic sets both name colors (core.color.ink and
light.color.ink), so the kit template's shared --color-ink custom property
would clash. This builder prefixes each set (--core-color-ink,
--light-color-ink) and paints specimens from the light set, with a toggle
that swaps in the dark set.
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
            yield from flat(v, prefix + k + ".")


def css_name(setname, path):
    return "--" + setname + "-" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def css_val(setname, token):
    v, ty = token["$value"], token["$type"]
    if isinstance(v, str) and v.startswith("{"):
        target = v.strip("{}")
        # Semantic aliases point at the same set (color.ink) or at core.
        if target.startswith("core."):
            owner, target = "core", target[5:]
        elif target.startswith("color."):
            # A bare color.* alias lives on the same set, so the theme toggle swaps it.
            owner = setname
        elif target.split(".")[0] in ("color", "font", "radius", "spacing", "motion", "component"):
            owner = "core"
        else:
            owner = setname
        return f"var({css_name(owner, target)})"
    if ty == "cubicBezier":
        return "cubic-bezier(%s)" % ", ".join(str(x) for x in v)
    if ty == "fontFamily":
        return v
    return str(v)


def block(setname):
    lines = []
    for path, token in flat(T[setname]):
        val = css_val(setname, token)
        if val:
            lines.append(f"  {css_name(setname, path)}: {val};")
    return "\n".join(lines)


def js(obj):
    """JSON for an inline <script>: a "<" in a value could otherwise close the script early."""
    return json.dumps(obj).replace("<", "\\u003c")


def literal(token):
    """The printed swatch label. An alias to core resolves to that hex."""
    v = token["$value"]
    if not isinstance(v, str) or not v.startswith("{") or not v.endswith("}"):
        return v
    parts = v[1:-1].split(".")
    if not parts or parts[0] != "core":
        return v
    node = T["core"]
    for part in parts[1:]:
        node = node.get(part) if isinstance(node, dict) else None
    if isinstance(node, dict) and "$value" in node and not str(node["$value"]).startswith("{"):
        return node["$value"]
    return v


def swatch(setname, group):
    rows = []
    node = T[setname].get(group) or T["core"].get(group) or {}
    for name, token in node.items():
        if not isinstance(token, dict) or token.get("$type") != "color":
            continue
        # color group lives on both core and the theme. Specimens use the theme.
        var = css_name(setname, f"{group}.{name}")
        rows.append(
            f'<div class="sw"><i style="background:{var}"></i><div><b>{group}.{name}</b><code>{var}</code></div></div>'
        )
    return "\n".join(rows)


html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Kinhive style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
  --page: var(--light-background-page);
  --ink: var(--light-text-ink);
  --body: var(--light-text-body);
  --muted: var(--light-text-muted);
  --line: var(--light-border-line);
  --canvas: var(--light-background-canvas);
  --fill: var(--light-action-fill);
  --on: var(--light-action-ink);
  --butter: var(--light-background-butter);
  --chartreuse: var(--core-color-chartreuse);
  --sans: var(--core-font-family-sans);
  --heading: var(--core-font-family-heading);
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
  --page: var(--dark-background-page);
  --ink: var(--dark-text-ink);
  --body: var(--dark-text-body);
  --muted: var(--dark-text-muted);
  --line: var(--dark-border-line);
  --canvas: var(--dark-background-canvas);
  --fill: var(--dark-action-fill);
  --on: var(--dark-action-ink);
  --butter: var(--dark-background-butter);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--ink); font: 400 15px/1.5 var(--sans); }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 28px; border-bottom: 1px solid var(--line); position: sticky; top: 0; background: var(--page); }}
header h1 {{ font: 400 22px/1 var(--heading); margin: 0; letter-spacing: 0.04em; }}
header button {{ margin-left: auto; height: 32px; padding: 0 14px; border-radius: 8px; border: 1px solid var(--line); background: var(--canvas); color: var(--ink); font: 500 13px var(--sans); }}
main {{ max-width: 1080px; margin: 0 auto; padding: 32px 28px 80px; }}
h2 {{ font: 400 32px/1.1 var(--heading); margin: 40px 0 8px; }}
p.note {{ color: var(--body); max-width: 68ch; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }}
.sw {{ display: grid; grid-template-columns: 40px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 40px; height: 40px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--line); }}
.sw b {{ display: block; font-size: 13px; }}
.sw code, code {{ font: 12px/1.4 ui-monospace, Menlo, monospace; color: var(--muted); }}
.row {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 16px 0; }}
.cta {{ display: inline-flex; align-items: center; height: 32px; padding: 0 14px; border-radius: 8px; background: var(--fill); color: var(--on); font: 500 13.5px var(--sans); text-decoration: none; }}
.field {{ height: 44px; min-width: 240px; border: 1px solid var(--line); border-radius: 8px; background: var(--page); color: var(--muted); padding: 0 12px; display: flex; align-items: center; }}
.card {{ background: var(--butter); color: var(--ink); border-radius: 16px; padding: 24px; max-width: 420px; }}
.card h3 {{ font: 400 36px/1.05 var(--heading); margin: 8px 0; }}
.price {{ background: var(--chartreuse); color: #111; border-radius: 16px; padding: 24px; max-width: 320px; }}
.price .amt {{ font: 400 64px/1 var(--heading); }}
.chip {{ width: 36px; height: 36px; border-radius: 10px; background: var(--chartreuse); display: inline-flex; align-items: center; justify-content: center; color: #111; font-weight: 600; }}
nav.sample a {{ color: var(--body); text-decoration: none; font: 500 14px var(--sans); padding: 8px 12px; border-radius: 8px; }}
</style>
</head>
<body>
<header>
  <h1>KINHIVE</h1>
  <span>Style guide, rendered from tokens.json</span>
  <button type="button" id="theme">Dark palette</button>
</header>
<main>
  <p class="note">Values come from kinhive.com's declared custom properties, resolved on 2026-11-18. The dark palette is the declared <code>prefers-color-scheme: dark</code> set on <code>html[data-app-theme=system]</code>. The live public document does not set that attribute, so the painted site is light. Figtree and Affairs are not loaded here; the stacks fall back.</p>

  <h2>Colour</h2>
  <div class="grid" id="colors"></div>

  <h2>Type</h2>
  <p style="font: 400 44px/1.05 var(--heading); margin: 0">Meet the women you should already know.</p>
  <p class="note">Heading is Affairs at 44px on desktop. Body is Figtree.</p>

  <h2>Controls</h2>
  <div class="row">
    <a class="cta" href="#cta">Join free</a>
    <div class="field">Your email to join free</div>
    <span class="chip">+</span>
  </div>
  <nav class="sample row"><a>Features</a><a>Use Cases</a><a>Pricing</a><a>About</a></nav>

  <h2>Hero card</h2>
  <div class="card">
    <div style="font-size:13px;color:var(--body)">AI introductions for women who build</div>
    <h3>Meet the women you should already know.</h3>
    <div class="field" style="background:var(--page)">Your email to join free</div>
  </div>

  <h2>Pricing card</h2>
  <div class="price">
    <div>Every member</div>
    <div class="amt">$0</div>
    <div>Per month, per year, forever</div>
  </div>
</main>
<script>
const palettes = {{
  light: {js({name: literal(T["light"]["color"][name]) for name in T["light"]["color"]})},
  dark: {js({name: literal(T["dark"]["color"][name]) for name in T["dark"]["color"]})}
}};
const root = document.getElementById("colors");
function showPalette(mode) {{
  root.replaceChildren();
  for (const [name, value] of Object.entries(palettes[mode])) {{
    const d = document.createElement("div");
    d.className = "sw";
    d.innerHTML = '<i style="background:var(--' + mode + '-color-' + name + ')"></i><div><b>color.' + name + '</b><code>' + value + '</code></div>';
    root.appendChild(d);
  }}
}}
showPalette("light");
document.getElementById("theme").onclick = () => {{
  const dark = document.documentElement.getAttribute("data-mode") !== "dark";
  document.documentElement.setAttribute("data-mode", dark ? "dark" : "light");
  document.getElementById("theme").textContent = dark ? "Light palette" : "Dark palette";
  showPalette(dark ? "dark" : "light");
}};
</script>
</body>
</html>
"""
# The f-string doubled braces so CSS emits single braces. The script block
# used the same doubling, which would leave literal {{ }} in the page.
script_at = html.index("<script>")
html = html[:script_at] + html[script_at:].replace("{{", "{").replace("}}", "}")
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
