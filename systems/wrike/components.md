# Wrike components

Public signed-out surfaces only. Values are computed styles from 2026-11-18. Crops were not cut: the preview browser could not produce screenshot frames, and the headless shots are full pages in [screenshots/](screenshots/).

| Component | Where | What was read |
|---|---|---|
| Accent button | Home, pricing, trial, features | Fill `#00e05c`, text `#162136`, weight 600. Small: 40px, radius 8px, padding 8px 14px, 16px/20px. Large: 60px, radius 12px, padding 14px 22px, 20px/28px. Border 2px transparent. |
| Ghost button | Pricing "Get started", features "Request a demo" | Transparent fill, 2px solid `#162136`, same radii and type as the accent button of that size. |
| Text link | Banner "Read the report", "Wrike in 3 minutes" | `#0073d3`, no underline. Hover computed `#078eff` on the report link. |
| Nav link | Header at 1440 | 16px / 24px / 600, colour `#162136`, radius 4px, padding 3px 10px. |
| Trial email field | `/free-trial/` and the home form | Label 60px, radius 12px, fill `#f2f5fa`, border 2px `#bfc7d9`. Input text `#162136`, 16px. Placeholder copy is "Enter your business email". Nothing was typed. |
| Bento card | Home | Fill `#f2f5fa`, radius 20px, border 2px same fill. |
| Pricing card | `/price/` | White fill. At 1169px the card radius was 16px and the wrapper border was 2px `#dce1eb`. At 1440 the first card's own radius computed 0. Title 24px/600 `#162136`. |
| Popular caption | Pinnacle card | 12px / 600 / 1.5px tracking / uppercase, colour `#ffa200`. |
| Pricing tabs | Core Plans, Add-Ons, Wrike AI, FAQs | 16px/600, colour `#657694`, padding 15px 1px. Selected underline was not a computed border; the `::after` height was 2px with a transparent background in the read. |
| Footer | Home | Background `#162136`. Footer links `#bfc7d9`, 16px/400. |
| Login field | login.wrike.com/login/ | 48px, radius 12px, fill `rgba(0, 59, 157, 0.05)`, text `rgba(0, 2, 27, 0.973)`, 18px, system font. Placeholder "Email or corporate ID". |
| Login Next | Same page | Fill `#008262`, text white, 48px, radius 12px, 18px/400, transition 0.1s ease-out. Not clicked. |
| Login text button | Forgot password?, Get started now | Colour `#0054b2`, 14px, radius 8px. |
| Login OAuth chip | Google, Apple, Office | Fill `rgba(0, 59, 157, 0.05)`, 32px, radius 8px, 14px. Not clicked. |
| Login panel | Same page | White, radius 12px, shadow `0 2px 8px rgba(0,39,128,.1), 0 8px 12px rgba(0,59,157,.05)`. Page fill `#f8fafc`. |

## States

| State | Status |
|---|---|
| Default | Captured on the controls above. |
| Hover | Link hover captured (`#078eff`). Accent button hover did not change the computed fill under a mouse move. The declared hover token `--main-color-light` is `#14ff75`. |
| Focus-visible | Not captured as a painted ring. Calling `focus()` on the login email field produced no visible outline or shadow. Marketing focus transition of 0.25s ease on box-shadow and outline-color was read from computed styles at rest. |
| Pressed | Not forced. Declared active token `--main-color-dark` is `#00c652`. |
| Disabled, loading, error, selected | Not captured. The error colour `#e51739` is the light-theme custom property, not a submitted form. Login invalid border `#d2223e` is a declared token, not a painted field. |

## Gaps

- Signed-in app, password step, OTP, Google, Apple, Office, and company SSO were not entered.
- Trial submit, "or use Google account", demo request, and Contact us were not followed.
- No checkbox, radio, switch, select, textarea, toast, dialog, tooltip, table, avatar, or badge was measured on the public pages. The login app declares a switch radius of `10000px`; that control was not on the sign-in screen.
- Reduced-motion emulation was not run. A `prefers-reduced-motion: reduce` rule exists in the marketing stylesheets.
- Element crops were not cut.
