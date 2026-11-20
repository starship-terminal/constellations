# Components

Public signed-out controls on onesoil.ai, measured 2026-11-19. Crops are in [components/crops/](components/crops/). Values name tokens in [tokens.json](tokens.json).

## Button

Primary action is a 48px pill, radius `{radius.pill}`, padding 12px 16px, gap 8px, type `{typography.button}`.

| State | Fill | Label | Crop |
|---|---|---|---|
| Primary default | `{action.primary.background}` #27AE60 | `{action.primary.text}` | [button-primary-default.png](components/crops/button-primary-default.png) |
| Primary hover | same green at 0.9 alpha (not tokenised) | white | [button-primary-hover.png](components/crops/button-primary-hover.png) |
| Secondary default | `{action.secondary.background}` #151515 | white | [button-secondary-default.png](components/crops/button-secondary-default.png) |
| Submit | #27AE60, height 40px, padding 12px 24px | white | [button-submit-default.png](components/crops/button-submit-default.png) |

Pressed, disabled, and loading were not painted. Nothing was submitted.

Outline ghost buttons (Preview Data) use a 1px border and a transparent fill. The border colour was not a stable computed hex in the reading, so it stays a gap.

## Text field

Contact fields on `/en/contact-us` are 53px tall, radius 13px, padding 12px, type 18px Geologica, fill `{color.field}`.

| State | What changed | Crop |
|---|---|---|
| Default | fill #F6F4EF, 2px transparent border | [text-field-default.png](components/crops/text-field-default.png) |
| Focus | fill #FFFFFF, 2px solid rgba(109, 99, 81, 0.2), outline width 0 | [text-field-focus.png](components/crops/text-field-focus.png) |

The phone field is present. It was not filled. Error, disabled, and success states were not shown.

## Text area

Message field, same fill and radius, height 129px. [text-area-default.png](components/crops/text-area-default.png).

## Select

Country is a native-looking control, 53px, same fill and radius as the text field. Options were not opened.

## Navigation

The desktop bar is a 74px pill, radius 40px, white at 0.4 with an 18px backdrop blur and a 1px white/50 border. [nav-bar-default.png](components/crops/nav-bar-default.png).

Products opens a white shell, radius 40px, shadow `0 10px 15px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.1)`, over a black/20 scrim. Menu cards are 200 by 120, radius 16px, padding 24px, black at 0.05. Screenshot: [home-light-menu-open.png](screenshots/home-light-menu-open.png).

Phone width replaces the links with a 48px menu button labelled "Open menu". The open phone menu was not captured.

## Link

Footer links are 16px, weight 300, colour #6D6351, underline. Header text links are 16px, weight 400, colour #171717.

## Card

Audience tiles on the home page are 400 by 135, radius 24px, fill #151515, with a photo behind the label. They are links, not a separate card component.

## Help center

help.onesoil.ai is a different product: Noto Sans, white page, hero #30BF3C, search field white at 0.2 with radius 10px. It is not the marketing token set. Screenshot: [help-light-default.png](screenshots/help-light-default.png).

## Gaps

- Checkbox, radio, switch, tabs, tooltip, dialog, toast, table, avatar, and badge were not on the captured pages.
- No error, disabled, loading, or success state. The contact form was not submitted. It asks for a phone number, so it was not treated as email-only signup.
- Pressed state was not forced.
- App shell at app.onesoil.ai returned an empty Graphik page. No login form was measured. No account was created.
- Icon set was not lifted. Inline SVGs stay in the screenshots.
