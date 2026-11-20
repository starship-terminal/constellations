# Components

Public controls only. Values are the computed style, named with a token when one matches. A state that was not on the page is listed under Gaps.

## Button

Sign in, home nav. Ink face, white label, 36px radius, 36px tall, padding 4px 16px, width 75px. Sana Sans 14px / 450. [components/crops/button-signin-default.png](components/crops/button-signin-default.png)

| State | What changed |
|---|---|
| Default | Background `#0a1217`, text `#ffffff` |
| Hover | Not measured. A synthetic mouseenter did not change the computed background. |
| Focus | Browser outline `rgb(229, 151, 0) auto 1px`. No product focus ring on this control. |

Explore, on each product card. Ink face, white label, 24px radius, 39px tall, padding 8px 16px, width 82px. Sana Sans 14px / 450. Border `1px solid transparent`. [components/crops/button-explore-default.png](components/crops/button-explore-default.png)

Accept, cookie notice. Ink face, white label, pill radius, 36px tall, padding 6px 16px. Sana Sans 14px / 500. Class `duration-200`.

Only necessary, cookie notice. Transparent face, ink label, `1px solid rgba(10, 18, 23, 0.1)`, pill radius, 36px tall, padding 6px 16px.

Enter your work email, sign-in, disabled until an address is present. Face `rgba(232, 232, 232, 0.04)`, label `rgba(232, 232, 232, 0.4)`, pill radius, 44px tall, padding 12px 24px, 352px wide. Sana Sans 14px / 500. The label becomes Continue once an address is in the field. The face did not change in the reading taken then.

Back, code step. Fog face `#e8e8e8`, night label `#131314`, pill radius, 44px tall, padding 12px 20px, width 74px.

Continue, code step, disabled. Same disabled face as the email submit, 44px tall, 318px wide.

## Link

Home nav links are Sana Sans 14px / 400, ink `#0a1217`, line-height 19.6px, padding 2px 12px, radius 6px, 36px tall. The stylesheet hover is `rgba(0, 0, 0, 0.03)`. A synthetic mouseenter did not paint it.

Footer links are Sana Sans 14px / 450, ink, line-height 21px. The hover rule sets the colour to `rgba(10, 18, 23, 0.7)`.

Sign-in nav links sit in a 302 by 44 pill, background `#1e1f20`, radius 9999px. The links are 13px / 500, `rgba(232, 232, 232, 0.6)`.

Agreement links on the sign-in form are 13px / 400, `rgba(232, 232, 232, 0.4)`, no underline in the computed style.

## Text field

Work email, sign-in, at rest. Transparent face, fog text `#e8e8e8`, 352 by 48, radius 24px, padding 12px 24px, border `1px solid rgba(232, 232, 232, 0.15)`. Placeholder `rgba(232, 232, 232, 0.4)`, 14px / 500.

Focused. Outline `rgb(232, 232, 232) none 3px`, no shadow, border unchanged. The class names `focus:enabled:border-foreground-20`. That rule did not paint.

One-time code. A 400 by 50 pill, border `1px solid rgba(232, 232, 232, 0.6)`, padding 0 42px. Digits are 14px / 500 with letter-spacing 52.3333px. Focus outline on the input was the browser default `rgb(229, 151, 0) auto 1px`.

## Card

Product card, home. 544 by 583 at innerWidth 1169, 342 by 367 at 390. Radius 24px, overflow hidden, no shadow. The face is a photograph. Title is 20px / 450. [components/crops/card-product.png](components/crops/card-product.png)

Cookie card. White, radius 32px, padding 32px, width 510px. It was dismissed and is not in the screenshots.

Sign-in hero panel. `#17181a`, radius 18px, 653 by 605. The image inside had no painted source in the reading.

## Menu

Products dropdown. Mounted and hidden. White, radius 10px, width 240, shadow `rgba(0, 0, 0, 0.05) 0 0 0 1px, rgba(0, 0, 0, 0.08) 0 8px 16px`. A click did not open it. The hover rule on a dropdown row is `rgba(0, 0, 0, 0.03)`.

Phone menu. At 390 the desktop nav is `display: none`. The menu button is 38 by 38, radius 9999px. A click painted a fixed overlay, `rgba(0, 0, 0, 0.5)`, full viewport. The panel that should list the links did not report a box.

## Accordion

FAQ on the sign-in page. Title is 20px / 500, fog. An item button is 14px / 500, `rgba(232, 232, 232, 0.8)`, padding 10px 18px, radius 14px, 40px tall, transparent face. The open answer is 14px / 400, `rgba(232, 232, 232, 0.4)`, line-height 19.6px.

## Gaps

- Pressed, loading and error states were not on the page.
- Sign in and Explore hover were not painted by a synthetic mouseenter. The stylesheet hover for nav links is recorded above.
- The Products dropdown was mounted and not opened.
- The phone menu panel did not report a box. Only the overlay was measured.
- Text area, select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar and badge were not on these pages.
- Google sign-in is an iframe. It was not clicked, so its face was not measured.
- The sign-in page has no screenshot. The preview tab could not produce frames, and a headless shot of that page was not kept.
