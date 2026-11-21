# Components

Public controls on doctronic.ai, 2026-11-21. Values are token names. Crops are in [components/crops/](components/crops/).

## Button

Log in is a quiet pill. Sign up is the solid pill. Start chat and Log in with email are the accent pill.

| State | Crop | Fill | Text | Radius | Height |
|---|---|---|---|---|---|
| Log in, default | [button-login-default.png](components/crops/button-login-default.png) | transparent wrapper; paper shows through | `light.text` | 32px | 35px |
| Sign up, default | [button-signup-default.png](components/crops/button-signup-default.png) | `light.solid` | `light.solidText` | 32px | 35px |
| Start chat, default | [button-start-chat-default.png](components/crops/button-start-chat-default.png) | `light.accent` | `light.onAccent` | 52px | 44px |
| Log in with email, default | [button-login-email-default.png](components/crops/button-login-email-default.png) | `light.accent` | `light.onAccent` | 52px | 44px |
| Google, default | [button-google-default.png](components/crops/button-google-default.png) | `light.page` | `light.text` | 40px | 44px |

Hover, focus, and pressed crops exist for Log in and Log in with email. The wrapper's computed background stays transparent in those states. The declared hover and pressed accents are `light.accentHover` and `light.accentPressed`.

## Icon button

| Control | Crop | Size |
|---|---|---|
| Open sidebar | [icon-button-sidebar-default.png](components/crops/icon-button-sidebar-default.png) | 40px, radius 100px |
| Send message | [button-send-default.png](components/crops/button-send-default.png) | 32px circle, accent fill |

## Text field

The home composer and the chat composer are textareas. They were left empty.

| Control | Crop | Notes |
|---|---|---|
| Hero input | [field-hero-default.png](components/crops/field-hero-default.png) | Geist 14px. Placeholder: Describe symptom or ask any health questions... |
| Chat input | [field-chat-default.png](components/crops/field-chat-default.png) | Geist 16px. Not submitted. |

## Chip and badge

| Control | Crop | Fill |
|---|---|---|
| Anonymous | [chip-anonymous-default.png](components/crops/chip-anonymous-default.png) | white chip, 32px, radius 34px. Opens the anonymous-info dialog. |
| Suggestion | [chip-suggestion-default.png](components/crops/chip-suggestion-default.png) | `light.sunken` (`#f5f5f0`), radius 8px |

## Dialog

Login, signup, and anonymous info. Screenshots: [home-light-login.png](screenshots/home-light-login.png), [home-light-signup.png](screenshots/home-light-signup.png), [home-light-anonymous.png](screenshots/home-light-anonymous.png).

The login dialog title is "Access Your Private AI Doctor". The email step asks for an email and offers Get Login Code. That button was not clicked.

## Menu

Marketing sidebar: [home-light-sidebar.png](screenshots/home-light-sidebar.png). Phone: [mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png). Rows and destinations are in [site-tree.md](site-tree.md).

## Heading

Home h1 is Fraunces 48px, weight 400, colour `light.text`. That matches `--text-display-48`.

## Gaps

- Select, checkbox, radio, switch, tabs, toast, and table were not on the captured pages.
- Tooltip text on the "Doctronic" headline trigger was not read.
- Disabled, loading, and error states of buttons were not shown.
- Signed-in components were not captured.
