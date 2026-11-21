---
# Written by hand for this public capture because catalog.json was left alone.
# Source of truth: tokens.json. DESIGN.md spec version alpha.
version: "alpha"
name: "ClickUp"
description: "Work management marketing site: white page, Plus Jakarta Sans hero, ink button, purple named accent, signed-out email and password walls"
colors:
  primary: "#202020"
  neutral: "#ffffff"
  surface: "#f8f9fa"
  on-surface: "#202020"
  on-surface-variant: "#646464"
  outline: "#e8e8e8"
  page: "#ffffff"
  text: "#202020"
  muted: "#646464"
  accent: "#6647f0"
  border: "#e8e8e8"
  button: "#202020"
  on-button: "#ffffff"
  ink: "#292d34"
typography:
  hero:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "60px"
    fontWeight: 700
    lineHeight: "66px"
    letterSpacing: "-2.1px"
  body:
    fontFamily: "Plus Jakarta Sans"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "24px"
rounded:
  nav: "8px"
  hero: "12px"
  xxs: "4px"
  md: "20px"
spacing:
  nav-x: "12px"
  nav-y: "8px"
  hero-x: "24px"
components:
  button-primary:
    backgroundColor: "#202020"
    textColor: "#ffffff"
    rounded: "12px"
---

## Overview

Public ClickUp marketing site, captured signed out on 2026-11-22. Values come from computed styles and named custom properties on the homepage. catalog.json was left alone, so this file was not produced by `make design-md`.

## Colors

Page `#ffffff`, text `#202020`, button `#202020`, accent `#6647f0`, muted `#646464`, border `#e8e8e8`.

## Typography

The hero uses Plus Jakarta Sans at 60px. Body uses Plus Jakarta Sans at 16px. Nav controls use Inter at 14px. The families are proprietary and are not in the package.

## Layout

The header is 60px under a 40px promo bar. Desktop shots are 1440. Phone shots of the homepage, pricing, and the empty walls are 390.

## Do's and Don'ts

Use the ink button for the primary action. Keep the purple accent off that button. Do not treat the homepage illustration as a signed-in workspace.
