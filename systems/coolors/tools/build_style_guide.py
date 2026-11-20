#!/usr/bin/env python3
"""Render style-guide.html from tokens.json for the Coolors block record.

The tokens are computed-style readings from coolors.co taken in the signed-in
preview tab (the headless probe met a Cloudflare challenge); the guide says
which evidence it shows. Deterministic.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def flat(node, prefix=""):
    for k, v in node.items():
        if str(k).startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + k, v
        elif isinstance(v, dict):
            yield from flat(v, prefix + k + ".")


def cssname(path):
    return "--" + path.replace(".", "-")


rows = []
for setname in ("core", "light"):
    for path, token in flat(T[setname]):
        value = token["$value"]
        source = token.get("$extensions", {}).get("source", "")
        rows.append((setname + "." + path, value, token["$type"], source))

swatches = "\n".join(
    f'<div class="sw"><i style="background:var({cssname(p)})"></i><div><code>{p}</code><small>{v}</small><p>{s}</p></div></div>'
    for p, v, ty, s in rows if ty == "color"
)

# Resolve aliases simply: light tokens that alias {color.unmeasured} point at the core colour.
resolved = {}
for path, token in list(flat(T["core"])) + list(flat(T["light"])):
    resolved[path] = token

def resolve(value, seen=()):
    if isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        key = value[1:-1]
        if key in seen:
            raise SystemExit("alias cycle: " + key)
        return resolve(resolved[key]["$value"], seen + (key,))
    return value

var_lines = []
for setname in ("core", "light"):
    for path, token in flat(T[setname]):
        if token["$type"] != "color":
            continue
        # core paths are already unprefixed in flat(); keep a stable custom property.
        name = setname + "." + path
        var_lines.append(f"  {cssname(name)}: {resolve(token['$value'])};")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coolors style guide</title>
<style>
:root {{
{chr(10).join(var_lines)}
  color-scheme: light;
  --ink: var(--light-text);
  --page: var(--light-page);
  --line: var(--light-border);
}}
* {{ box-sizing: border-box; }}
body {{ margin: 0; background: var(--page); color: var(--ink); font: 16px/1.45 system-ui, sans-serif; }}
main {{ max-width: 880px; margin: 0 auto; padding: 32px 20px 64px; }}
h1 {{ font-size: 28px; margin: 0 0 8px; }}
p {{ max-width: 68ch; }}
.note {{ border: 1px solid var(--line); padding: 12px 16px; }}
.swatches {{ display: grid; gap: 16px; margin-top: 24px; }}
.sw {{ display: grid; grid-template-columns: 56px 1fr; gap: 12px; align-items: start; }}
.sw i {{ display: block; width: 56px; height: 56px; border: 1px solid var(--line); }}
code {{ font-family: ui-monospace, monospace; font-size: 13px; }}
small, .sw p {{ display: block; color: var(--light-muted); font-size: 13px; margin: 4px 0 0; }}
</style>
</head>
<body>
<main>
  <h1>Coolors</h1>
  <p class="note">This page renders tokens.json: colours read with getComputedStyle on coolors.co in the signed-in preview tab (each token's source names the element and page). The headless Playwright probe got a Cloudflare managed challenge (HTTP 403, title Just a moment...) and measured nothing, so no value here comes from it.</p>
  <div class="swatches">
    {swatches}
  </div>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("style-guide.html:", len(html.encode()), "bytes")
