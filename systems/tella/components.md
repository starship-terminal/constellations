# Components

Measured on www.tella.com and authkit.tella.tv on 19 November 2026, signed out, at 1440 by 900 and 2x. Crops are cut from the full-colour captures before quantizing.

## Button

Primary nav (Sign up): fill `#5E51F8`, white label, 15px medium Oracle, padding 4px 24px, height 30.5px, full pill, no shadow. Transition transform, box-shadow and opacity, 150ms ease-out.

Primary body (Get started, Buy now on the highlighted plan): same fill, 16px medium, padding 8px 48px, min-height 44px, full pill. The class is `bg-indigo-800`. The painted colour is `#5E51F8`, not Tailwind indigo-800.

Secondary (Log in, Buy now on the other plans, Contact sales): white fill, `#0C0A09` label, 1px border at black 8% (flattened `#EAEAE9` over the page), same pill and padding as the matching size.

Hover, pressed and disabled were not forced. AuthKit declares hover `#5345E1` and active `#4833CF` on `--branded-button-hover-background` and `--branded-button-active-background`. Those states were not painted.

![Sign up](components/crops/button-primary.png)

![Get started](components/crops/button-primary-large.png)

## Link

Footer and nav text links are 15px Oracle regular, black at 50% (flattened `#848483` over the page), 4px radius, colour transition 150ms, hover to black. Focus is declared as a 2px ring. The ring was not forced.

## Text field

The marketing pages that were read have no text field. AuthKit's email field is 40px tall, 6px radius, white at 85%, with an inset 1px ring at black 19%. The input itself is 5px radius, 16px, placeholder "Your email address". Focus paints a 2px outline `#939BFF` and keeps the inset ring. The field was focused and not submitted.

## Switch

Annual billing, on: track `#5E51F8`, 44 by 24px, 2px transparent border, full pill. Thumb white, 20px, full pill. Transition colours 200ms ease-out. Focus is declared `ring-2 ring-indigo-500`. The off state was not captured.

![Annual switch on, with the 50% off badge](components/crops/switch-on.png)

## Badge

"50% off": `#111111` fill, white 12px regular, padding 2px 8px, full pill, height 22px.

## Card

Pricing article: 32px radius, 1px border at black 8%, inset 1px white ring, 24px padding. The plan head is white at 50%. The highlighted plan uses the primary body button. The others use the secondary button.

![Pricing cards](components/crops/card-plan.png)

The home hero frame uses the same 32px radius, hairline and inset ring, with a gradient from black 1% to black 3.5%.

## Accordion

FAQ rows are buttons, min-height 64px, padding 20px 0, 16px. Focus-visible is declared as a 2px inset indigo-500 ring. A row was not opened, so the expanded state is a gap.

## Not on these pages

Text area, select, checkbox, radio, tabs, menu, tooltip, dialog, toast, list row, table and avatar were not on the home page, the pricing page, or the signed-out sign-in. The signed-in product was not entered.

## Icons

Inline SVGs are on the page (24px and 20px, some `currentColor`). They were not extracted into `icons/`. The wordmark is in the screenshots. `icon.png` is the site's favicon.ico, the largest frame at 48px, placed on a 128px canvas.
