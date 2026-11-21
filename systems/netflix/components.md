# Components

Public Netflix marketing and help surfaces, measured on 2026-11-21. Crops were not cut. Each row names the screenshot that shows the control. Values are token names from [tokens.json](tokens.json).

| Component | States seen | Where |
|---|---|---|
| Button | Default red fill, white label, 4px radius. Hover darkens to `#c11119`. Focus draws a 2px white outline. Pressed, disabled, and loading were not captured. | [home-dark-default](screenshots/home-dark-default.png), Get Started and Sign In |
| Icon button | Close on the title dialog and the cookie dialog. Play, unmute, expand, and subtitles on the title page. Values not read per icon. | [home-dark-title-dialog](screenshots/home-dark-title-dialog.png), [title-dark-default](screenshots/title-dark-default.png) |
| Link | Footer links are 14px, underlined, white at 70% opacity. Help links are black at 70% opacity. | [home-dark-full](screenshots/home-dark-full.png), [help-dark-default](screenshots/help-dark-default.png) |
| Text field | Email shell is 56px, 4px radius, 1px grey border, translucent `#161616` fill. Login field matches. Not typed. Error state not captured. | [home-dark-email-focus](screenshots/home-dark-email-focus.png), [login-wall-dark-default](screenshots/login-wall-dark-default.png) |
| Text area | Not present on the captured public pages. | |
| Select | Language select in the header and footer. Native menu not captured in headless Chromium. | [home-dark-default](screenshots/home-dark-default.png) |
| Checkbox | Only inside the cookie vendor list, not opened. | |
| Radio | Not present. | |
| Switch | Not present. | |
| Tabs | Cookie preference categories. Title page in-page nav (Trailers, Episodes, More to watch, Plans). | [home-dark-cookie-dialog](screenshots/home-dark-cookie-dialog.png), [title-dark-default](screenshots/title-dark-default.png) |
| Menu | Language select only. No app menu. | |
| Tooltip | Not present. | |
| Dialog | Title preview dialog, 8px radius, `#161616`, shadow `0 4px 8px` black at 80%, scrim black at 70%. Cookie preference dialog is a white OneTrust panel. | [home-dark-title-dialog](screenshots/home-dark-title-dialog.png), [home-dark-cookie-dialog](screenshots/home-dark-cookie-dialog.png) |
| Toast | Not present. | |
| Card | Trending title buttons are 180 by 252 px, `#232323`, 8px radius. Reason cards sit on the homepage. | [home-dark-default](screenshots/home-dark-default.png) |
| List row | FAQ rows are `#2d2d2d`, 24px type, 24px padding. | [home-dark-faq-open](screenshots/home-dark-faq-open.png) |
| Table | Not present on the captured pages. Plan comparison was not opened (signup Next was not clicked). | |
| Avatar | Not present signed out. | |
| Badge | Title dialog shows year and rating chips. Values not read. | [home-dark-title-dialog](screenshots/home-dark-title-dialog.png) |

## Gaps

- Signed-in browse, profiles, player, search results, and account settings are behind the login wall.
- Pressed, disabled, loading, and validation-error states were not produced. No form was submitted.
- Hover and focus were read on Get Started. They were not screenshotted as separate files.
- Component crops were not cut.
- Icons were not extracted ([docs/RIGHTS.md](../../docs/RIGHTS.md)).
