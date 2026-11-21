---
version: alpha
name: Conductor
description: Public marketing site at conductor.build. Dark is the default theme recorded here. Light exists and is in tokens.json.
colors:
  primary: "#f3f2f1"
  neutral: "#141110"
  surface: "#211e1c"
  on-surface: "#eae8e6"
  on-surface-variant: "#a5a09c"
  outline: "#ffffff1a"
  text-strong: "#ffffff"
  accent-text: "#141110"
  highlight: "#2a1e1d"
  positive: "#16a249"
typography:
  display:
    fontFamily: ui-sans-serif
    fontSize: 36px
    fontWeight: 600
    lineHeight: 40px
    letterSpacing: -0.9px
  body:
    fontFamily: ui-monospace
    fontSize: 16px
    fontWeight: 400
    lineHeight: 24px
  nav:
    fontFamily: ui-sans-serif
    fontSize: 14px
    fontWeight: 400
    lineHeight: 20px
  button:
    fontFamily: ui-sans-serif
    fontSize: 14px
    fontWeight: 500
    lineHeight: 20px
  banner:
    fontFamily: ui-sans-serif
    fontSize: 15px
    fontWeight: 500
    lineHeight: 22.5px
rounded:
  xs: 0.125rem
  sm: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  control: 6px
spacing:
  banner: 44px
  header: 57px
  button-sm: 32px
  button: 40px
  content: 56.25rem
components:
  button:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.accent-text}"
    rounded: "{rounded.control}"
    height: "{spacing.button-sm}"
---

# Conductor

Hand-written from measured tokens on 2026-11-22. This file is the dark theme only. Light roles are in [tokens.json](tokens.json). The catalog generator was not run, so this file is not a `make design-md` output.

## Color

The dark page is `#141110`. Text is `#eae8e6`. The headline is white. Muted text is `#a5a09c`. The Download pill is `#eae8e6` with a `#141110` label. `--primary` on `html.dark` is `#f3f2f1`, close to the pill and not the same value.

## Typography

The stylesheet names Geist Sans. The capture browser computed the marketing sans as `ui-sans-serif, system-ui, sans-serif`. The homepage body is the system mono at 16px. The headline is 36px, weight 600, line-height 40px, tracking -0.9px.

## Layout

The announcement bar is 44px. The header is 57px. Content width token `--site-content-width` is 56.25rem. Desktop captures are 1440 CSS pixels. Phone captures are 390 CSS pixels.

## Do's and Don'ts

Paint the dark page `#141110`. Keep nav links quiet. Use the light pill for Download and Get Conductor. Do not invent a pricing page. Do not treat the homepage product mock as the signed-in app. Do not click through the identity-provider wall.

## Elevation

The download dialog sits on a scrim. No shadow token was measured on the header button. The button's computed `box-shadow` was `none`.
