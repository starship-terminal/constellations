---
version: "alpha"
name: "Duolingo"
description: "Public signed-out marketing site, measured 2026-11-22. Page snow #FFFFFF, text eel #4B4B4B, Get started owl #58CC02, login macaw #1CB0F6, footer owl green. UI text is duolingo-sans. Display headlines are feather. Login is an empty overlay. Signed-in extraction was not started."
colors:
  primary: "#58CC02"
  neutral: "#FFFFFF"
  surface: "#FFFFFF"
  on-surface: "#4B4B4B"
  on-surface-variant: "#777777"
  outline: "#E5E5E5"
  link: "#1CB0F6"
  field: "#F7F7F7"
  login-button: "#1CB0F6"
  login-lip: "#1899D6"
  cta-lip: "#58A700"
  footer: "#58CC02"
rounded:
  button: "12px"
  login-button: "16px"
  field: "12px"
spacing:
  button-x: "16px"
  field-height: "48px"
  button-height: "50px"
typography:
  body:
    fontFamily: "duolingo-sans"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: "20px"
  heading:
    fontFamily: "duolingo-sans"
    fontSize: "32px"
    fontWeight: 700
    lineHeight: "40px"
  display:
    fontFamily: "feather"
    fontSize: "48px"
    fontWeight: 700
    lineHeight: "normal"
  label:
    fontFamily: "duolingo-sans"
    fontSize: "15px"
    fontWeight: 700
    lineHeight: "normal"
components:
  button-get-started:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.button}"
    height: "{spacing.button-height}"
    typography: "{typography.label}"
  button-login:
    backgroundColor: "{colors.login-button}"
    textColor: "#FFFFFF"
    rounded: "{rounded.login-button}"
    height: "{spacing.button-height}"
    typography: "{typography.label}"
  text-field:
    backgroundColor: "{colors.field}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.field}"
    height: "{spacing.field-height}"
    typography: "{typography.body}"
---

# Duolingo public readings

Public signed-out readings from https://www.duolingo.com/ on 2026-11-22. This file was written by hand. `make design-md` was not run, so [DESIGN.md](DESIGN.md) stays the earlier generated file. catalog.json was left alone.

Get started paints owl `#58CC02` with white uppercase type. The login submit paints macaw `#1CB0F6`. Both buttons are 50px tall. The homepage radius is 12px. The login overlay radius is 16px. The lip is a `::before` face, 4px shorter than the button: tree frog `#58A700` under Get started, whale `#1899D6` under Log in.

The page is snow `#FFFFFF`. Headlines are eel `#4B4B4B` in duolingo-sans 700 at 32px. Section headlines such as "free. fun. effective." are feather 700 at 48px in owl green. The footer is the same owl green. Course cards on `/courses` sit under a macaw header.

The login overlay fields are empty. The shell is polar `#F7F7F7` with a 2px swan `#E5E5E5` border, 12px radius, 48px tall, 375px wide. Sign up stops on an empty Age field. Next is disabled and paints swan.
