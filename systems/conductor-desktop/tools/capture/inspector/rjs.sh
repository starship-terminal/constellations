#!/bin/sh
# rjs.sh <file.js> [out] | rjs.sh -e '<code>' [out]
# Run an async function body in Conductor's page through Safari's Web Inspector console. The body
# returns a value; it comes back through the console's copy() and the clipboard, and is printed or
# written to [out]. Needs a Web Inspector window open on Conductor's page (Develop > this Mac >
# Conductor > localhost) and System Events access for the terminal: console.applescript raises that
# window, pastes the code into the console prompt and presses Return. Conductor is raised again after.
#
# The clipboard is the only way back, so it carries the page's result (which can hold account text). The
# owner's clipboard text is saved first and put back on every exit, and the temporary files are removed,
# so neither the result nor the code stays behind. (Only text is put back: an image on the clipboard is lost.)
HERE=$(cd "$(dirname "$0")" && pwd)
tmp=; saved=$(mktemp "${TMPDIR:-/tmp}/rjs-clip.XXXXXX"); result=$(mktemp "${TMPDIR:-/tmp}/rjs-out.XXXXXX")
pbpaste > "$saved" 2>/dev/null
cleanup() { pbcopy < "$saved"; rm -f "$saved" "$result" ${tmp:+"$tmp"}; }
trap cleanup EXIT
trap 'exit 130' INT TERM
if [ "$1" = "-e" ]; then tmp=$(mktemp "${TMPDIR:-/tmp}/rjs.XXXXXX"); printf '%s\n' "$2" > "$tmp"; set -- "$tmp" "$3"; fi
marker="__rjs_pending_$$_$(date +%s)"
{
  # copy() is part of the console's command-line API, which is gone after the first await, so it is
  # passed in as an argument.
  printf '(async(__cp)=>{const __m=%s;try{const __r=await (async()=>{\n' "'$marker'"
  cat "$1"
  printf '\n})();__cp(typeof __r==="string"?__r:JSON.stringify(__r));}catch(e){__cp("ERR "+e+" "+(e&&e.stack))}})(copy);void 0\n'
} | pbcopy
res=$(osascript "$HERE/console.applescript")
[ "$res" = ok ] || { echo "console: $res" >&2; exit 1; }
i=0
while [ $i -lt 80 ]; do
  sleep 0.5
  if ! pbpaste | grep -q "$marker"; then break; fi
  i=$((i+1))
done
osascript -e 'tell application "Conductor" to activate' >/dev/null 2>&1
sleep 0.4
if pbpaste | grep -q "$marker"; then echo "rjs: no result after 40 s" >&2; exit 1; fi
pbpaste > "$result"
if [ -n "$2" ]; then cp "$result" "$2"; else cat "$result"; echo; fi
if head -c 4 "$result" | grep -q '^ERR '; then exit 1; fi
