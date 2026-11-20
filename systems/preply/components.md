# Preply components

Signed-out surfaces on preply.com, measured 2026-11-19 at 1440x900. Values are computed styles. Crops are from the home page at 2x. Login crops were not taken: a later headless load of /en/login returned a Cloudflare challenge. The login control values below come from the earlier load that rendered the form.

## Button

| Variant | Where | Fill | Text | Border | Height | Radius |
|---|---|---|---|---|---|---|
| primary | Log in submit, scroll-to-top | #ff7aac | #121117 | 2px #121117 | 48px medium, 56px large icon | 8px |
| onColor | Find your tutor | #121117 | #ffffff | 2px transparent | 56px | 8px |
| onColor hover | same, real pointer | rgba(18, 17, 23, 0.72) | #ffffff | unchanged | 56px | 8px |
| secondary | header Log In | transparent | #121117 | 2px #121117 | 40px | 8px |
| secondary hover | same, real pointer | rgba(71, 71, 133, 0.06) | #121117 | 2px #121117 | 40px | 8px |
| secondary on pink | Book a demo | #99c5ff | #121117 | 2px #121117 | 56px | 8px |
| tertiary | English / SGD | transparent | #121117 | 2px #dcdce5 | 48px | 8px |
| ghost | How our platform works | transparent | #121117 | 2px transparent, underline | 56px | 8px |

Focus-visible on ButtonBase: 2px solid #006af5, offset 2px. Transition: color, border-color and background-color, 220ms, cubic-bezier(0.22, 1, 0.36, 1).

Crops: [button-oncolor-default.png](components/crops/button-oncolor-default.png), [button-oncolor-hover.png](components/crops/button-oncolor-hover.png), [button-oncolor-focus.png](components/crops/button-oncolor-focus.png), [button-login-default.png](components/crops/button-login-default.png), [button-login-hover.png](components/crops/button-login-hover.png).

Pressed, disabled and loading were not captured.

## Icon button

Header close is onColor small, 40px square, 8px radius, #121117 fill, white icon. Menu open is ghost medium, 48px, transparent. Crop not separated from the header shot: [header.png](components/crops/header.png).

## Link

Nav links are Link--variant-accentDark: Figtree 16px, #121117, no underline, 4px radius. Footer links are the same variant on the inverse ground, white. The Ukraine banner "Join us" is Link--variant-neutralInverted: 14px, 600, white, underline.

## Text field

Login email and password: the input is transparent, 16px Figtree, color #000000, 44px tall. The wrap (.root__USarf) is 48px, 400px wide, 2px solid #dcdce5, 8px radius, padding 0 14px. Placeholder "Your email" / "Your password". Focus ring on the wrap was not re-measured after Cloudflare blocked a second login load.

Tutor search wrap: white, 48px, 8px radius, 2px #dcdce5, padding 0 16px. Placeholder "English".

## Checkbox

Remember me on the login form. Native input is 16px and transparent. The painted box (.checkbox__KtCna) is 20px, #121117 fill, 2px #121117 border, 4px radius. Unchecked and error states were not captured.

## Card

Step card (styles_card): white, 1px solid #121117, 4px radius, padding 32px 32px 0. Tutor card: white, 0.5px solid #6a697c, 8px radius, padding 12px. Crop: [step-card.png](components/crops/step-card.png).

## Heading

Platform, 700. At 1440: hero 63/68, display 96/96, section 48/52, stat 32/36, tile 24/32, label 20/24. At 390 the hero is 40/36.8. Crop: [heading-hero.png](components/crops/heading-hero.png).

## Gaps

- Select, radio, switch, tabs, tooltip, dialog, toast, avatar, badge, table, list row: not present on the captured signed-out pages, or not opened.
- Language and currency menus exist in the header. The visible trigger was measured. The menu panel was not opened: the first matching button was hidden.
- Validation error, empty, loading, destructive confirm: not reached. The login form was not submitted.
- Signup is "Sign up as a student" and "Sign up as a tutor", plus Google, Facebook, Apple and corporate SSO. Not an email-only form. Not entered.
- Dark theme: not present. prefers-color-scheme: dark did not restyle the page.
- Pressed and disabled button states: not captured.
