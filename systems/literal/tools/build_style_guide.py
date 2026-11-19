#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Light and dark. Deterministic."""
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


def colours(theme):
    rows = []
    for name, tok in flat(T[theme]):
        if tok.get("$type") != "color":
            continue
        val = tok["$value"]
        rows.append(
            f'<div class="sw"><i style="background:{val}"></i>'
            f"<div><code>{name}</code><span>{val}</span></div></div>"
        )
    return "\n".join(rows)


def type_rows():
    rows = []
    for name, tok in flat(T["core"]["typography"]):
        v = tok["$value"]
        family = "Libre Baskerville, Georgia, serif" if "serif" in v["fontFamily"] else "Inter, sans-serif"
        rows.append(
            f'<div class="ty" style="font:{v["fontWeight"]} {v["fontSize"]}/{v["lineHeight"]} {family}">'
            f'{name}<small>{v["fontSize"]} / {v["lineHeight"]} / {v["fontWeight"]} / {family.split(",")[0]}</small></div>'
        )
    return "\n".join(rows)


spaces = "".join(
    f'<div class="sp"><i style="width:{t["$value"]}"></i><code>{n}</code><span>{t["$value"]}</span></div>'
    for n, t in flat(T["core"]["spacing"])
)
radii = "".join(
    f'<div class="rd" style="border-radius:{t["$value"]}"><code>{n}</code><span>{t["$value"]}</span></div>'
    for n, t in flat(T["core"]["radius"])
)

motion = T["core"].get("motion", {})
motion_bits = []
for group in ("duration", "easing", "transition"):
    node = motion.get(group, {})
    if not isinstance(node, dict):
        continue
    for name, tok in flat(node):
        val = tok.get("$value")
        if isinstance(val, dict):
            val = " ".join(f"{k}:{v}" for k, v in val.items())
        motion_bits.append(f"<div class=\"sp\"><code>{group}.{name}</code><span>{val}</span></div>")
motion_rows = "\n".join(motion_bits) or "<p>No motion tokens.</p>"

light = T["light"]
dark = T["dark"]
L = {k: light["accent"][k]["$value"] for k in ("primary", "primaryHover", "primaryActive", "alert", "danger")}
page_l = light["ui"]["overlayBackground"]["$value"]
text_l = light["text"]["primary"]["$value"]
muted_l = light["text"]["discreet"]["$value"]
surface_l = light["ui"]["boxBackground"]["$value"]
line_l = light["ui"]["outline"]["$value"]
page_d = dark["ui"]["boxBackground"]["$value"]
text_d = dark["text"]["primary"]["$value"]
accent_d = dark["accent"]["primary"]["$value"]
line_d = dark["ui"]["outline"]["$value"]
surface_d = dark["ui"]["overlayBackground"]["$value"]

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Literal.club style guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Libre+Baskerville:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
  :root {{
    --page: {page_l};
    --text: {text_l};
    --muted: {muted_l};
    --line: {line_l};
    --surface: {surface_l};
    --accent: {L["primary"]};
    --accent-hover: {L["primaryHover"]};
    --ink: #000000;
  }}
  :root[data-theme="dark"] {{
    --page: {page_d};
    --text: {text_d};
    --muted: #acacac;
    --line: {line_d};
    --surface: {surface_d};
    --accent: {accent_d};
    --accent-hover: {L["primaryHover"]};
    --ink: #f9f9f9;
  }}
  * {{ box-sizing: border-box; }}
  body {{ margin: 0; background: var(--page); color: var(--text); font: 400 14px/20px Inter, sans-serif; }}
  header {{ display: flex; align-items: center; gap: 16px; padding: 16px 28px; border-bottom: 1px solid var(--line); position: sticky; top: 0; background: var(--page); }}
  header h1 {{ font: 400 20px/28px "Libre Baskerville", Georgia, serif; margin: 0; }}
  header button {{ margin-left: auto; border: 0; background: var(--accent); color: #fff; height: 40px; padding: 0 16px; font: 500 14px/20px Inter, sans-serif; cursor: pointer; }}
  :root[data-theme="dark"] header button {{ color: #000; }}
  main {{ padding: 28px; max-width: 1100px; }}
  h2 {{ font: 400 24px/36px "Libre Baskerville", Georgia, serif; margin: 36px 0 12px; }}
  p.note {{ color: var(--muted); max-width: 68ch; }}
  .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 10px; }}
  .sw {{ display: flex; gap: 10px; align-items: center; border: 1px solid var(--line); background: var(--surface); padding: 8px; }}
  .sw i {{ width: 36px; height: 36px; border: 1px solid var(--line); flex: none; }}
  .sw code, .sp code, .rd code {{ display: block; font: 500 12px/16px ui-monospace, monospace; }}
  .sw span, .sp span, .rd span, .ty small {{ color: var(--muted); font-size: 12px; }}
  .ty {{ padding: 8px 0; border-bottom: 1px solid var(--line); }}
  .ty small {{ display: block; font: 400 12px/16px Inter, sans-serif; }}
  .sp {{ display: flex; align-items: center; gap: 12px; margin: 4px 0; }}
  .sp i {{ height: 8px; background: var(--accent); }}
  .rd {{ width: 88px; height: 48px; border: 1px solid var(--line); display: inline-flex; align-items: center; justify-content: center; margin: 4px 8px 4px 0; }}
  .controls {{ display: flex; flex-wrap: wrap; gap: 12px; align-items: center; }}
  .btn {{ height: 48px; padding: 0 20px; border: 0; font: 500 14px/20px Inter, sans-serif; }}
  .btn.green {{ background: var(--accent); color: #fff; }}
  :root[data-theme="dark"] .btn.green {{ color: #000; }}
  .btn.ink {{ background: var(--ink); color: var(--page); }}
  .field {{ width: 280px; height: 50px; border: 0; background: var(--surface); color: var(--text); padding: 0 12px; font: 400 14px/20px Inter, sans-serif; }}
  .link {{ color: var(--muted); }}
</style>
</head>
<body>
<header>
  <h1>Literal</h1>
  <span>public signed-out tokens</span>
  <button type="button" id="theme">Dark</button>
</header>
<main>
  <p class="note">Values come from tokens.json, harvested from literal.club on 2026-11-18. Light is the default. Dark is the product's :root.dark set, resolved when prefers-color-scheme is dark. There is no public theme toggle. Corners on the measured controls are square.</p>
  <h2>Light colours</h2>
  <div class="grid">
{colours("light")}
  </div>
  <h2>Dark colours</h2>
  <div class="grid">
{colours("dark")}
  </div>
  <h2>Type</h2>
  {type_rows()}
  <h2>Spacing</h2>
  {spaces}
  <h2>Radius</h2>
  {radii}
  <h2>Motion</h2>
  <p class="note">The reduced-motion probe kept every measured transition. The product ignores prefers-reduced-motion on the public pages that were read.</p>
  {motion_rows}
  <h2>Controls</h2>
  <div class="controls">
    <button class="btn green" type="button">Join</button>
    <button class="btn ink" type="button">Want to read</button>
    <input class="field" placeholder="Email address" readonly>
    <a class="link" href="#theme">Forgot password?</a>
  </div>
</main>
<script>
  const root = document.documentElement;
  const btn = document.getElementById("theme");
  btn.addEventListener("click", () => {{
    const dark = root.getAttribute("data-theme") === "dark";
    root.setAttribute("data-theme", dark ? "light" : "dark");
    btn.textContent = dark ? "Dark" : "Light";
  }});
</script>
</body>
</html>
"""

(HERE / "style-guide.html").write_text(html)
print("wrote", HERE / "style-guide.html")
