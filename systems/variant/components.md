# Variant components

Signed-out surfaces only, read on 2026-11-19 from `https://variant.com/`. Values are computed styles. Page shots from 2026-11-22 are in [screenshots/](screenshots/). There are no element crops.

## Homepage

### Display title

`h1.HomepageV3_title`. Variant Neue Display, 32px, weight 400, line-height 36px, letter-spacing 0.32px, colour `rgb(240, 237, 229)`. Box 360×72 at x 24, y 87, on both 1169 and 1440 viewports. The column stays 408px wide.

### Subtitle

`.HomepageV3_subtitlePrimary` and `.HomepageV3_subtitleSecondary`. Variant Neue Text, 14px, weight 400, line-height 24px, letter-spacing 0.28px, colour `rgba(240, 237, 229, 0.65)`. Primary margin `40px 0 16px`. Secondary margin `0 0 25px`.

### Suggestion chip

`button.HomepageV3_suggestionButton`. "Sign up / Sign in" and "Surprise me". Height 26px, padding `0 8px 0 7px`, gap 7px, radius 6px, border `0.5px solid rgba(255, 255, 255, 0.1)`, background `rgb(7, 7, 6)`, text `rgb(240, 237, 229)`, Variant Neue Text 11px, line-height 11px, letter-spacing 0.22px. Hover and pressed were not measured. The first chip was clicked once to open authentication, so its pressed frame was not held.

### Composer

`.HomepageInput_inputContainer`. Background `rgb(30, 30, 28)`, radius 10px, padding `8px 8px 0`, size 384×72, box-shadow `rgba(255, 255, 255, 0.1) 0px 0px 0px 0.5px`.

The contenteditable editor is Variant Neue Text 14px, line-height 22px, letter-spacing 0.28px, colour `rgba(255, 255, 255, 0.85)`. Placeholder "See endless designs for..." is the same size at `rgba(255, 255, 255, 0.4)`.

### Icon buttons

"Add image" and "Select style". 24×24, radius 6px, transparent background, colour `rgba(255, 255, 255, 0.5)`. Not opened. A hidden `input[type=file]` sits behind Add image.

### Submit

`button[aria-label=Submit]`. 27×24, radius 6px, transparent background, colour `rgb(255, 255, 255)`. Not clicked. Hover and pressed not measured.

### Widget card

`.HomepageWidgetGrid_widgetCard`. Radius 8px, overflow hidden, background transparent, no shadow. Transition `opacity 0.5s ease` with delay `0.3s`. Content is an iframe (`/homepage-widgets/...`). The inner design was not measured. Placeholders (`.HomepageWidgetGrid_placeholder`) were in the DOM with transparent backgrounds when read.

## Authentication

Opened at `https://variant.com/authentication` by the Sign up chip. Page background `rgb(0, 0, 0)`. Left padding `64px 48px`. Card max-width 520px, no fill, no radius, no shadow. Controls are 400px wide.

### Title

"Sign in or sign up". Inter, 21px, weight 500, line-height 32px, letter-spacing -0.21px, colour `rgba(255, 255, 255, 0.5)`.

### Google button

`button.page_button`. "Continue with Google". Height 40px, padding `0 14px`, radius 6px, background `rgba(255, 255, 255, 0.1)`, text `rgba(255, 255, 255, 0.85)`, Inter 13px, letter-spacing 0.13px, no border. Not clicked. That control starts Google sign-in.

### Divider

The word "or". 12px, weight 400, colour `rgba(255, 255, 255, 0.3)`.

### Email field

`input[type=email]`, placeholder "Email address". Height 40px, padding `0 16px 0.5px`, radius 6px, background `rgba(255, 255, 255, 0.03)`, text `rgba(255, 255, 255, 0.85)`, Inter 13px, border `0.5px solid rgba(255, 255, 255, 0.1)`. Click focus did not change border, outline or shadow.

### Email button

`button.page_primaryButton`. "Continue with Email". Height 40px, radius 6px, Inter 13px, letter-spacing 0.13px.

| State | What was read |
|---|---|
| Empty | Background `rgba(255, 255, 255, 0.1)`, text `rgba(255, 255, 255, 0.5)`, disabled. Hover did not change it. |
| Filled | Same background, text `rgba(255, 255, 255, 0.85)`, cursor pointer. Typed text was cleared. Not submitted. |
| Hover, filled | Background `rgba(255, 255, 255, 0.15)`. |
| Focus-visible | Outline `rgb(229, 151, 0) auto 1px`, offset 0. Same outline on the Google button. This is the user-agent ring. |
| Pressed | Not captured. A click submits. |

### Fine print

Inter 12px, line-height 20px, letter-spacing 0.12px, colour `rgba(255, 255, 255, 0.5)`. Links are weight 500, same colour, and point at `/terms-and-privacy`.

## Legal page

`https://variant.com/terms-and-privacy`. Article width 920px.

| Element | Style |
|---|---|
| h1 | Inter 21px, weight 500, line-height 32px, tracking -0.21px, colour `rgba(255, 255, 255, 0.5)` |
| h2 and h3 | Inter 13px, weight 500, line-height 20px, tracking 0.13px, colour `rgba(255, 255, 255, 0.85)` |
| p | Inter 13px, weight 400, line-height 20px, tracking 0.13px, colour `rgba(255, 255, 255, 0.85)` |
| Prose link | Same colour, underline |
| Tab | 13px, weight 500, tracking 0.13px, padding `10px 0`, height 36px, radius 0. Active text `rgba(255, 255, 255, 0.85)`. Inactive `rgba(255, 255, 255, 0.5)`. No border, no fill. |

The Privacy Policy tab was clicked. It replaces the article. No other control on the page.

## Gaps

- No element crops. Page shots are in [screenshots/](screenshots/).
- Pressed, loading and error states of the email button. Capturing them means submitting.
- Google button hover, focus was read, hover was not, click was not.
- Homepage chip hover, composer focus, Submit hover and pressed, Add image, Select style.
- Widget iframe contents.
- Signed-in shell: sidebar, chat, menus, dialogs, toasts, billing. Their CSS is in the bundle and was not on screen.
- Checkbox, radio, switch, select, textarea, table, avatar, badge, list row: not on these pages.
- A second theme: not painted.
