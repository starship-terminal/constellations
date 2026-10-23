#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from the native kit (systems/grokbot). core() and semantic() map Grab's readings to roles.
Grab has no dark UI, so there is one semantic set, light.

    python3 tools/build_tokens.py

raw/readings.json is written by tools/measure.py from the full-colour iPhone Mirroring captures.
Every token here names the reading it came from, so `$extensions.source` = {evidence, capture} is
the reading's own label and file. A value worked out from readings (a scale step, a scrim alpha, a
rounded size) is Derived and says how in `$description`. Dimensions are px with 1 px = 1 pt.

The builder refuses a token without a source, an alias that points at nothing, a colour that is not
#RRGGBB(AA), a dimension that is not one px length, and a light and dark set whose keys differ.
Standard library only. Deterministic: the same readings give the same bytes.
"""
import json
import pathlib
import re

PKG = pathlib.Path(__file__).resolve().parent.parent
_READINGS = PKG / "raw" / "readings.json"
READ = json.loads(_READINGS.read_text()) if _READINGS.exists() else {}  # empty in the kit copy, for its tests
MEASURED = f"raw/{PKG.name}-measured.md"


class Missing(Exception):
    pass


def rd(rid, theme="light"):
    try:
        return READ[rid][theme]
    except KeyError:
        raise Missing(f"no reading {rid} for {theme}")


def tok(value, typ, desc, evidence, capture):
    return {"$value": value, "$type": typ, "$description": desc,
            "$extensions": {"source": {"evidence": evidence, "capture": capture}}}


def from_reading(rid, theme, typ, desc):
    r = rd(rid, theme)
    note = desc
    if r.get("share") is not None and r["evidence"] == "Derived":
        note += f" The box's dominant colour covers {round(r['share'] * 100)}% of it (a gradient, glass or a thin mark), so it is a reading, not an exact fill."
    return tok(r["value"], typ, note, r["evidence"], r["capture"])


def px(v):
    return f"{v:g}px"


def pt_of(rid, theme="light", index=0):
    """A number in pt from an extent ('45pt') or bbox ('343x54pt') reading."""
    v = rd(rid, theme)["value"].rstrip("pt")
    return float(v.split("x")[index])


def derived(value, typ, desc, capture=MEASURED):
    return tok(value, typ, desc, "Derived", capture)


def alias(path, typ, desc):
    return tok("{" + path + "}", typ, desc, "Derived", MEASURED)


# ---------------------------------------------------------------- core

def neutral_ramp():
    """Every grey the semantic set uses, sorted light to dark. Not a published ramp: the steps are
    the values the app shows, named by order."""
    ids = ["bg.page", "bg.section", "border.divider", "border.card", "border.field", "border.chip", "border.control",
           "text.placeholderField", "text.placeholder", "text.navInactive", "text.secondary", "text.label",
           "text.rowValue", "text.tab", "text.body", "text.primary", "scrim.dialog"]
    seen = {}
    for rid in ids:
        r = rd(rid)
        v = r["value"]
        rr, gg, bb = int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)
        if max(rr, gg, bb) - min(rr, gg, bb) <= 12:     # neutral enough
            seen.setdefault(v, []).append((rid, r["evidence"], r["capture"]))
    lum = lambda h: sum(int(h[i:i + 2], 16) for i in (1, 3, 5))
    rank = ["Sampled", "Sampled (text)", "Derived"]   # the most exact reading of the value wins
    out = {}
    for i, v in enumerate(sorted(seen, key=lum, reverse=True)):
        uses = sorted(set(seen[v]))
        best = min(uses, key=lambda u: rank.index(u[1]))
        listed = ", ".join(f"{name} ({ev})" for name, ev, _ in uses)
        out[f"{i * 50:03d}"] = tok(v, "color", f"Used by: {listed}.", best[1], best[2])
    return out


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    b = lambda rid, desc: from_reading(rid, "light", "color", desc)
    c["color"] = {
        "brand": {
            "green": b("button.primary", "Grab green: primary buttons, the active tab bar item, status 'Bill paid', green text links, the caret."),
            "forest": b("tab.indicator", "Darker green: the active tab underline and the compact Buy button."),
            "deep": b("fab", "Deep green: the floating action button and the tooltip."),
            "teal": b("chip.selected", "Dark teal: the selected chip and the centre scan button in the tab bar."),
            "mint": b("bg.tint", "Pale mint: secondary buttons, unselected chips, the account and Moments headers."),
        },
        "service": {
            "food": b("bg.headerFood", "GrabFood's blue header."),
            "flash": b("bg.flash", "Flash-deal orange: the flash deals sheet and bar, discount tags."),
            "peach": b("bg.promoPeach", "Peach behind Offer Zone and the Transport header."),
            "cream": b("bg.promoCream", "Cream behind a promo interstitial."),
            "timer": b("surface.timer", "Dark brown countdown digit boxes on the flash deals sheet."),
        },
        "neutral": neutral_ramp(),
    }
    c["radius"] = {
        "tooltip": derived("8px", "dimension", f"Tooltip: {rd('radius.tooltip')['value']}. Plus or minus 2 pt."),
        "field": derived("12px", "dimension", f"Search and text fields: {rd('radius.searchField')['value']}. Plus or minus 2 pt."),
        "card": derived("16px", "dimension", f"Cards and promo cards: account card {rd('radius.card')['value']}, promo card {rd('radius.promo')['value']}. Plus or minus 2 pt."),
        "sheet": derived("24px", "dimension", f"Top corners of a bottom sheet: {rd('radius.sheet')['value']} (pre-prompt), {rd('radius.sheetFlash')['value']} (flash deals)."),
        "capsule": derived("999px", "dimension", f"Fully round ends: buttons ({rd('radius.button')['value']} on a {pt_of('size.buttonPrimary', index=1):g} pt button), chips ({rd('radius.chip')['value']} on {pt_of('size.chip', index=1):g} pt), pills and badges."),
    }
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps are multiples of 4 pt within a pixel or two."),
        "xs": derived("4px", "dimension", "Between an icon and its label inside a chip."),
        "sm": derived("8px", "dimension", "Between chips in a row (about 8 to 10 pt in 17-search-focused-chips-recent-pills)."),
        "md": derived("12px", "dimension", "Between two cards side by side (Finance and Ride to on Home: about 11 pt)."),
        "lg": derived("16px", "dimension", "Screen margin: cards, fields and buttons start 16 pt from the screen edge (cards begin at x 48 in the capture, 32 px right of the screen edge at x 16)."),
        "xl": derived("24px", "dimension", "Space above a section title (For more value, Recent & popular)."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, fields, chips and buttons."),
    }
    tab_top = rd("size.tabBar")["value"][0]
    c["size"] = {
        "button": tok(px(round(pt_of("size.buttonSecondary", index=1))), "dimension", f"Full-width button height: primary {rd('size.buttonPrimary')['value']}, secondary {rd('size.buttonSecondary')['value']}, disabled {rd('size.buttonDisabled')['value']}.", "Sampled", rd("size.buttonSecondary")["capture"]),
        "buttonCompact": tok(px(round(pt_of("size.buttonCompact", index=1))), "dimension", f"Compact button in a card (Buy): {rd('size.buttonCompact')['value']}.", "Sampled", rd("size.buttonCompact")["capture"]),
        "chip": tok(px(round(pt_of("size.chipDefault", index=1))), "dimension", f"Filter chip height: selected {rd('size.chip')['value']}, unselected {rd('size.chipDefault')['value']}.", "Sampled", rd("size.chipDefault")["capture"]),
        "field": tok(px(pt_of("size.field")), "dimension", f"Text and search field height: pickup field {rd('size.field')['value']}, grey search field {rd('size.searchField')['value']}, home search {rd('size.searchHome')['value']}.", "Sampled", rd("size.field")["capture"]),
        "row": tok(px(float(rd("rows.settings")["value"].rstrip("pt"))), "dimension", "Single-line settings row, label to label (For more value list).", "Derived", rd("rows.settings")["capture"]),
        "card": {
            "height": tok(px(pt_of("size.cardH")), "dimension", f"Small shortcut card (Finance, Ride to): {rd('size.cardW')['value']} wide, {rd('size.cardH')['value']} tall.", "Sampled", rd("size.cardH")["capture"]),
        },
        "checkbox": tok(px(pt_of("size.checkbox")), "dimension", "Square checkbox with rounded corners, outline only when unchecked.", "Sampled", rd("size.checkbox")["capture"]),
        "scanButton": derived("58px", "dimension", f"Centre scan button in the tab bar, a circle that rises above the bar: {rd('size.scan')['value']} including its anti-aliased edge."),
        "fab": tok(px(pt_of("size.fab")), "dimension", f"Floating action button (circle): {rd('size.fab')['value']}.", "Sampled", rd("size.fab")["capture"]),
        "tabBar": derived(px((1764 - tab_top) / 2), "dimension", f"Tab bar from its top edge (y {tab_top} in capture pixels) to the bottom of the screen, home indicator area included."),
        "touchTarget": derived("44px", "dimension", "Buttons, rows and fields are 40 pt or more; chips (35 pt), the Buy button (31.5 pt) and the checkbox (20 pt) sit inside larger rows."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers under list rows: one device pixel at 2x (border.divider reads a one-pixel row)."),
        "default": derived("1px", "dimension", "Card, field and outlined-chip borders: two device pixels."),
        "control": derived("2px", "dimension", "Checkbox outline: about four device pixels."),
    }}
    c["fontFamily"] = {
        "base": tok("system", "fontFamily", "Not determinable from pixels. Body text, rows, labels, buttons and chips use a neo-grotesque sans close to Inter (single-storey 'g' absent, straight-legged 'R'); use the platform font.", "Not captured", MEASURED),
        "display": tok("system", "fontFamily", "Not determinable from pixels. Page and section titles (Messages, Activity, For more value, sheet titles) use a rounded geometric display face with a single-storey 'a' and 'y' with a curved tail, Grab's own; it is not identified here. Use the platform font or a rounded geometric sans.", "Not captured", MEASURED),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Secondary lines, row subtitles, placeholders. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Row labels, tab labels, chip labels. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Button labels, list titles, card values. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "Display titles. Judged by stroke width."),
    }

    def ty(size_rid, family, weight, lh, desc, extra=()):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.%s}" % family, "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{float(rd(rid)['value'].rstrip('pt')):g}px"
    c["typography"] = {
        "largeTitle": ty("type.largeTitle", "display", "bold", None, "Tab page titles (Messages, Activity)."),
        "sheetTitle": ty("type.sheetTitle", "display", "bold", lines("lines.sheetTitle"), "Sheet and empty-state titles, on up to two lines."),
        "display": ty("type.display", "display", "bold", None, "Banner titles on a service header (Night munchies)."),
        "title": ty("type.title", "display", "bold", None, "Pushed page titles and section titles (Dietary preferences, For more value, Recent).", ("type.sectionTitle", "type.sectionHeader")),
        "button": ty("type.button", "base", "semibold", None, "Full-width button labels (Yes, Later, Book Standard)."),
        "body": ty("type.body", "base", "medium", lines("lines.body"), "Settings rows, row labels, sheet body text."),
        "chip": ty("type.chip", "base", "medium", None, "Chip and tab labels.", ("type.tab",)),
        "subhead": ty("type.subhead", "base", "regular", lines("lines.paragraph"), "Row subtitles, merchant names and intro paragraphs.", ("type.listTitle",)),
        "label": ty("type.label", "base", "regular", None, "Card labels (Finance, Ride to) and meta lines."),
        "caption": ty("type.caption", "base", "regular", None, "Tab bar labels."),
    }
    c["$extensions"] = {"notTokenised": [
        "Gradients: the Home header (deep green to darker green, bg.headerHome to bg.headerHomeEnd) and the Pickup header (green to teal) are gradients; only their ends were read",
        "Shadows: cards on Home and the floating map controls carry a soft drop shadow that was not measured",
        "Illustrations and 3D service icons: Grab's artwork, not tokens",
        "Motion and easing: stills only",
        "Line heights of one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic set (light only)

def scrim(rid, ref, desc):
    """Black at the alpha that turns the reference reading into the dimmed one (green channel)."""
    a = 1 - int(rd(rid)["value"][3:5], 16) / int(rd(ref)["value"][3:5], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: {desc} reads {rd(ref)['value']} undimmed and {rd(rid)['value']} dimmed.",
                   rd(rid)["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Page background on every screen."),
            "section": f("bg.section", "Grey band between groups on the account page and behind reviews."),
            "tint": alias("color.brand.mint", "color", "Pale mint behind the account card and the Moments header."),
            "header": f("bg.headerHome", "Home header, top of its gradient (deep green)."),
            "headerEnd": f("bg.headerHomeEnd", "Home header, bottom of its gradient."),
            "scrim": scrim("scrim.dialog", "scrim.ref", "a sheet's backdrop: the Messages page"),
            "scrimLight": scrim("scrim.sheet", "scrim.sheetRef", "a lighter sheet backdrop: the Food header"),
        },
        "surface": {
            "card": f("surface.card", "Cards, list sections, the search field on a coloured header."),
            "field": f("surface.field", "Grey search field on a white page."),
            "pill": f("surface.pill", "Recent-search pills."),
            "sheet": f("surface.sheet", "Bottom sheets and the coach mark."),
            "tooltip": alias("color.brand.deep", "color", "Tooltip bubble (white text)."),
        },
        "border": {
            "divider": f("border.divider", "Hairline under list rows."),
            "card": f("border.card", "Outline of small cards (Finance, Ride to) and the voucher card."),
            "field": f("border.field", "Text field outline, unfocused."),
            "chip": f("border.chip", "Outlined filter chips on Moments (Location, Services)."),
            "control": f("border.control", "Checkbox outline, unchecked."),
            "selected": f("border.selected", "Selected option card (the chosen ride type)."),
        },
        "text": {
            "primary": f("text.primary", f"Titles, row labels, prices (rows read {rd('text.body')['value']})."),
            "secondary": f("text.secondary", f"Dates, meta lines, card labels (reads {rd('text.label')['value']}), helper text."),
            "strong": f("text.rowValue", "Row values and inactive tab labels: a dark grey between primary and secondary."),
            "placeholder": f("text.placeholder", f"Placeholders on a white field (reads {rd('text.placeholderField')['value']} on a grey field)."),
            "disabled": f("text.disabled", "Label of a disabled button."),
            "link": f("text.link", "Text links (View History, See latest posts, Add pickup details)."),
            "linkBrand": f("text.linkBrand", "Green text actions (Explore Available Options)."),
            "onPrimary": f("text.onPrimary", "Label on a green button."),
            "onSecondary": f("text.onSecondary", "Label on a mint secondary button and on unselected chips."),
            "onTooltip": f("text.onTooltip", "Text on the tooltip."),
            "highlight": f("text.promo", "Orange highlight inside a sentence (3.2M+ recent visitors)."),
            "danger": f("text.danger", "Status 'Cancelled' and the red 'New' marker."),
            "success": f("text.success", "Status 'Bill paid' and 'Open'."),
        },
        "accent": {
            "default": alias("color.brand.green", "color", "The app's one accent: primary buttons, active tab bar item, green links."),
            "strong": alias("color.brand.teal", "color", "Selected chip, centre scan button."),
        },
        "focus": {
            "ring": f("focus.ring", "Border of a focused text field: a darker green than the brand green, about 1 pt."),
            "glow": f("focus.glow", "Soft green halo just outside the focused field's border."),
            "caret": f("focus.caret", "Text caret: Grab green."),
        },
        "button": {
            "primary": {"bg": alias("color.brand.green", "color", "Full-width primary button."),
                        "text": alias("color.text.onPrimary", "color", "Primary button label.")},
            "secondary": {"bg": f("button.secondary", "Full-width secondary button (Later): pale mint, no border."),
                          "text": alias("color.text.onSecondary", "color", "Secondary button label (dark teal).")},
            "disabled": {"bg": f("button.disabled", "Primary button, disabled: light grey."),
                         "text": alias("color.text.disabled", "color", "Disabled button label.")},
            "compact": {"bg": f("button.compact", "Compact Buy button inside a card: the forest green, not the brand green."),
                        "text": alias("color.text.onPrimary", "color", "Compact button label.")},
        },
        "chip": {
            "selected": {"bg": alias("color.brand.teal", "color", "Selected filter chip."),
                         "text": alias("color.text.onPrimary", "color", "Selected chip label.")},
            "default": {"bg": f("chip.default", "Unselected filter chip: pale mint."),
                        "text": f("text.chip", "Unselected chip label.")},
        },
        "tab": {
            "active": f("text.tabActive", "Active tab label (For you, Deals)."),
            "inactive": f("text.tab", "Inactive tab label."),
            "indicator": alias("color.brand.forest", "color", "Underline under the active tab."),
        },
        "nav": {
            "active": f("text.navActive", "Active tab bar icon and label (Grab green)."),
            "inactive": f("text.navInactive", "Inactive tab bar icon and label."),
            "scan": f("nav.scan", "Centre scan button, a raised circle."),
            "fab": f("fab", "Floating action button."),
        },
        "badge": {
            "new": f("badge.new", "'New' badge on a chip: red pill, white text."),
            "discount": f("badge.discount", "Discount tags and the flash deals bar."),
        },
        "status": {
            "success": alias("color.text.success", "color", "Success: green status text. No success fill was seen."),
            "danger": alias("color.text.danger", "color", "Danger: red status text and the New badge. No error state was captured."),
            "info": alias("color.text.link", "color", "Info: the blue link colour."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Dark theme: not applicable, Grab has no dark UI (it stays light with the phone in dark mode)",
        "Pressed and hover states: stills only",
        "Warning colour and error states: none were seen",
        "Switch colours: no switch was captured",
    ]}
    return s


# ---------------------------------------------------------------- build and checks

def walk(node, path=()):
    if isinstance(node, dict) and "$value" in node:
        yield path, node
        return
    if isinstance(node, dict):
        for k, v in node.items():
            if not k.startswith("$"):
                yield from walk(v, path + (k,))


def aliases(v):
    """Every {alias} in a value, including those inside a composite (a typography style)."""
    if isinstance(v, str):
        return re.findall(r"\{([^{}]+)\}", v)
    if isinstance(v, dict):
        return [a for x in v.values() for a in aliases(x)]
    return []


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            assert src.get("evidence") and src.get("capture"), f"{where}: no source"
            v = t["$value"]
            for a in aliases(v):
                assert a in paths, f"{where}: alias {{{a}}} points at nothing"
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                assert re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v), f"{where}: bad colour {v}"
            elif t["$type"] == "dimension":
                assert re.fullmatch(r"-?\d+(\.\d+)?px", v), f"{where}: bad dimension {v}"
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        assert keys("light") == keys("dark"), "light and dark keys differ"


def build():
    doc = {
        "core": core(),
        "light": semantic("light"),
        "$themes": [  # PRODUCT (adapt): Grab has no dark UI, so one theme
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "Grab's only theme: it stays light with the phone in dark mode. Read from screenshots/light/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light"]},
    }
    check(doc)
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "light") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens")


if __name__ == "__main__":
    if not READ:
        raise SystemExit("no raw/readings.json: run tools/measure.py first")
    build()
