# Components

Public marketing components, measured on reclaim.ai on 2026-11-21. Crops of individual states were not cut this pass. The screenshots below show each control in place. Values are token names where a token exists.

## Shell

| Component | States | Where |
|---|---|---|
| Product menu | closed, open | [home-light-default](screenshots/home-light-default.png), [home-light-product-menu](screenshots/home-light-product-menu.png) |
| Solutions menu | open | [home-light-solutions-menu](screenshots/home-light-solutions-menu.png) |
| Resources menu | open | [home-light-resources-menu](screenshots/home-light-resources-menu.png) |
| Get Started | default | [home-light-default](screenshots/home-light-default.png). Fill `light.accent` #0061fe, text `light.onAccent`, radius 10px, height 40px. |
| Book a Demo | default | Same shot. Transparent fill, 1px black border, 10px radius. |
| Pricing link | default | Same shot. Colour `light.link` #333333, Poppins 18px. |
| Phone menu | open | [mobile-home-light-menu](screenshots/mobile-home-light-menu.png) |

Hover, focus-visible, and pressed were not cropped. The stylesheet declares Osano focus-visible rings. Those are the cookie vendor, not the product controls.

## Home

| Component | Where |
|---|---|
| Display headline | h1, Sharp Grotesk 90px / 90px, weight 500, letter-spacing -2px. `core.typography.display`. |
| Section heading | h2, Sharp Grotesk 48px / 57.6px. `core.typography.heading`. |
| FAQ | Questions are buttons. The open state was not captured. |

## Pricing

| Component | Where |
|---|---|
| Billing toggle | [pricing-light-default](screenshots/pricing-light-default.png) yearly, [pricing-light-monthly](screenshots/pricing-light-monthly.png) monthly |
| Feature table | [pricing-light-features](screenshots/pricing-light-features.png) |
| Plan CTA | Get Started on a plan. Not followed. Same blue as the nav CTA. |

## Auth

| Component | Where |
|---|---|
| Provider button | [login-light-wall](screenshots/login-light-wall.png). Google, Microsoft, Dropbox, SSO. Not clicked. |

## Not present on the public site

Text area, select (except the pomodoro sound select and the calculator select), checkbox, radio, switch, tabs (except pomodoro session tabs and home audience tabs), tooltip, toast, table (except the pricing comparison), avatar, badge. The signed-in app was not reached, so those may exist there. That is not captured.

## Gaps

- No `components/crops/` set. Element states are visible in page screenshots, not as isolated crops.
- Hover, focus-visible, pressed, disabled, loading, and error were not measured on product controls.
- The contact scheduler is a HubSpot iframe. It was not filled.
- Dark theme tokens are declared (`core.declaredDark`) and not painted.
