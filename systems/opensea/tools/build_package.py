#!/usr/bin/env python3
"""Write tokens.json, style-guide.html, and the reconstruction PNGs for OpenSea.

Every colour comes from raw/css-vars.json (the probe-resolved --color-* pairs).
Every component size comes from raw/components-computed.json. The PNGs are
reconstructions: preview_snapshot returned "The browser is not producing
screenshot frames", so no live pixels are in this package.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "css-vars.json").read_text())
COMP = json.loads((ROOT / "raw" / "components-computed.json").read_text())

SOURCE = "Measured. :root, .dark and .light in 42m_qrqpbfsj8.css, probe-resolved on opensea.io 2026-11-19."
MEASURED = "Measured. getComputedStyle on a signed-out element, opensea.io, dark, 2026-11-19."


def color(value: str, source: str = SOURCE) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value: str, source: str = MEASURED) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def text(value: str, source: str) -> dict:
    return {"$type": "fontWeight", "$value": value, "$extensions": {"source": source}}


def shadow(value: str, source: str) -> dict:
    return {"$type": "shadow", "$value": value, "$extensions": {"source": source}}


def other(value, source: str) -> dict:
    return {"$value": value, "$extensions": {"source": source}}


def _type(family: str, size: str, weight: str, line: str, tracking: str, source: str) -> dict:
    """One composite token. catalog.py reads fontFamily, fontSize, fontWeight, lineHeight, letterSpacing off $value."""
    return {
        "$type": "typography",
        "$value": {
            "fontFamily": family,
            "fontSize": size,
            "fontWeight": weight,
            "lineHeight": line,
            "letterSpacing": tracking,
        },
        "$extensions": {"source": source},
    }


def pair(name: str) -> tuple[str, str]:
    row = RAW["colors"][name]
    return row["light"], row["dark"]


def semantic(theme: str) -> dict:
    c = RAW["colors"]

    def pick(name: str) -> str:
        return c[name][theme]

    return {
        "page": color(pick("bg-app")),
        "surface": color(pick("bg-primary")),
        "text": color(pick("text-primary")),
        "muted": color(pick("text-secondary")),
        "accent": color(pick("blue-3")),
        "border": color(pick("border-1")),
        "background": {
            "app": color(pick("bg-app")),
            "primary": color(pick("bg-primary")),
            "secondary": color(pick("bg-secondary")),
            "additional-1": color(pick("bg-additional-1")),
            "additional-2": color(pick("bg-additional-2")),
            "additional-3": color(pick("bg-additional-3")),
            "contrast-1": color(pick("bg-contrast-1")),
            "contrast-2": color(pick("bg-contrast-2")),
        },
        "foreground": {
            "primary": color(pick("text-primary")),
            "secondary": color(pick("text-secondary")),
            "tertiary": color(pick("text-tertiary")),
            "link": color(pick("link")),
            "link-hover": color(pick("link-hover")),
        },
        "line": {
            "1": color(pick("border-1")),
            "2": color(pick("border-2")),
            "3": color(pick("border-3")),
        },
        "status": {
            "success": color(pick("success-1")),
            "success-2": color(pick("success-2")),
            "warning": color(pick("warning")),
            "caution": color(pick("caution")),
            "error": color(pick("error-1")),
            "error-2": color(pick("error-2")),
        },
        "rarity": {
            "legendary": color(pick("legendary")),
            "epic": color(pick("epic")),
            "rare": color(pick("rare")),
            "common": color(pick("common")),
        },
        "brand": {
            "blue-1": color(pick("blue-1")),
            "blue-2": color(pick("blue-2")),
            "blue-3": color(pick("blue-3")),
            "blue-4": color(pick("blue-4")),
            "blue-5": color(pick("blue-5")),
            "pink-1": color(pick("pink-1")),
            "purple-1": color(pick("purple-1")),
            "purple-2": color(pick("purple-2")),
        },
        "overlay": color(c["overlay"][theme], SOURCE + " Declared as rgb(var(--color-black) / percent)."),
        "component": {
            "button": {
                "primary": {
                    "bg": color(pick("blue-3"), MEASURED + " Phone Sign in and Buy Now use --color-blue-3."),
                    "text": color("#ffffff", MEASURED + " Phone Sign in and Buy Now."),
                    "radius": dim("9999px", MEASURED + " Nav and Sign in computed border-radius was 1.67772e7px, the pill keyword."),
                    "height": dim("32px", MEASURED + " Sign in button."),
                },
                "nav": {
                    "bg": color(pick("bg-additional-1"), MEASURED + " Selected Home pill."),
                    "text": color(pick("text-primary"), MEASURED + " Nav label."),
                    "radius": dim("9999px"),
                    "height": dim("32px"),
                },
                "filter": {
                    "bg": color(pick("bg-primary"), MEASURED + " Resting Listed pill."),
                    "text": color(pick("text-secondary"), MEASURED + " Resting filter label."),
                    "radius": dim("9999px"),
                    "height": dim("28px", MEASURED + " Collection status pills."),
                },
                "oauth": {
                    "bg": color(pick("bg-primary"), MEASURED + " Continue with Google at rest."),
                    "text": color(pick("text-primary")),
                    "radius": dim("12px", MEASURED + " Connect dialog OAuth buttons."),
                    "height": dim("48px"),
                },
            },
            "field": {
                "bg": color(pick("bg-primary"), MEASURED + " Search wrap and email wrap."),
                "text": color(pick("text-primary")),
                "radius": dim("12px", MEASURED + " Email field in the connect dialog. Search is a pill."),
                "height": dim("56px", MEASURED + " Email wrap."),
            },
            "dialog": {
                "bg": color(pick("bg-app"), MEASURED + " Connect with OpenSea dialog."),
                "text": color(pick("text-primary")),
                "radius": dim("12px"),
            },
            "menu": {
                "bg": color(pick("bg-primary"), MEASURED + " More menu."),
                "text": color(pick("text-primary")),
                "radius": dim("12px"),
            },
            "card": {
                "bg": color(pick("bg-additional-1"), MEASURED + " Item media well."),
                "radius": dim("8px", MEASURED + " Item card shell."),
            },
        },
    }


def tokens() -> dict:
    sans = RAW["fonts"]["sans"]
    mono = RAW["fonts"]["mono"]
    return {
        "core": {
            "font": {
                "sans": font(sans, "Measured. computed font-family on body, and --font-family-sans on .x9T2SG_variable."),
                "mono": font(mono, "Measured. computed font-family on FLOOR PRICE, and --font-family-mono on .K3wO1q_variable."),
            },
            "typography": {
                "hero": _type("gtAmerica", "60px", "500", "63px", "-1.5px", MEASURED + " /tools h1 'Equip your AI agents'."),
                "title": _type("gtAmerica", "32px", "500", "48px", "0px", MEASURED + " Collection name span, CryptoPunks."),
                "dialog-title": _type("gtAmerica", "24px", "500", "30px", "0px", MEASURED + " Connect with OpenSea h4, and Drops h1."),
                "body": _type("gtAmerica", "16px", "400", "24px", "0px", MEASURED + " Body, terms paragraphs, nav root."),
                "label": _type("gtAmerica", "14px", "500", "21px", "0px", MEASURED + " Nav pills and Sign in."),
                "stat": _type("gtAmericaMono", "12px", "400", "15px", "0px", MEASURED + " FLOOR PRICE label."),
            },
            "radius": {
                "none": dim("0px", MEASURED + " Item media and Buy Now."),
                "avatar": dim("4px", MEASURED + " Collection avatar img."),
                "menu-item": dim("8px", MEASURED + " More menu row."),
                "card": dim("8px", MEASURED + " Item card shell."),
                "control": dim("12px", MEASURED + " Dialog, menu, OAuth button, email field, wallet list."),
                "help-search": dim("19px", MEASURED + " support.opensea.io search. A separate skin."),
                "help-card": dim("20px", MEASURED + " support.opensea.io category card."),
                "pill": dim("9999px", MEASURED + " Computed 1.67772e7px on nav pills, filters, Sign in, close."),
            },
            "spacing": {
                "4": dim("4px", MEASURED + " Menu padding, Get the app gap, close padding."),
                "6": dim("6px", MEASURED + " Banner vertical padding, nav icon gap."),
                "8": dim("8px", MEASURED + " Menu item padding-left, chain pill padding-right."),
                "12": dim("12px", MEASURED + " Banner gap, field horizontal padding, OAuth gap."),
                "16": dim("16px", MEASURED + " Sign in horizontal padding, wallet row padding."),
                "24": dim("24px", MEASURED + " Logo left offset and category row left offset at 1440."),
                "32": dim("32px", MEASURED + " Footer and nav control height."),
                "48": dim("48px", MEASURED + " Promo banner height."),
                "64": dim("64px", MEASURED + " Desktop nav height."),
            },
            "size": {
                "nav": dim("64px"),
                "banner": dim("48px"),
                "control": dim("32px"),
                "filter": dim("28px"),
                "oauth": dim("48px"),
                "field": dim("56px"),
                "dialog": dim("480px", MEASURED + " Connect dialog width."),
                "logo": dim("30px"),
            },
            "motion": {
                "duration": {
                    "nav": other("200ms", MEASURED + " Nav pill transitionDuration 0.2s."),
                    "search": other("200ms", MEASURED + " Search wrap transitionDuration 0.2s."),
                },
                "easing": {
                    "ease-out": other("ease-out", MEASURED + " Nav pill transitionTimingFunction."),
                    "standard": other("cubic-bezier(0.4, 0, 0.2, 1)", MEASURED + " Search wrap."),
                },
            },
            "color": {
                "focus": color("#99c8ff", MEASURED + " Email input focused outline color."),
                "white": color("#ffffff"),
                "black": color("#000000"),
            },
        },
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [
            {
                "id": "dark",
                "name": "Dark",
                "selectedTokenSets": {"core": "source", "dark": "enabled"},
                "$description": "The live theme. html had class dark and color-scheme dark. Home, collection, activity, discover, drops, tools and terms were measured in this theme.",
            },
            {
                "id": "light",
                "name": "Light",
                "selectedTokenSets": {"core": "source", "light": "enabled"},
                "$description": "Declared on .light in the same stylesheet. Resolved on a probe. The signed-out pages did not offer a theme switch, and settings/customize bounced to the connect dialog, so light was not seen live.",
            },
        ],
        "$metadata": {
            "tokenSetOrder": ["core", "light", "dark"],
        },
    }


def write_tokens() -> None:
    path = ROOT / "tokens.json"
    path.write_text(json.dumps(tokens(), indent=2) + "\n")
    print(f"wrote {path}")


def style_guide() -> str:
    return """<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<title>OpenSea style guide</title>
<style>
:root, [data-mode="dark"] {
  color-scheme: dark;
  --page: #080808; --surface: #0c0c0c; --ink: #ffffff; --muted: #acacac;
  --line: #202020; --line-2: #2c2c2c; --accent: #0086ff; --selected: #161616;
  --up: #47bb64; --down: #e24756; --link: #83c3ff;
}
[data-mode="light"] {
  color-scheme: light;
  --page: #fafafa; --surface: #ffffff; --ink: #171717; --muted: #666666;
  --line: #ebebeb; --line-2: #dcdcdc; --accent: #0086ff; --selected: #f2f2f2;
  --up: #28a948; --down: #ea3943; --link: #0086ff;
}
body { margin: 0; background: var(--page); color: var(--ink); font: 16px/24px ui-sans-serif, system-ui, sans-serif; }
main { max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }
h1 { font-size: 32px; line-height: 48px; font-weight: 500; margin: 0 0 8px; }
h2 { font-size: 24px; line-height: 30px; font-weight: 500; margin: 40px 0 12px; }
p.note { color: var(--muted); max-width: 68ch; }
.hero { font-size: 60px; line-height: 63px; font-weight: 500; letter-spacing: -1.5px; margin: 12px 0; }
.row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
button, .pill { font: 14px/21px inherit; font-weight: 500; border-radius: 9999px; height: 32px; padding: 0 16px; }
button.primary { background: var(--accent); color: #fff; border: 0; }
button.nav { background: var(--selected); color: var(--ink); border: 0; }
button.ghost { background: transparent; color: var(--ink); border: 0; }
button.filter { height: 28px; background: var(--surface); color: var(--muted); border: 1px solid var(--line); font-weight: 400; }
button.filter.on { background: var(--selected); color: var(--ink); border-color: var(--line-2); font-weight: 500; }
button.oauth { height: 48px; border-radius: 12px; background: var(--surface); color: var(--ink); border: 1px solid var(--line); padding: 0 12px; }
.field { height: 56px; border-radius: 12px; background: var(--surface); border: 1px solid var(--line); color: var(--muted); display: flex; align-items: center; padding: 0 12px; width: 280px; }
.dialog { width: 320px; background: var(--page); border: 1px solid var(--line); border-radius: 12px; padding: 16px; }
.swatch { width: 160px; }
.swatch i { display: block; height: 48px; border-radius: 8px; border: 1px solid var(--line); }
code, .stat { font-family: ui-monospace, SFMono-Regular, Menlo, monospace; font-size: 12px; }
.up { color: var(--up); } .down { color: var(--down); } a { color: var(--link); }
.toggle { float: right; }
table { border-collapse: collapse; width: 100%; }
td { border-top: 1px solid var(--line); padding: 6px 8px; vertical-align: top; font-size: 14px; }
</style>
</head>
<body>
<main>
<button class="primary toggle" id="theme" type="button">Light</button>
<h1>OpenSea</h1>
<p class="note">Rendered from the measured tokens. gtAmerica is proprietary and is not embedded, so this page uses the system sans. The live signed-out site was dark. Light colours are the declared .light pair, resolved on a probe, not a live theme switch.</p>
<p class="hero">Equip your AI agents</p>
<div class="row">
  <button class="primary" type="button">Sign in</button>
  <button class="nav" type="button">Home</button>
  <button class="ghost" type="button">Explore</button>
  <button class="filter on" type="button">All</button>
  <button class="filter" type="button">Listed</button>
</div>
<h2>Connect</h2>
<div class="dialog">
  <h2>Connect with OpenSea</h2>
  <p class="note">Email</p>
  <div class="field">Continue with email</div>
  <p></p>
  <div class="row">
    <button class="oauth" type="button">Continue with Google</button>
  </div>
  <p class="note">or continue with an external wallet</p>
</div>
<h2>Type</h2>
<p>Collection titles are 32px / 48px, weight 500. Stats are mono 12px / 15px. A move up is <span class="up">+68.6%</span> and a move down is <span class="down">-22.1%</span>. A terms link is <a href="#colours">this blue</a>.</p>
<h2 id="colours">Dark colours</h2>
<div class="row" id="swatches"></div>
<h2>Radii</h2>
<table>
<tr><td>Pill</td><td>9999px</td><td>Nav, filters, Sign in, close</td></tr>
<tr><td>Control</td><td>12px</td><td>Dialog, menu, OAuth, email field</td></tr>
<tr><td>Card</td><td>8px</td><td>Item card shell and menu row</td></tr>
<tr><td>Avatar</td><td>4px</td><td>Collection avatar</td></tr>
<tr><td>None</td><td>0</td><td>Item media, Buy Now</td></tr>
</table>
</main>
<script>
const dark = [
  ["page", "#080808"], ["surface", "#0c0c0c"], ["selected", "#161616"],
  ["text", "#ffffff"], ["muted", "#acacac"], ["border", "#202020"],
  ["accent", "#0086ff"], ["link", "#83c3ff"], ["up", "#47bb64"], ["down", "#e24756"]
];
const box = document.getElementById("swatches");
for (const [name, hex] of dark) {
  const d = document.createElement("div");
  d.className = "swatch";
  d.innerHTML = "<i style='background:" + hex + "'></i><code>" + name + "</code> <span>" + hex + "</span>";
  box.appendChild(d);
}
document.getElementById("theme").addEventListener("click", () => {
  const html = document.documentElement;
  const next = html.getAttribute("data-mode") === "dark" ? "light" : "dark";
  html.setAttribute("data-mode", next);
  document.getElementById("theme").textContent = next === "dark" ? "Light" : "Dark";
});
</script>
</body>
</html>
"""


def write_guide() -> None:
    path = ROOT / "style-guide.html"
    path.write_text(style_guide())
    print(f"wrote {path}")


def write_pngs() -> None:
    """Reconstruction boards. Not live screenshots."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow missing; reconstruction PNGs skipped")
        return

    def font(size):
        for path in (
            "/System/Library/Fonts/Supplemental/Arial.ttf",
            "/System/Library/Fonts/Helvetica.ttc",
            "/Library/Fonts/Arial.ttf",
        ):
            if Path(path).exists():
                return ImageFont.truetype(path, size)
        return ImageFont.load_default()

    def board(name, width, height, painter):
        image = Image.new("RGB", (width, height), "#080808")
        painter(ImageDraw.Draw(image), font)
        out = ROOT / "screenshots" / name
        image.save(out, "PNG")
        print(f"wrote {out}")

    def crop(name, width, height, painter):
        image = Image.new("RGB", (width, height), "#080808")
        painter(ImageDraw.Draw(image), font)
        out = ROOT / "components" / "crops" / name
        image.save(out, "PNG")
        print(f"wrote {out}")

    def home(draw, font):
        draw.rectangle((0, 0, 1440, 48), fill="#0c0c0c")
        draw.text((24, 14), "OpenSea Mobile is live", font=font(16), fill="#ffffff")
        draw.rounded_rectangle((1180, 12, 1320, 36), 12, fill="#0f0f0f", outline="#202020")
        draw.text((1192, 14), "Get the app", font=font(14), fill="#ffffff")
        draw.ellipse((24, 66, 54, 96), fill="#0086ff")
        draw.text((120, 72), "Home", font=font(14), fill="#ffffff")
        draw.rounded_rectangle((100, 64, 180, 96), 16, fill="#161616")
        draw.text((116, 72), "Home", font=font(14), fill="#ffffff")
        draw.text((200, 72), "Explore   Feed   Activity", font=font(14), fill="#ffffff")
        draw.rounded_rectangle((1280, 64, 1380, 96), 16, outline="#202020")
        draw.text((1296, 72), "Sign in", font=font(14), fill="#ffffff")
        draw.text((24, 140), "All    Memes    Trading Cards    Art", font=font(16), fill="#ffffff")
        draw.text((24, 200), "CryptoPunks", font=font(32), fill="#ffffff")
        draw.text((24, 260), "FLOOR PRICE", font=font(12), fill="#ffffff")
        draw.text((180, 260), "+68.6%", font=font(14), fill="#47bb64")
        draw.text((280, 260), "-22.1%", font=font(14), fill="#e24756")
        draw.rectangle((0, 868, 1440, 900), fill="#080808", outline="#202020")
        draw.text((24, 874), "Platform Terms    Privacy Policy", font=font(14), fill="#ffffff")
        draw.text((24, 820), "Reconstruction. Not a live screenshot.", font=font(12), fill="#acacac")

    def phone(draw, font):
        draw.rectangle((0, 0, 390, 48), fill="#0c0c0c")
        draw.text((16, 14), "OpenSea Mobile is live", font=font(14), fill="#ffffff")
        draw.ellipse((16, 64, 40, 88), fill="#0086ff")
        draw.rounded_rectangle((300, 62, 374, 94), 16, fill="#0086ff")
        draw.text((312, 70), "Sign in", font=font(14), fill="#ffffff")
        draw.text((16, 120), "Mudwater Cards", font=font(24), fill="#ffffff")
        draw.text((16, 800), "Reconstruction. 390 x 844.", font=font(12), fill="#acacac")

    def dialog(draw, font):
        draw.rectangle((0, 0, 960, 800), fill="#000000")
        draw.rounded_rectangle((240, 48, 720, 752), 12, fill="#080808", outline="#202020")
        draw.text((264, 72), "Connect with OpenSea", font=font(24), fill="#ffffff")
        draw.text((264, 130), "Email", font=font(16), fill="#ffffff")
        draw.rounded_rectangle((264, 160, 696, 216), 12, fill="#0c0c0c", outline="#202020")
        draw.text((280, 178), "Continue with email", font=font(14), fill="#acacac")
        draw.rounded_rectangle((264, 240, 470, 288), 12, fill="#0c0c0c", outline="#202020")
        draw.text((280, 256), "Continue with Google", font=font(14), fill="#ffffff")
        draw.rounded_rectangle((480, 240, 696, 288), 12, fill="#0c0c0c", outline="#202020")
        draw.text((496, 256), "Continue with Apple", font=font(14), fill="#ffffff")
        draw.text((300, 312), "or continue with an external wallet", font=font(12), fill="#acacac")
        draw.rounded_rectangle((264, 340, 696, 620), 12, fill="#0c0c0c", outline="#2c2c2c")
        draw.text((280, 360), "MetaMask", font=font(16), fill="#ffffff")
        draw.text((280, 420), "WalletConnect", font=font(16), fill="#ffffff")
        draw.text((280, 480), "Robinhood Wallet", font=font(16), fill="#ffffff")
        draw.text((280, 540), "More Wallet Options", font=font(16), fill="#ffffff")
        draw.text((264, 680), "Reconstruction. Dialog was not submitted.", font=font(12), fill="#acacac")

    board("home-dark-default.png", 1440, 900, home)
    board("home-dark-phone.png", 390, 844, phone)
    board("signin-dark-dialog.png", 960, 800, dialog)

    def pill(fill, label, width=160, height=64):
        def paint(draw, font):
            draw.rounded_rectangle((8, 16, width - 8, 48), 16, fill=fill)
            draw.text((24, 22), label, font=font(14), fill="#ffffff")
        return paint

    crop("button-nav-selected.png", 160, 64, pill("#161616", "Home"))
    crop("button-signin-desktop.png", 160, 64, pill("#080808", "Sign in"))
    crop("button-signin-phone.png", 160, 64, pill("#0086ff", "Sign in"))
    crop("button-filter-selected.png", 140, 56, pill("#161616", "All", 140, 56))
    crop("button-oauth.png", 280, 80, lambda draw, font: (
        draw.rounded_rectangle((8, 16, 272, 64), 12, fill="#0c0c0c", outline="#202020"),
        draw.text((24, 30), "Continue with Google", font=font(14), fill="#ffffff"),
    ))
    crop("field-email.png", 320, 88, lambda draw, font: (
        draw.rounded_rectangle((8, 16, 312, 72), 12, fill="#0c0c0c", outline="#202020"),
        draw.text((24, 34), "Continue with email", font=font(14), fill="#acacac"),
    ))
    crop("menu-row.png", 220, 56, lambda draw, font: (
        draw.rounded_rectangle((4, 8, 216, 48), 8, fill="#0c0c0c"),
        draw.text((16, 18), "Drops", font=font(14), fill="#ffffff"),
    ))
    crop("card-media.png", 180, 180, lambda draw, font: draw.rectangle((0, 0, 180, 180), fill="#161616"))


def main() -> None:
    write_tokens()
    write_guide()
    write_pngs()


if __name__ == "__main__":
    main()
