# Components

Public signed-out Threads, measured on 2026-11-21. Crops were not cut. The screenshots in [screenshots/](screenshots/) are the evidence. Values are token names from [tokens.json](tokens.json).

| Component | Status | Where |
|---|---|---|
| Button | Captured | Log in, black pill, 34px, radius 10px, label 15px / 600. [home-light-default.png](screenshots/home-light-default.png). Token `light.accent`, `light.onAccent`. |
| Icon button | Observed | Post more (three dots), back arrow on a profile, close on the cookie bar. No size token. |
| Link | Captured | Topic chips and "Log in with username instead". Token `light.link`. |
| Text field | Captured | Search placeholder and the login username field (55px, radius 18px). [search-light-default.png](screenshots/search-light-default.png), [login-light-default.png](screenshots/login-light-default.png). Not typed. |
| Text area | Not present | The composer is behind the sign-up dialog. |
| Select | Not present | Appearance is a segmented control (sun, moon, Auto), not a select. |
| Checkbox | Not present | |
| Radio | Not present | |
| Switch | Observed | Sounds panel, Activity and Messages, both off. [home-light-sounds.png](screenshots/home-light-sounds.png). Not toggled. |
| Tabs | Observed | Profile tabs Threads, Replies, Media, Reposts. Clicks did not change the URL or the visible list in this pass. [profile-light-default.png](screenshots/profile-light-default.png). |
| Menu | Captured | More menu: Appearance, Sounds, Report a problem. [home-light-more-menu.png](screenshots/home-light-more-menu.png). |
| Tooltip | Not present | |
| Dialog | Captured | Join dialog, sign-up-to-post, sign-up-to-follow, phone "Thread on Threads". [home-light-join-dialog.png](screenshots/home-light-join-dialog.png), [home-light-new-thread-wall.png](screenshots/home-light-new-thread-wall.png), [profile-light-follow-wall.png](screenshots/profile-light-follow-wall.png). Instagram was not clicked. |
| Toast | Not present | |
| Card | Observed | Feed post and the right-hand "Log in or sign up" card. Radius not read. |
| List row | Observed | Feed posts. |
| Table | Not present | |
| Avatar | Observed | 36px in the feed on desktop. Size is from the layout box, not a token. |
| Badge | Token only | `--notification-badge` is declared. No badge was on the signed-out chrome. |

## Gaps

- Pressed, loading, error, and disabled states were not reached. Hover on Log in did not change its computed background.
- Focus on the login field did not paint an outline in this pass (`outline: none`). The declared focus ring is `--focus-ring-blue` and `--focus-ring-shadow-default`.
- Dialog radius and icon glyph sizes are Not captured.
- Signed-in screens (messages, activity, profile of the viewer, insights, composer) stop at a login wall. See [site-tree.md](site-tree.md).
