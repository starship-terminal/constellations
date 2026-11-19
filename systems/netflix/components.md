# Components

Public signed-out chrome on https://www.netflix.com/sg/ and https://www.netflix.com/sg/login, read on 2026-11-19. Values are token names. Crops were not saved: the preview browser returned no screenshot frames.

## Button

The red action. Sign In in the header, Get Started beside the email field, Continue on the login page.

| State | What was read |
|---|---|
| Default | `component.button.bg` `#e50914`, `component.button.text` white, `component.button.radius` 4px. Get Started is `component.button.height` 56px, padding 12px 24px, type `typography.button` 18px medium. Sign In is 32px tall, padding 4px 16px, type `typography.sign-in` 14px medium. Continue is 48px tall, padding 8px 16px, 18px medium, full width of the 440px column. |
| Hover | Declared `--hcw--local-design--Button-SurfaceHovered` `#c11119`. Not hovered in the live page. |
| Pressed | Declared surface `#99161d`, foreground `rgba(255, 255, 255, 0.7)`. Duration 0. Not pressed in the live page. |
| Focus | Declared ring: 0.125rem solid white, offset 0.125rem, on `:focus`. A mouse focus clears the outline via `:focus:not(:focus-visible)`. |
| Disabled | Declared surface `rgba(229, 9, 20, 0.4)`, foreground `rgba(255, 255, 255, 0.4)`. Not shown. |

Transition on the live Get Started and Sign In: background-color and border-color, 0.25s, `cubic-bezier(0.4, 0, 0.68, 0.06)`.

## Icon button

Get Started contains a 24px `ChevronRightMedium` SVG, fill `currentColor`. Saved as [icons/chevron-right.svg](icons/chevron-right.svg). No separate icon-button component was measured.

## Link

Footer links are 14px regular, line-height 21px, `text.secondary`, underlined, radius 2px. Login "Get help" is 16px, `text.link` `#448ef4`, underlined. "Questions? Contact us." is 16px, `text.secondary`.

## Text field

Email on the home page and "Email address or mobile number" on the login page. The visible chrome is a sibling of the input: `component.field.bg` `rgba(22, 22, 22, 0.7)`, 1px `border.stroke` `rgba(128, 128, 128, 0.7)`, `component.field.radius` 4px, height 56px. The input itself is transparent, white, 16px, padding 24px 16px 8px. The empty label is 16px `text.secondary`. Focus draws the white ring on the chrome, not on the input.

Declared and not shown: error border `#eb3942`, success `#2bb871`, warning `#d89d31`, disabled border `rgba(128, 128, 128, 0.4)`, disabled surface `rgba(22, 22, 22, 0.2)`.

## Text area

Not present on these pages.

## Select

The language picker is a native select inside the same field chrome, 32px tall on the header, padding 6px 36px 6px 34px, 16px white. Declared select tokens match the input border, surface, and radius.

## Checkbox, radio, switch

Not present on the marketing or login chrome. OneTrust cookie controls are a third-party dialog and were not measured as Netflix components.

## Tabs

Not present.

## Menu

"Get help" on the login page is a button. The menu it opens was not opened.

## Tooltip

Not present.

## Dialog

No Netflix dialog was opened. The signup wall after Get Started was not entered. OneTrust's preference center is mounted and hidden.

## Toast

`--hcw--local-design--ToastGroup-*` spacing is declared (1.5rem between, stacking index 1002). No toast was on screen.

## Card

"More reasons to join" cards use a 149deg gradient from `#192247` to `#210e17`, radius 16px. Title 20px medium white. Body 16px `text.secondary`. Inner text padding 24px 24px 96px. Four cards, all the same gradient.

Trending tiles are buttons, 140 by 196, radius 8px, background `#232323`, 44px apart. They open a title, which was not followed.

## List row

The FAQ row is the list. Background `#2d2d2d`, padding 24px, type 24px regular white, square corners. Declared hover surface `#414141`. Gap between headline and panel is 0.0625rem. Space between items is 0.5rem declared. The clicked row set `aria-expanded` to true. The answer panel's scroll height was 265 and its painted height stayed 0 in the hidden preview pane, so the open state is a gap.

## Table, avatar, badge

Not present on these pages.

## Gaps

- Signup after Get Started, including plan choice and payment, was not entered.
- No account was created. No card, phone, or government ID was entered. The login form was not submitted.
- Playback, profiles, and the signed-in browse shell were not opened.
- Hover, pressed, disabled, error, success, and warning were read from declared custom properties, not from a painted state.
- The FAQ answer did not paint open.
- Screenshots and crops are missing because the preview browser returned "The browser is not producing screenshot frames".
- A 1440 CSS-pixel width was not reached. The fill viewport was 1169 by 731. Phone width 390 was confirmed on the login page via `window.innerWidth`.
- No light theme exists on these pages.
- `prefers-reduced-motion` was false. A reduce pass was not run.
