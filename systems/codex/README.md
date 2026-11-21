# Codex public site

A token set and page reference for the public Codex marketing page at https://openai.com/codex/, OpenAI's coding-agent product page. It was read on 2026-11-22, signed out, in the T3 preview (incognito) at 1440×900 and 390×844. The look is a black header over a pale wash, OpenAI Sans at 64px for the headline, and two pills: a black Download for macOS and a quiet Try on web. Plan prices sit on the page (Plus, Pro, Business) in SGD. The developer docs link leaves openai.com and lands on https://learn.chatgpt.com/docs.

`systems/codex-desktop` already exists and is the desktop app. This package is the public site. Slug: `systems/codex`.

**Boundary:** Log in opens a menu (ChatGPT, API Platform). Both walls were photographed empty. Google, Apple, Microsoft, phone and Continue were not clicked. No email, password, code or phone was typed. Try on web, Get Plus, Get Pro and Try ChatGPT Business were not followed. The cookie banner was hidden, never accepted. `login-extracted` is `not-started`. catalog.json was not edited.

| File | What it is |
|---|---|
| [icon.png](icon.png) | 128 px PNG from openai.com/favicon.ico, scaled up from 48 px |
| [tokens.json](tokens.json) | Measured colours, type sizes, radii and motion. `dark` is the marketing page. `login` is the ChatGPT wall, a different host. |
| [DESIGN.md](DESIGN.md) | Hand-written from the measured tokens. Not generated, so the catalog was not rewritten. |
| [style-guide.html](style-guide.html) | The marketing buttons and the login card, painted from the token values |
| [site-tree.md](site-tree.md) | Which control opens which page, menu, drawer or wall |
| [login-review.json](login-review.json) | The empty walls. `login_extracted` is `not-started`. |
| [components.md](components.md) | The controls that exist on the public page |
| [patterns.md](patterns.md) | Header, hero, pricing, docs, phone, walls |
| [screenshots/](screenshots) | Homepage, products menu, pricing band, footer, docs, phone, empty login walls |
| [raw/](raw) | Playwright notes from the failed headless pass, kept so the Cloudflare stop is on record |
| [tools/](tools) | `build_tokens.py`, `build_style_guide.py`, and the kit copy |

## How the values were read

Headless Playwright was stopped by a Cloudflare "Verify you are human" wall on openai.com. Those shots were discarded. The values below were read in the T3 preview tab, which already had the page, with `getComputedStyle` on the live DOM. The cookie banner was hidden with `display:none`. It was not accepted.

| Reading | Where |
|---|---|
| Body `#000` / `#fff`, OpenAI Sans | `document.body` on https://openai.com/codex/ |
| H1 64px / 500 / `#000` | The headline, painted over the hero wash |
| Download 40px tall, 40px radius, `#000` on `#fff` | The macOS download link |
| Try on web `rgba(0,0,0,0.04)` | The quiet pill beside it |
| Log in 36px, `rgba(255,255,255,0.12)` | Header button |
| Nav link 17px, `rgba(255,255,255,0.6)` | Research |
| Radii and durations | Computed custom properties `--radius-*`, `--transition-duration-*`, `--ease-out` |
| Login card | https://chatgpt.com/auth/login, empty |

## What to distrust

The hero wash is a video. A still cannot stand in for it. Prices are SGD because the preview resolved that currency. They are not a token. The favicon was scaled from 48 px to 128 px, so [icon.png](icon.png) is soft. `--color-brand-*` on `:root` is a large unused ramp. Only the roles the page paints are in [tokens.json](tokens.json). The login wall uses system UI, not OpenAI Sans. Do not mix those families.

## Fonts

OpenAI Sans and OpenAI Sans Variable Scripts, loaded by openai.com. The tokens name the family. The font files are not in this package. The login wall uses the system sans.

## Coverage

| Item | Status | File |
|---|---|---|
| Page colour, text, nav | captured | [screenshots/home-dark-default.png](screenshots/home-dark-default.png) |
| Display type | captured | same, h1 64px |
| Primary and secondary buttons | captured | same |
| Pricing cards | captured | [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png) |
| Products menu | captured | [screenshots/nav-products-dark-open.png](screenshots/nav-products-dark-open.png) |
| Footer | captured | [screenshots/footer-dark-default.png](screenshots/footer-dark-default.png) |
| Docs (inner page) | captured | [screenshots/docs-dark-default.png](screenshots/docs-dark-default.png) |
| Phone home | captured | [screenshots/mobile-home-dark-default.png](screenshots/mobile-home-dark-default.png) |
| Phone drawer | captured | [screenshots/mobile-nav-dark-open.png](screenshots/mobile-nav-dark-open.png) |
| Phone docs | captured | [screenshots/mobile-docs-dark-default.png](screenshots/mobile-docs-dark-default.png) |
| Login menu | captured | [screenshots/login-menu-dark-empty.png](screenshots/login-menu-dark-empty.png) |
| Login and signup wall | captured, empty | [screenshots/login-dark-empty.png](screenshots/login-dark-empty.png) |
| API login wall | captured, empty | [screenshots/login-api-dark-empty.png](screenshots/login-api-dark-empty.png) |
| Light theme | not present | the public page paints dark only |
| Signed-in app, hover, focus, error, empty app states | not captured | stopped at the walls. `login-extracted` is not-started |
| Checkbox, radio, switch, tabs, toast, table, avatar | not present | none on the marketing page |

## Do and don't

**Do** paint the header black and the headline black over the wash. The download button is the only solid black pill in the hero. See [screenshots/home-dark-default.png](screenshots/home-dark-default.png).

**Do** keep plan prices on the page, three cards, one accent card for Business. See [screenshots/pricing-dark-default.png](screenshots/pricing-dark-default.png).

**Don't** treat the login wall as the marketing type. It is system UI on `#000`, pills at 9999px. See [screenshots/login-dark-empty.png](screenshots/login-dark-empty.png).

**Don't** follow Try on web, Get Plus, Get Pro or an identity provider from this package. Those leave the public page.

## Rebuild

```bash
cd systems/codex && python3 tools/build_tokens.py && python3 tools/build_style_guide.py
```

DESIGN.md is hand-written. Do not run `make design-md` for this package unless catalog.json is meant to change. It was left alone.
