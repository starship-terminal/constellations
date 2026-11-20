# Components

Measured on the public signed-out surfaces of me.sh (the 301 target of clay.earth) and the signed-out card at app.me.sh/login, 2026-11-19, desktop 1440x900 and phone 390x844. Crops are in [components/crops/](components/crops).

| Component | States read | Crop | Notes |
|---|---|---|---|
| Page ground | default | [page-default.png](components/crops/page-default.png) | `html` paints `#000` on marketing routes. `body` is transparent. |
| Hero title | default | [hero-title-default.png](components/crops/hero-title-default.png) | VerlagCondensed 64/700, `#fefef7`, letter-spacing 0.88px. |
| Section title | default | | Light-band h2, VerlagCondensed 48/900, `#1d1d1f`. |
| Nav pill | default | [nav-pill-default.png](components/crops/nav-pill-default.png) | 16px radius, 24px horizontal padding. Sheen is a `::before` gradient, not a flat fill. |
| Nav link | default, hover, focus-visible | [nav-link-default.png](components/crops/nav-link-default.png) | Verlag 12/700, tracking 1px. Hover and programmatic focus did not change the computed colour. |
| Nav menu trigger | default, opened | [nav-menu-trigger-default.png](components/crops/nav-menu-trigger-default.png) | Local toggle. Opened panel is [nav-menu-default.png](components/crops/nav-menu-default.png). |
| Sign in link | default, hover | [signin-link-default.png](components/crops/signin-link-default.png) | Rest `rgba(255,255,255,0.64)`, hover `#fff` on `rgba(255,255,255,0.08)`, radius 8px. Not followed. |
| Header CTA | default, hover | [primary-cta-default.png](components/crops/primary-cta-default.png) | Tan `#f2b98b`, hover `#efab74`, inset 1px `rgba(255,255,255,0.24)` ring, radius 8px. Not followed. |
| Hero CTA | default, hover | [hero-cta-default.png](components/crops/hero-cta-default.png) | Inner 204x54 `#fdfcfa`, radius 14px, black 18/600 text, white glow. Outer ring is a 225deg cyan-violet-amber gradient. Not followed. |
| Bottom CTA | default | [bottom-cta-default.png](components/crops/bottom-cta-default.png) | White 183x52 pill, radius 16px, on the `#0f0f10` footer. |
| Filter pill | default, hover | [filter-pill-default.png](components/crops/filter-pill-default.png) | 480x48, Verlag 20/400, `#1d1d1f`. Hover did not change the computed fill. |
| Footer | default | [footer-default.png](components/crops/footer-default.png) | `#0f0f10`, padding-top 150px. Links at 12/700, `rgba(255,255,255,0.4)`, tracking 1px. |
| Pricing ground | default | [pricing-ground-default.png](components/crops/pricing-ground-default.png) | `#f9f8f6`, text `#1f1f1f`. |
| Pricing title | default | [pricing-title-default.png](components/crops/pricing-title-default.png) | VerlagCondensed 48/700, line-height 56px. |
| Plan card | default | [plan-card-default.png](components/crops/plan-card-default.png) | 288px, radius 16px, 1px `#eceae8`, fill `rgba(149,149,149,0.06)`, padding 22px 24px 24px. |
| Popular plan | default | [plan-popular-default.png](components/crops/plan-popular-default.png) | Same card plus 1px `#fb7232` border and a 3px orange ring shadow. |
| Plan CTA | default, hover | [plan-cta-default.png](components/crops/plan-cta-default.png) | 238x44, radius 10px, 1px `rgba(31,31,31,0.4)`. Hover fills `#fb7232` with white text. Not followed. |
| Billing toggle | default | [billing-toggle-default.png](components/crops/billing-toggle-default.png) | 227x40, radius 12px, fill `rgba(31,31,31,0.06)`. Not flipped. |
| Sign-in email | default, focus | [signin-email-default.png](components/crops/signin-email-default.png) | 272x40, radius 6px, fill `rgba(72,73,74,0.04)`, border `rgba(72,73,74,0.1)`, SFProText 14. Focus did not paint an outline. Nothing typed. |
| Sign in with email | default, hover | [signin-email-btn-default.png](components/crops/signin-email-btn-default.png) | 272x40, radius 12px, fill `#ff6821`, label `rgba(255,255,255,0.6)`. Hover did not change the fill. Not clicked. |
| Google button | default | [signin-google-default.png](components/crops/signin-google-default.png) | 272x44, radius 12px, `#5383ec`. Not clicked. |
| Apple button | default | | 272x44, radius 12px, `#1f1f1e`. Not clicked. |

## Gaps

- Text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, badge: not present on the captured public pages.
- Disabled, loading, error, and validation states: nothing was submitted, so they were not painted.
- Pressed: not forced. Hover was a real pointer hover.
- Nav link focus-visible: programmatic focus did not change the computed style. A keyboard-only ring was not observed.
- Sign-in focus: the email field's computed outline stayed `0px none`.
- Status colours (success, warning, danger, info): not painted on these pages.
- Dark theme as a user toggle: not present. Dark and light are different routes.
- `systems/clay-earth` is a different package for the same redirect target. This package does not copy its tokens.
