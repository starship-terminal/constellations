# Components

Measured on o-p-e-n.com, signed out, 2026-11-19. Token names point at [tokens.json](tokens.json). Raw values are the computed styles.

## Button

Primary is `.o-btn--primary`. Height 60px (`core.size.control`). Radius 999px (`core.radius.pill`). Transition background and color 300ms.

| State | Where | Fill | Text | Border |
|---|---|---|---|---|
| Filled, dark page | `.start-cta` at /global | `dark.accent` #eeece7 | `dark.on-accent` #000000 | none |
| Filled, cream page | Continue with Apple at /signin | `light.accent` #000000 | `light.on-accent` #eeece7 | none |
| Outline, cream page | Continue with email | transparent | `light.text` #000000 | 1px `light.border` |
| Outline, dark page | Try Open at /about | transparent | `dark.text` #eeece7 | 1px `dark.border` |
| Disabled | Next, empty email | transparent | #000000 | 1px #000000, class `o-btn--disabled` |
| Hover, filled dark | stylesheet only | `core.color.hoverBlack` #000000cc | | not hovered live |
| Hover, filled light | stylesheet only | `core.color.hoverCream` #eeece7cc | | not hovered live |
| Glow | `.o-btn--glow` on Try for free | | | shadow rgba(255, 255, 255, 0.6) 0 0 60px |

Padding on the fit-content primary is 0 40px. The sign-in buttons computed padding 1px 6px and font 12px Semi-Mono uppercase, which is the tertiary size sitting on a primary height. The trial button computed 18px Regular, letter-spacing -0.18px.

Tertiary is Sign in: transparent, 12px Semi-Mono, uppercase, padding 1px 6px 2px, radius 0. Crop: [components/crops/button-primary-glow.png](components/crops/button-primary-glow.png), [components/crops/button-disabled.png](components/crops/button-disabled.png), [components/crops/button-filled.png](components/crops/button-filled.png).

Book is a separate control. `.event-card-actions__button--book` is 50px tall, radius 100px, fill #eeece7, text #000000, 14px. Crop: [components/crops/button-book.png](components/crops/button-book.png).

## Link

Hero links (App, IRL, Start Free Trial) are 36px Regular, line-height 36px, letter-spacing -0.36px, color #eeece7, no underline. Footer section links are 12px Semi-Mono, 48px row height, color #eeece7. Legal links are 12px Semi-Mono uppercase. The phone-signup link is underlined.

## Text field

Email at /signin?auth=check-email. Transparent background, color #000000, 18px Regular, line-height 20.7px, padding 6px 0, radius 0, bottom border 1px #000000. Placeholder `your@email.com`. Label EMAIL is 12px Semi-Mono, color #5f5e5c, uppercase, letter-spacing -0.18px. Focus computed `outline: none`. The Next button stays disabled until the field has a value. Nothing was typed and nothing was submitted. Crops: [components/crops/text-field-default.png](components/crops/text-field-default.png), [components/crops/text-field-focus.png](components/crops/text-field-focus.png).

## Accordion

FAQ rows on /global use `.expandable`. Toggle is 18px, color #eeece7, transparent, radius 0, about 80px tall. The plus is an inline SVG. Rows on /faq are static sections, not a closed accordion: heading 14px, article title 24px.

## Card

Event card at /in-person. Image fill #1a1a1a. Place label copper #bf7d41 at 14px. Title 24px cream. Dates 18px. Class card at /all uses white text over a photo with a black 20% scrim.

## Menu

Header menu mark is a 24px filled circle, [icons/menu.svg](icons/menu.svg). The word MENU is 12px Semi-Mono uppercase. The open menu was not captured.

## Gaps

Text area, select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar, and badge were not on the captured signed-out pages.

Dialog exists as the sign-in modal (cream, padding 20px, about 574 by 500 at 1169px wide). A second dialog style, `.modal` with cream fill and shadow rgba(0, 0, 0, 0.25) 0 0 100px, is declared and was not the one on screen.

Pressed, loading, and error states were not on screen. Disabled is the empty Next button only.

Focus-visible is declared as a 2px cream outline on event booking controls. The controls that were focused (email, Next, Back) computed outline none.
