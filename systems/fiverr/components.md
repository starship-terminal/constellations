# Components

The login wall is the only page with a screenshot. Homepage controls were read as DOM text on one load and were not measured. States other than the resting login page were not captured.

| Component | Status | Where |
|---|---|---|
| Button | observed | Join, search icon, Continue with Google, Continue with email/username, Apple, Facebook on [login-light-default.png](screenshots/login-light-default.png). Hover, focus, pressed, disabled, loading: not captured. |
| Icon button | observed | Search icon on the login header. States beyond default: not captured. |
| Link | observed | Join here, Terms of Service, Privacy Policy, category labels. Destinations of the legal links were not followed. |
| Text field | observed | Header search, placeholder "What service are you looking for today?". Not typed into. Focus, error, disabled: not captured. |
| Text area | not present | Not on the painted login page. |
| Select | not captured | EN and currency controls were seen as buttons. Their menus were not opened. |
| Checkbox | not present | Not on the painted login page. |
| Radio | not present | Not on the painted login page. |
| Switch | not present | Not on the painted login page. |
| Tabs | not captured | Quick search and Trending searches were buttons on the homepage. Not opened after the first paint. |
| Menu | not captured | Connect to your AI and EN show a chevron. Neither menu was opened. |
| Tooltip | not present | None observed. |
| Dialog | not captured | No dialog was opened. The human-check is a full page, not a dialog, and is not in the package. |
| Toast | not present | None observed. |
| Card | observed | Sign-in card and the maroon left panel on the login page. |
| List row | not captured | Homepage search suggestions were visible as text. Their rows were not measured. |
| Table | not present | Not on the painted pages. |
| Avatar | not present | No account avatar. signed_in is false. |
| Badge | not present | None observed on the login page. |

## Gaps

- No crops. Element screenshots were not taken before the human-check.
- No hover, focus-visible, pressed, selected, disabled, loading, or error state.
- Signed-in components were not reached.
