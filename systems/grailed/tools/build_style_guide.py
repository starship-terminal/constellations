#!/usr/bin/env python3
"""Render systems/grailed/style-guide.html from tokens.json.

Reads the token file next to this package and writes one self-contained page.
Colours are the token values. Type falls back to Helvetica and Arial because
the Video files are not in this package.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKENS = ROOT / "tokens.json"
OUT = ROOT / "style-guide.html"


def flatten(node, prefix=""):
    rows = []
    if isinstance(node, dict) and "$value" in node:
        rows.append((prefix, node))
        return rows
    if isinstance(node, dict):
        for key, child in node.items():
            if key.startswith("$"):
                continue
            path = f"{prefix}.{key}" if prefix else key
            rows.extend(flatten(child, path))
    return rows


def resolve(value, tokens):
    seen = set()
    while isinstance(value, str) and value.startswith("{") and value.endswith("}"):
        path = value[1:-1]
        if path in seen:
            break
        seen.add(path)
        node = tokens
        for part in path.split("."):
            node = node[part]
        value = node["$value"]
    return value


def main() -> None:
    tokens = json.loads(TOKENS.read_text())
    swatches = []
    for path, token in flatten(tokens.get("core", {}).get("color", {}), "core.color"):
        value = resolve(token["$value"], tokens)
        swatches.append((path, value, token["$extensions"]["source"]))
    roles = []
    for group in ("surface", "text", "border", "action"):
        for path, token in flatten(tokens["light"][group], f"light.{group}"):
            roles.append((path, resolve(token["$value"], tokens)))

    def chip(name, value):
        ink = "#000000" if value.lower() in {"#ffffff", "#fafafa", "#f2f2f2", "#e0f1ec", "#e1e1e1"} or value.startswith("rgba") else "#ffffff"
        return (
            f'<div class="swatch"><div class="chip" style="background:{value};color:{ink}">{value}</div>'
            f"<div class=\"meta\"><strong>{name}</strong></div></div>"
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Grailed style guide</title>
<style>
  body {{ margin: 0; background: #ffffff; color: #000000; font-family: Helvetica, Arial, sans-serif; }}
  header, main {{ max-width: 960px; margin: 0 auto; padding: 32px 24px; }}
  h1 {{ font-size: 32px; font-weight: 600; letter-spacing: 0; margin: 0 0 8px; }}
  p {{ font-size: 14px; line-height: 1.4; max-width: 62ch; }}
  h2 {{ font-size: 16px; font-weight: 700; margin: 32px 0 12px; }}
  .row {{ display: flex; flex-wrap: wrap; gap: 12px; }}
  .swatch {{ width: 180px; }}
  .chip {{ height: 72px; border: 1px solid #e1e1e1; display: flex; align-items: flex-end; padding: 8px; font-size: 12px; font-family: ui-monospace, monospace; }}
  .meta {{ font-size: 12px; margin-top: 6px; }}
  .bar {{ background: #000000; color: #ffffff; padding: 8px 16px; font-size: 11px; font-weight: 700; letter-spacing: 0.44px; text-transform: uppercase; display: inline-block; }}
  .ghost {{ background: #ffffff; color: #000000; border: 1px solid #e1e1e1; padding: 8px 16px; font-size: 11px; font-weight: 700; letter-spacing: 0.44px; text-transform: uppercase; display: inline-block; }}
  .pill {{ background: #000000; color: #ffffff; border-radius: 32px; height: 48px; padding: 0 16px; display: inline-flex; align-items: center; font-size: 14px; letter-spacing: 0.28px; text-transform: uppercase; }}
  .ticker {{ height: 40px; display: flex; align-items: center; padding: 0 16px; color: #208368; font-size: 12px; font-weight: 700; letter-spacing: -0.24px; text-transform: uppercase; background: radial-gradient(50% 50%, #ffffff 18.27%, #e0f1ec 100%); }}
  .search {{ width: 280px; height: 40px; border: 1px solid #000000; border-radius: 2px; padding: 0 12px; font-size: 16px; font-family: Helvetica, Arial, sans-serif; }}
  .note {{ font-size: 12px; color: #737373; }}
</style>
</head>
<body>
<header>
  <h1>Grailed</h1>
  <p>Public shop, signed out, 2026-11-22. Light only. Video is not loaded here, so labels use Helvetica.</p>
</header>
<main>
  <h2>Colours</h2>
  <div class="row">{"".join(chip(n, v) for n, v, _ in swatches)}</div>
  <h2>Roles</h2>
  <div class="row">{"".join(chip(n, v) for n, v in roles)}</div>
  <h2>Controls</h2>
  <p class="ticker">Lower fees on sales under $120</p>
  <p><span class="bar">Log in</span> <span class="ghost">Sign up</span></p>
  <p><span class="pill">Log in with email</span></p>
  <p><input class="search" placeholder="Search for anything" aria-label="Search"></p>
  <p class="note">Search is shown empty. Nothing was typed on the live site.</p>
</main>
</body>
</html>
"""
    OUT.write_text(html)


if __name__ == "__main__":
    main()
