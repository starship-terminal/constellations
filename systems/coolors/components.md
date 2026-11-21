# Coolors components

Measured on the signed-in Coolors page on 2026-11-20, theme `light`, desktop CSS viewport 1440x900 at devicePixelRatio 2. Phone CSS viewport was 390x844. Values are `getComputedStyle` readings in [raw/components-computed.json](raw/components-computed.json).

## Button

Header and generator toolbar buttons are `a.btn.btn--s`. Height 36px, radius 8px, padding 0 12px, Inter 15px weight 500.

| Variant | Fill | Label | Where |
|---|---|---|---|
| transparent | rgba(0, 0, 0, 0) | rgb(0, 0, 0) | Tools, View, Export, Save |
| selected | rgba(23, 89, 232, 0.1) | rgb(18, 71, 186) | open toolbar popover |
| go pro | rgba(0, 0, 0, 0) | rgb(236, 72, 153) | header Go Pro |
| primary | rgb(37, 99, 235) | rgb(255, 255, 255) | account page primary |
| icon | transparent | ink | 36x36 toolbar icons |

## Header

Height 60px. Fill rgb(255, 255, 255). Shadow `rgba(0, 0, 0, 0.07) 0px 1px 0px 0px`. Logo at the left, Tools, Go Pro, and the avatar at the right when signed in. Sign in and Sign up are `display: none`.

## Generator column

Desktop columns are 288px by 784px (`.generator_color_background`). The hex is Inter 30px weight 600, tracking 0.9px. Ink flips between white and black against the column. Phone columns stack at 390x146, and the hex chip is 16px weight 600 with a 10px radius.

## Text input

Account text fields are 46px tall, radius 10px, padding 0px 14px, 15px. Focus border is `#3b82f6` (`--input-focus-border`). Error border is `#ef4444`.

## Display type

The account page h1 is Inter 70px weight 800, tracking -2.45px, line-height 77px, color rgb(10, 10, 10).

## Gaps

No focus ring was painted on the controls that were measured. Checkbox, switch, toast, table, and menu rows were not opened as their own screens. Dark theme was not switched on, because the theme control sits in the account menu and writes a preference.
