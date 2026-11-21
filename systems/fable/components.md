# Fable components

Public site, signed out, 2026-11-21. Values are token names from [tokens.json](tokens.json). Crops are the controls that were cut; the rest are in [screenshots/](screenshots).

| Component | States | Where |
|---|---|---|
| Button (Get the app) | default, hover, focus-visible | [components/crops/cta-default.png](components/crops/cta-default.png). Fill `light.action.quiet`, label `light.action.onQuiet`, radius `core.radius.pill`, height `core.size.cta`. Focus outline `core.border.focus` in `light.focus.ring`. |
| Button (Login with email, Sign up with Email) | default | [screenshots/signin-light-default.png](screenshots/signin-light-default.png). Fill `light.action.primary`, label `light.action.onPrimary`, height `core.size.authButton`. |
| Button (Read or listen free today) | default | [screenshots/book-light-default.png](screenshots/book-light-default.png). Outline pill, border `light.border.strong`. |
| Icon button (cart, person, close) | default | Header and dialogs. Close is a 24px circle. |
| Link (nav, footer, legal) | default | Nav is Inter 16/24. Dialog legal links use `light.text.link`. |
| Text field | empty | Signup dialog and signin wall. Height `core.size.field`. Not filled. |
| Search field | empty | Clubs "Find a club" dialog. [screenshots/clubs-light-search.png](screenshots/clubs-light-search.png). Not submitted. |
| Chip | default | Genre chips on `/clubs`. Radius `core.radius.chip`, border `light.border.default`. |
| Dialog | signup, get-app, search, discover-about | Radius `core.radius.dialog`, surface `light.background.surface`. |
| Card | book cover, club card | Cover grids on home, books, clubs. |
| Badge | spoiler | `core.color.badge` on "May contain spoilers!". |
| List row | FAQ accordion | Book, club, and genre pages. |
| Avatar | club moderator | Small circle on club cards. Published avatars, not an account. |

## Gaps

Text area, select, checkbox (the signup terms box is visible and was not toggled), radio, switch, tabs, menu (Want to read has a chevron; the menu was not opened), tooltip, toast, and table are not present as measured components on the public pages. Disabled, loading, error, and pressed were not held. Dark theme is not shipped on the public site.
