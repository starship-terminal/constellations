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
    ids = ["bg.page", "bg.list", "bg.groupedSystem", "surface.button", "neutral.muted", "surface.glass",
           "surface.tabSelected", "surface.fab", "surface.gutter", "border.divider", "border.section",
           "text.primary", "text.secondary", "text.sectionHeader", "neutral.emphasis", "switch.off"]
    seen = {}
    for rid in ids:
        for theme, r in READ[rid].items():
            v = r["value"]
            rr, gg, bb = int(v[1:3], 16), int(v[3:5], 16), int(v[5:7], 16)
            if max(rr, gg, bb) - min(rr, gg, bb) <= 20:     # neutral enough (GitHub's greys lean blue)
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


# PRODUCT (adapt) from here to semantic()'s end: the mapping from readings to tokens.
def core():
    c = {}
    c["color"] = {"neutral": neutral_ramp()}
    c["radius"] = {
        "card": derived("26px", "dimension", f"Grouped cards (Home, Explore, Settings, Code Options): {rd('radius.card')['value']} on Home in both themes, {rd('radius.cardSettings')['value']} in Settings, {rd('radius.codeCard')['value']} on the code preview. Plus or minus 2 pt."),
        "button": derived("14px", "dimension", f"Full-width and paired buttons (Add Favorites, Star): {rd('radius.button')['value']} dark and {rd('radius.button', 'light')['value']} light on Add Favorites, {rd('radius.buttonRepo')['value']} and {rd('radius.buttonRepo', 'light')['value']} on Star. Plus or minus 2 pt."),
        "status": derived("12px", "dimension", f"The profile status card: {rd('radius.status')['value']} in both themes."),
        "tile": derived("7px", "dimension", f"Coloured icon tiles in rows: {rd('radius.tile')['value']} on a 32 pt tile."),
        "branch": derived("3px", "dimension", "Branch-name pills ('main'): the 1 px rim turns its corner over about 6 px (3 pt) in dark/05 and light/05; read from the pixels, not with diag, because the rim stops the diagonal walk."),
        "capsule": derived("999px", "dimension", "Fully round ends: filter chips, state badges (Open, Draft, Merged, Locked), issue labels, status chips, the New badge, switches, the tab bar and its selected pill, glass nav buttons, the search field and the floating New Session button."),
    }
    c["space"] = {
        "base": derived("4px", "dimension", "Measured gaps land on multiples of 4 pt within a pixel or two, except the 13 to 14 pt title gap."),
        "xs": derived("4px", "dimension", "Gap between a state badge and the next badge or pill."),
        "sm": derived("8px", "dimension", "Gap between filter chips (8 to 9 pt in 03 and 13)."),
        "md": derived("12px", "dimension", "Gap between an icon tile and its row title (12 pt: tile ends at 76 pt, text starts at 88 pt in 01)."),
        "lg": derived("16px", "dimension", "Screen margin: cards, section titles and full-bleed list text start 16 pt from the screen edge (x 48 px in every capture)."),
        "xl": derived("20px", "dimension", "Padding inside a grouped card: the icon tile and settings row text start 20 pt from the card's edge."),
        "titleGap": derived("14px", "dimension", "From a section title's baseline area to its card: 13.5 pt from the cap bottom of 'My Work' to the card in 01, 13 pt for 'Favorites'."),
        "sectionGap": derived("36px", "dimension", "From a card's bottom to the next section title's cap top: 37 pt in 01 (card ends at y 713, 'Favorites' caps start at 787)."),
        "screenMargin": alias("space.lg", "dimension", "Left and right margin of cards, titles and list rows."),
        "cardPadding": alias("space.xl", "dimension", "Inner padding of grouped cards."),
    }
    c["size"] = {
        "row": tok("57px", "dimension", f"Grouped row with an icon tile (Home My Work, Explore, repository, profile) and search scope rows, divider to divider: dividers at {rd('rows.home')['value'][0]} and {rd('rows.home')['value'][5]} px in 01.", "Sampled", rd("rows.home")["capture"]),
        "rowSettings": tok("53px", "dimension", "Settings row without a tile: dividers 106 to 107 px apart in 21 (452, 558, 665, 774, 881).", "Sampled", rd("rows.settings")["capture"]),
        "navButton": tok("45px", "dimension", f"Round glass back, close and more buttons: {rd('size.navButton.w')['value']} wide dark, {rd('size.navButton.w', 'light')['value']} light, {rd('size.navButton.h')['value']} tall, the glass rim's soft edge included.", "Sampled", rd("size.navButton.h")["capture"]),
        "tabBar": {
            "height": tok(px(pt_of("size.tabBar.h")), "dimension", "Floating glass tab bar (Home, Inbox, Explore, Copilot).", "Sampled", rd("size.tabBar.h")["capture"]),
            "width": tok(px(pt_of("size.tabBar.w")), "dimension", "Tab bar width, inset from the screen edges.", "Sampled", rd("size.tabBar.w")["capture"]),
        },
        "searchField": tok(px(pt_of("size.search.h")), "dimension", "Search field (glass capsule) at the top of search.", "Sampled", rd("size.search.h")["capture"]),
        "chip": derived("29px", "dimension", f"Filter chip height: {rd('size.chip.h')['value']} dark, {rd('size.chip.h', 'light')['value']} light, glass rim included."),
        "button": tok(px(round(pt_of("size.button", "dark", 1))), "dimension", f"Full-width and paired buttons (Add Favorites {rd('size.button')['value']}, Star {rd('size.buttonRepo')['value']}).", "Sampled", rd("size.button")["capture"]),
        "iconButton": tok(px(pt_of("size.iconButtonRepo", "dark", 1)), "dimension", f"Square icon button beside Star (fork, watch): {rd('size.iconButtonRepo')['value']}.", "Sampled", rd("size.iconButtonRepo")["capture"]),
        "buttonCompact": tok(px(pt_of("size.doneButton", "dark", 1)), "dimension", f"Inline buttons in a card: Copilot's 'Email me a download link' ({rd('size.doneButton')['value']}), Configure ({rd('size.configure')['value']}).", "Sampled", rd("size.doneButton")["capture"]),
        "fab": tok(px(pt_of("size.fab", "light", 1)), "dimension", f"Floating New Session button ({rd('size.fab', 'light')['value']} in light, where its ink fill gives a clean edge).", "Sampled", rd("size.fab", "light")["capture"]),
        "switch": {
            "width": tok(px(pt_of("size.switch")), "dimension", "Switch track.", "Sampled", rd("size.switch")["capture"]),
            "height": tok(px(pt_of("size.switch", "dark", 1)), "dimension", f"Switch track height ({rd('size.switch')['value']}).", "Sampled", rd("size.switch")["capture"]),
            "thumb": tok(px(pt_of("size.switchThumb")), "dimension", f"Switch thumb width (a pill {rd('size.switchThumb')['value']}).", "Sampled", rd("size.switchThumb")["capture"]),
        },
        "badge": tok(px(round(pt_of("size.badge", "dark", 1))), "dimension", f"State badge height (Open {rd('size.badge')['value']}, Draft {rd('size.draft')['value']}).", "Sampled", rd("size.badge")["capture"]),
        "branch": derived("26px", "dimension", f"Branch-name pill height: {rd('size.branch')['value']} dark, {rd('size.branch', 'light')['value']} light."),
        "statusChip": tok(px(pt_of("size.chipStatus", "dark", 1)), "dimension", f"Agent-session status chip (Completed, Failed): {rd('size.chipStatus')['value']}.", "Sampled", rd("size.chipStatus")["capture"]),
        "newBadge": derived("22px", "dimension", f"The 'New' badge before a settings row: {rd('size.newBadge')['value']}."),
        "label": derived("19px", "dimension", f"Issue label capsule ('area: documentation' {rd('size.label')['value']})."),
        "tile": tok(px(pt_of("size.tile")), "dimension", f"Coloured icon tile in a row: {rd('size.tile')['value']} dark, {rd('size.tile', 'light')['value']} light.", "Sampled", rd("size.tile")["capture"]),
        "avatar": {
            "header": derived("40px", "dimension", f"Account avatar at the top left of Home: {rd('size.avatarHeader')['value']}, anti-aliased edge included."),
            "comment": tok(px(pt_of("size.avatarComment")), "dimension", "Comment and PR author avatar.", "Sampled", rd("size.avatarComment")["capture"]),
            "profile": tok(px(pt_of("size.avatarProfile")), "dimension", "Profile avatar.", "Sampled", rd("size.avatarProfile")["capture"]),
        },
        "touchTarget": derived("44px", "dimension", "Nav buttons, icon buttons, rows and full buttons are 44 pt or more. Chips (29 pt), badges and the compact buttons (34 pt) are smaller."),
    }
    c["border"] = {"width": {
        "hairline": derived("0.5px", "dimension", "Dividers between rows and between list sections: one device pixel at 2x, anti-aliased over two rows."),
    }}
    c["fontFamily"] = {
        "base": tok("system", "fontFamily", "Not determinable from pixels. The letterforms are close to the iOS system face; use the platform font.", "Not captured", MEASURED),
        "mono": tok("system-mono", "fontFamily", "Code, diffs, branch names and search qualifiers use a monospace face. Not determinable from pixels; use the platform monospace.", "Not captured", MEASURED),
    }
    c["fontWeight"] = {
        "regular": derived(400, "fontWeight", "Body text, row titles, settings rows, meta lines. Judged by stroke width, not measured."),
        "medium": derived(500, "fontWeight", "Badge and chip labels, tab labels. Judged by stroke width."),
        "semibold": derived(600, "fontWeight", "Nav titles, button labels, empty-state titles. Judged by stroke width."),
        "bold": derived(700, "fontWeight", "The large title, section titles, issue and repository titles, grouped section headers. Judged by stroke width."),
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
        "largeTitle": ty("type.largeTitle", "bold", None, "Tab root titles (Inbox, Explore, Copilot)."),
        "title": ty("type.title1", "bold", lines("lines.title1"), "Issue and PR titles, Home and Explore section titles, empty-state lines (semibold there).", ("type.title2", "type.emptyTitle")),
        "headline": ty("type.navTitle", "semibold", None, "Nav titles and button labels.", ("type.button",)),
        "body": ty("type.body", "regular", lines("lines.body"), "Comment and Markdown body text, Settings rows.", ("type.settingsRow",)),
        "rowTitle": ty("type.headline", "regular", None, "Titles of rows in a grouped card (Issues, Top Repositories) and the row age.", ("type.time",)),
        "callout": ty("type.inboxTitle", "regular", lines("lines.headline"), "Inbox, issue and PR row titles, result owner lines, banner text (on the same 20 pt line).", ("type.meta",)),
        "sectionHeader": ty("type.sectionHeader", "bold", None, "Grey grouped section headers on Code Options (Preview, Display, Editing)."),
        "caption": ty("type.chip", "medium", None, "Filter chip and state badge labels.", ("type.badge",)),
        "footnote": ty("type.footnote", "regular", None, "Author role labels (Member, Contributor)."),
        "tab": ty("type.tab", "medium", None, "Tab bar labels."),
        "code": ty("type.mono", "regular", lines("lines.diff"), "Diff code, one row per line; the code preview runs on a " + lines("lines.code") + " line.", (), "mono"),
    }
    c["$extensions"] = {"notTokenised": [
        "iOS 26 glass (nav buttons, the tab bar, the search field, filter chips, menus, the dark New Session button): blur and refraction come from the system material",
        "Continuous (squircle) corners: DTCG has no value for corner smoothing",
        "Motion and easing: stills only",
        "Shadows: none drawn; separation comes from the page and card fills and the glass material",
        "Issue and PR label colours: each repository sets its own, so they are data, not tokens",
        "Line heights of one-line labels: only multi-line blocks were measured",
    ]}
    return c


# ---------------------------------------------------------------- semantic sets

def dark_only(theme, rid, desc, light_from=None, why=""):
    """A role read in dark only. Light reuses the dark value (light_from None) or the light value of
    the closest role, as Derived, and says which."""
    if theme == "dark":
        return from_reading(rid, "dark", "color", desc)
    src = rd(light_from, "light") if light_from else rd(rid, "dark")
    return derived(src["value"], "color", desc + " Not captured in light: " + why, src["capture"])


TILES = [("green", "Issues"), ("gray", "Top Repositories, Repositories"), ("yellow", "Starred"), ("blue", "Pull Requests"),
         ("purple", "Discussions, Trending Repositories"), ("gold", "Actions"), ("pink", "Agents"), ("red", "Awesome Lists"),
         ("orange", "Organizations")]


def semantic(theme):
    f = lambda rid, desc, typ="color": from_reading(rid, theme, typ, desc)
    s = {"color": {
        "bg": {
            "page": f("bg.page", "Page behind grouped cards: Home, Explore, Copilot, Settings, Appearance, the Filters sheet."),
            "list": f("bg.list", "Full-bleed list and detail pages: Inbox, search scopes, Issues, Pull Requests, the repository, issue and PR pages. The same value as surface.card."),
            "grouped": f("bg.groupedSystem", "Code Options, a system grouped table: the iOS grouped background, not the GitHub page colour."),
        },
        "surface": {
            "card": f("surface.card", f"Grouped cards, list rows and the code preview. Settings cards read {rd('surface.cardSettings', theme)['value']}, Code Options cells {rd('surface.cardSystem', theme)['value']}."),
            "button": f("surface.button", f"Neutral buttons (Add Favorites, Get started, Star, fork and watch; Star reads {rd('surface.buttonRepo', theme)['value']})."),
            "muted": f("neutral.muted", f"Muted fills: the Locked badge, agent-session status chips ({rd('neutral.chip', theme)['value']}) and the profile status card ({rd('surface.status', theme)['value']})."),
            "glass": f("surface.glass", f"Glass controls (tab bar, nav buttons, search field, filter chips) over an empty page; nav buttons read {rd('surface.navButton', theme)['value']}. The material tints with what is behind it."),
            "tabSelected": f("surface.tabSelected", "The selected tab's pill inside the tab bar."),
            "menu": dark_only(theme, "surface.menu", "Pull-down and pop-up menus (glass; the reading picks up the page behind).", "surface.glass", "filled from surface.glass, the closest light role."),
            "fab": f("surface.fab", "Floating New Session button: grey glass in dark, the theme's ink in light."),
            "code": f("surface.code", "Unchanged lines in a diff."),
            "gutter": f("surface.gutter", "Line-number gutter of unchanged diff lines."),
        },
        "border": {
            "divider": f("border.divider", "Hairline between rows in a card or list, inset to the row text."),
            "section": f("border.section", "Full-width hairline between list sections (under the Inbox chips, around the notification banner)."),
        },
        "text": {
            "primary": f("text.primary", "Titles, row titles, body text, button labels on neutral buttons."),
            "secondary": f("text.secondary", f"Meta lines (repository and number), row values, ages, empty-state bodies, line numbers. Readings in this role: {', '.join(sorted({rd(r, theme)['value'] for r in ('text.secondary', 'text.rowValue', 'text.time', 'text.emptyBody', 'text.lineNumber')}))}."),
            "sectionHeader": f("text.sectionHeader", "Grouped section headers on Code Options: the system grey, not GitHub's."),
            "placeholder": dark_only(theme, "text.placeholder", "Search field placeholder.", "text.secondary", "filled from text.secondary, the closest light role."),
            "link": f("text.link", f"Links and text buttons (View All, Configure reads {rd('accent.text', theme)['value']}, hunk headers {rd('text.hunk', theme)['value']})."),
            "onEmphasis": f("text.onEmphasis", f"Labels on filled badges and buttons (Merged, Draft, Open, the purple Copilot button {rd('text.onDone', theme)['value']}, New Session {rd('text.onFab', theme)['value']})."),
            "tab": f("text.tab", "Unselected tab label and icon."),
            "tabSelected": f("text.tabSelected", "Selected tab label and icon: the accent."),
        },
        "accent": {
            "fg": f("accent.fg", "Unread dots, the Appearance tick, the search caret and links."),
            "emphasis": f("accent.emphasis", "Switch on: in dark the same blue as accent.fg."),
            "subtle": f("accent.subtle", f"Tinted fills behind accent text: Configure, the New badge, unread counts, branch-name pills ({rd('accent.branch', theme)['value']}), hunk headers ({rd('diff.hunk', theme)['value']})."),
        },
        "focus": {
            "caret": dark_only(theme, "accent.caret", "Text caret in a focused field: the only focus indicator (no ring). A one-pixel column, so the share is low.", "accent.fg", "filled from accent.fg, the closest light role (the caret blinked off in light/08)."),
        },
        "success": {
            "fg": f("text.success", "Additions in a diffstat, open-issue and open-PR icons" + (f" (the open-issue icon reads {rd('icon.success')['value']})." if theme == "dark" else ".")),
            "emphasis": dark_only(theme, "success.emphasis", "The Open state badge, white label.", "tile.green", "filled from tile.green, the Issues tile, the closest light green."),
        },
        "danger": {
            "fg": f("text.danger", f"Deletions in a diffstat and failure icons (the Failed agent-session icon reads {rd('icon.danger', theme)['value']}). No red fill was seen."),
        },
        "attention": {
            "subtle": f("attention.subtle", "The Archived banner under a repository's nav bar."),
            "fg": f("text.attention", "Archived banner text and icon."),
        },
        "done": {
            "fg": f("text.done", "Purple text buttons (Dismiss on the Copilot card)."),
            "emphasis": f("done.emphasis", "The Merged state badge."),
            "button": f("done.button", "The filled purple Copilot button ('Email me a download link')."),
        },
        "neutral": {
            "emphasis": f("neutral.emphasis", "The Draft state badge, white label."),
        },
        "diff": {
            "addition": f("diff.addition", "Added line."),
            "additionGutter": f("diff.additionGutter", "Gutter of an added line."),
            "deletion": f("diff.deletion", "Deleted line."),
            "deletionGutter": f("diff.deletionGutter", "Gutter of a deleted line."),
            "hunk": f("diff.hunk", "Hunk header row; its text is text.link."),
        },
        "syntax": {
            "keyword": f("syntax.keyword", "Keywords in code ('def', 'return', 'end')."),
            "entity": f("syntax.entity", "Function and entity names."),
            "constant": f("syntax.constant", "Numbers and constants."),
        },
        "switch": {
            "on": alias("color.accent.emphasis", "color", "Switch on track."),
            "off": f("switch.off", "Switch off track."),
            "thumb": f("switch.thumb", "Switch thumb, both states."),
        },
        "tile": {name: f(f"tile.{name}", f"Icon tile behind a white glyph: {rows}. A Derived reading means the glyph covers part of the box.")
                 for name, rows in TILES},
        "button": {
            "neutral": {"bg": alias("color.surface.button", "color", "Neutral button fill."),
                        "text": alias("color.text.primary", "color", "Neutral button label.")},
            "accent": {"bg": alias("color.accent.subtle", "color", "Accent button fill (Configure)."),
                       "text": alias("color.text.link", "color", "Accent button label.")},
            "done": {"bg": alias("color.done.button", "color", "The purple Copilot button."),
                     "text": alias("color.text.onEmphasis", "color", "Its label.")},
            "fab": {"bg": alias("color.surface.fab", "color", "Floating New Session button."),
                    "text": alias("color.text.onEmphasis", "color", "Its label and icon.")},
        },
        "status": {
            "success": alias("color.success.fg", "color", "Success: green text and icons; the Open badge fills with success.emphasis."),
            "danger": alias("color.danger.fg", "color", "Danger: red text and icons."),
            "warning": alias("color.attention.fg", "color", "Warning: the archived banner's text."),
            "info": alias("color.accent.fg", "color", "Info: the blue accent."),
            "done": alias("color.done.emphasis", "color", "Done: GitHub's purple for merged and completed."),
        },
    }}
    s["$extensions"] = {"notTokenised": [
        "Danger fill: no red badge, button or banner was seen",
        "Pressed states: stills only",
        "Issue and PR label colours: set per repository",
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


class CheckError(ValueError):
    """A token file check() rejects. Raised explicitly so the check still runs under python3 -O."""


def check(doc):
    sets = [s for s in ("core", "light", "dark") if s in doc]  # a one-theme app has no light or no dark
    paths = {".".join(p) for name in sets for p, _ in walk(doc[name])}
    for name in sets:
        for p, t in walk(doc[name]):
            where = name + "." + ".".join(p)
            src = t.get("$extensions", {}).get("source", {})
            if not (src.get("evidence") and src.get("capture")):
                raise CheckError(f"{where}: no source")
            v = t["$value"]
            for a in aliases(v):
                if a not in paths:
                    raise CheckError(f"{where}: alias {{{a}}} points at nothing")
            if isinstance(v, str) and v.startswith("{"):
                continue
            elif t["$type"] == "color":
                if not re.fullmatch(r"#[0-9A-F]{6}([0-9A-F]{2})?", v):
                    raise CheckError(f"{where}: bad colour {v}")
            elif t["$type"] == "dimension":
                if not re.fullmatch(r"-?\d+(\.\d+)?px", v):
                    raise CheckError(f"{where}: bad dimension {v}")
    keys = lambda s: sorted(".".join(p) for p, _ in walk(doc[s]))
    if "light" in doc and "dark" in doc:
        if keys("light") != keys("dark"):
            raise CheckError("light and dark keys differ")


def build():
    doc = {
        "core": core(),
        "light": semantic("light"),
        "dark": semantic("dark"),
        "$themes": [  # PRODUCT (adapt): how each theme was set for the capture; drop a theme the app lacks
            {"id": "light", "name": "Light", "selectedTokenSets": {"core": "source", "light": "enabled"},
             "$description": "The app's Settings > Appearance > Light, set for the capture and put back to Automatic afterwards. Read from screenshots/light/."},
            {"id": "dark", "name": "Dark", "selectedTokenSets": {"core": "source", "dark": "enabled"},
             "$description": "Settings > Appearance > Automatic with the phone in dark mode. Read from screenshots/dark/."},
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
