# Components

Public signed-out chrome only. Values are computed styles from 2026-11-19. Crops are absent because the preview browser returned "The browser is not producing screenshot frames" and headless Playwright was stopped by a Cloudflare challenge.

## Button

Header **Get Started** at 1440x900: background `rgb(255, 255, 255)`, text `rgb(0, 0, 0)`, height 47px, padding 15px 21px, radius 30px, Oracle 13.5px, weight 350, letter-spacing -0.24px, 1px solid white.

In-page **Get started** on `/pricing`: same size and radius, background `rgb(0, 0, 0)`, text `rgb(255, 255, 255)`.

At 390 the same header link computed to height 41px, padding 10px 14px, radius 40px, 16px.

Hover, pressed, disabled and loading were not captured.

## Link

**Log in** at 1440: transparent background, white text, 1px solid white, height 47px, padding 15px 21px, radius 30px, weight 350.

Footer column links at 390, on a black footer: white, 24px, weight 300, letter-spacing 0.36px. Social links: 18px, weight 350.

## Text field

**Find a Creator** on the marketing header: computed radius 60px, font-size 18px, transparent background. Its box was 0x0 at 390, so padding and height are a gap.

Login **Email** field: wrapper background `rgba(120, 119, 118, 0.25)`, radius 8px, height 40px, width 400px. The input itself is transparent, 14px, weight 337, placeholder "Email". The label "Email *" is 14px, weight 500, white. The field was not typed into. Error, focus and filled states were not captured.

## Icon button

**Open menu** at 390: 20x20, transparent, white, radius 0. **Close** in the off-canvas menu is an inline SVG, viewBox `0 0 22 22`, stroke currentColor, stroke-width 2. Hover and pressed were not captured.

## Menu

Creators mega menu, opened from the header: a full-width list, 1440px by 229px, padding 35.1px 35.1px 27px. Links such as Podcasters computed to 15px, weight 400, black. The panel's own background computed transparent because the paint sits on a parent. At 390 the same menu is a black full-screen sheet; Podcasters computed to 30px, weight 300, white.

## Card

Creator names (Rachel Maksy, RossDraws) sit in links about 250px wide. The link background computed transparent and no image radius was readable from the anchor. Card fill, radius and shadow are a gap.

## Other checklist components

Text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, list row, table, avatar and badge were not on the signed-out pages that loaded. The login wall has SSO buttons (Continue with Apple, Continue with Facebook): white, 1px solid `rgb(218, 220, 224)`, radius 4px, height 40px, width 400px, 14px, weight 550. Continue is white on black text, radius 8px, height 40px, width 400px.

## Gaps

- No screenshot crops. Preview frames never arrived. Headless Playwright got HTTP 403 "Just a moment..." and was not used on the login page after that.
- Signup was not submitted. No account, no email, no SSO, no card.
- Hover, pressed, disabled, loading, error and validation were not captured.
- Dark theme of the marketing site was not found. `color-scheme` on the login page is `light dark`, but no dark toggle was used.
- Footer mailing address is published on the page and is not copied into this package.
