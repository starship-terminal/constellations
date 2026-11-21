# Limitless components

Measured on the public site on 2026-11-18, light theme, 1440 CSS pixels. Crops are 256-colour PNGs. A colour is followed by the token that holds the same value.

## Navigation

**Nav link** ([default](components/crops/nav-link-default.png), [hover](components/crops/nav-link-hover.png), [focus](components/crops/nav-link-focus-visible.png), [pressed](components/crops/nav-link-pressed.png)). 16px / 600, slate 600 `light.textBody`, pill radius. Hover paints slate 800 ink on `light.navHover` (8% slate). Focus-visible is the browser outline, 1px auto `#005fcc` `light.focus`. Pressed matches hover (forced `:active`).

**Solutions** ([default](components/crops/nav-solutions-default.png), [hover](components/crops/nav-solutions-hover.png)). Same pill as the nav link. Opens the menu; it does not navigate.

**Wordmark** ([default](components/crops/wordmark-default.png)). Bold 700, the purple star plus "Limitless".

**Sign in** ([default](components/crops/signin-link-default.png)). 16px / 500, slate 500 at 70% `light.textMuted`. Destination is `https://app.limitless.ai`. The link was measured, never followed from this control.

**Footer link** ([default](components/crops/footer-link-default.png)). 14px / 500, gray 300 `light.footerInk`, on the dark footer band.

## Menu

**Solutions menu** ([opened](screenshots/home-light-solutions.png)). White panel, soft shadow `core.elevation.popover`, grouped By use case / By role / By job / By condition.

**Menu item** ([default](components/crops/menu-item-default.png), [hover](components/crops/menu-item-hover.png)). 12.8px / 500 zinc 600, 6px radius. Hover is zinc 700 on a 5% purple wash `color.purple.tint`. Items were not followed from the open menu.

## Type

**Display** ([hero](components/crops/hero-title-default.png), [product](components/crops/product-title-default.png)). 60px, weight 600 on the acquisition home and 700 on solution pages, tracking -1.5px, slate 900 `light.text`.

**Section heading** ([crop](components/crops/section-heading-default.png)). 36px / 700, slate 900.

**Body** ([crop](components/crops/body-copy-default.png)). 18px / 400, slate 600, relaxed leading. The letter sits in a 24px-radius card ([crop](components/crops/letter-card-default.png)).

## Button

**Copy** ([default](components/crops/copy-button-default.png), [hover](components/crops/copy-button-hover.png), [focus](components/crops/copy-button-focus-visible.png), [pressed](components/crops/copy-button-pressed.png)). Purple 500 `light.accent` fill, white label, 4px radius, 32px tall. Hover is purple 600 `light.accentHover`. Copies the MCP URL to the clipboard; it does not submit.

**Carousel next** ([default](components/crops/carousel-next-default.png), [hover](components/crops/carousel-next-hover.png)). 40px circle, white, slate 700 icon, small shadow. Hover fills slate 50. The slide was not advanced.

**Open roles** ([default](components/crops/roles-link-default.png)). Text link to Ashby. Measured, not followed.

## Field

**Email** ([default](components/crops/email-field-default.png), [focused](components/crops/email-field-focused.png)). On the sign-in card. Placeholder "Continue with your email", zinc 800 ink, white fill. Submitting it (2026-11-18 signed-in pass) opened Sign Up Unavailable. Google was not used.

**Help search** ([default](components/crops/search-field-default.png), [focused](components/crops/search-field-focused.png)). 18px on a translucent white pill over the purple help band. Focus turns the fill solid white and the ink `#1a1a1a`. Nothing was queried.

## Disclosure

**FAQ** ([closed](components/crops/faq-default.png), [hover](components/crops/faq-hover.png), [opened](components/crops/faq-open-opened.png)). Native `details`/`summary` on `/privacy`. Closed summary is 18px / 700 on gray 100, 8px radius. Opening is local; nothing is submitted.

## Docs

**Anchor** ([default](components/crops/anchor-link-default.png)). Purple 500 `light.link`, 16px / 500. In-page only.

**Code** ([crop](components/crops/code-block-default.png)). 14px mono on slate 100, 4px radius.

## Card

**Help collection** ([default](components/crops/collection-card-default.png), [hover](components/crops/collection-card-hover.png)). White, 8px radius, 16px ink. Staff names on the cards are published help-center bylines.

## Auth boundary

**Continue with Google** ([default](components/crops/google-button-default.png), [hover](components/crops/google-button-hover.png), [focus](components/crops/google-button-focus-visible.png)). White, 8px radius, 48px tall, zinc 800 label, hairline shadow. Hover fills `#fafafa`. Focus adds a purple 700 ring. The button starts OAuth. It was not pressed.

**Email field, empty.** Focused on 2026-11-21 with nothing typed ([shot](screenshots/signin-light-email-focused.png)). The submit arrow was not clicked.

**Sign Up Unavailable** is a 2026-11-18 reading only. Those screenshots were removed on this refresh. The crop [signup-unavailable-dialog-default](components/crops/signup-unavailable-dialog-default.png) remains from that earlier submit. Do not treat it as a state this pass displayed.

## Gaps

- Select, checkbox, radio, switch, tabs, tooltip, toast, table, avatar and badge do not appear on the signed-out marketing surface or on this dialog. The help cards show staff avatars; those are Intercom artwork, not a Limitless avatar component.
- Disabled, loading, error and validation states were not reached. Nothing was submitted on 2026-11-21.
- The support chat widget on `/support` is a third-party embed. It was not opened or typed into.
- Lifelogs, settings, billing and account deletion were not reached. Limitless is no longer accepting new users.
- Checkout and Pendant purchase were not opened. The dialog tells Pendant owners to email support@limitless.ai.
- Ashby careers (`jobs.ashbyhq.com/limitless`) and the Slack community invite are off-site. Neither was followed.
