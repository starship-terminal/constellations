# Modyfi components

Measured on the Wayback replay of the public homepage, snapshot `20250219221151`, at 1440 x 900, on 2026-11-19. Live `modyfi.com` is a Webflow 404. Colours below are computed styles, written as hex where the channel values convert cleanly.

## Signup button

The nav Sign up control. At rest it is a magenta outline. Hover fills it.

| State | Background | Text | Radius | Border |
|---|---|---|---|---|
| default | transparent | `#ffffff` | 15px | `rgba(255, 3, 87, 0.47)` 2px |
| hover | `#ff0357` | `#ffffff` | 15px | same |

Padding 8px 16px. Jokker 12.8px / 19.2px, weight 400. Crop: [signup-button-default.png](components/crops/signup-button-default.png).

## Primary call to action

"Start playing for free" is a white pill with black text.

| State | Background | Text | Radius | Outline |
|---|---|---|---|---|
| default | `#ffffff` | `#000000` | 15px | none |
| focus-visible | `#ffffff` | `#000000` | 15px | `rgb(153, 200, 255) auto 1px` |

Padding 16px 24px. The face is `system-ui`, 16px, weight 600. Crop: [cta-button-default.png](components/crops/cta-button-default.png).

## Log in

Ghost control. Text `rgba(255, 255, 255, 0.8)`, transparent fill, 15px radius, 8px 16px padding, Jokker 12.8px.

## Nav link

Jokker 12.8px, `rgba(255, 255, 255, 0.8)`, padding 8px 19.2px. The bar itself is 80px tall on a 1440px viewport, transparent over the black page.

## Display type

`h1` "Design without limits": Jokker 56px, weight 600, line-height 67.2px, letter-spacing -3px, white.

Section `h2`: Jokker 48px, weight 600, line-height 57.6px, letter-spacing -1px, white.

Hero body: Jokker 17.6px, weight 400, line-height 31.68px, letter-spacing -1px, `#c9c9c9`.

## Page

Background `#000000` (`--background-a: black`). Body text colour `#c9c9c9`. Body font stack is Inter; the marketing headlines and nav use Jokker.

## Gaps

- Text field, text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, table, avatar, badge: not painted as product controls on the signed-out marketing pages. The canvas in the hero is a marketing image, not the signed-in app.
- Disabled, loading, error, and pressed states were not shown.
- `app.modyfi.com` does not resolve. Sign-in and sign-up were not opened.
- Privacy snapshot `20241210053539` returned an archive page this client treated as missing. The joining-Figma post snapshot returned "Temporarily Offline" and was left out.
- Webflow IX2 motion is JavaScript-driven. Durations were not read from computed style.
