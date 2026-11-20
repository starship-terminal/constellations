# Components

Signed-out controls measured on 2026-11-19. Values are computed styles of the node that paints the control. Token names are the nearest semantic role. Crops are 2x.

## Button

The login wall's primary action is a `role="button"` whose paint sits on an inner `role="none"` div.

| State | Crop | Background | Text | Radius | Height |
|---|---|---|---|---|---|
| Login, rest, disabled until a field has a value | [button-login-default.png](components/crops/button-login-default.png) | `rgb(0, 100, 224)` (declared `--primary-button-background` is `#0095f6`, `light.accent.button`) | white | 22px | 44px |
| Login, hover | [button-login-hover.png](components/crops/button-login-hover.png) | same, the control is disabled so hover does not repaint | white | 22px | 44px |
| Explore Log in | [button-explore-login-default.png](components/crops/button-explore-login-default.png) | `rgb(74, 93, 249)` | white | 8px | 32px |
| Profile-gate Sign up | [button-dialog-signup-default.png](components/crops/button-dialog-signup-default.png) | `rgb(74, 93, 249)` | white | 12px | 42px |
| Log in with Facebook | [button-facebook-default.png](components/crops/button-facebook-default.png) | `rgb(243, 244, 245)` | `#111112` | 22px | 44px |
| Password-reset Continue | [password-reset-light-default.png](screenshots/password-reset-light-default.png) | saturated blue, enabled because the field is empty and the control is still the primary | white | pill | 44px |

The disabled login pill looks washed in the crop because the control is `cursor: not-allowed` until a username is entered. That wash was not entered as a token. The declared disabled wash is `--disabled-button-background` `rgba(0, 149, 246, 0.3)`, `light.component.button.primary.disabled`.

## Link

| State | Crop | Colour |
|---|---|---|
| Forgot password | [link-forgot-default.png](components/crops/link-forgot-default.png) | `#111112` on the login wall (the label is black, not the accent) |
| Create new account | [link-create-default.png](components/crops/link-create-default.png) | `rgb(65, 80, 247)`, 22px outline pill |
| Help topic | [help-light-default.png](screenshots/help-light-default.png) | `#0095f6`, `light.accent.default` |
| about.instagram.com TRY IT NOW | [link-about-cta-default.png](components/crops/link-about-cta-default.png) | black label, spectrum gradient border, 90px radius on hover |

## Text field

| State | Crop | Notes |
|---|---|---|
| Username, rest | [field-username-default.png](components/crops/field-username-default.png) | 38px field inside a rounded wrapper. Placeholder `#65676b`, `light.text.muted` |
| Username, focus | [field-username-focus.png](components/crops/field-username-focus.png) | Focus ring sits on the wrapper, a 1px blue border. The input itself stays transparent |
| Help search | [field-help-search-default.png](components/crops/field-help-search-default.png) | `#fafafa` fill, 16px radius, 72px tall |
| Birthday month | [select-month-default.png](components/crops/select-month-default.png) | 16px radius, 60px tall. The list was not opened |

No field was filled. The placeholder strings are the product's own.

## Dialog

The public profile `/instagram/` mounts a signup dialog over a dimmed grid. White surface, 32px radius, a blue Sign up pill and a Log in link. Crop: [dialog-signup-gate.png](components/crops/dialog-signup-gate.png). Screenshot: [instagram-light-default.png](screenshots/instagram-light-default.png).

## Logo

The glyph on the login wall is [logo-mark.png](components/crops/logo-mark.png). It is the product's artwork. Do not copy it into something that ships.

## Gaps

- No text area, checkbox, radio, switch, tabs, tooltip, toast, or avatar was mounted signed out.
- The about.instagram.com hamburger was not opened.
- Select lists were not opened.
- Pressed, loading and error were not provoked, because a press submits.
- The logged-in app shell, feed, stories, reels and DMs were not entered.
