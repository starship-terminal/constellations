#!/usr/bin/env python3
"""Split raw/css-vars.json readings by host, from the saved stylesheet rules.

vars.mjs used to load marketing, app and docs into one probe, so a shared
name kept whichever host loaded last. This rebuilds resolvedByHost from the
declarations already saved on each rule (file starts with the host name) and
rewrites the flat resolved passes so a shared name keeps one chosen host.

No live recapture. A value is copied from a declaration, never invented.
A shared name whose saved reading is a resolved var() and that no other
host declared as a different literal keeps the saved reading.

Run once, on a css-vars.json straight from vars.mjs. It rewrites that file
in place, so its own output is not a valid input: on a second run the flat
passes already hold the restored literals, the "saved" reading matches the
other host, and replaced names flip back (--font-weight-bold 700 -> 600).
It therefore refuses a file that already carries hostPick. The committed
raw/css-vars.json was split once on 2026-11-18. A fresh vars.mjs capture
records resolvedByHost itself and does not need this step.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent.parent
RAW = HERE / "raw"
HOSTS = ("marketing", "app", "docs")
# Product names come from the signed-out app, then marketing. Docs is the
# source only for a name the other two hosts do not declare.
# Product colour roles are the signed-out app's. A name only marketing or
# docs declares keeps that host. Docs never overwrites a product name.
PICK = ("app", "marketing", "docs")
PASSES = ("plain", "light", "dark", "colorModeLight", "colorModeDark", "htmlDark")


def host_of(file):
    name = (file or "").split(" ", 1)[0]
    return name if name in HOSTS else None


def rootish(rule):
    """A declaration on :root / :host / html, not a theme or component override.

    Marketing's unscoped :root is a light shadcn layer the live page does not
    paint (the page sets .dark). That layer is recorded, and it is not the
    host's product root.
    """
    sel = rule.get("selector") or ""
    ctx = " ".join(rule.get("context") or [])
    if any(mark in sel for mark in (".dark", "data-color-mode", "data-theme", ":not(", "callout")):
        return False
    if "prefers-color-scheme" in ctx or "data-color-mode" in ctx:
        return False
    head = sel.split(",")[0].strip()
    return head in (":root", ":host", "html") or sel.strip() in (":root, :host", ":root,:host")


def collect(rules):
    """host -> name -> literal, from rules whose declaration is not a var().

    Root declarations win over a later component override. The first root
    literal is kept; a component literal fills a name that has no root one.
    """
    out = {h: {} for h in HOSTS}
    root = {h: set() for h in HOSTS}
    refs = {h: {} for h in HOSTS}
    for rule in rules:
        host = host_of(rule.get("file"))
        if not host:
            continue
        on_root = rootish(rule)
        for name, raw in (rule.get("properties") or {}).items():
            if not name.startswith("--"):
                continue
            text = str(raw).strip()
            if text.startswith("var("):
                refs[host].setdefault(name, text)
                continue
            if not text:
                continue
            if name in root[host]:
                continue
            if on_root or name not in out[host]:
                out[host][name] = text
                if on_root:
                    root[host].add(name)
    return out, refs


def reading(raw, saved):
    """A per-host reading. Reuse the saved computed value when it is this
    literal. Otherwise keep the literal and do not invent a computed colour."""
    item = {"raw": raw if len(raw) <= 300 else raw[:300] + "…"}
    if saved and saved.get("raw") == raw:
        item.update({k: v for k, v in saved.items() if k not in ("host", "stale")})
        return item
    if re.fullmatch(r"-?\d+(?:\.\d+)?", raw):
        item["kind"] = "number"
        item["value"] = float(raw) if "." in raw else int(raw)
        return item
    item["kind"] = "other"
    item["value"] = raw
    item["note"] = "declared literal from this host's saved stylesheet; no separate computed reading was stored"
    return item


def norm(text):
    return re.sub(r"\s+", "", str(text or "")).strip().lower()


def same_literal(saved, raw):
    if not saved:
        return False
    return norm(saved.get("raw")) == norm(raw) or norm(saved.get("value")) == norm(raw)


def host_literals(name, declared):
    return [(h, declared[h][name]) for h in PICK if name in declared[h]]


def main():
    path = RAW / "css-vars.json"
    data = json.loads(path.read_text())
    if "hostPick" in data:
        raise SystemExit(
            f"{path} was already split (it carries hostPick). Its resolved passes are this "
            "script's output, so a rerun would flip replaced names back. Recapture with "
            "tools/capture/vars.mjs instead.")
    rules = []
    for key in ("theme", "app", "skins", "vendor", "utility", "tailwind"):
        rules.extend(data.get(key) or [])
    declared, refs = collect(rules)
    resolved = data.get("resolved") or {}
    by_host = {h: {} for h in HOSTS}
    for host in HOSTS:
        for name, raw in declared[host].items():
            for pass_name in PASSES:
                saved = (resolved.get(pass_name) or {}).get(name)
                by_host[host].setdefault(pass_name, {})[name] = reading(raw, saved)
    # The flat passes keep the saved computed reading. A shared name is
    # replaced only when another host saved a different literal, so the
    # published value is that host's declaration, not a guessed colour.
    # A var()-only collision has no saved literal to restore, so the saved
    # computed reading is kept.
    replaced = []
    for pass_name in PASSES:
        flat = resolved.setdefault(pass_name, {})
        for name, saved in list(flat.items()):
            owners = [h for h in HOSTS if name in declared[h] or name in refs[h]]
            literals = host_literals(name, declared)
            distinct = {norm(raw) for _, raw in literals}
            if len(distinct) < 2:
                # One saved literal, or none. The computed reading is that
                # value. Name the host whose literal matches it.
                host = next((h for h, raw in literals if same_literal(saved, raw)), owners[0] if owners else None)
                if host:
                    flat[name] = {**saved, "host": host}
                continue
            # Hosts saved different literals. The computed reading belongs to
            # the host whose literal it equals: the shared page let that host
            # overwrite the others. Publish the other product host's literal
            # and keep every host under resolvedByHost.
            matched = [(h, raw) for h, raw in literals if same_literal(saved, raw)]
            others = [(h, raw) for h, raw in literals if (h, raw) not in matched and h in ("app", "marketing")]
            if not matched or not others:
                # The saved reading is a computed value (a var() resolved on
                # the shared page) and no other host stored a different
                # literal. Keep it, and name the host that declared the name.
                # There is no second literal to restore.
                host = next((h for h in ("app", "marketing", "docs") if h in owners), owners[0])
                flat[name] = {**saved, "host": host}
                continue
            chosen, raw = others[0]
            flat[name] = {**reading(raw, None), "host": chosen,
                          "note": f"restored from the {chosen} declaration; the saved probe reading {saved.get('raw')!r} matches {matched[0][0]}"}
            replaced.append((pass_name, name, chosen, raw, saved.get("raw")))
    data["resolved"] = resolved
    data["resolvedByHost"] = by_host
    data["hostPick"] = {
        "order": list(PICK),
        "replaced": [{"pass": p, "name": n, "host": h, "literal": lit, "was": was} for p, n, h, lit, was in replaced if p == "plain"],
        "note": (
            "resolvedByHost holds each host's saved literals. resolved keeps "
            "the computed probe reading, and replaces a shared name only when "
            "the chosen host (app, then marketing, then docs) saved a different "
            "literal. A shared name with no per-host literal keeps the computed reading."
        ),
    }
    path.write_text(json.dumps(data, indent=1) + "\n")
    print("declared", {h: len(declared[h]) for h in HOSTS})
    print("replaced", len({n for _, n, _, _, _ in replaced}))
    for row in data["hostPick"]["replaced"]:
        print(" replaced", row["name"], row["was"], "->", row["literal"], "from", row["host"])
    print("published bold", resolved["plain"].get("--font-weight-bold"))
    print("published background", resolved["plain"].get("--background"))


if __name__ == "__main__":
    main()
