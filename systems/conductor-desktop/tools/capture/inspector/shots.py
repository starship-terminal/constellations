#!/usr/bin/env python3
"""Take Conductor's shots in the theme on screen, through Safari's Web Inspector.

    python3 tools/capture/inspector/shots.py <theme> [name ...]     every shot in shots.json, or the named
    python3 tools/capture/inspector/shots.py <theme> --vars         the custom properties (css-vars.<theme>.json)
    python3 tools/capture/inspector/shots.py <theme> --js '<body>'  run one function body in the page

For each shot: rjs.sh runs cap.js, prelude.js and the shot's `reveal` in the page, waits, measures the
shot's `parts` (computed style and box), and returns them; shot.sh then captures the window. The shot's
`after` runs last (close the menu, clear the text). Readings merge into
$RAW/<theme>/captures.json: {name: {state, viewport, parts: {part: {box, style}}}}, boxes in
screenshot pixels. RAW defaults to ~/.design-systems/conductor-desktop/raw-shots, outside the repo.

Look, don't act: reveals open and close, type and clear, never submit, archive or delete.
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
RAW = Path(os.environ.get("RAW", Path.home() / ".design-systems/conductor-desktop/raw-shots"))
LIB = (HERE / "cap.js").read_text() + "\n" + (HERE / "prelude.js").read_text() + "\n"


def run_js(body, out=None):
    args = [str(HERE / "rjs.sh"), "-e", LIB + body]
    if out:
        args.append(str(out))
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError((r.stdout + r.stderr).strip()[:2000])
    return r.stdout.strip()


def shoot(theme, name):
    r = subprocess.run([str(HERE / "shot.sh"), theme, name], capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr.strip())
    return r.stdout.strip()


def take(theme, shot):
    body = f"""
C.unforce(); C.untag();
await P.ready({json.dumps(bool(shot.get('toast')))}, {json.dumps(bool(shot.get('keepOpen')))});
{shot.get('reveal', '')}
await C.sleep({shot.get('wait', 700)});
const parts = {{{shot.get('parts', '')}}};
const forced = {json.dumps(shot.get('force', {}))};
for (const [k, st] of Object.entries(forced)) {{ const s = parts[k]; const e = typeof s === 'function' ? s() : typeof s === 'string' ? C.$(s)[0] : s; if (e) C.force(e, st); }}
await C.sleep(Object.keys(forced).length ? 350 : 0);
return {{ state: {json.dumps(shot.get('state', 'default'))}, viewport: C.viewport(), parts: C.measure(parts) }};
"""
    res = run_js(body)
    data = json.loads(res)
    path = shoot(theme, shot["name"])
    data["file"] = f"{theme}/{shot['name']}.png"
    # A shot that forces different states on different parts (hover on most, focus-visible on one) records each
    # part under the state it was in: `partState` names them, and they go to `<shot>~<state>` (same screenshot).
    entries = {shot["name"]: data}
    for part, st in shot.get("partState", {}).items():
        if part in data["parts"]:
            key = f"{shot['name']}~{'focus' if st == 'focus-visible' else st}"
            entries.setdefault(key, {"state": st, "viewport": data["viewport"], "parts": {}, "file": data["file"],
                                     "note": f"split from {shot['name']}: this part was forced to {st}"})
            entries[key]["parts"][part] = data["parts"].pop(part)
    write(theme, shot["name"], entries)
    if shot.get("after") or shot.get("force"):
        run_js("C.unforce();\n" + shot.get("after", "") + "\nreturn 'after ok';")
    return path, sorted(data["parts"])


def write(theme, name, entries):
    """Replace every reading of shot `name` (and its `~` splits) with `entries`; {} removes them."""
    out = RAW / theme / "captures.json"
    allc = json.loads(out.read_text()) if out.exists() else {}
    allc = {k: v for k, v in allc.items() if k != name and not k.startswith(name + "~")}
    allc.update(entries)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(allc, indent=1) + "\n")


def main():
    theme, *rest = sys.argv[1:]
    if rest[:1] == ["--vars"]:
        out = RAW / f"css-vars.{theme}.json"
        run_js("return __cap.vars([]);", out)
        print(out)
        return
    if rest[:1] == ["--js"]:
        print(run_js(rest[1]))
        return
    shots = json.loads((HERE / "shots.json").read_text())
    names = [s["name"] for s in shots]
    for n in rest:
        if n not in names:
            sys.exit(f"no shot named {n}")
    failed = []
    for shot in shots:
        if rest and shot["name"] not in rest:
            continue
        if shot.get("themes") and theme not in shot["themes"]:
            continue
        if shot.get("manual") and shot["name"] not in rest:
            continue                   # needs a state reached by hand (see its note); run it by name
        try:
            path, parts = take(theme, shot)
            print(shot["name"], len(parts), "parts", ",".join(parts)[:160])
        except Exception as e:  # one failed shot never stops the rest
            failed.append(shot["name"])
            print("FAILED", shot["name"], str(e)[:600])
            write(theme, shot["name"], {})   # no stale reading survives a failed attempt; quantize.py then drops its image
            try:
                run_js("await P.closeAll(); return 'closed';")
            except Exception:
                pass
        time.sleep(0.2)
    if failed:
        print("failed:", " ".join(failed))
        sys.exit(1)


if __name__ == "__main__":
    main()
