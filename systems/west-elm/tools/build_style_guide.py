#!/usr/bin/env python3
"""Render style-guide.html from tokens.json. No network, no invented colours."""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent
TOKENS = json.loads((HERE / "tokens.json").read_text())


def resolve(value, trail=()):
    if not isinstance(value, str) or not value.startswith("{") or not value.endswith("}"):
        return value
    path = value[1:-1]
    if path in trail:
        raise ValueError("alias cycle: " + path)
    node = TOKENS["core"]
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"], trail + (path,))


def color(path):
    return walk(path)


def walk(path):
    node = TOKENS
    for part in path.split("."):
        node = node[part]
    return resolve(node["$value"])


def swatch(name, path):
    value = walk(path)
    return (
        f'<div class="swatch"><i style="background:{value}"></i>'
        f"<b>{name}</b><code>{value}</code><small>{path}</small></div>"
    )


def row(label, sample, style):
    return f'<div class="type"><div style="{style}">{sample}</div><small>{label}</small></div>'


page = walk("light.background.page")
ink = walk("light.text.primary")
muted = walk("light.text.muted")
sunken = walk("light.background.sunken")
sale = walk("light.action.conversion")
promo = walk("light.background.promo")
sans = walk("core.fontFamily.sans")
serif = walk("core.fontFamily.serif")

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>West Elm style guide</title>
<style>
  :root {{
    --page: {page};
    --ink: {ink};
    --muted: {muted};
    --sunken: {sunken};
    --sale: {sale};
    --promo: {promo};
    --sans: {sans};
    --serif: {serif};
  }}
  body {{ margin: 0; background: var(--page); color: var(--ink); font-family: var(--sans); font-weight: 300; }}
  main {{ max-width: 880px; margin: 0 auto; padding: 40px 24px 80px; }}
  h1 {{ font-family: var(--serif); font-weight: 300; font-size: 48px; line-height: 60px; letter-spacing: 0.96px; margin: 0 0 8px; }}
  h2 {{ font-family: var(--serif); font-weight: 300; font-size: 28px; margin: 40px 0 12px; }}
  p.lede {{ color: var(--muted); font-size: 14px; letter-spacing: 0.42px; max-width: 46em; }}
  .swatches, .type-list {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 12px; }}
  .swatch {{ border: 1px solid #d9d9d9; padding: 8px; }}
  .swatch i {{ display: block; height: 48px; border: 1px solid #d9d9d9; }}
  .swatch b, .swatch code, .swatch small, .type small {{ display: block; font-size: 12px; letter-spacing: 0.36px; }}
  .swatch code {{ color: var(--muted); }}
  .promo {{ background: var(--promo); color: #fff; font-size: 10px; letter-spacing: 1px; text-transform: uppercase; padding: 16px 20px; font-weight: 375; }}
  .bar {{ background: var(--sunken); font-size: 12px; padding: 8px 20px; }}
  .nav {{ border-top: 1px solid #d9d9d9; font-size: 10px; letter-spacing: 0.4px; text-transform: uppercase; padding: 12px 0; }}
  .cta, .atc, .ghost {{ display: inline-block; border-radius: 0; font-size: 14px; letter-spacing: 1.4px; text-transform: uppercase; text-decoration: none; }}
  .cta {{ background: #fff; color: var(--ink); border: 1px solid #fff; padding: 12px 24px; font-weight: 375; }}
  .hero-demo {{ background: #8a847c; padding: 48px 32px; margin: 12px 0; }}
  .atc {{ background: var(--sale); color: #fff; border: 1px solid var(--sale); padding: 16px 8px; min-width: 280px; text-align: center; font-weight: 300; }}
  .ghost {{ background: transparent; color: var(--ink); padding: 12px 0; }}
  .field {{ border: 1px solid var(--ink); height: 56px; padding: 0 16px; width: 280px; font: inherit; font-size: 16px; border-radius: 0; }}
  .row {{ display: flex; gap: 16px; align-items: center; flex-wrap: wrap; margin: 12px 0; }}
  .price {{ color: var(--sale); font-size: 24px; letter-spacing: 0.72px; }}
  .was {{ text-decoration: line-through; font-size: 16px; margin-left: 8px; }}
  .note {{ font-size: 12px; color: var(--muted); letter-spacing: 0.36px; }}
</style>
</head>
<body>
<main>
  <h1>West Elm</h1>
  <p class="lede">Public signed-out surfaces, measured 2026-11-19. One light theme. Square corners, Sanomat headlines, GT Eesti Text for everything else, conversion red only on the sale price and Add to cart.</p>
  <div class="promo">Up to 60% off &nbsp; Shop early black friday deals</div>
  <div class="bar">west elm · west elm office · west elm kids</div>
  <div class="nav">New &nbsp; Furniture &nbsp; Outdoor &nbsp; Bedding &nbsp; Sale</div>
  <div class="hero-demo">
    <div style="font-family:var(--serif);font-size:48px;line-height:60px;letter-spacing:0.96px;font-weight:300;color:#fff">The Winter Edit</div>
    <p style="color:#fff;font-size:18px;letter-spacing:0.54px">New furniture, tabletop and more.</p>
    <a class="cta">Shop new arrivals</a>
  </div>

  <h2>Colour</h2>
  <div class="swatches">
    {swatch("page", "light.background.page")}
    {swatch("sunken", "light.background.sunken")}
    {swatch("text", "light.text.primary")}
    {swatch("muted", "light.text.muted")}
    {swatch("sale", "light.action.conversion")}
    {swatch("promo", "light.background.promo")}
    {swatch("border", "light.border.default")}
    {swatch("focus", "light.focus.ring")}
  </div>

  <h2>Type</h2>
  <div class="type-list">
    {row("hero 48 / 60 Sanomat", "The Winter Edit", "font-family:var(--serif);font-size:48px;line-height:60px;letter-spacing:0.96px;font-weight:300")}
    {row("product title 32 / 40", "Hyde Dining Chair", "font-family:var(--serif);font-size:32px;line-height:40px;letter-spacing:0.64px;font-weight:300")}
    {row("product name 16", "Locke Perforated Metal Buffet", "font-size:16px;line-height:20.8px;letter-spacing:0.48px")}
    {row("nav 10 uppercase", "FURNITURE", "font-size:10px;letter-spacing:0.4px;text-transform:uppercase;line-height:40px")}
    {row("button 14 / 1.4px", "CONTINUE WITH EMAIL", "font-size:14px;letter-spacing:1.4px;text-transform:uppercase")}
  </div>
  <p class="note">GT Eesti Text and Sanomat are West Elm's own files. This page falls back to Helvetica and Georgia.</p>

  <h2>Controls</h2>
  <div class="row"><button class="atc">Add to cart</button><span class="price">$279.20<span class="was">$299</span></span></div>
  <div class="row"><input class="field" placeholder="Enter email" aria-label="Enter email"><button class="atc" style="background:#212121;border-color:#212121;min-width:0;padding:12px 16px">Continue</button></div>
  <p class="note">Add to cart is #af1a31. Other filled buttons are ink #212121. Radius is 0, except the quantity stepper's 2px outer corners.</p>
</main>
</body>
</html>
"""

(HERE / "style-guide.html").write_text(html)
print("wrote style-guide.html")
