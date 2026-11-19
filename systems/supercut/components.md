# Components

Public signed-out Supercut, measured on 2026-11-19. Computed styles came from a T3 preview tab at 1169 by 731 CSS pixels, devicePixelRatio 2. Screenshots in [screenshots/](screenshots/) came from a later headless Playwright pass of the same public pages at 1169 by 900 and 390 by 844, because `preview_snapshot` returned "The browser is not producing screenshot frames." Login and signup were not opened in that headless session.

## Button

Marketing buttons are pills. The class list includes `corner-superellipse`. Computed `border-radius` was `1.67772e+07px`.

| State | Where | Values |
|---|---|---|
| Primary | Home "Get started free" | background `rgb(253, 255, 240)`, text `rgb(16, 14, 14)`, 15px / 500 / 20px, padding 0 16px, height 40px, gap 6px, border 1px transparent, transition 0.15s `cubic-bezier(0, 0, 0.2, 1)` on background, border, shadow, colour, opacity, transform |
| Primary, header | "Sign up" | same cream and ink, 13px / 500 / 18px, height 32px, padding 11px 11px 12px |
| Secondary | "Talk to us" and "Talk to sales" | background `oklab(0.994451 -0.00763747 0.0181944 / 0.05)`, text the same colour at 70 percent, border 1px at 10 percent, height 40px, padding 0 16px, 15px / 500 |
| Ghost | Header "Log in" | transparent, text `rgb(150, 150, 146)`, 13px / 500 / 18px, height 32px, radius 10px, width 40px |
| Auth primary | Signup "Sign up with Google", login "Continue with Google" | cream and ink, height 48px, width 320px, padding 0 18px 0 16px, 15px / 500. Not clicked |
| Auth secondary | "Sign up with Email", "Continue with Email" | same oklab fill as Talk to us, height 48px, width 320px. Not clicked |
| Auth ghost | "Sign up with SSO", "Continue with SSO" | transparent, muted text, height 40px, width 320px, links to `/auth/sso`. Not followed |
| Focus | "Get started free" after `focus()` | outline-style `none`, outline-width 1px, outline-color `rgb(153, 200, 255)`. No visible ring was shown |
| Pressed | class `[&:active:not([data-active]):not([data-disabled])]:translate-y-px` | not shown |

Hover, loading, disabled and error were not shown.

## Link

Nav "Pricing" is 13px / 500, `rgb(150, 150, 146)`, height 32px, radius 10px. Legal links on signup ("Terms", "Privacy", "Cookie policy") are 13px, muted, underline, underline-offset 4px. SSO is a link, not a form.

## Text field

Signup and login do not show an email field until "Sign up with Email" or "Continue with Email". Those buttons were not clicked. No text field, placeholder, or error was measured.

## Text area, select, radio

Not present on the measured public pages.

## Checkbox

Signup shows a label "I agree to the Terms, Privacy & Cookie policy." The page has 3 inputs. Their painted size was not measured. Checked and error states were not shown.

## Switch

Pricing "Billed yearly" is `role=switch`, `aria-checked=true`, 40 by 24, padding 2px, background `rgb(253, 255, 240)`, pill radius. The off state was not clicked.

## Tabs

Not present.

## Menu

The Product control opens a `nav` (`aria-controls` id `base-ui-_r_6_`). Background `rgb(24, 22, 22)`, border 1px `rgb(33, 33, 33)`, radius 14px, 653 by 144, shadow `rgba(0, 0, 0, 0.8) 0px 12px 40px 0px`. Items are 13px, muted, padding 16px. Hover was not painted by a synthetic mouse event. Screenshot: [screenshots/home-menu-dark.png](screenshots/home-menu-dark.png).

## Tooltip, dialog, toast

A cookie note was on first paint and dismissed with Accept. Its panel was not measured after dismiss. Sonner toast tokens exist in an inline stylesheet (`--gray1` through `--gray12`, success, info, warning, error). No toast was shown. Tooltip and dialog were not shown.

## Card

Pricing plan cards were visible. A single card element with both the price and the feature list was not isolated, so card radius and padding stay a gap. The page screenshot is [screenshots/pricing-dark.png](screenshots/pricing-dark.png).

## List row

FAQ questions are buttons, height 66px, padding 20px 16px 20px 0, radius 4px, 16px / 400, width 1073px at 1169. Expanded and error states were not opened.

## Table

The pricing comparison is on the page below the fold. It was not measured as a table component.

## Avatar

Not on the marketing chrome. The home hero is a public product demo, not a signed-in avatar.

## Badge

"PRO" is height 32, padding 0 14px, pill, 13px / 500, background `oklab(0.722997 -0.18884 0.110898 / 0.2)`, text `lab(78.503 -64.9265 39.7492)`. "ENTERPRISE" uses `oklab(0.622989 -0.0378532 -0.210606 / 0.25)` and text `lab(65.0361 -1.42065 -56.9802)`.

## Icon button

The phone header has a menu icon. It was not measured. The wordmark SVG is 126 by 28 on desktop (`viewBox="0 0 252 56"`, fill `#FDFFF1` on the measured path).

## Gaps

Hover, pressed, disabled, loading, error, text fields, textarea, select, radio, tooltip, dialog, toast, table, and signed-in components were not captured. Light theme is not the public site's class (`html.dark` only).
