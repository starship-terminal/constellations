#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

The kit template is Claude's guide. Uber's tokens use different paths, so
this builder writes a page that only reads names this package actually has.
Colours, radii and type samples come from tokens.json. Re-running it on the
same tokens reproduces the file.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    if not isinstance(node, dict):
        return
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        else:
            yield from flat(value, path)


def css_name(path: str) -> str:
    return "--" + path.replace(".", "-")


def main() -> None:
    light = {path: token for path, token in flat(T["light"]) if token["$type"] == "color"}
    dark = {path: token for path, token in flat(T["dark"]) if token["$type"] == "color"}
    radii = [(path, token) for path, token in flat(T["core"]) if path.startswith("radius.")]
    type_roles = [(path, token) for path, token in flat(T["core"]) if path.startswith("typography.")]
    families = {path: token["$value"] for path, token in flat(T["core"]) if path.startswith("family.")}

    def vars_for(mapping: dict) -> str:
        return "\n".join(f"  {css_name(path)}: {token['$value']};" for path, token in mapping.items())

    swatches = "\n".join(
        f'<div class="sw"><i style="background:{css_name(path) in light and "var(" + css_name(path) + ")" or token["$value"]}"></i>'
        f'<div><b>{path}</b><span>{token["$value"]}</span></div></div>'
        for path, token in light.items()
    )
    # fix the botched ternary above by rebuilding cleanly
    swatches = "\n".join(
        f'<div class="sw"><i style="background:var({css_name(path)})"></i>'
        f'<div><b>{path}</b><span>{token["$value"]}</span></div></div>'
        for path, token in light.items()
    )
    radius_row = "\n".join(
        f'<div class="rad"><i style="border-radius:{token["$value"]}"></i><span>{path.split(".",1)[1]} {token["$value"]}</span></div>'
        for path, token in radii
    )
    type_rows = "\n".join(
        f'<div class="ty"><code>{path}</code><p style="font:{token["$value"]["fontWeight"]} {token["$value"]["fontSize"]}/{token["$value"]["lineHeight"]} {token["$value"]["fontFamily"].split(",")[0]}">Request a ride</p></div>'
        for path, token in type_roles
    )
    body = families.get("family.body", "system-ui, sans-serif")
    display = families.get("family.display", body)
    html = f"""<!doctype html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Uber style guide</title>
<style>
:root {{
{vars_for(light)}
  color-scheme: light;
  --page: var(--background-primary);
  --ink: var(--content-primary);
  --muted: var(--content-secondary);
  --line: var(--border-subtle);
}}
[data-theme="dark"] {{
{vars_for(dark)}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--ink); font: 400 16px/24px {body}; }}
header {{ display: flex; gap: 16px; align-items: center; padding: 16px 24px; background: #000; color: #fff; }}
header h1 {{ margin: 0; font: 400 24px/32px {display}; }}
header button {{ margin-left: auto; height: 36px; padding: 10px 12px; border: 0; border-radius: 999px; background: #fff; color: #000; font: 500 14px/16px {body}; }}
main {{ max-width: 1100px; margin: 0 auto; padding: 32px 24px 64px; }}
h2 {{ font: 700 36px/44px {display}; margin: 40px 0 12px; }}
.grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 12px; }}
.sw {{ display: grid; grid-template-columns: 44px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 44px; height: 44px; border-radius: 8px; box-shadow: inset 0 0 0 1px var(--line); }}
.sw b {{ display: block; font: 500 12px/16px ui-monospace, monospace; }}
.sw span {{ color: var(--muted); font-size: 12px; }}
.row {{ display: flex; gap: 16px; flex-wrap: wrap; align-items: end; }}
.rad i {{ display: block; width: 64px; height: 40px; background: var(--background-secondary); box-shadow: inset 0 0 0 1px var(--line); }}
.rad span {{ display: block; margin-top: 6px; font-size: 12px; color: var(--muted); }}
.ty {{ display: grid; grid-template-columns: 180px 1fr; gap: 16px; align-items: baseline; padding: 8px 0; border-bottom: 1px solid var(--line); }}
.ty p {{ margin: 0; }}
.btn {{ display: inline-flex; align-items: center; height: 48px; padding: 14px 25px; border-radius: 8px; background: var(--component-button-primary-bg, #111); color: var(--component-button-primary-text, #fcfcfc); font: 500 16px/20px {body}; }}
.pill {{ display: inline-flex; align-items: center; height: 36px; padding: 10px 12px; border-radius: 999px; background: #111; color: #fcfcfc; font: 500 14px/16px {body}; }}
.field {{ height: 56px; width: 280px; border-radius: 8px; background: #f6f6f6; color: #111; display: flex; align-items: center; padding: 0 16px; }}
.note {{ color: var(--muted); max-width: 70ch; }}
</style>
</head>
<body>
<header>
  <h1>Uber</h1>
  <span>Signed-out public capture</span>
  <button type="button" id="theme">Dark tokens</button>
</header>
<main>
  <p class="note">Values are the v2 Base tokens from Uber's public stylesheet, with aliases resolved, plus computed styles from the signed-out ride page. Dark tokens are declared for data-theme=dark. The marketing pages measured here stay in light.</p>
  <h2>Colour</h2>
  <div class="grid">
{swatches}
  </div>
  <h2>Radius</h2>
  <div class="row">
{radius_row}
  </div>
  <h2>Type</h2>
  <div>
{type_rows}
  </div>
  <h2>Chrome</h2>
  <div class="row">
    <span class="pill">Ride</span>
    <span class="btn">See prices</span>
    <span class="field">Pickup location</span>
  </div>
</main>
<script>
document.getElementById("theme").addEventListener("click", () => {{
  const html = document.documentElement;
  const next = html.getAttribute("data-theme") === "dark" ? "light" : "dark";
  html.setAttribute("data-theme", next);
  document.getElementById("theme").textContent = next === "dark" ? "Light tokens" : "Dark tokens";
}});
</script>
</body>
</html>
"""
    (HERE / "style-guide.html").write_text(html)
    print("wrote style-guide.html", len(html))


if __name__ == "__main__":
    main()
