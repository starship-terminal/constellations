# Skillshare components

Public signed-out surface, measured 2026-11-21. Crops are element screenshots. Values are token names where a token exists.

| Component | States | Where |
|---|---|---|
| Button (Sign Up, login Sign In) | default, hover, focus-visible, pressed | [btn-signup-default](components/crops/btn-signup-default.png), [btn-signup-hover](components/crops/btn-signup-hover.png). Fill `core.color.green` `#55da9b`, hover `core.color.green-hover` `#50cf93`, text `core.color.ink`, radius 4px, height 40px, weight 700. Focus ring `light.focus` `#5620c1` 1px auto. Pressed via CDP reads the same as hover. |
| Social button | default | [btn-google-default](components/crops/btn-google-default.png). White fill, 1px `core.color.line-strong` `#394649`, 4px radius, 40px on home, 55px on `/en/login`. Not clicked. |
| Link | default | [btn-email-default](components/crops/btn-email-default.png), [link-terms-default](components/crops/link-terms-default.png). Continue with email and Sign up are `core.color.link` `#5620c1`, weight 700. |
| Text field | default, empty | [field-email-default](components/crops/field-email-default.png). Login email field. Not typed. White, 1px `core.color.line`, 4px radius, 40px, 15px regular. |
| Search | default, focus, typed | [search](screenshots/home-light-search-focus.png), [typed](screenshots/home-light-search-typed.png). Combobox, 500x40 on desktop, 1px `core.color.line`, 4px radius. Typing `watercolor` opens a public search link. Not an account form. |
| Menu | open | [home-light-menu](screenshots/home-light-menu.png), [mobile-home-light-menu](screenshots/mobile-home-light-menu.png). Header Browse and the phone drawer. |
| Checkbox | default, unchecked | Login "Keep me signed in". Not checked. Crop not cut. Visible in [login-light-default](screenshots/login-light-default.png). |
| Card | default | Class cards on search and home. [search-light-default](screenshots/search-light-default.png). |
| Badge | default | Staff Pick and New on search cards. Observed in the search screenshot. Values not separately measured. |
| Logo | default | [logo-default](components/crops/logo-default.png). |

## Gaps

| Item | Status |
|---|---|
| Icon button | The phone hamburger is an SVG with title Drawer. Captured open in the mobile menu shot. No separate crop. |
| Text area, select, radio, switch, tabs, tooltip, toast, table, avatar | Not present on the captured public pages. |
| Dialog | The about video is a YouTube embed over a scrim. [about-light-video](screenshots/about-light-video.png). No product dialog with actions was opened. |
| Disabled, loading, error | Not present. No form was submitted, so no validation error. |
| Class page player, lesson list, reviews | Class URLs return Cloudflare "Just a moment..." in this client. Not captured. |
| Dark theme | Not present. `color-scheme` is `normal`. No theme toggle. |
