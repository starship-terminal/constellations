#!/usr/bin/env python3
"""Write style-guide.html from tokens.json. Light only: the live pages stay light."""
import html
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
T = json.loads((HERE / "tokens.json").read_text())


def swatch(name, value):
    return (
        f'<div class="sw"><i style="background:{html.escape(value)}"></i>'
        f"<b>{html.escape(name)}</b><code>{html.escape(value)}</code></div>"
    )


def colors(node, prefix=""):
    bits = []
    for key, value in node.items():
        if key.startswith("$"):
            continue
        path = f"{prefix}{key}"
        if isinstance(value, dict) and value.get("$type") == "color":
            bits.append(swatch(path, str(value["$value"])))
        elif isinstance(value, dict) and "$value" not in value:
            bits.append(colors(value, path + "."))
    return "".join(bits)


type_rows = []
for name, token in T["core"]["typography"].items():
    v = token["$value"]
    type_rows.append(
        "<tr><td>{name}</td><td style=\"font-family:{fam};font-size:{size};font-weight:{w};"
        "line-height:{lh};letter-spacing:{ls}\">{sample}</td><td><code>{size} / {w}</code></td></tr>".format(
            name=html.escape(name),
            fam=html.escape(v["fontFamily"]),
            size=html.escape(str(v["fontSize"])),
            w=html.escape(str(v["fontWeight"])),
            lh=html.escape(str(v.get("lineHeight", "normal"))),
            ls=html.escape(str(v.get("letterSpacing", "normal"))),
            sample="Make a stunning site.",
        )
    )

page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Pop Site style guide</title>
<style>
  :root {{
    --page: {T["light"]["page"]["$value"]};
    --text: {T["light"]["text"]["$value"]};
    --muted: {T["light"]["muted"]["$value"]};
    --accent: {T["light"]["accent"]["$value"]};
    --border: {T["light"]["border"]["$value"]};
    --field: {T["light"]["field"]["$value"]};
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 500 15px/1.4 Satoshi, ui-sans-serif, system-ui, sans-serif; }}
  main {{ max-width: 1000px; margin: 0 auto; padding: 48px 24px 80px; }}
  h1 {{ font-size: 51px; line-height: 51px; letter-spacing: -3.82px; font-weight: 500; margin: 0 0 8px; }}
  h2 {{ font-size: 19px; letter-spacing: -0.57px; margin: 40px 0 12px; }}
  p {{ color: var(--muted); }}
  .swatches {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .sw {{ width: 140px; }}
  .sw i {{ display: block; height: 56px; border-radius: 10px; border: 1px solid #e3e3e3; }}
  .sw b, .sw code {{ display: block; font-size: 12px; font-weight: 500; }}
  .sw code {{ color: var(--muted); }}
  table {{ border-collapse: collapse; width: 100%; }}
  td {{ border-bottom: 1px solid #e3e3e3; padding: 10px 8px; vertical-align: middle; }}
  .claim {{ display: inline-flex; align-items: center; height: 40px; padding: 0 24px; border-radius: 26px; color: #fff; background: linear-gradient(110deg, #00a8f5, #3b82f6); }}
  .signin {{ display: inline-flex; align-items: center; height: 36px; padding: 0 16px; border-radius: 999px; color: #fff; background: linear-gradient(90.54deg, #1e293b 6.97%, #0f172a 93.03%); }}
  .field {{ display: inline-flex; height: 40px; border-radius: 999px; overflow: hidden; background: #fff; border: 1px solid #e3e3e3; }}
  .field span {{ padding: 10px 16px; color: #6e6e73; }}
  .field b {{ background: #fafafc; padding: 10px 16px; border-radius: 0 999px 999px 0; }}
</style>
</head>
<body>
<main>
  <h1>Pop Site</h1>
  <p>Measured from pop.site and the signed-out screen at app.pop.site. Light only.</p>
  <h2>Colour</h2>
  <div class="swatches">{colors(T["light"])}{colors(T["core"]["color"]["marketing"], "marketing.")}</div>
  <h2>Type</h2>
  <table>{"".join(type_rows)}</table>
  <h2>Controls</h2>
  <p><span class="claim">Claim your site</span></p>
  <p><span class="field"><span>yourname</span><b>.pop.site</b></span></p>
  <p><span class="signin">Sign in</span></p>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(page)
print("style-guide.html", len(page))
