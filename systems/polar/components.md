# Components

Public signed-out Polar, measured on 2026-11-19 at a 1169 by 731 CSS viewport. Screenshots were not saved: the preview browser returned "The browser is not producing screenshot frames." Values below are computed styles.

## Button

Marketing and auth buttons are pills (`border-radius` computed as a full pill, recorded as 9999px).

| State | Where | Values |
|---|---|---|
| Primary, default | Header "Get Started" on https://polar.sh/ | background `#ffffff`, text `#000000`, 14px / 550 / 20px, padding 12px 16px, height 40px, pill |
| Primary, hero | Home hero "Get Started" | same type, height 48px, padding 16px 20px |
| Ghost | Header "Sign in" | transparent background, text `#ffffff`, padding 12px 20px, height 40px, pill |
| Secondary | Auth "Sign in with Apple" and "Sign in with GitHub" | background `#212121`, 1px border `oklab(0.999994 0.0000455678 0.0000200868 / 0.05)`, text `#ffffff`, height 40px, pill |
| Submit | Auth "Sign in with email" | same as secondary |
| Underline link | Footer "Get Started" | text `#ffffff`, bottom border 1px currentColor, padding-bottom 2px, 16px / 450 |

Hover, focus-visible, pressed, disabled and loading were not forced. The button class names a 2px focus ring (`focus-visible:ring-2`) and `disabled:opacity-50`. Those states were not shown, so they stay gaps.

## Link

Nav links (Blog, Company) are 16px / 450, `#ffffff`, no underline. Docs links in dark are `#86efac` at 14px / 600. Docs links in light are `#166534`. Footer column headings are `#858585`.

## Text field

Auth email input on https://polar.sh/auth: background `#181818`, text `#ffffff`, border `1px solid #212121`, radius 12px, height 40px, padding 8px 12px, 14px / 450, shadow `0 1px 2px #0000000d`. Placeholder "Email". A hidden Cloudflare Turnstile response input sits beside it. The field was not filled and the form was not submitted, so error, filled and disabled states are gaps.

## Text area, select, checkbox, radio, switch, tabs, menu, tooltip, dialog, toast

Not present on the public pages that were opened. The docs search control is a button labelled "Search... ⌘K", not a text field that was typed into. Cookie preferences is a footer link and was not opened.

## Card

Blog index cards are unbordered links. The first card is 1073 by 297. Smaller cards are 417 by 299. No separate card fill was computed on those anchors (background transparent).

## Table

Pricing table on https://polar.sh/resources/pricing: header row background `#181818`, header cells 700 weight, body cells 450, padding 8px 16px, 16px, text `#ffffff`. No cell border.

## Avatar, badge

Not measured as components. A "Beta" span in the docs sidebar is 14px `#9e9e9e`.

## Gaps

- Signup was not completed. https://polar.sh/signup redirects to https://polar.sh/auth. The wall is the signup wall: Google, Apple, GitHub, and email, plus a Cloudflare Turnstile. Nothing was submitted.
- No card, bank, or KYC step was entered.
- OAuth buttons were not followed.
- Hover, focus, pressed, disabled, error and loading states were not captured.
- No screenshots.
