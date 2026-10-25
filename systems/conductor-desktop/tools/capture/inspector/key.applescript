-- osascript key.applescript <code|text> <value> [cmd,shift,opt,ctrl]
-- A real keystroke (key code or typed text) to Conductor, only while Conductor is frontmost.
-- For what a script event cannot do: native panels (the folder picker), and shortcuts.
on run argv
  set kk to item 1 of argv
  set v to item 2 of argv
  set mods to ""
  if (count of argv) > 2 then set mods to item 3 of argv
  tell application "Conductor" to activate
  delay 0.5
  tell application "System Events"
    set fp to name of (first process whose frontmost is true)
    if fp is not "conductor" then return "front is " & fp
    set ml to {}
    if mods contains "cmd" then set end of ml to command down
    if mods contains "shift" then set end of ml to shift down
    if mods contains "opt" then set end of ml to option down
    if mods contains "ctrl" then set end of ml to control down
    if kk is "code" then
      key code (v as integer) using ml
    else
      keystroke v using ml
    end if
  end tell
  return "ok"
end run
