#!/usr/bin/env python3
"""Write tokens.json and style-guide.html for OpenSea; with --drawings, also redraw the reconstruction PNGs.

Every colour comes from raw/css-vars.json (the probe-resolved --color-* pairs).
Every size, radius and type value labelled Measured comes from
raw/components-computed.json through C(), which stops the build when a reading
is missing; the one value no reading holds is labelled Reconstruction. The
style guide is rendered from the built tokens, not from a palette of its own.

The PNGs under screenshots/ and components/crops/ are reconstructions:
preview_snapshot returned "The browser is not producing screenshot frames", so
no live pixels are in this package. They are drawn by `--drawings` only, with
Pillow's bundled font, so a plain rebuild never rewrites them.
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = json.loads((ROOT / "raw" / "css-vars.json").read_text())
COMP = json.loads((ROOT / "raw" / "components-computed.json").read_text())

SOURCE = "Measured. :root, .dark and .light in 42m_qrqpbfsj8.css, probe-resolved on opensea.io 2026-11-19."
MEASURED = "Measured. getComputedStyle on a signed-out element, opensea.io, dark, 2026-11-19."
BY_HAND = ("Reconstruction. Entered by hand at capture time; raw/components-computed.json holds no reading "
           "for it.")


def C(path: str):
    """A reading from raw/components-computed.json by dotted path; a missing one stops the build."""
    node = COMP
    for key in path.split("."):
        if not isinstance(node, dict) or key not in node:
            raise SystemExit(f"raw/components-computed.json has no {path}")
        node = node[key]
    return node


def px(value) -> str:
    """A reading as one px length: 32 -> "32px", "6px 12px" -> its first length."""
    if isinstance(value, (int, float)):
        return f"{value:g}px"
    m = re.match(r"-?\d+(?:\.\d+)?px", value.strip())
    if not m:
        raise SystemExit(f"no px length in {value!r}")
    return m.group(0)


def nth(value: str, i: int) -> str:
    """The i-th length of a shorthand such as "0 12px 0 8px" (a bare 0 is 0px)."""
    parts = value.split()
    part = parts[i] if i < len(parts) else parts[-1]
    return "0px" if part == "0" else px(part)


def measured(path: str, note: str) -> str:
    return f"{MEASURED} {note} ({path} in raw/components-computed.json)."


def m_dim(path: str, note: str, pick=px) -> dict:
    return dim(pick(C(path)), measured(path, note))


PILL = C("controls.nav-item-selected.radius")
PILL_SOURCE = (f"Derived. Nav pills, filters, Sign in and close computed border-radius {PILL} "
               "(controls.*.radius in raw/components-computed.json), the fully rounded pill; written 9999px.")


def seconds_to_ms(text: str) -> str:
    m = re.search(r"(\d*\.?\d+)s\b", text)
    if not m:
        raise SystemExit(f"no duration in {text!r}")
    return f"{float(m.group(1)) * 1000:g}ms"


def bezier(text: str) -> list:
    m = re.search(r"cubic-bezier\(([^)]*)\)", text)
    if not m:
        raise SystemExit(f"no cubic-bezier in {text!r}")
    nums = [float(x) for x in m.group(1).split(",")]
    return [int(x) if x == int(x) else x for x in nums]


def color(value: str, source: str = SOURCE) -> dict:
    return {"$type": "color", "$value": value, "$extensions": {"source": source}}


def dim(value: str, source: str = MEASURED) -> dict:
    return {"$type": "dimension", "$value": value, "$extensions": {"source": source}}


def font(value: str, source: str) -> dict:
    return {"$type": "fontFamily", "$value": value, "$extensions": {"source": source}}


def duration(value: str, source: str) -> dict:
    return {"$type": "duration", "$value": value, "$extensions": {"source": source}}


def cubic(value: list, source: str) -> dict:
    return {"$type": "cubicBezier", "$value": value, "$extensions": {"source": source}}


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
                    "text": color(C("controls.sign-in-phone.color"), measured("controls.sign-in-phone.color", "Phone Sign in label")),
                    "radius": dim("9999px", PILL_SOURCE),
                    "height": m_dim("controls.sign-in-phone.h", "Phone Sign in"),
                },
                "nav": {
                    "bg": color(pick("bg-additional-1"), MEASURED + " Selected Home pill."),
                    "text": color(pick("text-primary"), MEASURED + " Nav label."),
                    "radius": dim("9999px", PILL_SOURCE),
                    "height": m_dim("controls.nav-item-selected.h", "Selected Home pill"),
                },
                "filter": {
                    "bg": color(pick("bg-primary"), MEASURED + " Resting Listed pill."),
                    "text": color(pick("text-secondary"), MEASURED + " Resting filter label."),
                    "radius": dim("9999px", PILL_SOURCE),
                    "height": m_dim("controls.filter-rest.h", "Collection status pills"),
                },
                "oauth": {
                    "bg": color(pick("bg-primary"), MEASURED + " Continue with Google at rest."),
                    "text": color(pick("text-primary")),
                    "radius": m_dim("dialog.oauth.radius", "Connect dialog OAuth buttons"),
                    "height": m_dim("dialog.oauth.h", "Continue with Google"),
                },
            },
            "field": {
                "bg": color(pick("bg-primary"), MEASURED + " Search wrap and email wrap."),
                "text": color(pick("text-primary")),
                "radius": m_dim("dialog.email-wrap.radius", "Email field in the connect dialog. Search is a pill"),
                "height": m_dim("dialog.email-wrap.h", "Email wrap"),
            },
            "dialog": {
                "bg": color(pick("bg-app"), MEASURED + " Connect with OpenSea dialog."),
                "text": color(pick("text-primary")),
                "radius": m_dim("dialog.box.radius", "Connect with OpenSea dialog"),
            },
            "menu": {
                "bg": color(pick("bg-primary"), MEASURED + " More menu."),
                "text": color(pick("text-primary")),
                "radius": m_dim("menu.more.radius", "More menu"),
            },
            "card": {
                "bg": color(pick("bg-additional-1"), MEASURED + " Item media well."),
                "radius": m_dim("collection-card.card-shell.radius", "Item card shell"),
            },
        },
    }


def typo(path: str, note: str, family: str = "gtAmerica") -> dict:
    """A type style from one reading: size, weight and line height as computed; tracking 0px unless read."""
    r = C(path)
    note = measured(path, note) + ("" if "ls" in r else " Letter-spacing was not read and is written 0px.")
    return _type(r.get("font", family), r["size"], r["weight"], r["lh"], r.get("ls", "0px"), note)


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
                "hero": typo("type.tools-hero", "/tools h1 'Equip your AI agents'"),
                "title": typo("type.collection-title", "Collection name span, CryptoPunks"),
                "dialog-title": typo("dialog.title", "Connect with OpenSea h4; Drops h1 is the same 24px / 500 / 30px"),
                "body": typo("type.body", "Body, terms paragraphs, nav root"),
                "label": typo("type.nav-label", "Nav pills and Sign in"),
                "stat": typo("type.stat-label", "FLOOR PRICE label", family="gtAmericaMono"),
            },
            "radius": {
                "none": m_dim("controls.buy-now.radius", "Buy Now; item media is 0px too"),
                "avatar": m_dim("collection-card.avatar.radius", "Collection avatar img"),
                "menu-item": m_dim("menu.more.item-radius", "More menu row"),
                "card": m_dim("collection-card.card-shell.radius", "Item card shell"),
                "control": m_dim("dialog.box.radius", "Dialog; menu, OAuth button, email field and wallet list are 12px too"),
                "help-search": m_dim("help-center.search.radius", "support.opensea.io search. A separate skin"),
                "help-card": m_dim("help-center.card.radius", "support.opensea.io category card"),
                "pill": dim("9999px", PILL_SOURCE),
            },
            "spacing": {
                "4": m_dim("menu.more.pad", "Menu padding; Get the app gap and close padding are 4px too"),
                "6": m_dim("shell.banner.pad", "Banner vertical padding"),
                "8": m_dim("menu.more.item-pad", "Menu item padding-left", lambda v: nth(v, 1)),
                "12": m_dim("shell.banner.gap", "Banner gap; field horizontal padding is 12px too"),
                "16": m_dim("controls.sign-in-desktop.pad", "Sign in horizontal padding", lambda v: nth(v, 1)),
                "24": dim("24px", BY_HAND + " Logo left offset and category row left offset at 1440."),
                "32": m_dim("shell.footer.h", "Footer height and nav control height"),
                "48": m_dim("shell.banner.h", "Promo banner height"),
                "64": m_dim("shell.nav.h", "Desktop nav height"),
            },
            "size": {
                "nav": m_dim("shell.nav.h", "Desktop nav"),
                "banner": m_dim("shell.banner.h", "Promo banner"),
                "control": m_dim("controls.sign-in-desktop.h", "Sign in and nav pills"),
                "filter": m_dim("controls.filter-rest.h", "Collection status pills"),
                "oauth": m_dim("dialog.oauth.h", "Continue with Google"),
                "field": m_dim("dialog.email-wrap.h", "Email wrap"),
                "dialog": m_dim("dialog.box.w", "Connect dialog width"),
                "logo": m_dim("shell.logo.w", "Wordmark circle"),
            },
            "motion": {
                "duration": {
                    "nav": duration(seconds_to_ms(C("controls.nav-item-selected.transition")),
                                    measured("controls.nav-item-selected.transition", "Nav pill transition 0.2s")),
                    "search": duration(seconds_to_ms(C("controls.search-field.transition")),
                                       measured("controls.search-field.transition", "Search wrap transition 0.2s")),
                },
                "easing": {
                    "ease-out": other("ease-out", measured("controls.nav-item-selected.transition", "Nav pill timing keyword")),
                    "standard": cubic(bezier(C("controls.search-field.transition")),
                                      measured("controls.search-field.transition", "Search wrap timing function")),
                },
            },
            "color": {
                "focus": color(re.search(r"#[0-9a-fA-F]{6}", C("dialog.email-focus")).group(0).lower(),
                               measured("dialog.email-focus", "Email input focused outline color")),
                "white": color(RAW["colors"]["white"]["dark"]),
                "black": color(RAW["colors"]["black"]["dark"]),
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


# The style guide's CSS names and the semantic token each one draws (finding 23-5: the guide's palette
# used to be typed in here and would have drifted from tokens.json on a recapture).
GUIDE_VARS = {
    "page": "page", "surface": "surface", "ink": "text", "muted": "muted", "line": "line.1",
    "line-2": "line.2", "accent": "brand.blue-3", "selected": "background.additional-1",
    "up": "status.success", "down": "status.error", "link": "foreground.link",
}
SWATCHES = ["page", "surface", "selected", "ink", "muted", "line", "accent", "link", "up", "down"]
SWATCH_NAMES = {"ink": "text", "line": "border"}
RADII = [("Pill", "pill", "Nav, filters, Sign in, close"), ("Control", "control", "Dialog, menu, OAuth, email field"),
         ("Card", "card", "Item card shell and menu row"), ("Avatar", "avatar", "Collection avatar"),
         ("None", "none", "Item media, Buy Now")]


def leaf(doc: dict, path: str) -> dict:
    node = doc
    for part in path.split("."):
        node = node[part]
    return node


def style_guide(doc: dict | None = None) -> str:
    """The guide page, with every colour, radius and type size taken from the token document."""
    doc = doc or tokens()
    esc = lambda v: html.escape(str(v), quote=True)  # noqa: E731

    def palette(theme: str) -> str:
        return " ".join(f"--{name}: {esc(leaf(doc[theme], path)['$value'])};" for name, path in GUIDE_VARS.items())

    label = leaf(doc, "core.typography.label")["$value"]
    swatches = json.dumps([[SWATCH_NAMES.get(n, n), leaf(doc["dark"], GUIDE_VARS[n])["$value"]] for n in SWATCHES])
    radii = "\n".join(f"<tr><td>{esc(name)}</td><td>{esc(leaf(doc, 'core.radius.' + key)['$value'])}</td><td>{esc(where)}</td></tr>"
                      for name, key, where in RADII)
    return (GUIDE.replace("/*DARK*/", palette("dark")).replace("/*LIGHT*/", palette("light"))
            .replace("/*LABEL*/", f"font-family: inherit; font-size: {esc(label['fontSize'])}; line-height: {esc(label['lineHeight'])}; font-weight: {esc(label['fontWeight'])};")
            .replace("/*SWATCHES*/", swatches.replace("<", "\\u003c")).replace("<!--RADII-->", radii))


GUIDE = """<!doctype html>
<html lang="en" data-mode="dark">
<head>
<meta charset="utf-8">
<title>OpenSea style guide</title>
<style>
:root, [data-mode="dark"] {
  color-scheme: dark;
  /*DARK*/
}
[data-mode="light"] {
  color-scheme: light;
  /*LIGHT*/
}
body { margin: 0; background: var(--page); color: var(--ink); font: 16px/24px ui-sans-serif, system-ui, sans-serif; }
main { max-width: 960px; margin: 0 auto; padding: 32px 24px 80px; }
h1 { font-size: 32px; line-height: 48px; font-weight: 500; margin: 0 0 8px; }
h2 { font-size: 24px; line-height: 30px; font-weight: 500; margin: 40px 0 12px; }
p.note { color: var(--muted); max-width: 68ch; }
.hero { font-size: 60px; line-height: 63px; font-weight: 500; letter-spacing: -1.5px; margin: 12px 0; }
.row { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; }
button, .pill { /*LABEL*/ border-radius: 9999px; height: 32px; padding: 0 16px; }
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
<!--RADII-->
</table>
</main>
<script>
const dark = /*SWATCHES*/;
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
    path.write_text(style_guide(json.loads((ROOT / "tokens.json").read_text())))
    print(f"wrote {path}")


def write_pngs() -> None:
    """Reconstruction boards. Not live screenshots."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow missing; reconstruction PNGs skipped")
        return

    def font(size):
        # Pillow's bundled face, so the drawings do not depend on the machine's fonts. The committed
        # PNGs were drawn with the system Arial before this change; a --drawings run redraws them.
        return ImageFont.load_default(size)

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
    if "--drawings" in sys.argv[1:]:
        write_pngs()


if __name__ == "__main__":
    main()
