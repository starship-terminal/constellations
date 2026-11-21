# Kickstarter components

Public signed-out components, measured in headed Chrome on 2026-11-18. Values are computed styles. Colours name the KDS token when the resolved value matches. Crops are in [components/crops/](components/crops).

Nothing was signed into, pledged, or submitted. Continue, Next, Back this project, Save, and Sign in with Apple were measured and never activated.

## Site chrome

### Wordmark

Green KICKSTARTER wordmark, 240 x 27. Fill is `#05CE78` (`light.color.brand`). [logo-default](components/crops/logo-default.png).

### Log in

Text button, 46 x 26, transparent fill, `#282828` text. Hover shifts the text to `#037362`. [nav-login-default](components/crops/nav-login-default.png), [nav-login-hover](components/crops/nav-login-hover.png).

### For creators

Outlined header link, 119 x 48, 1px `#c9c9c9` border (`light.color.border.bold`), 4px radius (`core.radius.small`), `#171717` text. [nav-creators-default](components/crops/nav-creators-default.png).

### Category link

Horizontal nav item, 65 x 60, black text. Hover opens the category panel (see [home-light-category-menu](screenshots/home-light-category-menu.png)). [nav-category-default](components/crops/nav-category-default.png).

### Search field

White field, 636 x 48 on desktop, 318 x 48 on phone, 1px `#e0e0e0` border (`light.color.border.subtle`), placeholder `#636363` (`light.color.text.placeholder`). Typed into and cleared. [search-default](components/crops/search-default.png), [search-focused](components/crops/search-focused.png).

## Home

### Hero heading

"Bring a creative project to life." 1246 x 42, `#282828`, Inter. [hero-h1-default](components/crops/hero-h1-default.png).

### Banner button

White pill on the dark editorial banner. Rest `#ffffff`, hover `#f2f2f2` (`light.color.background.inverse-hover`), pressed `#e0e0e0` (`light.color.background.inverse-pressed`). [banner-cta-default](components/crops/banner-cta-default.png), [banner-cta-hover](components/crops/banner-cta-hover.png), [banner-cta-pressed](components/crops/banner-cta-pressed.png).

### Project card

Media card on the home rail, 582 x 327. Green funding rule under the image. [project-card-default](components/crops/project-card-default.png).

### Save

16 x 19 bookmark icon button. Measured, never activated. Saving requires an account. [save-btn-default](components/crops/save-btn-default.png).

## Discover

### Show more

Filter expander, 82 x 20, `#4d4d4d` text (`light.color.text.secondary`), hover `#171717`. [filter-show-more-default](components/crops/filter-show-more-default.png).

### Discover card

Result title link, 208 x 73. [discover-card-default](components/crops/discover-card-default.png).

### Filter toggle

48 x 48 icon button. [filter-toggle-default](components/crops/filter-toggle-default.png).

## Project

### Back this project

Primary pledge button, 391 x 46. Rest `#028858`, hover and pressed `#015738`, white text. Not followed. Checkout is gated. [pledge-btn-default](components/crops/pledge-btn-default.png), [pledge-btn-hover](components/crops/pledge-btn-hover.png).

### Campaign tab

Section tab, 80 x 67. Hover text `#009e74`. [tab-campaign-default](components/crops/tab-campaign-default.png), [tab-campaign-hover](components/crops/tab-campaign-hover.png).

### Funding meter

386 x 9 green bar. [progress-default](components/crops/progress-default.png).

### Creator avatar

40 x 40 circle. [creator-avatar-default](components/crops/creator-avatar-default.png).

## Auth boundary

The `/login` card. Continue was never pressed. A Cloudflare Turnstile widget sits in the card and was not solved.

### Heading

"Log in or sign up", 310 x 32, `#171717`. [login-h1-default](components/crops/login-h1-default.png).

### Email field

310 x 48, placeholder `name@email.com`. Typed `name@example.com` and cleared. [login-email-default](components/crops/login-email-default.png), [login-email-filled](components/crops/login-email-filled.png).

### Continue

310 x 48, disabled fill `#b3b3b3` (`light.color.background.action-disabled`) until the email and the human check are valid. Never pressed. [login-continue-default](components/crops/login-continue-default.png).

### Sign in with Apple

310 x 48, fill `#171717` (`light.color.background.action`), hover `#000000`, pressed `#2c2c2c`. Never followed. [login-apple-default](components/crops/login-apple-default.png), [login-apple-hover](components/crops/login-apple-hover.png), [login-apple-pressed](components/crops/login-apple-pressed.png).

### Remember checkbox

13 x 13, checked by default on this visit. [login-checkbox-default](components/crops/login-checkbox-default.png).

### Recovery link

Underlined text link. Not followed. [login-link-default](components/crops/login-link-default.png).

## Start a project

`/start` is public through the category step. Next was never pressed.

### Category select

290 x 48. [start-select-default](components/crops/start-select-default.png).

### Next

230 x 41, disabled-looking grey `#464646` until a category is chosen, hover `#000000`. Never pressed. [start-next-default](components/crops/start-next-default.png).

## Mobile

390-wide home. Log in, search, and the menu glyph. [m-login-default](components/crops/m-login-default.png), [m-search-default](components/crops/m-search-default.png), [m-menu-default](components/crops/m-menu-default.png).

## Shared values

| Role | Token | Value |
|---|---|---|
| Brand green | `light.color.brand` | `#05ce78` |
| Page | `light.color.background.surface-primary` | `#ffffff` |
| Surface | `light.color.background.surface-secondary` | `#fafafa` |
| Text | `light.color.text.primary` | `#171717` |
| Muted | `light.color.text.secondary` | `#4d4d4d` |
| Action fill | `light.color.background.action` | `#171717` |
| Action hover | `light.color.background.action-hover` | `#000000` |
| Action pressed | `light.color.background.action-pressed` | `#2c2c2c` |
| Pledge rest | measured | `#028858` |
| Pledge hover | measured | `#015738` |
| Border | `light.color.border.subtle` | `#e0e0e0` |
| Focus border | `light.color.border.focus` | `#afaff9` |
| Radius small | `core.radius.small` | `4px` |
| Radius medium | `core.radius.medium` | `8px` |
| Radius large | `core.radius.large` | `16px` |

## Signed-in

Not captured on the 2026-11-21 public pass. The login dialog is the wall. See [login-light-default.png](screenshots/login-light-default.png) and [site-tree.md](site-tree.md).

## Gaps

- Text area, radio, switch, tooltip, dialog, toast, table, and list row do not appear on the signed-out surfaces that were captured. Dialog and toast rules exist in the atomic sheet and were not painted.
- Reward tiers sit below the fold on the project page. The selector matched a zero-size node, so no reward crop was kept.
- Disabled, loading, and error states of a submitted form were not captured. Continue stays disabled until Turnstile passes, which was not solved.
- Save, pledge, remind, share, and message open account or checkout flows. They were measured at rest and never activated.
