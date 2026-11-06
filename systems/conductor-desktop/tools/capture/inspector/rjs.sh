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
# Nothing touches the clipboard until the snapshot and every temporary file exist. The page copies its
# result only within DEADLINE ms of starting, so a body that outlives the wait below never overwrites the
# clipboard after it was put back.
HERE=$(cd "$(dirname "$0")" && pwd)
DEADLINE=38000
tmp=; saved=; result=
cleanup() { [ -n "$saved" ] && pbcopy < "$saved"; rm -f ${saved:+"$saved"} ${result:+"$result"} ${tmp:+"$tmp"}; }
abort() { echo "rjs: $1; the clipboard was not touched" >&2; rm -f ${saved:+"$saved"} ${result:+"$result"} ${tmp:+"$tmp"}; exit 1; }
saved=$(mktemp "${TMPDIR:-/tmp}/rjs-clip.XXXXXX") || abort "no temporary file"
result=$(mktemp "${TMPDIR:-/tmp}/rjs-out.XXXXXX") || abort "no temporary file"
if [ "$1" = "-e" ]; then
  tmp=$(mktemp "${TMPDIR:-/tmp}/rjs.XXXXXX") || abort "no temporary file"
  printf '%s\n' "$2" > "$tmp" || abort "could not write the code"
  set -- "$tmp" "$3"
fi
pbpaste > "$saved" || abort "could not save the clipboard"
trap cleanup EXIT
trap 'exit 130' INT TERM
marker="__rjs_pending_$$_$(date +%s)"
{
  # copy() is part of the console's command-line API, which is gone after the first await, so it is
  # passed in as an argument.
  printf '(async(__c)=>{const __m=%s,__t=Date.now(),__cp=v=>{if(Date.now()-__t<%s)__c(v)};try{const __r=await (async()=>{\n' "'$marker'" "$DEADLINE"
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
pbpaste > "$result" || exit 1
if [ -n "$2" ]; then cp "$result" "$2"; else cat "$result"; echo; fi
if head -c 4 "$result" | grep -q '^ERR '; then exit 1; fi
