# Patterns

Public pages only. No screenshot files: the preview browser did not paint
frames. Layout numbers below are computed boxes at an inner width of 1169px.

## Marketing shell

`https://scale.com/` and `https://scale.com/demo` share one header. It is
fixed, 88px tall, with a white inner bar (`--nav-background: white`). Left:
wordmark. Center: Products, Solutions, Research, Resources. Right: outline
Log In, black Get Started, 12px apart. The phone menu button exists and was
`display: none` at this width, so the 390 layout was not captured.

The home page is a long scroll (document height 9790px). The first display
line is white on the dark hero. Later display lines are black, sand, and
pine as the page rotates words. The footer is black, with 160px of padding
above the link columns and 24px below.

## Demo form

`https://scale.com/demo`. Heading "Let's Scale Together" at 40px, a grey
lede, then a 576px grid with a 16px column gap. Five text fields and three
selects, then a black Submit. A note under the form points at the privacy
policy. This is a sales booking form, not an account signup. Nothing was
typed or submitted.

## Signed-out login

`https://dashboard.scale.com/login`. White page, Inter, a 352px column.
Heading "Log in to your account", two social pills (Google, GitHub), an
"or" divider, email, password, a forgot-password link, and a black pill
submit. Container padding is 16px. Google and GitHub are company SSO, and
the form asks for a password, so the account was not created and no
credential was typed.

## Not captured

| Pattern | Why |
|---|---|
| App shell after login | Stopped at the signed-out form |
| Validation error | Would require submitting the demo or login form |
| Empty, loading, error | Not shown on these public pages |
| Destructive confirmation | Not on these pages |
| Search and filtering | Not on these pages |
| Data table | Not on these pages |
| Onboarding | Behind login, and signup is not email-only |
| Phone width | Viewport stayed at 1169px |
| Dark theme | The page advertised light only |
