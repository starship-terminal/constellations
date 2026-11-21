# LinkedIn components

Public guest pages, measured on 2026-11-21. Each value is a computed style. A state that did not resolve is listed under Gaps.

## button-primary

Page: https://www.linkedin.com/. Selector: `a.btn-primary`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgb(10, 102, 194) | rgb(255, 255, 255) | 16px | 24px | [default](components/crops/button-primary-default.png) |
| hover | rgb(0, 65, 130) | rgb(255, 255, 255) | 16px | 24px | [hover](components/crops/button-primary-hover.png) |
| focus-visible | rgb(10, 102, 194) | rgb(255, 255, 255) | 16px | 24px | [focus-visible](components/crops/button-primary-focus-visible.png) |
| active | rgb(0, 65, 130) | rgba(255, 255, 255, 0.6) | 16px | 24px | [active](components/crops/button-primary-active.png) |

## button-secondary

Page: https://www.linkedin.com/. Selector: `a.btn-secondary-emphasis`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(0, 0, 0, 0) | rgb(10, 102, 194) | 16px | 24px | [default](components/crops/button-secondary-default.png) |
| hover | rgba(112, 181, 249, 0.1) | rgb(0, 65, 130) | 16px | 24px | [hover](components/crops/button-secondary-hover.png) |
| focus-visible | rgba(0, 0, 0, 0) | rgb(10, 102, 194) | 16px | 24px | [focus-visible](components/crops/button-secondary-focus-visible.png) |

## button-email

Page: https://www.linkedin.com/. Selector: `a.sign-in-form__sign-in-cta`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0.75) | 16px | 24px | [default](components/crops/button-email-default.png) |
| hover | rgba(0, 0, 0, 0.04) | rgba(0, 0, 0, 0.9) | 16px | 24px | [hover](components/crops/button-email-hover.png) |

## link

Page: https://www.linkedin.com/. Selector: `a[href*="/legal/user-agreement"]`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|

## heading

Page: https://www.linkedin.com/. Selector: `h1`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0.9) | 48px | 0px | [default](components/crops/heading-default.png) |

## chip

Page: https://www.linkedin.com/. Selector: `a[href*="/top-content/career"]`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0.75) | 16px | 24px | [default](components/crops/chip-default.png) |
| hover | rgba(0, 0, 0, 0.04) | rgba(0, 0, 0, 0.9) | 16px | 24px | [hover](components/crops/chip-hover.png) |

## text-field

Page: https://www.linkedin.com/login/. Selector: `input[type="email"]`.
This control sits on a login wall. It was measured and not submitted.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(255, 255, 255, 0) | rgba(0, 0, 0, 0.9) | 16px | 4px | [default](components/crops/text-field-default.png) |

## checkbox

Page: https://www.linkedin.com/login/. Selector: `input[type="checkbox"]`.
This control sits on a login wall. It was measured and not submitted.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|

## button-signin

Page: https://www.linkedin.com/login/. Selector: `visible element`.
This control sits on a login wall. It was measured and not submitted.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0.9) | 14px | 0px | [default](components/crops/button-signin-default.png) |

## card

Page: https://www.linkedin.com/games. Selector: `a[href*="/games/zip"]`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgb(255, 255, 255) | rgb(10, 102, 194) | 16px | 8px | [default](components/crops/card-default.png) |
| hover | rgb(255, 255, 255) | rgb(10, 102, 194) | 16px | 8px | [hover](components/crops/card-hover.png) |

## search

Page: https://www.linkedin.com/learning/. Selector: `input[placeholder*="Search skills"]`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0.9) | 16px | 0px | [default](components/crops/search-default.png) |
| focus | rgba(0, 0, 0, 0) | rgba(0, 0, 0, 0.9) | 16px | 0px | [focus](components/crops/search-focus.png) |

## tab

Page: https://www.linkedin.com/learning/. Selector: `[role="tab"]`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|

## help-search

Page: https://www.linkedin.com/help/linkedin. Selector: `input[name="q"]`.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|

## text-field-password

Page: https://www.linkedin.com/login/. Selector: `input[type="password"]`.
This control sits on a login wall. It was measured and not submitted.

| State | Background | Color | Size | Radius | Crop |
|---|---|---|---|---|---|
| default | rgba(255, 255, 255, 0) | rgba(0, 0, 0, 0.9) | 16px | 4px | [default](components/crops/text-field-password-default.png) |

## Gaps

- link default: selector missed
- link hover: selector missed
- checkbox default: selector missed
- tab default: selector missed
- help-search default: Screenshot dimension mismatch: PNG 1168x112, expected 1170x112
- help-search focus: Screenshot dimension mismatch: PNG 1168x112, expected 1170x112

- Text area, select, radio, switch, tooltip, toast, table, avatar, and badge were not present as measurable public controls on the captured pages.
- Disabled, loading, and error states were not shown without submitting a form.
- The jobs listing opened a sign-in dialog on its own. That dialog was not dismissed by submitting it. The listing underneath is in the screenshot.
- Dark theme is declared in the guest CSS and was not painted.
