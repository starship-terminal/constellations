# Wise measurements

Live computed styles from the T3 preview browser on 2026-11-19. Viewport 1169 by 731 CSS pixels, devicePixelRatio 2, visualViewport scale 1. `color-scheme` was `normal`. `html` class was `np-theme-personal` on every page. Nothing was typed. No account, email, phone, card, bank, or KYC step was entered. No transfer was started.

`preview_snapshot` returned: "The browser is not producing screenshot frames." No screenshot was invented. Headless Playwright was not launched against the login page.

## Pages

| URL | Title | What was read |
|---|---|---|
| https://wise.com/ | Wise: The international account | Money without borders | Wise Singapore | Tokens, hero, nav buttons, calculator controls, plates |
| https://wise.com/login | Wise - Login | Empty email and password fields, submit, social buttons, error banner |
| https://wise.com/sg/pricing/ | Wise Fees & Pricing: Only Pay for What You Use | Heading, segment cards, inverted Sign up |

## Colour, resolved on :root

These are `getComputedStyle(document.documentElement)` values, not the losing declaration in a later stylesheet.

| Token name | Computed |
|---|---|
| --color-background-screen | #ffffff |
| --color-background-elevated | #ffffff |
| --color-background-neutral | rgba(22, 51, 0, 0.07843) |
| --color-background-neutral-solid | #edeeec |
| --color-background-neutral-hover | rgba(22, 51, 0, 0.12941) |
| --color-background-neutral-active | rgba(22, 51, 0, 0.18039) |
| --color-background-overlay | rgba(22, 51, 0, 0.07843) |
| --color-border-neutral | rgba(14, 15, 12, 0.12157) |
| --color-content-primary | #0e0f0c |
| --color-content-secondary | #454745 |
| --color-content-tertiary | #6a6c6a |
| --color-content-link | #163300 |
| --color-content-link-hover | #0d1f00 |
| --color-content-link-active | #0e0f0c |
| --color-interactive-accent | #9fe870 |
| --color-interactive-accent-hover | #80e142 |
| --color-interactive-accent-active | #65cf21 |
| --color-interactive-primary | #163300 |
| --color-interactive-primary-hover | #0d1f00 |
| --color-interactive-primary-active | #0e0f0c |
| --color-interactive-secondary | #868685 |
| --color-forest-green | #163300 |
| --color-bright-green | #9fe870 |
| --color-bright-orange | #ffc091 |
| --color-bright-yellow | #ffeb69 |
| --color-bright-pink | #ffd7ef |
| --color-bright-blue | #a0e1e1 |
| --color-dark-purple | #260a2f |
| --color-dark-charcoal | #21231d |
| --color-dark | #121511 |
| --color-content-negative | #cf2929 |
| --color-sentiment-negative | #cb272f |
| --color-sentiment-negative-secondary | #fbeaea |
| --color-content-positive | #008026 |
| --color-interactive-positive | #2ead4b |
| --color-content-warning | #9a6500 |
| --color-interactive-warning | #df8700 |
| --color-content-accent | #0097c7 |
| --color-contrast | #ffffff |
| --ring-outline-color | #163300 |

Footer background computed `rgba(22, 51, 0, 0.08)`, the same family as `--color-background-neutral`.

## Type

| Element | font | size | weight | line-height | letter-spacing | colour |
|---|---|---|---|---|---|---|
| body | Inter, Vazirmatn, Noto Sans SC, Zen Kaku Gothic Antique, Noto Sans KR, Noto Sans Thai, Noto Sans Hebrew, Helvetica, Arial, sans-serif | 16px | 400 |  |  | rgb(69, 71, 69) |
| h1 home | Wise Sans, Inter, Rubik, then the same CJK faces, sans-serif | 85.9091px | 800 | 74.9986px | normal | rgb(14, 15, 12) |
| hero paragraph `.eds-body-1` | Inter stack | 19.4954px | 400 | 27.2936px | -0.0974772px | rgb(69, 71, 69) |
| h2 pricing | Wise Sans | 77.9474px | 900 | 66.2553px | normal | rgb(22, 51, 0) |
| pricing card title `.eds-display-4` | Wise Sans | 40px | 900 | 34px |  | rgb(22, 51, 0) |
| pricing card body `.eds-body-3` |  | 16px | 400 | 24px |  | rgb(22, 51, 0) |
| login h1 | Inter | 26px | 600 | 31.72px |  | rgb(14, 15, 12) |
| login label | Inter | 14px | 600 | 21.7px |  | rgb(14, 15, 12) |
| login field | Inter | 16px | 400 | 24px | -0.176px | rgb(14, 15, 12) |
| nav button | Inter stack | 18px | 600 | 26px | -0.108px | rgb(22, 51, 0) |

`--eds-font-family-display` resolved to `"Wise Sans", Inter, Rubik, "Noto Sans SC", "Zen Kaku Gothic Antique", "Noto Sans KR", "Noto Sans Thai", "Noto Sans Hebrew", sans-serif`.

`--wds-font-size-display-large` resolved to `4rem`. The home h1 is a fluid clamp, not that static size.

## Controls, home

| Control | class | background | colour | height | padding | radius | weight | transition |
|---|---|---|---|---|---|---|---|---|
| Sign up (nav) | wds-Button--medium wds-Button--primary | rgb(159, 232, 112) | rgb(22, 51, 0) | 32px | 8px 12px | 9999px | 600 | color, background-color, border-color 0.35s cubic-bezier(0.8, 0.05, 0.2, 0.95) |
| Log in (nav) | wds-Button--medium wds-Button--tertiary | transparent | rgb(22, 51, 0) | 32px | 8px 12px | 9999px | 600 | same 350ms curve |
| Open an account | wds-Button--large wds-Button--primary | rgb(159, 232, 112) | rgb(22, 51, 0) | 48px | 12px 16px | 9999px | 600 | color, background-color 0.15s ease-in-out |
| Learn how to send money | wds-Button--large wds-Button--primary on a green plate | rgb(22, 51, 0) | rgb(159, 232, 112) | 48px | 12px 16px | 9999px | 600 | 0.15s ease-in-out |
| Explore getting paid | wds-Button--large wds-Button--secondary-neutral | rgba(22, 51, 0, 0.08) | rgb(14, 15, 12) | 48px | 12px 16px | 9999px | 600 | 0.15s ease-in-out |
| Currency combobox | wds-Button--medium wds-Button--secondary-neutral | rgba(62, 59, 7, 0.07) | rgb(14, 15, 12) | 40px | 8px | 9999px | 400 | 0.15s ease-in-out |
| Send money (calculator) | wds-Button--block wds-Button--large wds-Button--primary | rgb(159, 232, 112) | rgb(22, 51, 0) | 48px | 12px 16px | 9999px | 400 | 0.15s ease-in-out |
| Green plate section | Section_root | rgb(159, 232, 112) | rgb(22, 51, 0) |  | 54.223px 0 | 0 |  |  |
| Footer | footer | rgba(22, 51, 0, 0.08) | rgb(69, 71, 69) |  | 0 |  |  |  |

`--btn-padding` resolved to `calc(12px - 1px) 24px`. `--btn-radius-base` resolved to `9999px`. `--size-large` is 48px. `--size-medium` is 40px. `--size-small` is 32px.

## Login, https://wise.com/login

The form was empty after the read. Email value was `""`. Password value was `""`.

| Control | background | border / shadow | height | padding | radius | size |
|---|---|---|---|---|---|---|
| Email input `.np-input--shape-rectangle` | transparent | inset `rgb(134, 134, 133) 0 0 0 1px` | 48px | 12px 16px | 10px | 16px / 24px, weight 400, letter-spacing -0.176px |
| Password input | transparent | none (show-password control sits in the field) | 48px | 12px 16px | 10px | same |
| Email focused | transparent | inset ring stayed `rgb(134, 134, 133) 0 0 0 1px`. outline 0 | 48px |  | 10px |  |
| Log in submit | rgb(159, 232, 112) | none | 48px | 12px 16px | 9999px | 14px, weight 400 |
| Can't log in | transparent | none | 48px | 12px 16px | 9999px | 14px, weight 600 |
| Login with Google | transparent | 1px solid rgba(14, 15, 12, 0.12) | 40px | 11px 24px 11px 44px | 9999px | 16px / 600, colour rgb(66, 133, 244) |
| Login with Facebook | transparent | same border | 40px | same | 9999px | colour rgb(59, 89, 152) |
| Login with Apple | transparent | same border | 40px | same | 9999px | colour rgb(0, 0, 0) |
| Log in with a passkey | transparent | same border | 50px | 12px 16px | 9999px | 14px / 400 |
| Close | transparent | none | 48px | 0 | 9999px | colour rgb(22, 51, 0) |
| Sign up link | transparent | none |  |  | 2px | 14px / 600, underline, colour rgb(22, 51, 0) |
| Error `.alert-negative` | rgba(22, 51, 0, 0.08) | none |  | 16px | 16px | 14px, text colour rgb(69, 71, 69) |
| Error icon circle | rgb(203, 39, 47) |  |  |  | 50% | glyph colour rgb(251, 234, 234) |

The error text "Something went wrong." was already on the page. Nothing was submitted. The page includes a hidden Cloudflare Turnstile field (`cf-turnstile-response`). The visible page was the login form, not a challenge interstitial.

The form column is 486px wide inside `.container--narrow` at 550px with 32px horizontal padding. Page background is the white on the theme root.

## Pricing, https://wise.com/sg/pricing/

| Element | value |
|---|---|
| html class | np-theme-personal |
| --color-interactive-accent | #9fe870 |
| --color-forest-green | #163300 |
| Sign up in the nav | background rgb(22, 51, 0), colour rgb(159, 232, 112), height 32px, padding 8px 12px, radius 9999px |
| Sign up today | background rgb(159, 232, 112), colour rgb(22, 51, 0), height 48px, padding 11px 24px, radius 9999px, 16px / 600, border 1px solid the same green |
| Segment card | border 1px solid rgba(22, 51, 0, 0.12), radius 10px, width 374px |
| Card content padding | 16px |

## Motion (computed, not a reduced-motion emulation)

| Name | value |
|---|---|
| --navigation-animation-duration | 350ms |
| --navigation-animation-duration-short | 200ms |
| --navigation-animation-duration-long | 600ms |
| --navigation-transition-timing-function | cubic-bezier(0.8, 0.05, 0.2, 0.95) |
| primary button transition | color, background-color 0.15s ease-in-out |
| login field transition | box-shadow 0.3s ease-in-out |
| --navigation-box-shadow | 0px 4px 16px rgba(0, 0, 0, 0.16) |

`prefers-reduced-motion` was not emulated. That verdict is a gap.

## Radius and spacing scales, resolved

| Name | computed |
|---|---|
| --radius-small | 10px |
| --radius-medium | 16px |
| --radius-large | 24px |
| --radius-xlarge | 32px |
| --radius-full | 9999px |
| --padding-x-small | 8px |
| --padding-small | 16px |
| --padding-medium | 24px |
| --padding-large | 32px |
| --space-small | 16px |
| --space-medium | 32px |
| --space-large | 40px |
| --space-x-large | 56px |
| --space-content-horizontal | 16px |
| --input-padding | 12px 16px |
| --input-padding-small | 4px 12px |

`--eds-space-*` and `--eds-radius-*` are `clamp()` expressions. They are recorded in raw/css-vars-home.json and are not stored as dimension tokens, because the checker accepts only a single px length.

## Not measured

Hover, pressed, disabled, and loading fills were not forced. Focus on the login email did not change the inset ring. Dark theme was not on these pages. Phone width was not set. Screenshots were not produced.
