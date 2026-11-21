---
# Hand-written from tokens.json on 2026-11-21. Not regenerated, so catalog.json stayed as it was.
# Source of truth: tokens.json.
version: "alpha"
name: "Vercel"
description: "Public Vercel marketing site. Light by default, dark from the footer label. Geist Sans, 64px display, filled primary button."
colors:
  primary: "#171717"
  neutral: "#fafafa"
  surface: "#ffffff"
  on-surface: "#171717"
  on-surface-variant: "#a8a8a8"
  outline: "#00000014"
  surface-page: "#fafafa"
  surface-raised: "#ffffff"
  text-primary: "#171717"
  text-secondary: "#a8a8a8"
  text-onAccent: "#ffffff"
  text-link: "#0070f3"
  border-default: "#00000014"
  accent: "#171717"
  status-success: "#0070f3"
  status-warning: "#f5a623"
  status-danger: "#ee0000"
  dark-surface-page: "#000000"
  dark-surface-raised: "#0a0a0a"
  dark-text-primary: "#ededed"
  dark-text-secondary: "#a1a1a1"
  dark-accent: "#ededed"
  dark-link: "#52a9ff"
typography:
  display:
    fontFamily: "GeistSans"
    fontSize: "64px"
    fontWeight: 400
    lineHeight: "128px"
  heading:
    fontFamily: "GeistSans"
    fontSize: "32px"
    fontWeight: 600
    lineHeight: "40px"
  body:
    fontFamily: "GeistSans"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
  label:
    fontFamily: "GeistSans"
    fontSize: "14px"
    fontWeight: 500
  code:
    fontFamily: "Geist Mono"
    fontSize: "16px"
    fontWeight: 400
rounded:
  control: "6px"
  field: "8px"
spacing:
  header-x: "6px"
  button-x: "14px"
  field-x: "12px"
  code: "16px"
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.control}"
    height: "32px"
  button-primary-dark:
    backgroundColor: "{colors.dark-accent}"
    textColor: "{colors.dark-surface-raised}"
    rounded: "{rounded.control}"
    height: "32px"
  text-field:
    backgroundColor: "{colors.surface}"
    textColor: "#000000"
    height: "40px"
    padding: "0 12px"
---

# Vercel

Public marketing site, measured 2026-11-21, signed out. Light is the default. Dark is the footer `dark` label.

## Overview

The page is off-white in light (`#fafafa`) and black in dark (`#000000`). The primary action is a filled near-black button in light and a filled near-white button in dark. GeistSans is the UI face. Geist Mono is the code face.

## Colors

Light page `#fafafa`, raised `#ffffff`, text `#171717`, link `#0070f3`. Dark page `#000000`, raised `#0a0a0a`, text `#ededed`, link `#52a9ff`. Success token `#0070f3` is not the primary button.

## Typography

Homepage display is 64px weight 400. Login heading is 32px weight 600. Body is 16px weight 400. Header labels are 14px weight 500.

## Layout

Desktop captures are 1440 by 900. Phone captures are 390 by 844. Header controls are 32px. Login controls are 40px. Control radius is 6px. Login buttons are 8px.

## Components

See [components.md](components.md). The email field was photographed empty and not submitted.
