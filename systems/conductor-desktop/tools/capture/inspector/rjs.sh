#!/bin/sh
# rjs.sh <file.js> [out] | rjs.sh -e '<code>' [out]
# Run an async function body in Conductor's page through Safari's Web Inspector console. The body
# returns a value; it comes back through the console's copy() and the clipboard, and is printed or
# written to [out]. Needs a Web Inspector window open on Conductor's page (Develop > this Mac >
# Conductor > localhost) and System Events access for the terminal: console.applescript raises that
# window, pastes the code into the console prompt and presses Return. Conductor is raised again after.
HERE=$(cd "$(dirname "$0")" && pwd)
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
if [ -n "$2" ]; then pbpaste > "$2"; else pbpaste; echo; fi
if pbpaste | head -c 4 | grep -q '^ERR '; then exit 1; fi
