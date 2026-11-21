#!/usr/bin/env python3
"""Render style-guide.html from tokens.json for the Coolors package.

The kit template is Claude's example and refuses to render until it is
adapted. This builder writes a self-contained guide from the Coolors token
tree instead. Every painted color is a custom property generated from
tokens.json. Dark values are stylesheet evidence, not a live screenshot.
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


def css_val(token):
    v, ty = token["$value"], token["$type"]
    if ty == "shadow":
        return ", ".join(
            f'{s["offsetX"]} {s["offsetY"]} {s["blur"]} {s["spread"]} {alias(s["color"])}'
            for s in v
        )
    if ty == "typography":
        return (
            f'{alias(v["fontWeight"])} {alias(v["fontSize"])}'
            f'/{alias(v["lineHeight"])} {alias(v["fontFamily"])}'
        )
    if ty == "fontFamily":
        return ", ".join(v)
    return alias(v)


def block(setname):
    # Keep the set name so aliases such as {core.color.primary.600} resolve.
    return "\n".join(
        f"  {cssname(setname + '.' + n)}: {css_val(t)};"
        for n, t in flat(T[setname])
    )


def role_rows(mode):
    rows = []
    for name, token in T[mode].items():
        paint = alias(token["$value"]) if str(token["$value"]).startswith("{") else token["$value"]
        rows.append(
            f'<div class="sw" data-role="{name}"><i style="background:{paint}"></i>'
            f'<div><b>{mode}.{name}</b><code>{token["$value"]}</code></div></div>'
        )
    return rows


swatches = role_rows("light")
dark_rows = {name: token for name, token in T["dark"].items()}

ramps = []
for ramp, stops in T["core"]["color"].items():
    if "$value" in stops:
        continue
    cells = "".join(
        f'<i title="{ramp}-{stop}" style="background:{stops[stop]["$value"]}"></i>'
        for stop in stops
    )
    ramps.append(f'<div class="ramp"><span>{ramp}</span>{cells}</div>')

html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coolors style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--light-page); color: var(--light-text); font: 450 15px/22px Inter, sans-serif; }}
header {{ display: flex; align-items: center; gap: 16px; height: 60px; padding: 0 24px; box-shadow: var(--core-shadow-header); background: var(--light-page); position: sticky; top: 0; }}
header h1 {{ font-size: 18px; margin: 0; letter-spacing: -0.4px; }}
header button {{ margin-left: auto; height: 36px; padding: 0 12px; border-radius: 8px; border: 0; background: var(--light-accent); color: #fff; font: 500 15px/36px Inter, sans-serif; }}
main {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 80px; }}
h2 {{ font-size: 28px; letter-spacing: -0.8px; margin: 36px 0 12px; }}
.swatches, .roles {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }}
.sw, .role {{ display: flex; gap: 10px; align-items: center; }}
.sw i, .role i {{ width: 36px; height: 36px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.12); display: block; }}
code {{ font-family: "IBM Plex Mono", ui-monospace, monospace; font-size: 12px; color: var(--light-muted); }}
.ramp {{ display: grid; grid-template-columns: 88px repeat(11, 1fr); gap: 3px; align-items: center; margin: 4px 0; }}
.ramp i {{ height: 22px; border-radius: 3px; display: block; }}
.demo {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; padding: 16px; background: var(--light-surface); border-radius: 10px; }}
.btn {{ height: 36px; padding: 0 12px; border-radius: 8px; border: 0; font: 500 15px/36px Inter, sans-serif; }}
.btn.primary {{ background: var(--light-accent); color: #fff; }}
.btn.ghost {{ background: transparent; color: var(--light-text); }}
.btn.pro {{ background: transparent; color: var(--light-pro); }}
.btn.gray {{ background: var(--light-button-gray); color: var(--light-button-gray-text); }}
.cols {{ display: flex; height: 160px; border-radius: 8px; overflow: hidden; }}
.cols span {{ flex: 1; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 12px; font-weight: 600; letter-spacing: 0.9px; }}
p.note {{ color: var(--light-muted); max-width: 70ch; }}
</style>
</head>
<body>
<header>
  <h1>Coolors</h1>
  <button type="button" id="theme">Dark tokens</button>
</header>
<main>
  <p class="note">Rendered from tokens.json. Light values were computed on the signed-in page. Dark values are the stylesheet's smart-alias flip, not a live theme switch.</p>
  <h2>Roles</h2>
  <div class="swatches">
    {''.join(swatches)}
  </div>
  <h2>Controls</h2>
  <div class="demo">
    <button class="btn primary" type="button">Start the generator</button>
    <button class="btn ghost" type="button">Tools</button>
    <button class="btn gray" type="button">Gray</button>
    <button class="btn pro" type="button">Go Pro</button>
  </div>
  <h2>Generator columns</h2>
  <div class="cols">
    <span style="background:#264653;color:#fff">264653</span>
    <span style="background:#2A9D8F;color:#fff">2A9D8F</span>
    <span style="background:#E9C46A;color:#000">E9C46A</span>
    <span style="background:#F4A261;color:#000">F4A261</span>
    <span style="background:#E76F51;color:#fff">E76F51</span>
  </div>
  <p class="note">Sample palette from the signed-in generator at /264653-2a9d8f-e9c46a-f4a261-e76f51. Column colors are palette data, not tokens.</p>
  <h2>Ramps</h2>
  {''.join(ramps)}
</main>
<script>
const darkRoles = {json.dumps({name: {"label": f"dark.{name}", "value": token["$value"], "paint": alias(token["$value"]) if str(token["$value"]).startswith("{") else token["$value"]} for name, token in dark_rows.items()})};
const lightRoles = {json.dumps({name: {"label": f"light.{name}", "value": token["$value"], "paint": alias(token["$value"]) if str(token["$value"]).startswith("{") else token["$value"]} for name, token in T["light"].items()})};
document.getElementById("theme").addEventListener("click", () => {{
  const html = document.documentElement;
  const next = html.getAttribute("data-mode") === "dark" ? "light" : "dark";
  html.setAttribute("data-mode", next);
  document.body.style.background = "";
  document.body.style.color = "";
  const roles = next === "dark" ? darkRoles : lightRoles;
  document.querySelectorAll("[data-role]").forEach((row) => {{
    const role = roles[row.dataset.role];
    if (!role) return;
    row.querySelector("i").style.background = role.paint;
    row.querySelector("b").textContent = role.label;
    row.querySelector("code").textContent = role.value;
  }});
}});
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html.encode()), "bytes")
