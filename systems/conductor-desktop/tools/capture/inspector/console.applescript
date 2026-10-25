-- Paste the clipboard into Web Inspector's console for Conductor and run it.
tell application "Safari" to activate
delay 0.4
tell application "System Events" to tell process "Safari"
  set target to missing value
  repeat with w in windows
    if name of w starts with "Web Inspector" then set target to w
  end repeat
  if target is missing value then return "no inspector window"
  perform action "AXRaise" of target
  delay 0.3
  if (name of first process whose frontmost is true) of application "System Events" is not "Safari" then return "safari not front"
  keystroke "c" using {command down, option down}
  delay 0.4
  keystroke "a" using {command down}
  key code 51
  keystroke "v" using {command down}
  delay 0.3
  key code 36
end tell
return "ok"
