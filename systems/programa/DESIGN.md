---
version: alpha
name: Programa
description: Public marketing site of Programa, interior-design project management. One light theme, captured 2026-11-21.
---

# Programa

Public marketing site. Values are the light theme from tokens.json. This file was written by hand because the capture does not edit catalog.json, so `make design-md` cannot generate it. tokens.json remains the source of truth.

## Overview

A warm white marketing surface. Headlines use Rhymes Display. UI uses Inter. The declared accent is a pale yellow. The header call to action is a separate mint button.

## Colors

The catalog swatch mapping is not registered. Roles below are the light semantic set.

- primary: `#fdffa2` (`light.accent`)
- neutral: `#ffffff` (`light.page`)
- surface: `#fcfbf9` (`light.surface`)
- on-surface: `#1a1916` (`light.text`)
- on-surface-variant: `#aaa59c` (`light.muted`)
- outline: `#eeece6` (`light.border`)

Other measured colours:

- raised: `#f8f6f3`
- link: `#7b736c`
- accent hover: `#ccca88`
- success: `#064e3b`
- danger: `#ff427b`
- header button background: `rgb(217, 237, 242)`
- header button text: `rgb(2, 85, 77)`
- dark button: `#1a1916`
- badge background: `#d1fae5`

## Typography

- display: Rhymes Display, 80px, weight 300, line-height 64px
- body: Inter, 16px, weight 400, line-height 24px
- label: Inter, 14px, weight 500, line-height 20px
- caption: Inter, 12px, weight 400, line-height 16px

## Rounded

- 2px
- 6px on controls
- 12px

## Spacing

4, 8, 12, 16, 24, 32, 40, 60, 68, 80. Header height 72px. Container padding 16px, 24px from the md step.

## Components

- button, dark: background `#1a1916`, text `#ffffff`, radius 6px, height 36px
- button, header: background `rgb(217, 237, 242)`, text `rgb(2, 85, 77)`, radius 6px, height 28px
- button, secondary: background `#ffffff`, text `#1a1916`, radius 6px, height 36px
- badge: background `#d1fae5`, text `#064e3b`, radius 6px

## Do's and Don'ts

Set headlines in Rhymes Display. Keep the page warm white. Use the yellow button for the trial. Do not treat the header mint as the accent. Do not invent a dark theme. Do not follow Log in or Start free into the app.
