#!/usr/bin/env python3
"""Build tokens.json (W3C DTCG, Tokens Studio multi-set layout) from raw/readings.json (native kit).

Copied from systems/grokbot. Adapt core() and semantic(), marked PRODUCT (adapt): they map this
product's readings to roles. Keep the helpers, check() and build().

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


def rd(rid, theme="dark"):
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


def pt_of(rid, theme="dark", index=0):
    """A number in pt from an extent ('45pt') or bbox ('343x54pt') reading."""
    v = rd(rid, theme)["value"].rstrip("pt")
    return float(v.split("x")[index])


def derived(value, typ, desc, capture=MEASURED):
    return tok(value, typ, desc, "Derived", capture)


def alias(path, typ, desc):
    return tok("{" + path + "}", typ, desc, "Derived", MEASURED)


# ---------------------------------------------------------------- core

def neutral_ramp():
    """Every grey the semantic sets use, both themes, sorted light to dark. Not a published ramp:
    the steps are the values the app shows, named by order."""
    ids = ["bg.page", "bg.sheet", "bg.sheetGrouped", "surface.secondary", "surface.inset", "surface.avatar",
           "surface.iconButton", "surface.composer", "surface.composerButton", "surface.menu", "surface.popup",
           "border.dividerColour", "border.tile", "border.menuDivider", "text.primary", "text.muted",
           "text.secondary", "text.tertiary", "text.placeholder", "switch.off", "button.send", "button.mic"]
    seen = {}
    for rid in ids:
        for theme, r in READ[rid].items():
            v = r["value"]
            rr, gg, bb = int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)
            if max(rr, gg, bb) - min(rr, gg, bb) <= 12:     # neutral enough
                seen.setdefault(v, []).append((f"{theme} {rid}", r["evidence"], r["capture"]))
    lum = lambda h: sum(int(h[i:i + 2], 16) for i in (1, 3, 5))
    rank = ["Sampled", "Sampled (text)", "Derived"]   # the most exact reading of the value wins
    out = {}
    for i, v in enumerate(sorted(seen, key=lum, reverse=True)):
        uses = sorted(set(seen[v]))
        best = min(uses, key=lambda u: rank.index(u[1]))
        listed = ", ".join(f"{name} ({ev})" for name, ev, _ in uses)
        out[f"{i * 50:03d}"] = tok(v, "color", f"Used by: {listed}.", best[1], best[2])
    return out


def edges(rid, theme="dark"):
    """Runs of consecutive positions in a find reading, as (first, last) pairs."""
    runs = []
    for p in rd(rid, theme)["value"]:
        if runs and p - runs[-1][1] <= 2:
            runs[-1][1] = p
        else:
            runs.append([p, p])
    return runs


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    heat = {f"{n}00": from_reading(f"heat.{n}", "light", "color",
                                   f"Activity heatmap level {n} of 4 on the profile, read in light (the dark profile bottom was not captured). "
                                   + ("The busiest level is the chart orange itself." if n == 4 else "A tint of the chart orange."))
            for n in (1, 2, 3, 4)}
    c["color"] = {
        "orange": heat,
        "neutral": neutral_ramp(),
    }
    c["radius"] = {
        "tile": derived("16px", "dimension", f"Inbox tiles: {rd('radius.tile')['value']} dark, {rd('radius.tile', 'light')['value']} light. Plus or minus 2 pt."),
        "card": derived("16px", "dimension", f"The Changes card in a thread: {rd('radius.card')['value']} in both themes. Plus or minus 2 pt."),
        "banner": derived("12px", "dimension", f"The photo-access card in the Context sheet: {rd('radius.banner')['value']}."),
        "composerPanel": derived("26px", "dimension", f"The expanded composer panel: {rd('radius.composerOpen')['value']} (dark)."),
        "menu": derived("32px", "dimension", f"Pull-down and pop-up menus (iOS 26 glass): {rd('radius.menu')['value']} pull-down, {rd('radius.popup')['value']} pop-up, both dark."),
        "sheet": derived("36px", "dimension", f"Top corners of a sheet: {rd('radius.sheetHalf')['value']} on the half-height Model sheet, {rd('radius.sheet', 'light')['value']} on the full-height Customize sheet (light)."),
        "capsule": derived("999px", "dimension", "Fully round ends: the composer, search fields, filter chips, segments, the Continue and '7 PRs' capsules, and the round nav, icon and send buttons."),
    }
    tx, ty_ = edges("size.tile.x"), edges("size.tile.y")
    tile_w = (tx[1][1] - tx[0][0] + 1) / 2
    tile_h = (ty_[1][1] - ty_[0][0] + 1) / 2
    gap_x, gap_y = (tx[2][0] - tx[1][1] - 1) / 2, (ty_[2][0] - ty_[1][1] - 1) / 2
    comp_from = rd("size.composer.w")["from"]
    card = rd("size.card")["box"]
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two."),
        "sm": derived("8px", "dimension", "Gap between a row's title and its subtitle line, and inside chips."),
        "md": derived("12px", "dimension", f"Gap between Inbox tiles: {gap_x:g} pt across and {gap_y:g} pt down (size.tile.x, size.tile.y), and the composer's inset from the screen edge ({(comp_from - 16) / 2:g} pt)."),
        "lg": derived("16px", "dimension", f"Inbox tiles' inset from the screen edge: {(tx[0][0] - 16) / 2:g} pt."),
        "xl": derived("20px", "dimension", f"Screen margin for text, rows and cards: titles and row icons start 20.5 pt in, the Changes card {(card[0] - 16) / 2:g} pt."),
        "screenMargin": alias("space.xl", "dimension", "Left and right margin of titles, rows, replies and cards."),
    }
    rows1 = edges("rows.single")
    dots = edges("rows.double")
    centres = [(a + b) / 2 for a, b in dots]
    c["size"] = {
        "row": tok(px((rows1[-1][0] - rows1[0][0]) / 2 / (len(rows1) - 1)), "dimension", "Single-line row (Projects, Workspaces, Customize, Add Workspace), divider to divider.", "Sampled", rd("rows.single")["capture"]),
        "rowTwoLine": tok(px((centres[-1] - centres[0]) / 2 / (len(centres) - 1)), "dimension", "Agent row with a status line (title, then branch state, diffstat and repo), dot to dot.", "Sampled", rd("rows.double", "dark")["capture"]),
        "navButton": tok(px(pt_of("size.navButton.w")), "dimension", f"Round glass back, close, search and filter buttons: {rd('size.navButton.w')['value']} x {rd('size.navButton.h')['value']} in dark, rim included.", "Sampled", rd("size.navButton.w")["capture"]),
        "composer": tok(px(pt_of("size.composer.h")), "dimension", f"Composer capsule height ({rd('size.composer.w')['value']} wide in dark).", "Sampled", rd("size.composer.h")["capture"]),
        "composerPanel": tok(px(pt_of("size.composerOpen.h")), "dimension", "The composer once it has text: a panel with the model picker, microphone and send along its bottom.", "Sampled", rd("size.composerOpen.h")["capture"]),
        "composerButton": tok(px(pt_of("size.composerButton")), "dimension", "Round + and microphone buttons inside the composer.", "Sampled", rd("size.composerButton")["capture"]),
        "sendButton": tok(px(pt_of("size.send")), "dimension", "Round send button (a circle).", "Sampled", rd("size.send")["capture"]),
        "searchField": tok(px(pt_of("size.search.h")), "dimension", "Search field height in a sheet (glass capsule).", "Sampled", rd("size.search.h")["capture"]),
        "chip": tok(px(pt_of("size.chip.h")), "dimension", f"Filter chip height; 'All' is {rd('size.chip.w')['value']} wide.", "Sampled", rd("size.chip.h")["capture"]),
        "segment": tok(px(pt_of("size.segment.h", "light")), "dimension", f"Segment height in the Pull Requests sheet (light only); 'All' is {rd('size.segment.w', 'light')['value']} wide.", "Sampled", rd("size.segment.h", "light")["capture"]),
        "capsuleButton": tok(px(pt_of("size.continue.h")), "dimension", f"Small capsule button (Continue): {rd('size.continue')['value']} wide.", "Sampled", rd("size.continue.h")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch")), "dimension", "Switch track.", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(pt_of("size.switch", "dark", 1)), "dimension", f"Switch track height ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb width (a pill {rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "tile": {
            "width": tok(px(tile_w), "dimension", "Inbox tile width, rim included: two tiles per row.", "Sampled", rd("size.tile.x")["capture"]),
            "height": tok(px(tile_h), "dimension", "Inbox tile height, rim included.", "Sampled", rd("size.tile.y")["capture"]),
        },
        "iconButton": derived("42px", "dimension", f"Round action buttons in the agent details sheet: {rd('size.iconButton')['value']} dark, {rd('size.iconButton', 'light')['value']} light."),
        "avatar": tok(px(pt_of("size.avatar")), "dimension", "Profile avatar (an initial on a grey circle).", "Sampled", rd("size.avatar")["capture"]),
        "menuWidth": tok(px(round(pt_of("size.menu.w"))), "dimension", f"Pull-down menu width ({rd('size.menu.w')['value']}); the Group by pop-up is {rd('size.popup.w')['value']}.", "Sampled", rd("size.menu.w")["capture"]),
        "grabber": {
            "width": tok(px(pt_of("size.grabber")), "dimension", "Sheet grabber width.", "Sampled", rd("size.grabber")["capture"]),
            "height": tok(px(pt_of("size.grabber", "dark", 1)), "dimension", "Sheet grabber height.", "Sampled", rd("size.grabber")["capture"]),
        },
        "chartBar": tok(px(pt_of("size.bar")), "dimension", "Width of one bar in the profile charts; bars have round tops.", "Sampled", rd("size.bar")["capture"]),
        "heatDot": tok(px(pt_of("size.heatDot", "light")), "dimension", "Dot in the profile's activity heatmap (light only).", "Sampled", rd("size.heatDot", "light")["capture"]),
        "touchTarget": derived("44px", "dimension", "Nav buttons, rows and the composer are 44 pt or more. Chips (38 pt), the send button (35 pt) and the composer + (36 pt) are smaller and sit inside larger bars."),
    }
    c["border"] = {"width": {
        "hairline": derived("1px", "dimension", "Row dividers and the tile rim: the divider is anti-aliased over two device pixels (border.dividerColour reads the darker row), so about 1 pt."),
    }}
    c["fontFamily"] = {
        "base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms are a neo-grotesque close to the iOS system face; use the platform font.", "Not captured", MEASURED),
        "mono": tok("monospace", "fontFamily", "Not determinable from pixels. Inline code, chart axis labels and the version footer use a monospace face; use the platform monospace.", "Not captured", MEASURED),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Body, rows, subtitles, stat values. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Large page titles and the agent title in its details sheet. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Sheet titles and bold runs in agent replies. Judged by stroke width."),
    }

    def ty(size_rid, weight, lh, desc, extra=(), family="base"):
        sizes = [rd(r)["value"] for r in (size_rid,) + tuple(extra)]
        v = {"fontFamily": "{fontFamily.%s}" % family, "fontWeight": "{fontWeight.%s}" % weight,
             "fontSize": sizes[0].replace("pt", "px")}
        if lh:
            v["lineHeight"] = lh
        return tok(v, "typography", desc + f" Cap-height readings: {', '.join(sorted(set(sizes)))}.", "Derived", rd(size_rid)["capture"])

    lines = lambda rid: f"{round(float(rd(rid)['value'].rstrip('pt')))}px"
    c["typography"] = {
        "largeTitle": ty("type.largeTitle", "medium", None, "Large page titles (Inbox, All Agents, a repo name).", ("type.largeTitle",)),
        "statValue": ty("type.statValue", "regular", None, "Big numbers on the profile (947M, 71, 3d)."),
        "detailTitle": ty("type.detailTitle", "medium", lines("lines.detailTitle"), "The agent's title in its details sheet, centred."),
        "profileName": ty("type.profileName", "regular", None, "The account name on the profile."),
        "title": ty("type.navTitle", "semibold", None, "Sheet titles (Profile, Model, Customize).", ("type.sheetTitle",)),
        "body": ty("type.body", "regular", lines("lines.body"), "Agent replies, row titles, menu items and the composer.", ("type.rowTitle", "type.menuItem", "type.composer")),
        "subheadline": ty("type.subtitle", "regular", lines("lines.empty"), "Row status lines, section and group headers, chips, tile labels, stat labels and empty states.", ("type.sectionHeader", "type.chip", "type.tileLabel", "type.statLabel", "type.emptyTitle", "type.emptyBody")),
        "code": ty("type.code", "regular", None, "Inline code in agent replies.", family="mono"),
        "caption": ty("type.chartAxis", "regular", None, "Chart axis labels and dates; the version footer uses the same monospace in upper case.", family="mono"),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (nav buttons, the composer, search fields, menus, the 7 PRs and Continue capsules): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: the light theme's glass controls and menus carry a soft shadow; it was not measured",
        "Line heights of titles and one-line labels: only multi-line blocks were measured",
        "The activity heatmap in dark: the profile bottom was captured in light only",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def scrim(theme):
    ref, dim = rd("scrim.ref", theme)["value"], rd("scrim.sheet", theme)["value"]
    a = 1 - int(dim[1:3], 16) / int(ref[1:3], 16)
    return derived("#000000%02X" % round(a * 255), "color",
                   f"Black at {round(a * 100)}%: the thread reads {ref} undimmed and {dim} under the Model sheet (a full-height sheet leaves {rd('scrim.fullSheet', theme)['value']} above it).",
                   rd("scrim.sheet", theme)["capture"])


def light_only(theme, rid, desc, dark_alias, why):
    """A role read in light only. Dark points at the closest role and is labelled Not captured."""
    if theme == "light":
        return from_reading(rid, "light", "color", desc)
    return tok("{" + dark_alias + "}", "color", desc + " Not captured in dark: " + why, "Not captured", rd(rid, "light")["capture"])


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Repo lists, Inbox, All Agents and the agent thread."),
            "sheet": f("bg.sheet", "Sheets (Customize, Search, Model, Profile, Add Workspace, Context). The same value as surface.card."),
            "sheetGrouped": f("bg.sheetGrouped", "The Changes sheet behind its file rows."),
            "scrim": scrim(theme),
        },
        "surface": {
            "card": f("surface.card", "Inbox tiles, the Changes card in a thread and the file rows of the Changes sheet."),
            "secondary": f("surface.secondary", "Selected filter chip, the photo-access card, inline code and the empty-heatmap dot (light)."),
            "inset": f("surface.inset", "An expanded file row's diff area ('Diff not available')."),
            "avatar": f("surface.avatar", "Initial avatar on the profile and in the Inbox nav button."),
            "iconButton": f("surface.iconButton", "Round action buttons in the agent details sheet (Rename, Unpin, Share)."),
            "glass": f("surface.composer", "Glass capsules and circles: the composer, the '7 PRs' capsule, nav buttons. A centre reading of a material that tints with what is behind it."),
            "glassField": f("surface.search", "Search fields in sheets (glass capsule)."),
            "glassButton": f("surface.composerButton", "The round + and microphone buttons inside the composer."),
            "composerPanel": f("surface.composerOpen", "The expanded composer panel once text is typed."),
            "menu": f("surface.menu", "Pull-down menus (glass). The reading picks up what is behind the menu."),
            "popup": f("surface.popup", "Pop-up menus over a sheet (Group by)."),
            "continue": f("surface.continue", "Small capsule button inside a card (Continue), glass."),
            "segment": light_only(theme, "surface.segment", "Selected segment in the Pull Requests sheet (All / Merged / Closed). The light reading equals surface.secondary.", "color.surface.secondary", "the Pull Requests sheet was captured in light only, so dark points at surface.secondary, the selected chip's fill."),
            "grabber": f("surface.grabber", "Sheet grabber."),
        },
        "border": {
            "divider": f("border.dividerColour", "Hairline between rows, inset to the row text."),
            "tile": f("border.tile", "Rim around Inbox tiles."),
            "menu": f("border.menuDivider", "Divider between groups of menu items."),
            "chartGrid": f("border.chartGrid", "Gridlines in the profile charts."),
        },
        "text": {
            "primary": f("text.primary", f"Titles, row titles, agent replies, menu items. Large titles read {rd('text.largeTitle', theme)['value']}."),
            "emphasis": f("text.navTitle", f"Sheet titles and glyphs on glass buttons (back chevron reads {rd('text.glyph', theme)['value']}): pure white in dark, black in light, a step past text.primary."),
            "muted": f("text.muted", f"Action rows (New Project), unselected chips and card text: between primary and secondary. Readings {', '.join(sorted({rd(r, theme)['value'] for r in ('text.muted', 'text.chip', 'text.onBanner')}))}."),
            "secondary": f("text.secondary", f"Row status lines, section and group headers, stat labels, empty states. Readings range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.secondary', 'text.sectionHeader', 'text.groupHeader', 'text.stat', 'text.empty')}))}."),
            "tertiary": f("text.tertiary", f"Repo names after a status line, tile counts, chevrons and outline row icons. Readings range {', '.join(sorted({rd(r, theme)['value'] for r in ('text.tertiary', 'text.count', 'text.chevron', 'text.icon')}))}."),
            "placeholder": f("text.placeholder", f"Composer placeholder (search fields read {rd('text.searchPlaceholder', theme)['value']})."),
            "code": f("text.code", "Inline code text, on surface.secondary."),
        },
        "accent": {
            "default": f("accent.unread", "Unread dots and the Working tile icon: the app's one accent."),
            "switch": f("switch.on", "Switch on track."),
        },
        "focus": {
            "caret": f("accent.caret", "Text caret in a focused field: the only focus indicator (no ring)."),
        },
        "diff": {
            "add": f("text.diffAdd", "Lines added in a diffstat (+17)."),
            "delete": f("text.diffDelete", "Lines deleted in a diffstat (-12)."),
        },
        "status": {
            "merged": f("status.merged", "Merged branch icon on agent rows and pull requests."),
            "draft": f("status.draft", "Draft pull-request icon: the tertiary grey."),
            "closed": light_only(theme, "status.closed", "Closed pull-request icon.", "color.diff.delete", "the Pull Requests sheet was captured in light only, so dark points at diff.delete, the same pink-red family."),
            "unread": alias("color.accent.default", "color", "Unread agent: a blue dot before the title."),
            "read": f("dot.read", "Read agent: a grey dot before the title."),
            "success": alias("color.diff.add", "color", "Success: no success message was seen; the diffstat green is the only green."),
            "danger": alias("color.diff.delete", "color", "Danger: no error was seen; the diffstat pink-red is the only red."),
        },
        "icon": {
            "allAgents": f("icon.allAgents", "All Agents tile icon (red-orange)."),
            "attention": f("icon.attention", "Needs Attention tile icon (amber bell)."),
            "working": f("icon.working", "Working tile icon (blue dots)."),
            "review": f("icon.review", "In Review tile icon (magenta)."),
            "projectTeal": f("icon.projectA", "Project icon colour (teal); each project gets a colour."),
            "projectViolet": f("icon.projectB", "Project icon colour (violet)."),
        },
        "chart": {
            "bar": f("chart.bar", "Bars in the profile's Tokens and Agents charts, the same orange in both themes."),
        },
        "switch": {
            "on": alias("color.accent.switch", "color", "Switch on track."),
            "off": f("switch.off", "Switch off track."),
            "thumb": f("switch.thumb", "Switch thumb, both states (light adds a blue rim when on)."),
        },
        "button": {
            "send": {"bg": f("button.send", "Send button: the inverse of the theme (near-white in dark, near-black in light)."),
                     "glyph": f("button.sendGlyph", "Arrow on the send button.")},
            "mic": {"bg": f("button.mic", "Microphone button beside send in the expanded composer.")},
            "clear": {"bg": f("button.clear", "Clear button in a typed search field: white in dark, black in light.")},
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Warning and error colours: no warning or error state was seen",
        "Pressed states: stills only",
        "Light-only roles (surface.segment, status.closed): their dark tokens point at the closest dark role and are labelled Not captured",
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
        "dark": semantic("dark"),
        "$themes": [  # PRODUCT (adapt): how each theme was set for the capture; drop a theme the app lacks
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "The phone set to light mode (Cursor follows the phone; it has no appearance setting), switched back afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "The phone in dark mode, its own setting. Read from screenshots/dark/."},
        ],
        "$metadata": {"tokenSetOrder": ["core", "light", "dark"]},
    }
    check(doc)
    (PKG / "tokens.json").write_text(json.dumps(doc, indent=1, ensure_ascii=False) + "\n")
    n = sum(1 for s in ("core", "light", "dark") for _ in walk(doc[s]))
    print(f"tokens.json: {n} tokens")


if __name__ == "__main__":
    if not READ:
        raise SystemExit("no raw/readings.json: run tools/measure.py first")
    build()
