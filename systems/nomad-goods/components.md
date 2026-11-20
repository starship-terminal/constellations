# Components

Public marketing components on nomadgoods.com, measured 2026-11-19. No crops: the preview browser did not produce screenshot frames.

## Button

Two painted kinds, both pills.

| Kind | Class | Face | Label | Height | Padding | Radius |
|---|---|---|---|---|---|---|
| Primary | `button-dark button-md` | gradient `#2f2f2f` to `#2f2f2f`, 1px `#000` border, inset shadow `#0e0e0e` and `#676767` | `#fff` | 48px | 0 24px | 100px |
| Secondary | `button-light button-md` | gradient `#fff` 15% to `#f1f1f1` | `#000` | 48px | 0 24px | 100px |
| Small | `button-sm` | same faces | same | 40px | 0 20px | 100px |
| Compact | `button-compact` | light face, seen on "Learn About Horween Leather" | `#000` | 44px | 0 20px | 100px |

Type is Gotham Bold, 16px on md and 14px on sm, weight 700, tracking `-0.04em`, line height 1.11.

`button-dark` transitions in `0.15s`. Active (not held) flips the inset shadow and adds `padding-top: 1px`. `button-light` transitions in `0.2s` and reverses the gradient on active. Neither class has a `:hover` colour rule. Disabled, from `buttons.css` and not painted here, is background `#adadad`, white label, no shadow.

A third class, `button-glass`, is frosted white at 60% opacity, blur 10px, and 90% white on hover. It was not on the measured pages.

## Icon button

`button-icon-sm` computed 28 by 28px, radius 50%, on a recommendation "add to cart" control with the light face. `button-icon-md` is `2.5rem` (40px) in `buttons.css` and was not painted. Header search, cart, and menu controls are plain buttons with 20px padding, not the icon-button class. Their boxes were 0 on the desktop header read because those controls are the phone set.

## Link

`a { color: inherit; text-decoration: none }` in `app.css`. Nav links computed black, 16px, 70px tall, padding `0 30px`.

`link-underline` draws a 2px `currentColor` bar that grows over `0.5s ease` on hover and focus-visible. Reduced motion sets that transition to `none`. The underline width at rest is 0, so a resting link shows no bar.

## Text field

`field field-md` computed white, 48px, radius 100px, Gotham Book 16px, tracking `-0.02em`, line height 24px. Inset ring `rgba(0,0,0,.1)`. Placeholder colour in `fields.css` is `#6b6b6b`. Focus-within is `outline: 2px solid #000` with offset `-2px`.

`field-sm` computed 40px, padding `0 16px`, on the footer email field. That field was not submitted.

## Text area

`field-textarea` in `fields.css`: radius 24px, min-height `7.5rem`, padding `0.75rem 1.25rem`. Not on the pages that were open.

## Select

Review sort on the product page is a native `select`, Gotham Book 14px, 17.5px line height. `select.field` in `fields.css` is a pill with a 14 by 9px chevron. The currency control (`$ SGD`) uses `field field-sm` as a wrapper.

## Checkbox and radio

`fields.css` only. 24 by 24px, 2px `#6b6b6b` border, white face. Checkbox radius 6px. Radio is a circle, and checked draws a 4px white inset ring on a black face. Checked checkbox is black with a white tick. Focus-visible outline is 2px solid `#000`, offset 2px. Disabled face is `#f3f3f3` with a `#adadad` border. Not painted on the measured pages.

## Switch

Not present.

## Tabs

`tab-bar` in `buttons.css`: background `#e5e5e5`, 1px `rgba(0,0,0,.03)` border, radius 16px, padding 2px. Selected radius 13px. Not painted on the measured pages.

## Menu

Phone menu at 390px, opened with "Open menu". The card is `.surface-card`: `#f3f3f3`, radius 25px, about 380px wide. Scrim is `rgba(0, 0, 0, 0.6)`. Section titles use `type-heading-sm` (Gotham Bold 16px). Desktop nav is a row of text links, not a menu button.

Search popover (`.surface-popover`) was mounted and `display: none`. White, radius 20px, padding 10px, same stacked shadow as the card.

## Tooltip

Not captured.

## Dialog

Klaviyo signup dialog on the home page. Scrim `rgba(0, 0, 0, 0.5)`. Card 1000 by 690px, white, radius 40px. Close control 35px, radius 50%. Email input 50px tall, radius 100px, padding-left 16px. Sign Up button `#050505` with white label, 50px, radius 100px, type `NomadGothamBold` at 17px. Headings in that widget computed at 16px, which does not match the storefront display scale. The dialog was closed. No email was entered.

## Toast

Not captured.

## Card

`.surface-card`: white, radius 25px, shadow stack of six `rgba(0,0,0,.06)` layers (`0 0 0 1px`, then 1, 3, 6, 12, and 24px blur with negative spread). Product buy card padding was `30px 40px 15px`. Collection tiles were about 353px wide. Their image buttons had no radius of their own.

## List row

Material choice on the product page (Horween Leather `$118`, Camino Leather `$99`) is a text link, Gotham Book 14px, line height 17.5px, tracking `-0.28px`, padding 15px. Not a separate list component.

## Table

Not present.

## Avatar

Not present.

## Badge

`.type-pill`: Gotham Bold 11px, uppercase, tracking `-0.44px`, line height 11px, padding `5.5px 9px`, radius 100px, white label.

| Label | Background |
|---|---|
| NEW | `rgb(0, 91, 211)` `#005bd3` |
| Black Friday, HOT | `rgb(203, 121, 76)` `#cb794c` |

## Focus

Bundle rules use `outline: 2px solid #000` and `outline-offset: 2px`, with offset `-2px` on two field-like classes. One rule uses a white outline (`#fff`) for controls on dark imagery. Focusing the waitlist button produced `outline: rgb(255, 255, 255) auto 3px` and offset 0, which is the browser default on a white-on-dark control, not the 2px authored ring. Keyboard focus on a field was not taken.

## Gaps

- No screenshots or crops.
- Hover and pressed were not held.
- Error, disabled, checkbox, radio, textarea, tabs, tooltip, toast, and switch were not on screen.
- Search results, cart drawer, and account were not opened.
- Dark theme does not exist on these pages.
