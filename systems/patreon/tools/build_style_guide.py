#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def walk(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict) and "$value" in value:
            yield path, value
        elif isinstance(value, dict):
            yield from walk(value, path)


rows = []
for group in ("core", "light", "dark"):
    for path, token in walk(T[group]):
        rows.append((group, path, token.get("$type", ""), json.dumps(token["$value"]), token["$extensions"].get("evidence", "")))

body = "\n".join(
    f"<tr><td>{g}</td><td><code>{p}</code></td><td>{t}</td><td><code>{v}</code></td><td>{e}</td></tr>"
    for g, p, t, v, e in rows
)
light = {path.split(".")[-1]: token["$value"] for path, token in walk(T["light"]) if token.get("$type") == "color"}
swatches = "".join(
    f'<div class="swatch"><i style="background:{v}"></i><span>{k}</span><code>{v}</code></div>'
    for k, v in light.items()
)
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Patreon style guide</title>
<style>
body {{ margin: 0; font: 14px/1.4 ui-sans-serif, system-ui, sans-serif; background: #f9f9f9; color: #111; }}
main {{ max-width: 980px; margin: 0 auto; padding: 32px 20px 64px; }}
h1 {{ font-weight: 500; letter-spacing: -0.03em; }}
.swatches {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
.swatch {{ background: #fff; border-radius: 12px; padding: 10px; }}
.swatch i {{ display: block; height: 48px; border-radius: 8px; border: 1px solid #00000017; }}
.swatch span, .swatch code {{ display: block; margin-top: 6px; }}
table {{ width: 100%; border-collapse: collapse; background: #fff; border-radius: 12px; overflow: hidden; }}
td, th {{ text-align: left; padding: 8px 10px; border-bottom: 1px solid #eee; vertical-align: top; font-size: 13px; }}
code {{ font-size: 12px; }}
.note {{ color: #333; max-width: 68ch; }}
</style>
</head>
<body>
<main>
<h1>Patreon public tokens</h1>
<p class="note">Rendered from tokens.json. Light swatches are the logged-out app studio tokens. The creator accent is the measured Join for free fill on one public membership page.</p>
<h2>Light roles</h2>
<div class="swatches">{swatches}</div>
<h2>Every token</h2>
<table>
<thead><tr><th>Set</th><th>Path</th><th>Type</th><th>Value</th><th>Evidence</th></tr></thead>
<tbody>
{body}
</tbody>
</table>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html", len(rows), "tokens")
