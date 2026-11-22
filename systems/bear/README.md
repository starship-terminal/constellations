# Bear public site

Public marketing capture for Bear, the Markdown notes app at [bear.app](https://bear.app/). Mapped and photographed on 2026-11-22, signed out. Desktop is 1440×900. Phone is 390×844.

This is the public site only. Tokens were measured from the live public site on 2026-11-22, signed out, in headless Chromium. `catalog.json` was left alone, so this folder is not registered yet. `systems/bear-ios/` is a different package and was not touched. `login-extracted` stays not-started. No `DESIGN.md`: the parent generates it after a catalog entry exists.

| File | What it is |
|---|---|
| [icon.png](icon.png) | Bear's site icon, 128 px PNG, fetched from `https://bear.app/images/website-icons/apple-touch-icon.png` and padded to a square. |
| [tokens.json](tokens.json) | W3C DTCG tokens in Tokens Studio's multi-set layout: `core` and `light`. No dark set. Every colour `$value` is a hex or rgba read from computed style. Every token carries `$extensions.source`. |
| [style-guide.html](style-guide.html) | One page that renders the tokens. Light only. Bear Sans is not bundled. |
| [site-tree.md](site-tree.md) | Public site tree mapped 2026-11-22. Nav, footer, photographed pages, and where the walk stopped. |
| [login-review.json](login-review.json) | Empty community login and signup walls, and the Bear Web Apple sign-in wall. |
| [screenshots/](screenshots/) | Page shots. Git LFS. Existing photographs were kept. No page was recaptured. |
| [raw/](raw/) | Computed-style readings the tokens were built from: [elements.json](raw/elements.json). |
| [tools/](tools/) | [build_tokens.py](tools/build_tokens.py) and [build_style_guide.py](tools/build_style_guide.py). See [tools/README.md](tools/README.md). |
| [DESIGN.md](DESIGN.md) | Generated export of the tokens |

The homepage has no login. Download goes to the App Store. Pricing is an anchor on the homepage: Free, and Bear Pro at $2.99/month or $29.99/year after a 7 day trial. The community login and signup walls, and the Bear Web "Sign in with Apple" wall, were photographed empty and not submitted.

## How the values were read

Headless Chromium, signed out, 1440×900, `getComputedStyle`. Custom properties on `:root` were assigned to a probe element and read back as computed rgb, then written as hex. Feature heading colours, PRO tag fills, the offer badge, the card fill, the Subscribe button, and the focus outline were read on the elements that paint them. `prefers-color-scheme: dark` left those paints unchanged, so there is no dark set.

No email, name, password, or code was typed. No identity provider was clicked. No form was submitted. Login, signup, checkout, subscribe, and cookie accept or reject were not clicked.

## What to distrust

- Body and html backgrounds computed transparent. The page role is the nav's computed white, which matches declared `--background-color`.
- `--stroke-color` computed to `#d9d9d9` and is the border role. No homepage control painted a 1px border in that colour.
- The nav also declares `rgba(255, 255, 255, 0.8)` when backdrop-filter is supported. The measured nav background on this pass was opaque white.
- PRO tags share one class and three fills: gold, sky, and accent red. The token records each fill. The default rule is the red.
- Blog (`blog.bear.app`) paints a different system: system-ui, `#242424` on white. Those values are not in this token file. Community reuses the same accent red and the tertiary grey.
- Focus is the browser default outline, `rgb(0, 95, 204)`, 1px auto. Hover did not change the nav link or the Subscribe button.
- Screenshots are the earlier capture. Read colours from `tokens.json`, not from the images.

## Fonts

Bear Sans (`bearsans`) is the body face. Bear Sans Headline (`bearsansheadline`) is the heading face. Both are self-hosted woff2 on bear.app and are not in this package. Code uses `roboto-mono`. The style guide falls back to the system sans.

## Coverage

| Item | Status |
|---|---|
| Colour roles | Captured in [tokens.json](tokens.json). One theme. |
| Type | Captured: 16px body, 51.2px display at 1440, 41.6px display at 390, 22.4px subtitle, 40px price. |
| Radii | Captured: 8px button, 40px card, 4.8px tag, 16px ribbon. |
| Elevation | None. Computed box-shadow was none. |
| Dark theme | Not present. A dark media emulation did not change paints. |
| Login, signup, subscribe, checkout | Stopped. See [login-review.json](login-review.json) and [site-tree.md](site-tree.md). |

## Do and don't

1. **Do set text in `#444444` on white.** Body, nav, and headings share that ink. See [home-desktop.png](screenshots/home-desktop.png).
2. **Do use `#dd4c4f` for the one filled action.** Subscribe is white on that red, 8px radius. See [home-desktop.png](screenshots/home-desktop.png).
3. **Do keep feature cards on `#f3f5f7` at 40px radius.** See [home-desktop.png](screenshots/home-desktop.png).
4. **Don't invent a dark theme.** The public site did not change under a dark colour scheme.
5. **Don't style Bear Web or the community from the blog.** The blog is a separate system-ui page. See [blog.png](screenshots/blog.png).
6. **Don't submit login or Sign in with Apple.** The walls were photographed empty. See [login-wall.png](screenshots/login-wall.png) and [web-signin-wall.png](screenshots/web-signin-wall.png).

## Rebuild

```sh
cd systems/bear
python3 tools/build_tokens.py
python3 tools/build_style_guide.py
```
