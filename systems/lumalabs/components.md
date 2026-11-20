# Components

Public marketing components from lumalabs.ai, captured 2026-11-21, signed out. Crops are the viewport screenshots that show each control. Values are token names from [tokens.json](tokens.json).

| Component | States | Where |
|---|---|---|
| Button | default, hover, focus-visible | Sign In and Try for free on [home-light-default.png](screenshots/home-light-default.png). Hover fill `#d9d9d9` measured with forced `:hover`. Focus outline `rgb(0, 95, 204)` offset 4px. Pressed computed no change. |
| Icon button | default | Submit prompt and social icons on the home page. |
| Link | default | Nav links PRODUCT through JOIN US. No underline. |
| Text field | default | Home prompt textarea. Not submitted. |
| Text area | default | Enterprise and contact-sales message fields. Not filled. |
| Select | default | Enterprise industry, size, and region. The listbox did not open from the hero viewport. Not captured open. |
| Checkbox | not present | No public checkbox. |
| Radio | not present | Billing is a two-button toggle, not a radio. |
| Switch | not present | |
| Tabs | default, selected | Monthly/Yearly on [pricing-light-default.png](screenshots/pricing-light-default.png) and [pricing-light-yearly.png](screenshots/pricing-light-yearly.png). Ray3.2/Uni-1.1 on [api-light-default.png](screenshots/api-light-default.png). |
| Menu | open | Phone nav on [mobile-home-light-nav-open.png](screenshots/mobile-home-light-nav-open.png). Desktop nav has no menu. |
| Tooltip | not present | |
| Dialog | not present as a modal | FAQ rows expand in place. See [api-light-faq-open.png](screenshots/api-light-faq-open.png). |
| Toast | not present | |
| Card | default | Pricing plan cards on [pricing-light-default.png](screenshots/pricing-light-default.png). |
| List row | default | Career role rows on [careers-light-full.png](screenshots/careers-light-full.png). |
| Table | default | Subprocessors page. |
| Avatar | not present | |
| Badge | default | Banner "It's here! Luma is now in Claude and ChatGPT". |

## Shared values

- Page `light.page` `#ffffff`. Text `light.text` `#000000`. Muted `light.muted` `#737373`.
- Primary controls are pills (`core.radius.pill`) with inverted fill: white on the black hero, black on the white page.
- Focus ring is the browser outline, colour `#005fcc`, offset 4px (`light.focus`).
- Display type is Graphik 52px / 500 / 62.4px, letter-spacing -2.08px.

## Gaps

- Signed-in app, password field, email code, passkey, Google, and Apple: not captured. Sign In opens `https://auth.lumalabs.ai/sign-up`.
- Dark theme: declared in CSS, not applied by any public control. Tokens exist. No live dark screenshot from this run.
- Select listbox open, tooltip, toast, checkbox, radio, switch, avatar: not present or not reached.
- Hover and focus crops are measurements, not separate PNG crops. The viewport shots show default.
- Validation error, destructive confirmation, and onboarding: behind the account wall.
