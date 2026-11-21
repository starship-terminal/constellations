# Pop Site measurements

Read on 2026-11-21 from https://pop.site/ in headless Chromium, signed out.
Desktop viewport measured `innerWidth` 1440, `innerHeight` 900, `devicePixelRatio` 1.
Phone viewport measured `innerWidth` 390, `innerHeight` 844, `devicePixelRatio` 2.

No field was typed into. No form was submitted. Login and signup were not opened.

The numbers live in [components-computed.json](components-computed.json),
[css-vars.json](css-vars.json) and [extra-readings.json](extra-readings.json).
This file is the short reading of those files.

## Colour

Framer declares colours on `body` as `--token-<uuid>`. The distinct values are
in [css-vars.json](css-vars.json). The ones a captured control paints:

| Value | Where |
|---|---|
| #ffffff | page background |
| #171717 | nav, headings, footer links |
| #545454 | hero sub line |
| #6e6e73 | nav and footer link hover |
| #474d50 | claim field placeholder |
| #fafafc | `.pop.site` suffix chip |
| #00a8f5 to #3b82f6 | claim button gradient, 110 degrees |
| #3b82f6 | 404 Go home link, flat fill |
| #005fcc | Chromium auto focus outline |
| #ffffff | claim button label |

## Type

Satoshi 500 at 69px / 62.1px, tracking -3.92px, for the display heading.
Satoshi 500 at 21px / 29.4px, tracking -0.63px, for the hero sub line.
Satoshi 500 at 15px / 19.5px, tracking -0.45px, for nav and the claim label.
Satoshi 400 at 13px / 15.6px, tracking -0.39px, for footer links.
Inter 500 at 18px / 25.2px for FAQ questions.
Inter 600 at 16px / 22.4px for article titles.
Inter 400 at 14px for the privacy form fields.
Inter 600 at 14px, white, for the privacy Submit label.

## Controls

Claim button: 40px tall, radius 26px, padding 16px 24px, gradient fill.
Suffix chip: 40px tall, radius 9999px on the right, fill #fafafc, padding 16px 20px 16px 12px.
Claim field: 40px tall, no border of its own, Satoshi 15px.
Privacy Submit: 360px by 40px, radius 10px, fill #333333, hover alpha 0.85.
Privacy checkbox: 16px, radius 4px.
404 Go home: 108px by 52px, radius 16px, fill #3b82f6, links to https://pop.site/.

## Not read

Pressed fill of the claim button beyond the resting gradient. Disabled, loading,
selected and error. Dark theme. Reduced motion. Spacing scale, elevation scale,
breakpoints and z-index. The editor behind https://app.pop.site/.
