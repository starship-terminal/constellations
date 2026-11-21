# Components

Public marketing controls. The November 2026 walk is [site-tree.md](site-tree.md). Crops were not cut. The screenshots that show each control are linked.

| Component | State | Where |
|---|---|---|
| Wordmark | default | [home-light-1440](screenshots/home-light-1440.png) |
| Nav menu | closed | Same shot. Product, Solutions, and Resources are buttons |
| Pricing link | default | Same shot. Madefor-Display 16px, black |
| Log In | default | Same shot. 1px black border, radius 42px |
| Start for free | default | Same shot. Fill `#166aea`, white type, radius 42px, height 40px |
| Hero heading | default | Same shot. wix-madefor-display-v2 82.5px, weight 400, black |
| Get Started | default | Same shot. Black pill, radius 50px, white 20px label |
| Email field | empty, focused | [login-empty-light-1440](screenshots/login-empty-light-1440.png). Value length 0. Wrapper radius 6px |
| Continue with Email | default | Same shot. Fill `#2f5dff`. Not clicked |
| Continue with Google | default | Same shot. White fill, 1px black border. Not clicked |
| Signup email | empty | [signup-empty-light-1440](screenshots/signup-empty-light-1440.png). Value length 0 |
| Phone header | default | [home-light-390](screenshots/home-light-390.png) |

Hover, pressed, loading, and error were not forced. No form was submitted.

Measured on signed-out pages on 2026-11-18. No component crop exists: the preview browser returned "The browser is not producing screenshot frames" on both snapshot attempts.

| Component | Where | What was read |
|---|---|---|
| Button | [wix.com](https://www.wix.com/) header, "Start for free" | Fill `#166aea`, label `#ffffff`, Madefor-Display 16px, padding 8px 30px, radius 42px, height 40px |
| Button | Homepage "Get Started" | Fill `#000000`, label `#ffffff` in madefor-text-mediumbold 20px, radius 50px, height 54px |
| Button | [Plans](https://www.wix.com/plans) "Start for Free" | Fill `#101585`, label `#ffffff` 20px, radius 99px, height 52px |
| Button | Plans "Compare Plan Features" | Transparent fill, 1px solid `#101585`, radius 99px, height 54px, padding 0 34px |
| Button | [Sign-in](https://users.wix.com/signin) "Continue with Email" | Fill `#2f5dff`, label `#ffffff`, Madefor 14px weight 530, padding 9px 30px, radius 6px, height 43px |
| Button | Sign-in social row | White fill, 1px solid `#000000`, label `#000624` Madefor 14px weight 500, radius 6px, height 43px |
| Link | Header "Log In" | `#000000`, 16px Madefor-Display, underline |
| Link | Homepage body | 22 links computed `#1a6aff` |
| Link | Sign-in "Sign Up" | `#2f5dff`, 14px, weight 500 |
| Text field | Homepage domain search | White, radius 999px, height 65px, 22px wix-madefor-text-v2, shadow `rgba(133, 154, 255, 0.4) 0px 30px 250px 20px` |
| Text field | Sign-in email | White, 1px solid `#868aa5`, radius 6px, height 52px (50px at 390), Madefor 18px, colour `#000624` |
| Menu | Header Product | White panel 1440 by 609px under a 72px bar. Scrim `rgba(0, 0, 0, 0.5)`. Eyebrow 14px `#5e5e5e` |
| Badge | Plans "RECOMMENDED" | madefor-text-bold 12px `#101585`, no fill |
| Focus | Header Product button | `box-shadow: 0 0 0 1px #000, 0 0 0 3px #000` |
| Focus | Sign-in primary button | `outline: 2px solid #1b73e8`, offset 2px |

## Gaps

- Hover and pressed: dispatching mouseenter did not change the computed fill of "Start for free". Not captured.
- Disabled, loading, error: no control on these pages was in those states. The disabled token `--wst-button-color-fill-primary-disabled` resolved to `rgb(194, 194, 194)`, with no element using it.
- Text area, select, checkbox, radio, switch, tabs, tooltip, dialog, toast, list row, table, avatar: not present on the signed-out pages that were opened.
- Icon button: the header logo and the hamburger are links and buttons, and their icon paths were not extracted.
- Validation: the email form was not submitted. No error message was shown.
- Dark theme: `prefers-color-scheme: dark` left the homepage light. No dark component was captured.
- Crops: no screenshot frames, so no crop.
