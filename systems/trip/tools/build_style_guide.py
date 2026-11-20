#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Trip.com publishes one light theme on the public pages captured here.
The guide starts in light and hides the theme toggle. Trip Geom is
proprietary and is not loaded; the page falls back to the system stack
the site itself names after Trip Geom.

Run from systems/trip: python3 tools/build_style_guide.py
"""
from __future__ import annotations

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
            yield from flat(v, prefix + k + "-")


def cssname(path):
    return "--" + re.sub(r"[^a-zA-Z0-9-]", "-", path.replace(".", "-"))


def alias(v):
    return re.sub(r"\{([^{}]+)\}", lambda m: f"var({cssname(m.group(1))})", str(v))


def css_val(token):
    v, ty = token["$value"], token["$type"]
    if ty == "shadow":
        return alias(v) if isinstance(v, str) else None
    if ty == "typography":
        return f'{alias(v["fontWeight"])} {alias(v["fontSize"])}/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
    if ty == "other":
        return None
    return alias(v)


def block(setname):
    return "\n".join(
        f"  {cssname(n)}: {css_val(t)};"
        for n, t in flat(T[setname])
        if css_val(t) is not None
    )


# Inlined into a <script>: "<" as \u003c keeps a value holding "</script>" from ending it early.
# Computed before the f-string, because a backslash inside an f-string expression needs Python 3.12.
TOK_JSON = json.dumps({"core": T["core"], "light": T["light"]}, separators=(",", ":")).replace("<", "\\u003c")
CSS = f""":root {{
{block("core")}
{block("light")}
  color-scheme: light;
  --sg-sans: "Trip Geom", system-ui, -apple-system, Roboto, Helvetica, Arial, sans-serif;
  --sg-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
  --page: var(--color-bg-surface);
  --ink: var(--color-text-primary);
  --muted: var(--color-text-tertiary);
  --line: var(--color-border-default);
  --brand: var(--color-bg-brand);
}}
* {{ box-sizing: border-box; }}
html, body {{ margin: 0; background: var(--page); color: var(--ink); font: 400 14px/22px var(--sg-sans); }}
.wrap {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 80px; }}
h1 {{ font: 700 32px/40px var(--sg-sans); margin: 0 0 8px; }}
h2 {{ font: 700 20px/26px var(--sg-sans); margin: 40px 0 8px; }}
p {{ max-width: 72ch; color: var(--muted); }}
code {{ font-family: var(--sg-mono); font-size: 12px; }}
.swatches {{ display: flex; flex-wrap: wrap; gap: 8px; }}
.swatch {{ width: 132px; }}
.swatch i {{ display: block; height: 48px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(18,24,38,.08); }}
.swatch span {{ display: block; font-size: 11px; line-height: 14px; margin-top: 4px; color: var(--muted); word-break: break-all; }}
.row {{ display: flex; flex-wrap: wrap; gap: 16px; align-items: flex-end; }}
.btn {{ display: inline-flex; align-items: center; justify-content: center; height: var(--component-button-l-height); min-width: 74px; padding: 0 16px; border-radius: var(--component-button-l-border-radius); border: 0; background: var(--component-button-primary-background-color); color: var(--component-button-primary-color); font: 700 16px/24px var(--sg-sans); }}
.btn.hover {{ background: var(--component-button-primary-hover-background); }}
.btn.off {{ background: var(--component-button-disabled-filled-background); color: #fff; }}
.btn.line {{ background: transparent; color: var(--component-button-secondary-color); box-shadow: inset 0 0 0 1px var(--component-button-secondary-border-color); }}
.field {{ width: 280px; height: 56px; border-radius: 4px; border: 1px solid var(--component-search-field-border); background: #fff; padding: 16px 12px; font: 700 16px/22px var(--sg-sans); color: var(--ink); }}
.field:focus {{ outline: none; border-color: var(--component-textinput-focus-border); }}
.card {{ width: 280px; border-radius: var(--component-card-border-radius); background: #fff; box-shadow: var(--shadow-search-card); padding: 16px; }}
.chip {{ display: inline-block; padding: 12px 16px; border-radius: 4px; background: var(--component-faq-chip-background); color: var(--ink); font: 400 14px/18px var(--sg-sans); }}
table {{ border-collapse: collapse; width: 100%; font-size: 13px; }}
th, td {{ text-align: left; padding: 6px 8px; border-bottom: 1px solid var(--line); vertical-align: top; }}
th {{ color: var(--muted); font-weight: 500; }}
"""

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Trip.com style guide</title>
<meta name="description" content="Trip.com public signed-out tokens, rendered from tokens.json. One light theme. Trip Geom is not loaded.">
<style>
{CSS}
</style>
</head>
<body>
<div class="wrap">
  <h1>Trip.com</h1>
  <p>Public signed-out surfaces, measured 2026-11-19. One light theme. The brand face Trip Geom is proprietary and is not loaded here, so the system stack the site names after it is the fallback. Screenshots were not captured: the preview browser returned no frames, and a fresh headless session was stopped by Trip's verification wall.</p>

  <h2>Roles</h2>
  <div class="swatches" id="roles"></div>

  <h2>Brand blue ramp</h2>
  <div class="swatches" id="blue"></div>

  <h2>Type</h2>
  <div id="type"></div>

  <h2>Search</h2>
  <div class="card">
    <div style="font:700 14px/21px var(--sg-sans); color:var(--component-tab-active-text); margin-bottom:12px">Hotels &amp; Homes</div>
    <input class="field" placeholder="Where to?" aria-label="Where to?">
    <div style="height:12px"></div>
    <button class="btn" type="button">Search</button>
    <button class="btn hover" type="button">Search hover</button>
    <button class="btn off" type="button" disabled>Disabled</button>
  </div>
  <p>Search rest is brand blue #2c61fe, 48px tall on the home card, radius 4px. Hover from the stylesheet is rgb(41, 83, 214). The disabled Continue control on sign-in paints rgb(206, 210, 217), which is not the token #b9bec7.</p>

  <h2>Chips and support</h2>
  <span class="chip">Hot topics</span>
  <span class="chip">Booking &amp; price</span>
  <p>Support hero background is cyan #047c88. FAQ chips are #f5f7fa, radius 4px, padding 12px 16px.</p>

  <h2>Spacing and radius</h2>
  <div id="space"></div>
</div>
<script>
const TOK = {TOK_JSON};
function val(path) {{
  const parts = path.replace(/\\{{|\\}}/g, "").split(".");
  let n = TOK;
  for (const p of parts) n = n && n[p];
  if (!n) return "";
  if (typeof n.$value === "string" && n.$value.startsWith("{{")) return val(n.$value);
  return n.$value;
}}
function swatch(name, color) {{
  const d = document.createElement("div");
  d.className = "swatch";
  d.innerHTML = "<i></i><span></span>";
  d.querySelector("i").style.background = color;
  d.querySelector("span").textContent = name + " " + color;
  return d;
}}
const roles = ["bg-page","bg-surface","bg-brand","bg-positive","bg-warning","bg-alert","bg-discount","text-primary","text-secondary","text-tertiary","text-brand","border-default"];
const roleBox = document.getElementById("roles");
for (const r of roles) roleBox.append(swatch(r, val("light.color." + r)));
const blue = document.getElementById("blue");
for (const k of Object.keys(TOK.core.color).filter(k => k.startsWith("blue") && !k.includes("a")).sort()) {{
  blue.append(swatch(k, TOK.core.color[k].$value));
}}
const type = document.getElementById("type");
const table = document.createElement("table");
table.innerHTML = "<tr><th>Role</th><th>Specimen</th><th>Value</th></tr>";
for (const [k, t] of Object.entries(TOK.core.typography)) {{
  if (!k.startsWith("body") && !k.startsWith("display") && !k.startsWith("typography-heading")) continue;
  const v = t.$value;
  const tr = document.createElement("tr");
  tr.innerHTML = "<td><code></code></td><td class='s'></td><td><code class='v'></code></td>";
  tr.querySelector("code").textContent = k;
  tr.querySelector(".s").textContent = "Where to?";
  tr.querySelector(".s").style.font = v.fontWeight + " " + v.fontSize + "/" + v.lineHeight + " var(--sg-sans)";
  tr.querySelector(".v").textContent = v.fontWeight + " " + v.fontSize + "/" + v.lineHeight;
  table.append(tr);
}}
type.append(table);
const space = document.getElementById("space");
const st = document.createElement("table");
st.innerHTML = "<tr><th>Token</th><th>Value</th></tr>";
for (const group of ["space", "radius"]) {{
  for (const [k, t] of Object.entries(TOK.core[group])) {{
    const tr = document.createElement("tr");
    tr.innerHTML = "<td><code></code></td><td></td>";
    tr.children[0].firstChild.textContent = group + "." + k;
    tr.children[1].textContent = t.$value;
    st.append(tr);
  }}
}}
space.append(st);
</script>
</body>
</html>
"""


def main() -> None:
    path = HERE / "style-guide.html"
    path.write_text(HTML)
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
