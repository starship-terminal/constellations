#!/usr/bin/env python3
"""Write components/focus.md from the live Tab pass in raw/2026-10/live-measurements.json.

One row per real Tab key press (2026-10-17, built-in browser pane, signed in): the control,
whether it matched :focus-visible, and every computed property of the control, its ::before /
::after and its parent that differed from the same element at rest.
"""
import json, pathlib

PKG = pathlib.Path(__file__).resolve().parent.parent
d = json.loads((PKG / "raw/2026-10/live-measurements.json").read_text())

def kind(r):
    dt, cls, tag, role, typ = r.get("dt") or "", r.get("cls") or "", r.get("tag"), r.get("role"), r.get("type")
    if dt.endswith("-nav") or dt == "profile-tab": return "Sidebar nav item (link)"
    if dt == "hint-token": return "Hint token (opens the word tooltip)"
    if dt.endswith("challenge-tap-token"): return "Word-bank tile (outline button)"
    if dt == "player-skip": return "Outline button (SKIP)"
    if dt == "notification-button": return "Filled button"
    if tag == "select": return "Select (theme)"
    if role == "radio": return "Radio card"
    if "_2mkWS" in cls: return "Switch"
    if tag == "input": return "Text field (%s)" % (typ or "text")
    if "_2rQ98" in cls: return "Link button (TRY CHESS)"
    if "_1GJVt" in cls: return "Icon button (speaker)"
    if "_1VC2W" in cls: return "Icon button (avatar edit)"
    if tag == "span" and role == "button": return "Sidebar MORE item"
    if "_3qEOY" in cls: return "Logo link"
    if tag == "a": return "Text link"
    return tag

def change(r):
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

L = ["# Duolingo: focus states, measured live", "",
     "Captured on 2026-10-17 in the signed-in web app (free account) by pressing the Tab key in the built-in browser pane and reading the focused element's computed styles after each press, against the same element at rest ([tools/capture/live-measure.js](../tools/capture/live-measure.js), data in [raw/2026-10/live-measurements.json](../raw/2026-10/live-measurements.json)).", "",
     "Duolingo draws no focus ring. Its stylesheets set `outline:none` on every element (`*,:after,:before,button,button:focus,input,textarea`) and on every web-ui button (`._7jW2t:not(._1ZhE5)`), and none of the 20 chunks the app loaded has a `:focus-visible` rule ([raw/2026-10/css-evidence.json](../raw/2026-10/css-evidence.json)). Every control below matched `:focus-visible`; only text fields change visibly, by turning their 2px border `border.focus`. Menu rows in the courses dropdown get a `surface.subtle` (polar) fill on `:focus` and `:focus-within`, from CSS only (the menu was not opened by keyboard). `core.focusRing.width` is 0px for that reason.", "",
     "| # | Page | Control | `:focus-visible` | What changed on focus |", "| --- | --- | --- | --- | --- |"]
n = 0
for r in d["focus"]:
    if r.get("el") == "body" or "programmatic" in (r.get("page") or ""):
        continue
    n += 1
    L.append(f"| {n} | {r['page']} | {kind(r)} | {'yes' if r.get('fv') else 'no'} | {change(r)} |")
L += ["", f"{n} Tab presses. Not reached by keyboard: tabs (Characters, Profile), the MORE and courses menus, dialog buttons other than the friend-streak dialog's SEE INVITES (Tab-focused live in light: it matched `:focus-visible` and kept its face and lip, with no ring; that press was read before the log started, so it has no row) and the quit dialog (its buttons were focused by script, which does not set `:focus-visible`), checkboxes in the lesson report form (native inputs, global `outline:none`).", ""]
(PKG / "components/focus.md").write_text("\n".join(L))
print("components/focus.md:", n, "rows")
