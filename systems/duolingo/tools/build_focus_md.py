#!/usr/bin/env python3
"""Write components/focus.md from the two live Tab passes in raw/2026-10/.

live-measurements.json (first pass) and live-measurements-2.json (second pass: menus, profile,
lesson footer, quit dialog, report form). One row per real key press (2026-10-17, built-in
browser pane, signed in): the control, whether it matched :focus-visible, and every computed
property of the control, its ::before / ::after and its ancestors that differed from the same
element at rest. Note records in the second file become the reachability list.
"""
import json, pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((PKG / "raw/2026-10/live-measurements.json").read_text())
d2 = json.loads((PKG / "raw/2026-10/live-measurements-2.json").read_text())

def kind(r):
    dt, cls, tag, role, typ = r.get("dt") or "", r.get("cls") or "", r.get("tag"), r.get("role"), r.get("type")
    if dt == "det-nav": return "MORE menu row (link)"
    if dt in ("settings-button", "help-button", "logout-button"): return "MORE menu row (button)"
    if dt.endswith("-nav") or dt == "profile-tab": return "Sidebar nav item (link)"
    if dt == "quit-button": return "Icon button (quit X)"
    if dt == "player-next": return "Filled button (CHECK / CONTINUE)"
    if dt == "notification-drawer-no-thanks-button": return "Text button (END SESSION)"
    if role == "menuitem": return "Courses menu row (menuitem)"
    if typ == "checkbox": return "Checkbox (native input)"
    if dt == "hint-token": return "Hint token (opens the word tooltip)"
    if "challenge-tap-token" in dt: return "Word-bank tile (outline button)"
    if dt == "player-skip": return "Outline button (SKIP)"
    if dt == "notification-button": return "Filled button"
    if tag == "select": return "Select (theme)"
    if role == "radio": return "Radio card"
    if "_2mkWS" in cls: return "Switch"
    if tag == "input": return "Text field (%s)" % (typ or "text")
    if "_2rQ98" in cls: return "Link button (TRY CHESS)"
    if "_1GJVt" in cls: return "Icon button (speaker)"
    if "_1VC2W" in cls: return "Icon button (avatar edit)"
    if "_2VEsk" in cls: return "Icon button (lesson settings gear)"
    if "_2xTPJ" in cls: return "Footer feedback button (Too easy / Too difficult)"
    if "_1642c" in cls: return "Footer feedback button (Report)"
    if "_1zl6C" in cls: return "Courses menu trigger"
    if cls.split()[:1] in (["_3KUWP"], ["_3w8he"], ["hCZR9"]): return "Top-bar stat button (streak / gems / hearts)"
    if "tFegI" in cls: return "Tooltip trigger (div with tabindex)"
    if "_2paU5" in cls: return "Link button (outline)"
    if "_3q--f" in cls: return "Link button (filled)"
    if "_2V6ug" in cls: return "Outline button"
    if tag == "span" and role == "button": return "Sidebar MORE item"
    if "_3qEOY" in cls: return "Logo link"
    if tag == "a": return "Text link"
    return tag

def change(r):
    if "ancestorDiff" in r or "key" in r:
        return change2(r)
    parts = []
    for scope, diff in (("self", r.get("diff")), ("parent", r.get("parentDiff"))):
        for k, (a, b) in (diff or {}).items():
            if k in ("width",):
                continue  # the clear button appearing beside the field narrows the input
            if k == "outline-offset":
                parts.append("outline-offset 1px with outline-style none (no ring drawn)")
                continue
            parts.append(f"{scope} {k} {a} -> {b}")
    if r.get("tag") == "input" and r.get("parentDiff") is None:
        return "input unchanged; its wrapper was not read in this first pass (the second pass on the same page reads it)"
    if any("border-top-color" in p for p in parts):
        return "wrapper border -> `border.focus` (" + [p for p in parts if "border-top-color" in p][0].split(" -> ")[1] + ")"
    return "; ".join(dict.fromkeys(parts)) or "no computed change"

def change2(r):
    parts = []
    for k, (a, b) in (r.get("diff") or {}).items():
        if k == "outline-offset":
            parts.append("outline-offset 1px with outline-style none (no ring drawn)")
        elif k == "background-color" and b == "rgb(32, 47, 54)":
            parts.append(f"fill {a} -> {b} (`surface.subtle`, dark polar)")
        else:
            parts.append(f"self {k} {a} -> {b}")
    anc = r.get("ancestorDiff") or {}
    if anc and all(set(v) == {"opacity"} for v in anc.values()):
        parts.append("control unchanged; the dialog's fade-in (ancestor opacity 0 -> 1) ended between the rest read and the press")
    else:
        for lvl, v in anc.items():
            parts += [f"ancestor {lvl} {k} {a} -> {b}" for k, (a, b) in v.items()]
    return "; ".join(dict.fromkeys(parts)) or "no computed change"

L = ["# Duolingo: focus states, measured live", "",
     "Captured on 2026-10-17 in the signed-in web app (free account) by pressing the Tab key in the built-in browser pane and reading the focused element's computed styles after each press, against the same element at rest ([tools/capture/live-measure.js](../tools/capture/live-measure.js), data in [raw/2026-10/live-measurements.json](../raw/2026-10/live-measurements.json)).", "",
     "Duolingo draws no focus ring. Its stylesheets set `outline:none` on every element (`*,:after,:before,button,button:focus,input,textarea`) and on every web-ui button (`._7jW2t:not(._1ZhE5)`), and none of the 20 chunks the app loaded has a `:focus-visible` rule ([raw/2026-10/css-evidence.json](../raw/2026-10/css-evidence.json)). Every control below matched `:focus-visible`; only text fields change visibly, by turning their 2px border `border.focus`. The one other visible keyboard state is the courses dropdown: its rows get a `surface.subtle` (polar) fill on `:focus` and `:focus-within`, read in CSS and confirmed live in the second pass (arrow keys move focus between rows). `core.focusRing.width` is 0px for that reason.", "",
     "| # | Page | Control | `:focus-visible` | What changed on focus |", "| --- | --- | --- | --- | --- |"]
n = 0
for r in d["focus"]:
    if r.get("el") == "body" or "programmatic" in (r.get("page") or ""):
        continue
    n += 1
    L.append(f"| {n} | {r['page']} | {kind(r)} | {'yes' if r.get('fv') else 'no'} | {change(r)} |")
L += ["", f"{n} Tab presses. The friend-streak dialog's SEE INVITES was also Tab-focused live in light (it matched `:focus-visible` and kept its face and lip, with no ring); that press was read before the log started, so it has no row.", "",
      "## Second pass: menus, profile, lesson footer, dialogs", "",
      "Same method, dark theme, 1440x900 ([tools/capture/tab-pass.js](../tools/capture/tab-pass.js), data in [raw/2026-10/live-measurements-2.json](../raw/2026-10/live-measurements-2.json)). Reads taken after a script `focus()` call are left out, so every row is a key press.", "",
      "| # | Page | Key | Control | `:focus-visible` | What changed on focus |", "| --- | --- | --- | --- | --- | --- |"]
m = 0
for r in d2["focus"]:
    if r.get("note"):
        continue
    m += 1
    L.append(f"| {m} | {r['page']} | {r['key']} | {kind(r)} | {'yes' if r.get('fv') else 'no'} | {change(r)} |")
L += ["", f"{m} key presses.", "", "## Reachability", "",
      "What the keyboard can and cannot reach, from the two passes:", ""]
L += list(dict.fromkeys(f"- {r['page']}: {r['note']}." for r in d2["focus"] if r.get("note")))
L += ["- MORE menu (sidebar): Enter on the trigger opens it; Tab then walks its four rows (Duolingo English Test, Settings, Help, Log out) with no visible change on any of them.",
      "- Courses menu (top bar): opens on hover. Enter on its trigger did not open it, and the next Tab presses moved on to the stat buttons. With the menu open, Tab lands on the current course row (the only row with tabindex 0) and ArrowDown moves between rows (roving tabindex).",
      "- Quit dialog: opens only once the lesson has progress (with none, the X leaves at once).",
      ""]
(PKG / "components/focus.md").write_text("\n".join(L))
print("components/focus.md:", n, "rows")
