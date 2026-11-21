---
version: "alpha"
name: "Brilliant"
description: "Public signed-out marketing site. Oat hero #F5F3F1, black text, green learner button #29CC57 with a #15B441 lip, CoFo Robert headlines, CoFo Brilliant body. Login page is gray-950 #141414. Signed-in extraction was not started."
colors:
  primary: "#29CC57"
  neutral: "#FFFFFF"
  surface: "#F5F3F1"
  on-surface: "#000000"
  on-surface-variant: "#00000066"
  outline: "#E4E4E4"
  link: "#456DFF"
  learner-lip: "#15B441"
  login-page: "#141414"
  login-button: "#E5E5E5"
rounded:
  field: "8px"
  pill: "60px"
  sign-in: "54px"
spacing:
  sign-in-y: "8px"
  sign-in-x: "14px"
typography:
  body:
    fontFamily: "CoFo Brilliant"
    fontSize: "18px"
    fontWeight: 400
    lineHeight: "27px"
  heading:
    fontFamily: "CoFo Robert"
    fontSize: "54px"
    fontWeight: 500
    lineHeight: "59.4px"
  label:
    fontFamily: "CoFo Brilliant"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
components:
  button-learner:
    backgroundColor: "{colors.primary}"
    textColor: "#FFFFFF"
    rounded: "{rounded.pill}"
    height: "47px"
  button-sign-in:
    textColor: "{colors.on-surface}"
    rounded: "{rounded.sign-in}"
    height: "36px"
    padding: "8px 14px"
  text-field:
    textColor: "#FFFFFF"
    rounded: "{rounded.field}"
    height: "52px"
    padding: "0px"
---

# Brilliant public

Hand-written from measurements on https://brilliant.org/ on 2026-11-21, signed out. `make design-md` was not run. catalog.json was left alone.

The homepage hero sits on oat `{colors.surface}`. The learner button is green `{colors.primary}` with a 4px lip `{colors.learner-lip}`. Headlines use CoFo Robert. UI text uses CoFo Brilliant. The login page background is `{colors.login-page}`.

The earlier signed-in DESIGN.md is kept as [DESIGN.signed-in-2026-10.md](DESIGN.signed-in-2026-10.md). This file does not replace those readings. It records the public pass.
