# Coolors components

Measured on the public Coolors homepage on 2026-11-21, theme `light`, desktop CSS viewport 1440x900 at devicePixelRatio 2. Phone CSS viewport was 390. Values are `getComputedStyle` readings in [raw/components-computed.json](raw/components-computed.json). Generator column size, hex chip, selected toolbar state, and account fields were not remeasured this pass.

## Button

| Variant | Fill | Label | Size | Where |
|---|---|---|---|---|
| primary | rgb(37, 99, 235) | rgb(255, 255, 255) | 36px, radius 8px, padding 0 12px, Inter 15px weight 500 | header Sign up, Start the Generator |
| gray | rgba(0, 0, 0, 0.06) | rgb(0, 0, 0) | 46px, radius 10px, padding 0 21px, Inter 16px weight 600 | Explore 10M+ Palettes |
| go pro | transparent | rgb(236, 72, 153) | 36px, radius 8px | header Go Pro |

Hover, focus, pressed, and disabled were not measured.

## Header

Height 60px. Fill rgb(255, 255, 255). Shadow `rgba(0, 0, 0, 0.07) 0px 1px 0px 0px`. Signed out: wordmark, Tools, Go Pro, Sign in, Sign up. No avatar.

## Tools menu

`#megamenu` is a fixed overlay from 60px down. Visible state sets `visibility: visible` and clears the inner translate. Two columns of tool links, then Discover, Download, and Company. Shot: [home-light-tools-menu.png](screenshots/home-light-tools-menu.png).

## Display type

Homepage h1 (`#homepage_title`) is Inter 110px weight 800, tracking -3.85px, line-height 99px, color rgb(10, 10, 10).

## Tool card

`.homepage_tool` fill rgb(207, 250, 254), label rgb(8, 145, 178), radius 14px, padding 40px. Color of the day card fill rgb(245, 245, 245), same radius and padding.

## Sign-in overlay

`#fullscreen-access` covers the page. Intro copy is "Hello!" and "Use your email or another service to continue with Coolors." Buttons: Continue with Google, Continue with Apple, Continue with email (primary fill). Not submitted. Shot: [home-light-signin-wall.png](screenshots/home-light-signin-wall.png).

## Gaps

Focus, hover, checkbox, switch, toast, table, and menu-row states were not opened as their own screens. Dark theme was not switched. Account inputs were not offered.
