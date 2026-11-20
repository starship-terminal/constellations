# Components

Public signed-out Resend, measured on 2026-11-19 at a 1169 by 731 CSS viewport. Screenshots were not saved: the preview browser returned "The browser is not producing screenshot frames." Values below are computed styles.

## Button

Marketing and auth buttons use `border-radius: 16px` (`rounded-2xl`).

| State | Where | Values |
|---|---|---|
| Primary, header | "Get started" on https://resend.com/ | transparent background, white text, 14px / 600 / 20px, padding 0 16px, height 40px, radius 16px, 2px border `oklab(0.999994 0.0000455678 0.0000200868 / 0.05)` |
| Primary, hero | Home "Get started" | same border and radius, 16px / 600 / 24px, padding 0 20px, height 48px, background image `linear-gradient(104deg, rgba(253, 253, 253, 0.05) 5%, rgba(240, 240, 228, 0.1) 100%)`, transition `0.2s cubic-bezier(0.4, 0, 0.2, 1)` |
| Ghost | Header "Log in" and hero "Documentation" | transparent background, text `#a1a4a5`, 16px radius. Header is 40px / 14px / 600. Hero is 48px / 16px / 600, padding 0 20px |
| OAuth | Login "Log in with Google" and "Log in with GitHub" | same glass border as primary, white text, 16px / 600, height 48px, width 248px, padding 0 20px |
| Submit, disabled | Signup "Create account" while the password was too short | text `oklab` white at 50 percent (canvas `#808080`), opacity 0.3, cursor not-allowed, height 48px, 14px / 600 |
| Submit, enabled | Same button after a 12-character mixed password was typed | opacity 1, color `#ffffff`, cursor pointer. The form was not submitted |
| Icon button | Password "Show value" | 24 by 24, radius 8px, text `#a1a4a5` |

Hover, focus-visible, pressed and loading were not forced. The button class names `duration-200`, `disabled:opacity-70` on ghost buttons, and `focus-visible:ring-2` on nav links. Those states were not shown, so they stay gaps.

## Link

Nav links (Pricing) are 14px / 500, `#a1a4a5`, height 58px, padding 4px 16px, no radius. "Learn more" on home is 14px / 400, `#f0f0f0` or `display-p3 0.988 0.992 1 / 0.937` (canvas `#ecedef`). Signup "Sign up" is 14px / 600, `#f0f0f0`. Docs links in dark are Inter 16px, `#f2f2f2`. Docs links in light are `oklch(0.21 0.034 264.665)`, canvas `#101828`.

## Text field

Login email on https://resend.com/login: transparent background, white text, 2px border `oklab` white at 5 percent, radius 16px, height 48px, padding 0 16px, 16px / 400, width 512px. Placeholder "alan.turing@example.com", color `oklab` white at 50 percent (canvas `#808080`). Password uses the same field with padding `0 44px 0 12px` and placeholder "••••••••••••". Label "Email" is 14px / 400, `#a1a4a5`. Focus outline on the email field computed as `rgb(153, 200, 255) none 1px` (none, so the colour is the outline colour, not a visible ring). A visible focus ring was not shown.

Signup at https://resend.com/signup uses the same fields. The email was set to kaichen@agentmail.to and the password to a 24-character mixed string, then both were cleared. The form was not submitted. Google and GitHub were not followed. An invisible Stripe hCaptcha iframe is in the page. It was not interacted with.

## Password hints

On signup, before a valid password: "At least 12 characters" and "Mix of letters, numbers, and symbols" at 12px, `#a1a4a5`, with "— not satisfied". After a valid password: the list item colour is `color(display-p3 0.434 0.828 0.573)` and the inner span is `oklab(0.346038 -0.00882651 -0.00805217)`. Those oklab and display-p3 strings are the reading. They are not forced into a hex token.

## Checkbox

Signup has a checkbox labelled "Send me occasional updates, guides, and promotions." The input itself measured 1 by 1 CSS pixels with `appearance: auto` and a transparent background. The painted box was not measured, so size, colour and checked state are gaps. The label is 14px / 400, `#a1a4a5`.

## Text area, select, radio, switch, tabs, menu, tooltip, dialog, toast

Not present on the public pages that were opened. Docs search is a button labelled "Search... ⌘K", not a field that was typed into. Pricing has no month/year switch in the buttons that were listed.

## Card

Pricing plan cards on https://resend.com/pricing: 271px wide, 681px tall at this viewport, padding 24px, radius 16px, transparent background, 1px border `color(display-p3 0.882 0.949 0.996 / 0.183)`. Four cards: Free, Pro, Scale, Custom. Plan titles are aBCFavorit 16px / 400, colour `display-p3 0.988 0.992 1 / 0.937`.

## Table

https://resend.com/pricing contains six `table` elements under the plan cards. Cell padding, borders and type were not read individually. That is a gap.

## Avatar, badge

Not captured as components. "Recommended" sits inside the plan `h3` and was not a separate badge. The footer status link "All systems operational" is 12px, `#f0f0f0`.

## Docs search, light

After "Switch to light theme" on https://resend.com/docs/introduction, the search button is background `#ffffff`, text `#6f6f6f`, radius 12px, border `#eeeeee`. Docs `h1` is Inter 36px / 600, `#161616`. Main background is `#ffffff`. `html` class becomes `light`.
