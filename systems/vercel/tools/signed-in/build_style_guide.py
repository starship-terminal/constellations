#!/usr/bin/env python3
"""Render style-guide.html from tokens.json and the retained screenshots.

Dark only. The dashboard offered system, light and dark, and this capture
did not switch the account theme. ADAPTED_FOR is vercel.
"""
import html
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ADAPTED_FOR = "vercel"


def leaves(node, prefix=""):
    for key, value in node.items():
        if key.startswith("$"):
            continue
        if isinstance(value, dict) and "$value" in value:
            yield prefix + key, value
        elif isinstance(value, dict):
            yield from leaves(value, prefix + key + ".")


def build():
    tokens = json.loads((HERE / "tokens.json").read_text())
    rows = []
    for name, token in leaves(tokens):
        shown = json.dumps(token["$value"]) if not isinstance(token["$value"], str) else token["$value"]
        swatch = ""
        if token["$type"] == "color" and not shown.startswith("oklch") and not shown.startswith("lab"):
            swatch = f'<i style="background:{html.escape(shown, quote=True)}"></i>'
        rows.append(
            "<tr><td><code>%s</code></td><td>%s%s</td><td>%s</td></tr>"
            % (
                html.escape(name),
                swatch,
                html.escape(shown),
                html.escape(token["$extensions"]["source"]),
            )
        )
    dark = tokens["dark"]
    palette = {
        "page": dark["bg"]["page"]["$value"],
        "surface": dark["bg"]["surface"]["$value"],
        "text": dark["text"]["primary"]["$value"],
        "muted": dark["text"]["secondary"]["$value"],
        "accent": dark["accent"]["default"]["$value"],
        "border": dark["border"]["default"]["$value"],
        "onaccent": dark["component"]["button"]["primary"]["text"]["$value"],
        "button": dark["component"]["button"]["primary"]["bg"]["$value"],
    }
    button = dark["component"]["button"]["primary"]
    specimen = (
        '<button type="button" style="background:%s;color:%s;border-radius:%s;height:%s;border:0;padding:0 10px;font:500 14px/20px Geist,sans-serif">Save</button>'
        % (button["bg"]["$value"], button["text"]["$value"], button["radius"]["$value"], button["height"]["$value"])
    )
    gallery = "".join(
        '<figure><a href="screenshots/%s"><img loading="lazy" src="screenshots/%s" alt="%s"></a><figcaption>%s</figcaption></figure>'
        % (p.name, p.name, html.escape(p.stem), html.escape(p.stem))
        for p in sorted((HERE / "screenshots").glob("*.png"))
    )
    doc = """<!doctype html>
<html lang="en" data-mode="dark">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vercel measured style guide</title>
<style>
:root { --page: @@PAGE@@; --surface: @@SURFACE@@; --text: @@TEXT@@; --muted: @@MUTED@@; --accent: @@ACCENT@@; --border: @@BORDER@@; --button: @@BUTTON@@; --onaccent: @@ONACCENT@@; }
body { margin: 32px; background: var(--page); color: var(--text); font: 400 14px/20px Geist, ui-sans-serif, system-ui, sans-serif; }
a { color: var(--accent); }
table { width: 100%; border-collapse: collapse; font-size: 13px; }
td { padding: 10px 12px; border-bottom: 1px solid var(--border); vertical-align: top; overflow-wrap: anywhere; }
i { display: inline-block; width: 28px; height: 18px; margin-right: 8px; vertical-align: middle; box-shadow: inset 0 0 0 1px var(--border); }
.gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 16px; }
figure { margin: 0; background: var(--surface); padding: 8px; }
img { width: 100%; max-height: 420px; object-fit: contain; object-position: top; }
figcaption { font-size: 12px; color: var(--muted); }
p.note { color: var(--muted); max-width: 72ch; }
</style>
<h1>Vercel</h1>
<p class="note">Signed-in dashboard, dark theme, measured 2026-11-21. Light was offered and not switched. This page renders tokens. The screenshots are the product.</p>
<h2>Primary button</h2>
<p class="note">Save, measured on Team Settings. Label is the control's own word.</p>
@@SPECIMEN@@
<h2>Tokens</h2>
<table>@@ROWS@@</table>
<h2>Screenshots</h2>
<div class="gallery">@@GALLERY@@</div>
</html>
"""
    parts = {
        "PAGE": palette["page"],
        "SURFACE": palette["surface"],
        "TEXT": palette["text"],
        "MUTED": palette["muted"],
        "ACCENT": palette["accent"],
        "BORDER": palette["border"],
        "BUTTON": palette["button"],
        "ONACCENT": palette["onaccent"],
        "SPECIMEN": specimen,
        "ROWS": "".join(rows),
        "GALLERY": gallery,
    }
    (HERE / "style-guide.html").write_text(re.sub(r"@@([A-Z]+)@@", lambda m: parts[m.group(1)], doc))
    print("wrote", HERE / "style-guide.html", "adapted for", ADAPTED_FOR)


if __name__ == "__main__":
    build()
