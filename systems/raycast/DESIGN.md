---
version: alpha
name: Raycast
description: Public marketing site at raycast.com. Dark is the only theme the public pages applied.
colors:
  primary: "#e6e6e6"
  neutral: "#07080a"
  surface: "#101111"
  on-surface: "#f4f4f6"
  on-surface-variant: "#9c9c9d"
  outline: "#242728"
  text-strong: "#f4f4f6"
  accent-text: "#18191a"
  highlight: "#ff6161"
  positive: "#59d499"
typography:
  display:
    fontFamily: Inter
    fontSize: 64px
    fontWeight: 600
    lineHeight: 70.4px
  body:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: 400
    lineHeight: 18.4px
  nav:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    letterSpacing: 0.2px
  button:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: 500
    lineHeight: 16px
rounded:
  sm: 6px
  md: 8px
  lg: 12px
  xl: 16px
  control: 8px
spacing:
  header: 76px
  button: 36px
  field: 42px
  content: 1204px
components:
  button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.accent-text}"
    rounded: "{rounded.control}"
    height: "{spacing.button}"
---

# Raycast

Public marketing site. Values are the computed custom properties and control styles from 2026-11-22. The catalog generator was not run. `catalog.json` was left alone.

The page colour is `#07080a`. Text is `#f4f4f6`. Quiet nav text is `#9c9c9d`. Download is a light pill, `#e6e6e6`, with an 8px radius. The red role in `:root` is `#ff6161`. The press kit names `#FF6363`, which is `--red-dark`, not `--color-red`.
