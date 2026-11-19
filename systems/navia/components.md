# Navia components

Measured on the public marketing site and the signed-out app gate, 2026-11-19. Viewport was 1169 by 731 at device pixel ratio 2. No crops: the preview browser returned "The browser is not producing screenshot frames".

## Button

The marketing button is `.button-base`. Default face is orange `#f88450`, white text, radius `4rem`, padding `0.75rem 1.5rem`. Computed height was 46px and horizontal padding 23.154px.

| Variant | Face | Label | Where |
|---|---|---|---|
| default | `#f88450` | `#ffffff` | Get started for free, Sign up |
| yellow nav | `#e8ff39` | `#332e29` | Nav Get started |
| yellow hero | `#e8ff39` | `#ffffff` | Hero Get started for free |
| white | `#ffffff` | `#ffffff` | Book a demo, on a white-text section |
| text | transparent | `#36312a`, weight 600 | View plans |
| contact submit | `#f88450` | `#36312a` | Contact form submit |

Hover, pressed, disabled and loading were not captured. The marketing button's focus outline computed to `none`. `.button` transitions `background-color` and `color` over `0.2s`.

The app gate buttons are 40px tall, radius 25px, padding `8px 24px`, weight 500. Sign In is white with a `#dfd5c0` border and ink text. Sign Up is orange `#f88450` with ink text. Focus is a 2px `#f88450` outline, offset 2px. Neither button was pressed.

## Link

Nav links are transparent, ink `#36312a`, Public Sans, 15.436px, radius 0. Article links inside `.w-richtext` are orange `#f88450`. Footer legal links were present and not opened beyond privacy.

## Text field

Contact fields are cream `#faf4e6`, 1px solid ink border, radius 0.25rem (computed 3.859px), padding `7.718px 11.577px`, height 42px. The textarea is 174px tall with 11.577px padding. Names: First-Name, Last-Name, Email, Phone, a topic select, Message. All required. None were filled. Error, disabled and focus styles on these fields were not read.

The app gate has no email field. Sign In and Sign Up are buttons.

## Card

`.pricing_plan` is 330px wide, radius 0.5rem (computed 7.718px), border 1px `#cdc7b8`, padding `38.59px 30.872px 30.872px`. The highlight plan drops the border, fills `#36312a`, and uses white text. Plan names use the handwriting face in orange, 2.5rem, letter-spacing -2px.

Prices read on the page: Basic plan, Free forever. Business plan, $49/mo. Growth plan, $79/mo.

## Wordmark

Inline SVG, viewBox `0 0 124 36`, displayed at 219 by 35. The mark fills `--nav-logo-mark` (`#E8FF39` on the light nav, `#F88450` on the dark nav). The word fills `--nav-logo-text`. Saved as [wordmark.svg](icons/wordmark.svg).

## Gaps

- No hover, pressed, disabled, loading or error state.
- No checkbox, radio, switch, tabs, menu, tooltip, dialog, toast, avatar or badge on the public pages. Cookie-consent controls are CookieYes, not Navia.
- No component crops. Screenshot frames failed.
- App components behind Sign In and Sign Up were not reached.
