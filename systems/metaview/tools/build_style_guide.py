#!/usr/bin/env python3
"""Render style-guide.html from tokens.json.

Every swatch is a CSS custom property generated from tokens.json. core and light
go on :root; dark goes on [data-mode="dark"]. The toggle sets data-mode on html.
Deterministic: same tokens, same bytes.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


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


def css_val(token):
    v, ty = token["$value"], token["$type"]
    if ty == "typography":
        return None
    if ty == "fontFamily":
        return ", ".join(f'"{p}"' if " " in p else p for p in v)
    if ty == "other":
        return None
    return alias(v)


def block(setname):
    lines = []
    for name, token in flat(T[setname]):
        val = css_val(token)
        if val is None:
            continue
        lines.append(f"  {cssname(name)}: {val};")
    return "\n".join(lines)


def swatches(setname, prefix):
    rows = []
    for name, token in flat(T[setname]):
        if token["$type"] != "color":
            continue
        if prefix and not name.startswith(prefix):
            continue
        var = cssname(name)
        rows.append(
            f'<div class="sw"><i style="background:var({var})"></i>'
            f'<div><div class="nm">{name}</div><div class="vl">{token["$value"]}</div></div></div>'
        )
    return "\n".join(rows)


def type_rows():
    rows = []
    for name, token in flat(T["core"]):
        if token["$type"] != "typography":
            continue
        v = token["$value"]
        sample = "Get the right butts in seats." if name.startswith("typography-h") else "Source, engage, and hire better."
        rows.append(
            f'<div class="typerow"><div class="k">{name}<small>{v["fontSize"]} / {v["lineHeight"]} / {v["fontWeight"]}</small></div>'
            f'<div class="sample" style="font-weight:{v["fontWeight"]};font-size:{v["fontSize"]};line-height:{v["lineHeight"]};letter-spacing:{v.get("letterSpacing","0")}">{sample}</div></div>'
        )
    return "\n".join(rows)


html = f"""<!doctype html>
<html lang="en" data-mode="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Metaview style guide</title>
<style>
:root {{
{block("core")}
{block("light")}
  color-scheme: light;
  --sg-sans: var(--font-family-sans);
  --sg-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}}
[data-mode="dark"] {{
{block("dark")}
  color-scheme: dark;
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--background-page); color: var(--text-primary); font: 400 16px/1.48 var(--sg-sans); }}
.wrap {{ max-width: 1120px; margin: 0 auto; padding: 32px 24px 80px; }}
header {{ display: flex; align-items: center; gap: 16px; margin-bottom: 28px; }}
h1 {{ font: 500 36px/1.04 var(--sg-sans); letter-spacing: -0.03em; margin: 0; }}
h2 {{ font: 500 22px/1.16 var(--sg-sans); letter-spacing: -0.02em; margin: 36px 0 12px; }}
p {{ max-width: 68ch; color: var(--text-faded); }}
button.toggle {{ margin-left: auto; border: 1px solid var(--border-stroke); background: var(--background-surface); color: var(--text-primary); border-radius: var(--radius-pill); padding: 8px 16px; font: 500 14px/1 var(--sg-sans); cursor: pointer; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 10px; }}
.sw {{ display: grid; grid-template-columns: 36px 1fr; gap: 10px; align-items: center; }}
.sw i {{ width: 36px; height: 36px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(1,5,27,.12); display: block; }}
.nm {{ font: 600 12px/1.3 var(--sg-mono); word-break: break-all; }}
.vl {{ font: 400 12px/1.3 var(--sg-mono); color: var(--text-faded); word-break: break-all; }}
.typerow {{ display: grid; grid-template-columns: 220px 1fr; gap: 16px; padding: 10px 0; border-bottom: 1px solid var(--border-divider); align-items: baseline; }}
.k {{ font: 600 12px/1.4 var(--sg-mono); }}
.k small {{ display: block; font-weight: 400; color: var(--text-faded); }}
.pills {{ display: flex; gap: 12px; flex-wrap: wrap; align-items: center; margin: 12px 0 24px; }}
.pill {{ display: inline-flex; align-items: center; height: 51px; padding: 0 24px; border-radius: var(--radius-pill); font: 500 16px/1 var(--sg-sans); text-decoration: none; }}
.pill.ink {{ background: var(--background-ink); color: var(--text-onInk); }}
.pill.line {{ background: var(--background-surface); color: var(--text-primary); border: 1px solid #000; }}
.bar {{ background: var(--background-ink); color: var(--text-onInk); padding: 11px 16px; border-radius: 0; }}
.field {{ width: 280px; height: 34px; border-radius: var(--radius-appControl); border: 1px solid var(--app-border); background: var(--app-surface); color: var(--app-text); padding: 0 8px; font: 400 13px/18px var(--font-family-inter); }}
.note {{ font-size: 13px; }}
</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>Metaview</h1>
  <button class="toggle" type="button" id="theme">App theme: light</button>
</header>
<p>Public marketing is one warm theme. The toggle swaps the signed-out app's light and dark sheets, which are the product's own <code>:root</code> and <code>:root[data-theme=dark]</code> values. Euclid Circular A and Inter are proprietary and are not loaded here, so type falls back to the system face.</p>
<h2>Marketing controls</h2>
<div class="pills">
  <span class="pill ink">Book a demo</span>
  <span class="pill line">Start for free</span>
  <span class="bar">Announcement bar</span>
</div>
<label class="note">Sign-in field<input class="field" placeholder="Work email"></label>
<h2>Type</h2>
{type_rows()}
<h2>Marketing colour</h2>
<div class="swatches">
{swatches("core", "color-marketing-")}
</div>
<h2>App colour, this theme</h2>
<div class="swatches">
{swatches("light", "color-")}
</div>
<h2>Roles</h2>
<div class="swatches">
{swatches("light", "background-")}
{swatches("light", "text-")}
{swatches("light", "accent-")}
{swatches("light", "border-")}
{swatches("light", "app-")}
</div>
</div>
<script>
const root = document.documentElement;
const btn = document.getElementById("theme");
btn.addEventListener("click", () => {{
  const next = root.getAttribute("data-mode") === "dark" ? "light" : "dark";
  root.setAttribute("data-mode", next);
  btn.textContent = "App theme: " + next;
}});
</script>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html", len(html))
