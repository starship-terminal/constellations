# Reddit design reference

Tokens and page notes for the public Reddit site at [reddit.com](https://www.reddit.com/). Captured 2026-11-22, signed out. Desktop screenshots are 1440 by 900 CSS pixels at device pixel ratio 2. The phone homepage is 390 by 844 CSS pixels at device pixel ratio 2.

The first paint was dark. `prefers-color-scheme: light` switched later pages to white. The homepage, the phone homepage, and r/reddit were shot after that switch. The public post, r/AskReddit, the missing-community dialog, and the login and signup walls were shot on the dark first paint. Dark custom properties from that paint are in [raw/home-tokens.json](raw/home-tokens.json). Tokens in [tokens.json](tokens.json) are the light values.

Public logged-out pages only: the homepage, one public post, two public communities, a missing-community dialog, the phone homepage, and the empty login and signup walls. No account was created. No email, username, password, phone, or code was typed. No identity provider was clicked. No vote, comment, join, or subscribe was used. No captcha was solved. `login-extracted` stays not-started.

catalog.json was left alone.

| File | What it is |
|---|---|
| [README.md](README.md) | This file. |
| [icon.png](icon.png) | The site icon, 128px, resized from the public 180px apple icon. |
| [tokens.json](tokens.json) | DTCG tokens from the light custom properties. |
| [DESIGN.md](DESIGN.md) | Hand-written from those tokens. The catalog generator was not run. |
| [style-guide.html](style-guide.html) | Renders the token roles. |
| [components.md](components.md) | Controls seen on the public pages, and the gaps. |
| [patterns.md](patterns.md) | How the logged-out pages are built, and where they stop. |
| [site-tree.md](site-tree.md) | Which header and footer controls open which pages and walls. |
| [login-review.json](login-review.json) | The empty auth walls. `login-extracted` is not-started. |
| [components/crops/](components/crops) | Empty. Element crops were not cut. |
| [screenshots/](screenshots) | Quantised page shots. |
| [raw/](raw) | Custom properties read on the homepage. |
| [tools/](tools) | `test_tokens.py`. |

<!-- brief:start -->
<!-- brief:end -->

<!-- health:start -->
<!-- health:end -->

## How the values were read

Custom properties were read with `getComputedStyle(document.documentElement)` on https://www.reddit.com/ on 2026-11-22, after `prefers-color-scheme` was set to light. The Log In button, the header, and the body were also read with `getComputedStyle`. Screenshots were quantised to 256 colours after the values were read.

## What to distrust

The wordmark is orange. The token for that role is `--color-global-orangered` (`#FF4500`). The Log In pill is `--color-brand-background` (`#D93900`). They are two oranges.

`--radius-full` computed as `624.9375rem`. The Log In pill's own `border-radius` was `999px`. The pill token uses the computed button radius.

Link blue is `#115BCA` in light and `#648EFC` in the dark paint that came first. This package's link token is the light value.

Screenshots are 256-colour PNGs at 2x. Read colours from [tokens.json](tokens.json), not from the images.

The missing-community shot still has a Mature Content dialog behind the community dialog. Escape did not close it. That shot is the empty state that loaded, with both dialogs.

## Fonts

The computed family is the system sans: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial. No font file is in this package.

## Coverage

| Item | Status |
|---|---|
| Colour, type, radius, space, sizing | Captured from custom properties and the Log In button. [tokens.json](tokens.json) |
| Light theme | Captured. Page background `#FFFFFF`. |
| Dark theme | Shot on the post, r/AskReddit, the missing-community dialog, and the empty login and signup walls. Custom properties from first paint are in [raw/home-tokens.json](raw/home-tokens.json). |
| Desktop 1440 | Homepage, post, r/AskReddit, r/reddit, missing community, login, signup. |
| Phone 390 | Homepage. [screenshots/home-light-phone.png](screenshots/home-light-phone.png) |
| Button, link, text field, checkbox | Seen empty on the auth walls. Fields were not typed. |
| Icon button | Seen: menu, overflow, upvote, downvote. Not cropped. |
| Select, radio, switch, tabs, toast, table, tooltip | Not isolated on the pages that were opened. Sort and view are menus that were not opened. |
| Menu | Header user menu and sort menus were not opened. |
| Dialog | Missing community and the Mature Content age gate. [screenshots/missing-community-dark-desktop.png](screenshots/missing-community-dark-desktop.png) |
| Card, list row, avatar, badge | Feed cards, popular-community rows, public avatars, and the ADMIN mark on r/reddit. |
| Empty state | "We couldn't find that community." |
| Form validation | Not captured. Nothing was submitted. Login stayed disabled. |
| Signed-in app | Not entered. `login-extracted` is not-started. |
| Principles and voice | Not captured. No public design-system voice page was opened. |

## Do and don't

- **Do paint Log In as an orange pill.** The fill is `#D93900`, the label is white, the radius is a pill, the height is 40px. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
- **Do keep Sign Up quiet.** It is a grey pill beside Log In. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)
- **Do use a second orange for the wordmark.** `--color-global-orangered` is `#FF4500`. It is not the button fill.
- **Do leave the login and signup cards empty.** Continue and Log In stay disabled until a field has text. [screenshots/login-dark-empty.png](screenshots/login-dark-empty.png)
- **Don't click Google, Apple, or phone.** Those are identity providers. They were not opened.
- **Don't treat the feed as a signed-in home.** The left rail is a join card. [screenshots/home-light-desktop.png](screenshots/home-light-desktop.png)

## Rebuild

```bash
python3 systems/reddit/tools/test_tokens.py
```

`make brief` and `make design-md` were not run. They rewrite catalog-backed files, and this capture leaves catalog.json alone.
