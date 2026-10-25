#!/usr/bin/env python3
"""Write components.md from raw/components.<theme>.json, tokens.json and components/crops/.

    python3 tools/build_components_md.py

One entry per checklist component (docs/DESIGN-SYSTEM.md, desktop wording), listing the parts that
show it, the states captured in each theme with their crops, and the measured values written as the
token that holds them (the value after it). A value no token holds is written raw and counted.
PRODUCT (adapt): INVENTORY, NOTES and GAPS. Standard library only, deterministic.
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from colour import color, is_color  # noqa: E402

PKG = pathlib.Path(__file__).resolve().parent.parent
TOK = json.loads((PKG / "tokens.json").read_text())
CAP = {t: json.loads((PKG / "raw" / f"components.{t}.json").read_text()) for t in ("dark", "light")}
CROPS = {p.name for p in (PKG / "components" / "crops").glob("*.png")}
STATE_ORDER = ["default", "hover", "focus-visible", "focus", "pressed", "filled", "empty"]

# PRODUCT (adapt): checklist component -> (parts that show it, note)
INVENTORY = [
    ("Button", ["button-primary", "button-primary-inverse", "button-primary-inverse-sm", "button-inverse-sm", "button-secondary", "button-outline", "button-quiet", "button-danger-outline"],
     "Five looks. Ink-filled (`button-primary-inverse`: Create automation, Add wiki, Generate, Go to Customize; `bg.accent-neutral` with `text.primary-inverse`, so white on dark and near-black on light); outlined (`button-outline`: Customize, Comment; a `border.primary` hairline); a quiet text button (Reset all); the danger outline (Unlink user, `text.red` on the same hairline); and the accent-blue primary, which only the workbench's own dialogs use (Trust Workspace & Continue, 32px, white text). All have a 6px radius (`radius.6`); heights are 24, 28 and 32px. Disabled and loading were not seen."),
    ("Icon button", ["icon-button", "composer-tool", "voice-button", "send-button", "send-more", "dialog-close", "toast-close", "expand-button", "sidebar-trigger"],
     "28 x 28 ghost squares, 6px radius, `text.secondary` at rest; under the pointer and when pressed they take a `tint.secondary` wash and `text.primary`. The send button is a split pill: Send and More send options share one ink fill, greyed while the composer is empty."),
    ("Link", ["link", "text-link", "dialog-link", "text-button-warning"],
     "Links in replies and settings are `text.link` (blue at 85%) and turn `text.link-strong` under the pointer; the Restricted Mode banner's Trust workspace is a text button in the warning hue."),
    ("Text field", ["settings-search", "search-field", "text-field", "palette-input", "number-field"],
     "28px fields on a `tint.secondary` wash (dark) or `bg.elevated` (light) with a `border.secondary` hairline and a 6px radius; focus draws the 1px accent ring. The number field is a stepper (minus, value, plus)."),
    ("Text area", ["composer", "composer-editor"],
     "The composer: `bg.elevated`, a `border.primary` hairline, 20px radius (`radius.20`), 14px prompt text with a rotating tip as its placeholder. Typing enables the split send button; Local mode adds a footer of chips (machine, folder, agent)."),
    ("Select", ["select", "listbox", "option", "option-selected", "mode-button", "capability-button", "view-switch"],
     "Two triggers. Settings selects are outlined (`border.secondary`, 28px, 6px radius) and open a listbox with a check on the chosen option. The composer's mode (Agent) and capability (Normal) are text-only triggers that open menus."),
    ("Checkbox", ["checkbox"], "16px boxes with a 4px radius, filled `bg.accent-primary` with a white check when on (Settings > Notifications, the Mobile column)."),
    ("Radio", ["menu-radio-row", "segment-selected", "option-selected"], "Not present as radio buttons. Single choice is a menu of radio items with a check (the Agents view / IDE view switch), a segmented control (Cloud / Local) or a select."),
    ("Switch", ["switch-on", "switch-off", "switch-sm-on", "switch-sm-off"],
     "36 x 20, `bg.accent-primary` when on and `tint.secondary` when off, with a white knob; 28 x 16 inside menus (Compact view, Sync view settings)."),
    ("Tabs", ["segmented", "segment", "segment-selected", "filter-chip", "filter-chip-selected", "tab", "tab-selected", "review-tab", "review-tab-selected"],
     "One segmented control does the work of tabs: a `tint.tertiary` track with a 20px radius, pill segments in `text.secondary`, and the selected one raised (`tint.secondary` in dark, `bg.elevated` in light) with a `border.secondary` hairline and the small shadow. Cloud / Local, Automations' categories and the notifications' All / Unread use it; the PR review uses plain text tabs."),
    ("Menu", ["menu", "submenu", "context-menu", "view-menu", "menu-row", "menu-section-title", "menu-separator", "menu-submenu-trigger", "command-list", "command-option", "nav-popover", "nav-popover-row"],
     "Popups on `bg.elevated-wax` (the elevated fill at 94%) with a `border.secondary` outline, a 10px radius and the large shadow (`shadow.L4` in dark, `shadow.L3` in light); 30px rows with a 6px radius and a `tint.secondary` highlight; 12px section titles in `text.secondary`; separators of `border.secondary`. More opens a navigation popover of the same look."),
    ("Context menu", ["context-menu", "menu-row", "menu-separator"], "A right-click on a session row opens the same menu (Folder, Rename, Copy session link, Open in web browser, Mark unread, Archive, More)."),
    ("Tooltip", ["tooltip"], "Always dark, in both themes (the tooltip carries the `dark` class): the dark theme's `bg.elevated`, a hairline, a 6px radius, 12px text, and the shortcut as small key caps."),
    ("Dialog", ["dialog", "palette", "notifications-panel"],
     "Two kinds. The workbench's own dialog (Do you trust the authors...) is 480px wide with a 12px radius, a shield icon, and secondary and primary buttons, over a dimmed window. Devin's command palette (Search) is a 680px, 16px-radius sheet on `bg.elevated-wax` with the L4 shadow and no scrim."),
    ("Toast", ["toast", "toast-button", "toast-close"],
     "The workbench's notification toast (The terminal process failed to launch...): 450px, 10px radius, an error icon in `text.red`, a close button and an Open Help button, bottom right."),
    ("Card", ["settings-card", "card", "banner-info", "banner-warning", "callout-info", "agent-row"],
     "Settings group rows on `bg.elevated` with a `border.secondary` hairline and a 10px radius, inside a `tint.tertiary` frame; automation templates are 12px cards on the same fill. The warning banner (Restricted Mode) is an 18px-radius pill on `bg.orange` with `text.orange`; the info banner has a blue left rule."),
    ("List row", ["sidebar-row", "sidebar-row-selected", "session-row", "settings-nav", "settings-nav-selected", "palette-row", "palette-row-selected", "notification-row", "explorer-row", "quick-input-row", "quick-input-row-focused"],
     "30px rows with a 6px radius; the current one takes a `tint.secondary` fill, and hover the same wash. Session rows are two lines (title, then time, PR count, trigger and source icons) with an unread dot on the right and actions (pin, folder, more) under the pointer."),
    ("Table", [], "Not present: lists (sessions, automations, wikis, PRs to review) are rows and cards, not tables."),
    ("Avatar", ["avatar", "identity"], "A 20px round photo beside the account name and organisation in the sidebar header."),
    ("Badge", ["badge-merged", "pr-badge", "unread-dot", "integration-badge", "kbd", "keybinding", "status-text"],
     "The PR status pill (Merged: `bg.purple` with `text.purple`, full radius); the sidebar's PR count in purple; the unread dot in `text.accent-primary`; integration chips (Slack, GitHub); keyboard caps; and plain status text (Enabled in `text.green`)."),
    ("Toolbar", ["left-header", "titlebar", "command-center", "status-bar", "panel-tab"],
     "The Agents view has only its 44px page headers; the IDE view has a 40px title bar with the command center, a 22px status bar and the panel's tab strip."),
    ("Inspector", ["agent-pane"], "The IDE view's right-hand agent pane (300px), a full Devin session beside the editor; in a session, the Agents view splits into the conversation and a Changes or PR pane."),
    ("Conversation", ["user-message", "agent-name", "status-line", "worked-row", "thoughts-row", "hook-error", "inline-code", "diff-file-header", "diff-line-added", "diff-line-removed", "session-title"],
     "Not on the checklist; the core of the product. The user's prompt is a right-aligned `tint.tertiary` bubble with a 16px radius; Devin's reply is plain 13px text under a name line; work folds into muted Worked for, Thoughts and Read rows; a status line closes each turn (Devin is awaiting instructions). Diffs are full-width rows tinted `tint.green` and `tint.red` over `bg.elevated`."),
    ("IDE", ["side-bar", "editor", "editor-tab", "line-numbers", "editor-empty", "quick-input", "quick-input-box", "terminal", "panel", "banner"],
     "The workbench under Devin's own theme: every VS Code colour is one of the same values (`ide.*`); the restricted-mode banner, quick open and the command palette, the editor and the terminal panel."),
]
GAPS = [
    "Approval prompt: the local agent (Devin Local, devin-cli) runs in the owner's Bypass Permissions mode, so no approval appeared; nothing was changed to force one.",
    "Destructive confirmation: none reachable without acting. Sessions have no delete (Archive acts at once), and Unlink user was not clicked. The workbench's trust dialog stands in as the confirmation pattern, cancelled.",
    "Table: Devin has no tables in the captured screens.",
    "Disabled and loading buttons were not seen (the send button's empty state is the only disabled control captured); no form validation error was reachable (settings apply on change).",
    "Onboarding: the account is set up; only empty-state hints (the composer's rotating tips, the IDE's Devin Cloud intro card) were seen.",
    "Pressed states set Base UI's `data-pressed` on the part while `:active` is forced (see the README); segments have no pressed shot because `data-pressed` is their selected state.",
    "The diff2html (`--d2h-*`) colours and the Sonner toaster's variables are in raw/css-vars.*.json but not tokenised: the first are a library's defaults, the second never showed.",
]


def flat(tree, prefix=()):
    for k, v in tree.items():
        if k.startswith("$"):
            continue
        if isinstance(v, dict) and "$value" in v:
            yield prefix + (k,), v
        elif isinstance(v, dict):
            yield from flat(v, prefix + (k,))


CORE = dict(flat(TOK["core"]))
SETS = {t: dict(flat(TOK[t])) for t in ("light", "dark")}
CORE_NAMES = re.compile(r"^(text|bg|border|tint)\.(primary|secondary|tertiary|disabled|page|wash|elevated|elevated-wax|accent-primary|accent-neutral|link|primary-inverse|always-white)$")
PREFER = ["role", "text", "bg", "border", "tint", "hue", "shadow-color", "ide"]


def resolve(t, v):
    while isinstance(v, str) and re.fullmatch(r"\{[^{}]+\}", v):
        p = tuple(v[1:-1].split("."))
        v = (SETS[t].get(p) or CORE[p])["$value"]
    return v


def colour_index(t):
    idx = {}
    for p, tok in SETS[t].items():
        if tok["$type"] == "color" and p[0] in PREFER:
            idx.setdefault(resolve(t, tok["$value"]), []).append(p)
    for v in idx.values():
        v.sort(key=lambda p: (not CORE_NAMES.match(".".join(p)), PREFER.index(p[0]), len(".".join(p)), p))
    return {k: [".".join(x) for x in v] for k, v in idx.items()}


# The token group a value is looked up in first, by the property it was read from.
BY_PROP = {"background-color": ["bg.", "tint.", "role.accent", "role."], "color": ["text.", "role.text", "role."],
           "border-top-color": ["border.", "role.border", "role."]}


def pick(paths, prop):
    for pre in BY_PROP.get(prop, []):
        for x in paths:
            if x.startswith(pre):
                return x
    return paths[0]


CIDX = {t: colour_index(t) for t in SETS}
DIDX = {}
for group in ("radius", "controlHeight", "spacing", "fontSize", "lineHeight", "letterSpacing"):
    for p, tok in CORE.items():
        if p[0] == group and isinstance(tok["$value"], str):
            DIDX.setdefault((group, tok["$value"]), ".".join(p))
stats = {"written": 0, "token": 0}


def as_token(t, prop, raw):
    stats["written"] += 1
    if prop in ("background-color", "color", "border-top-color") and is_color(raw):
        v = color(raw)
        if v == "rgba(0, 0, 0, 0)":
            stats["written"] -= 1
            return None
        if v in CIDX[t]:
            stats["token"] += 1
            return f"`{pick(CIDX[t][v], prop)}` {v}"
        return f"{v}"
    m = re.fullmatch(r"([\d.]+)px", raw)
    if m:
        v = "%gpx" % round(float(m.group(1)))
        group = {"border-top-left-radius": "radius", "height": "controlHeight", "padding-right": "spacing", "padding-left": "spacing",
                 "padding-top": "spacing", "font-size": "fontSize", "line-height": "lineHeight", "letter-spacing": "letterSpacing"}.get(prop)
        if v == "9999px" and prop == "border-top-left-radius":
            stats["token"] += 1
            return "`radius.full`"
        if (group, v) in DIDX:
            stats["token"] += 1
            return f"`{DIDX[(group, v)]}` {v}"
        if prop == "font-weight":
            stats["written"] -= 1
            return None
        return v
    stats["written"] -= 1
    return None


PROPS = [("background-color", "fill"), ("color", "text"), ("border-top-color", "edge"), ("border-top-left-radius", "radius"),
         ("height", "height"), ("padding-left", "padding"), ("font-size", "size"), ("line-height", "line")]


def first(t, part, state):
    for shot, d in CAP[t].items():
        if d["state"] == state and part in d["parts"]:
            return shot, d["parts"][part]["style"]
    return None, None


def states_of(t, part):
    return sorted({d["state"] for d in CAP[t].values() if part in d["parts"]}, key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99)


def crop_links(part, state):
    out = []
    for suffix, label in (("", "dark"), ("-light", "light")):
        name = f"{part}-{state}{suffix}.png"
        if name in CROPS:
            out.append(f"[{label}](components/crops/{name})")
    return " ".join(out)


lines = ["# Devin desktop: components", "",
         "Generated by `tools/build_components_md.py` from `raw/components.<theme>.json` (computed styles read live from Devin 3.11.216 on 2026-10-25), "
         "`tokens.json` and `components/crops/`. Each entry lists the parts that show the component, the states captured in each theme with "
         "links to their crops, and the measured values written as the token that holds them, the painted value after it. Values are CSS px "
         "(the window is 1440 x 900 at 2x, unzoomed). States: hover is a real pointer over the part, focus-visible real keyboard focus, pressed "
         "`:active` forced through the DevTools protocol with Base UI's `data-pressed` set on the part.", ""]
lines.append("| Component | Parts | Captured |")
lines.append("|---|---|---|")
for name, parts, note in INVENTORY:
    present = [p for p in parts if states_of("dark", p) or states_of("light", p)]
    lines.append(f"| [{name}](#{name.lower().replace(' ', '-')}) | {len(present)} | {'yes' if present else 'not captured'} |")
lines.append("")
seen = set()
for name, parts, note in INVENTORY:
    lines += [f"## {name}", "", note, ""]
    rows = []
    for part in dict.fromkeys(parts):
        for state in sorted(set(states_of("dark", part)) | set(states_of("light", part)), key=lambda s: STATE_ORDER.index(s) if s in STATE_ORDER else 99):
            vals = []
            for t in ("dark", "light"):
                shot, s = first(t, part, state)
                if not s:
                    continue
                cells = [f"{label} {v}" for prop, label in PROPS if not (prop == "border-top-color" and s.get("border-top-width") == "0px") and (v := as_token(t, prop, s.get(prop, "")))] if (part, state, t) not in seen else []
                seen.add((part, state, t))
                vals.append(f"{t}: " + "; ".join(cells) if cells else f"{t}: see crop")
            rows.append(f"| `{part}` | {state} | {crop_links(part, state) or 'no crop'} | {'<br>'.join(vals)} |")
    if rows:
        lines += ["| Part | State | Crops | Values |", "|---|---|---|---|"] + rows + [""]
lines += ["## Gaps", ""] + [f"- {g}" for g in GAPS] + [""]
lines.insert(4, f"{stats['token']} of {stats['written']} values written below are tokens ({round(100 * stats['token'] / max(1, stats['written']))}%); the rest no token holds and are written raw.")
lines.insert(5, "")
(PKG / "components.md").write_text("\n".join(lines))
print("components.md", len(INVENTORY), "components", stats)
