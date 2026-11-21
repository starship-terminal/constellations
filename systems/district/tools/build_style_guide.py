#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. Deterministic."""
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


rows = []
for path, tok in flat(T["light"]["color"]):
    val = tok["$value"]
    if isinstance(val, str) and val.startswith("{") and val.endswith("}"):
        paint = "var(--" + val[1:-1].replace(".", "-") + ")"
    else:
        paint = val
    rows.append(
        f"<tr><td><i style=\"background:{paint}\"></i></td>"
        f"<td>light.color.{path}</td><td>{val}</td></tr>"
    )

html = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>District style guide</title>
<style>
  body { margin: 0; font: 16px/24px sans-serif; background: #fff; color: #131316; }
  main { max-width: 880px; margin: 0 auto; padding: 32px 24px 64px; }
  h1 { font-size: 32px; line-height: 40px; }
  table { border-collapse: collapse; width: 100%; }
  td { border-bottom: 1px solid #f1f1f2; padding: 8px 12px; font-size: 14px; }
  i { display: inline-block; width: 28px; height: 28px; border-radius: 6px; border: 1px solid #f1f1f2; }
  .pill { display: inline-flex; align-items: center; height: 40px; padding: 0 16px; border-radius: 9999px; border: 1px solid #bfbfc4; font-weight: 600; }
  .primary { display: inline-flex; align-items: center; height: 48px; padding: 0 16px; border-radius: 12px; background: #6444e4; color: #fff; font-weight: 600; }
  .nav { color: #5815fd; font-weight: 600; border-bottom: 3px solid #5815fd; }
</style>
</head>
<body>
<main>
  <h1>District</h1>
  <p>Rendered from tokens.json. Public pages are light.</p>
  <p><span class="nav">For you</span> <span class="pill">Login</span> <span class="primary">Send message</span></p>
  <table>
""" + "\n".join(rows) + """
  </table>
</main>
</body>
</html>
"""
(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
