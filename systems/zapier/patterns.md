# Zapier patterns

Signed-out public pages only. Measured 2026-11-19. Screenshots were not produced (`preview_snapshot`: "The browser is not producing screenshot frames"), so each pattern is described from the DOM and computed styles.

## Marketing home

[https://zapier.com/](https://zapier.com/). Header is 56px, fill `{color.bg.page}`, padding 0 40px. Left: wordmark SVG 104 by 28. Center: Products, Solutions, Resources, Enterprise, Pricing, Contact sales. Right: Log in (subtle, 36px) and Sign up (brand pill, radius 18px).

Hero: uppercase eyebrow in `{color.text.muted}`, 12px, tracking 0.48px. Display heading in Degular Display, 56px / 56px, weight 500, `{color.text.primary}`. Subheading in Inter 14px / 21px, `{color.text.secondary}`. Two actions side by side: brand "Start free with email" and secondary "Start free with Google".

Lower sections alternate Degular Display headings (48px) and Serrif feature headings (28px, weight 300). Feature cards sit in a row: rest `{color.bg.raised}`, radius 12px; the active card uses `{color.bg.selected}` and a 1px ink ring.

Footer: fill `{color.bg.page}`, 1px `{color.border.subtle}` top border, padding 40px 20px, then an A to Z app index.

## Pricing

[https://zapier.com/pricing](https://zapier.com/pricing). Same header, with Sign up labelled "Get started for free". Eyebrow "PRICING", then the same 56px Degular heading.

Three tabs: Platform (selected, ink fill, cream label, radius 8px, 64px tall), Agents, Chatbots. Under them, a radio pair: Pay monthly (unchecked) and Pay yearly (checked, "Save 33%").

Four plan cards in a row, square corners, 1px `{color.border.default}`, padding 28px: Free ($0), Professional ($19.99), Team ($69), Enterprise (contact). Amounts are 36px / 54px. Card CTAs are ink buttons, 48px, full width. "Contact Sales" under one card is a text link. Those CTAs were not followed.

## Login

[https://zapier.com/app/login](https://zapier.com/app/login). A thinner app header: Help, Explore apps, Contact Sales (plum text, 1px border, radius 2px, 32px), Sign up (brand pill, radius 40px). Page fill `{color.bg.page}`. Body text on this host computed to rgb(55, 44, 43), a step the marketing ramp does not name.

Two columns. Left promo: 20px / 25px heading, weight 600, tracking -0.5px, plus a secondary "Explore Zapier Enterprise" button. Right card: 430px, padding 32px, 1px `{color.border.subtle}`, radius 4px. Title "Log in to your account". Four SSO buttons (Google, Facebook, Microsoft, SSO), 48px, secondary border. Then email and password fields and a disabled brand Continue button until the form is valid. "Forgot Password?" and "Sign Up" are underlined 14px links. Nothing was typed or submitted. SSO was not followed.

## Signup

[https://zapier.com/sign-up](https://zapier.com/sign-up). Same chrome as login, with Log in in the header. The form asks for work email, first name, last name and password, plus a password rule list and a terms line. "Get started for free" is an enabled brand button, 48px. Not submitted: the form is not email-only.

## Not captured

App shell after login, validation error after submit, empty, loading, error page, destructive confirmation, toast feedback, search, tables, onboarding. Dark theme was not offered on these pages.
