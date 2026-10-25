#!/bin/sh
# open_project.sh <folder>: Add project from the command palette, then pick <folder> in the native
# folder panel with real keystrokes (Go to Folder, the path, Return, Return). Used once per theme on
# harness-scratch/conductor/no-remote to reach the "Create a private GitHub repo?" dialog, which is
# measured and cancelled (shots.json, repo-dialog*); never confirm it. Each keystroke goes only after
# the panel (a window titled Open) is on screen, and the Go to Folder field shows the path typed.
HERE=$(cd "$(dirname "$0")" && pwd)
python3 "$HERE/shots.py" any --js "await P.ready(); await P.workspace(); C.click(P.sideText('Search').parentElement); await C.sleep(600); const o = C.\$('[role=option]').find(o => /^Add project/.test(o.innerText.trim())); if (!o) throw new Error('no Add project action'); C.click(o); return 'ok';" || exit 1
sleep 2.5
swift "$HERE/wins.swift" Conductor Open >/dev/null || { echo "no folder panel on screen; not typing" >&2; exit 1; }
osascript "$HERE/key.applescript" text g cmd,shift >/dev/null; sleep 1.2
osascript "$HERE/key.applescript" text "$1" >/dev/null; sleep 1
shot=$(swift "$HERE/wins.swift" Conductor Open) && screencapture -o -x -l "$shot" "${TMPDIR:-/tmp}/open-panel.png"
echo "check ${TMPDIR:-/tmp}/open-panel.png shows the path, then: osascript $HERE/key.applescript code 36 (twice)"
