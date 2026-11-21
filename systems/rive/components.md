# Rive components

Public marketing components on rive.app, read signed out on 2026-11-21. Crops live in [components/crops/](components/crops) when the measure pass wrote them. Values are token names from [tokens.json](tokens.json).

## Shell

| Component | States | Values |
|---|---|---|
| Header | default | Height 63px on the PRODUCTS control (`dark.component.header.height`). Label colour `dark.muted`. Inter 12px / 500, letter-spacing 0.96px (`core.typography.label`). |
| Logo | default | Home link `a[href="/"]`. |
| Nav link | default | PRICING anchor, colour `dark.link`. |
| Get started | default | White fill `dark.accent`, black text `dark.on-accent`, radius 4px, height 27px, padding 5px 9px 6px, inset 1px ring `dark.border`. |
| Products menu | opened | Desktop mega menu from `button.rn-top`. Screenshot [home-dark-products-menu.png](screenshots/home-dark-products-menu.png). |
| Mobile menu | opened | `button[aria-label="Open menu"]` at 390px. Screenshot [mobile-home-dark-menu-open.png](screenshots/mobile-home-dark-menu-open.png). |

## Home

| Component | States | Values |
|---|---|---|
| Hero title | default | Orbitron 48px / 900, line-height 48.96px, letter-spacing -1.44px, colour `dark.text`. |
| Section title | default | Orbitron 24px / 700, colour `dark.heading`. |
| Copy button | default | Height 29px, radius 4px, 1px solid white border, fill rgba(255,255,255,0.9). |
| Demo segment | default | `button[aria-label="Show Dashboard"]` and the other Show * controls. In-page switcher. |

## Pricing

| Component | States | Values |
|---|---|---|
| Pricing title | default | Orbitron 34px / 900, colour `dark.text`. |
| Billing period | default | YEARLY / MONTHLY text labels. MONTHLY colour `dark.muted-2`. Click swaps prices in place. |
| Plan CTA | default | GET STARTED on a plan card. Card control fill `dark.surface`, height 40px, radius 4px. Not followed. |
| Plan card | default | Ancestor of GET STARTED. |

## Forms

| Component | States | Values |
|---|---|---|
| Email field | default | `input[type=email]`, placeholder `email@rive.app`. Not filled. Not submitted. |
| Sign up button | default | Newsletter submit. Not pressed, so a pressed state was not captured. |

## Docs

| Component | States | Notes |
|---|---|---|
| Docs nav | default | Sidebar links on `/docs/getting-started/introduction`. |
| Theme preference | opened if the control mounted | "Change theme preference". A light theme was not applied. |
| Search | default | Not submitted. |

## Gaps

- Login and signup walls were recorded and not entered. No password, Google, Apple, or SSO control was used. Button, field, and error states behind the wall are Not captured.
- Editor app (`https://editor.rive.app`) is a separate host. Not captured.
- Checkbox, radio, switch, select, text area, toast, table, avatar, tooltip, and destructive confirmation were not present on the public marketing pages reached.
- Disabled, loading, and validation-error states were not shown without submitting a form.
- Focus ring colour is Not captured as a stable computed outline.
- Light theme: marketing pages paint dark only. Docs expose a preference control. A light docs theme was not applied, so light tokens are Not captured.
- Hover and pressed crops depend on the measure pass. Where a crop file is missing, the state is Observed in the page screenshots or Not captured, as the coverage table in the README says.
