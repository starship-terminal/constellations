# Components

Public Workleap marketing and the signed-out login, measured 2026-11-19 from computed styles. No component crops: the preview browser returned "The browser is not producing screenshot frames".

| Component | Where | Values |
|---|---|---|
| Button | `a.button` on [officevibe](https://workleap.com/officevibe) | Background `#2545ff`, text `#ffffff`, radius `100px`, border `2px solid #2545ff`, font Inter hosted 500. Small nav size computed at 11.577px, padding 7.718px 23.154px, height 32px. Default token is 1rem / 0.7em 2em. |
| Button, secondary | `a.button.is-secondary` | Transparent background, text and border `#2545ff`, radius `100px`. |
| Button, alternate | `a.button.is-alternate` on pricing | Background `#ffffff`, text `#2545ff`, radius `100px`, height 43px. |
| Link button | `a.button.is-link` | No border, radius 0, nav login computed 11.577px / weight 500 / colour `#171417`. Hover rule sets colour to `--content-colors--content-brand-default`. |
| Text field | `input[name=firstname]` on `/demo` | White fill, 1px `#a2a2a2` border, radius computed 1543.6px (`100rem` at html 15.436px), height 46px, padding 11.577px 15.436px, text `#484747`, Inter hosted. |
| Login field | `input[name=username]` on login.workleap.com | White fill, wrapper border 1px `#3b57ff` while focused, radius 24px, height 46px, padding 8px 16px, text `#3c3c3c`, Inter. |
| Login button | `button.o-ui-button-primary` | Background `#2545ff` (painted; `--hop-primary-surface-strong` is `#4767fe`), text `#f9f8f6`, radius 24px, height 46px, padding 0 16px, weight 400, font Arial. |
| Pricing card | `.pricing-card` on `/pricing` | White fill, radius 24px, shadow `rgba(37, 69, 255, 0.1) 0 4px 8px, rgba(37, 58, 177, 0.05) 0 12px 24px, rgba(37, 58, 177, 0.05) 0 32px 40px`. Popular header `#ffc13a`, radius 24px 24px 0 0. |
| Nav | `.navbar_component` | White, height 58px at 1169px, padding 0 58.4453px. Links `#222222`, 11.577px. |
| Footer | `footer.footer_main` | `#0c1754` background, `#f9f8f6` text. |
| Cookie dialog | Osano `.osano-cm-window` | Present on load. Accept fill computed `#2545ff` with text `#f9f8f6`. This is the consent vendor, not the product button. |

## States

| State | What was read |
|---|---|
| Default | Buttons, fields, cards, nav and footer above. |
| Focus | Marketing button outline `rgb(37, 69, 255) auto 3px`, offset 0. Login field wrapper border `#3b57ff` 1px while focused. Login primary button focus outline was `none`. |
| Hover | Stylesheet rules only. `.button:hover` sets radius `0.5rem` (a different radius from the 100px rest state). `.button.is-link:hover` sets colour to boardroom navy. A synthetic mouseover did not change the filled button's computed background. |
| Pressed, disabled, loading, error | Not shown on the pages that were open. |
| Selected | Pricing "most popular" is a header band, not a selected control. |

## Gaps

- Icon button, text area as its own control, select (the demo country `<select>` was not measured), checkbox, radio, switch, tabs, menu, tooltip, dialog (other than the Osano cookie dialog), toast, list row, table, avatar and badge were not present on the signed-out pages, or were not opened.
- The demo form has a country `<select>` and two textareas. They were not measured. The form asks for a phone number, so it was not submitted and its error state was not captured.
- Hover, pressed and disabled colours for the filled button were not computed.
- No component crops. Screenshot frames were unavailable.
