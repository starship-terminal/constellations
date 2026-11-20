# Mocha site tree

Mapped 2026-11-21 in headless Chromium, signed out. The product URL this capture opens first is `https://getmocha.com/`.

## The product host does not resolve

| Probe | Result |
|---|---|
| `https://getmocha.com/` | `net::ERR_NAME_NOT_RESOLVED`. `dig A` and `dig AAAA` return no records |
| `https://www.getmocha.com/` | same |
| `https://getmocha.com/login` | same. There is no sign-in form because the host never connects |
| `https://mocha.app/` | HTTP 301 to `https://getmocha.com/`, which then fails DNS |
| `https://getmocha.com/blog/mocha-shutdown` | the 410 page's only link. The host does not resolve, so the announcement was not opened |

This is not a login wall. No password field, code field, captcha, or OAuth button was shown, because the page never loaded.

## Product hosts that answer

These hosts resolve and return HTTP 410 with one static page. Visible text: "This app is no longer available. Mocha has shut down. Mocha apps can no longer be accessed. Read the shutdown announcement." The announcement link points at `https://getmocha.com/blog/mocha-shutdown`.

| URL | Status | What the control does |
|---|---|---|
| `https://app.mocha.app/` | 410 | the shutdown page |
| `https://login.mocha.app/` | 410 | the same page. No form |
| `https://auth.mocha.app/` | 410 | the same page |
| `https://dashboard.mocha.app/` | 410 | the same page |
| `https://studio.mocha.app/` | 410 | the same page |
| `https://build.mocha.app/` | 410 | the same page |
| `https://vidsync.mocha.app/` | 410 | the same page. Linked from the welcome doc as a sample app |

## The live designed surface

`https://docs.getmocha.com/` returns 308 to `/welcome`. It is a Mintlify docs site. `html` is `light` or `dark` from the theme preference. The index is `https://docs.getmocha.com/llms.txt` and `https://docs.getmocha.com/sitemap.xml` (35 pages).

### Header controls on `/welcome`

| Control | Opens |
|---|---|
| Logo, "Mocha home page" | `https://docs.getmocha.com/` which redirects to `/welcome` |
| Search, "Open search" (`#search-bar-entry`, also the mobile search button) | a dialog labelled "Search...". Empty until a query is typed. Escape closes it. No query was typed |
| Support | `mailto:support@getmocha.com`. Not followed |
| Go to Mocha | `https://getmocha.com/`. Does not resolve. Not followed past the failed navigation |
| Change theme preference | a menu: System, Light, Dark. Light and Dark were selected for captures, then left on the scheme the shot used |
| More actions | present in the header. The click did not open a menu in this pass |
| Ask a question | a readonly textarea (`#chat-assistant-textarea`) with a Send message button. The textarea is `pointer-events-none` until the assistant is opened. Nothing was typed and Send was not pressed |

### Sidebar groups

Each row is a link to a docs page. Community, YouTube, and Twitter leave the site and were not followed.

| Group | Link | URL |
|---|---|---|
| top | Documentation | `/welcome` |
| top | Community | `https://discord.gg/shDEGBSe2d` |
| top | YouTube | `https://www.youtube.com/@get_mocha` |
| top | Twitter | `https://x.com/get_mocha` |
| Get Started | Welcome | `/welcome` |
| Get Started | Getting Started with Mocha | `/getting-started` |
| Get Started | FAQ | `/getting-started/faq` |
| Get Started | Migrating older apps | `/getting-started/migrating` |
| Basics | Deploy your website | `/basics/hosting` |
| Basics | Analytics | `/basics/analytics` |
| Basics | Email | `/basics/email` |
| Basics | Discuss Mode | `/basics/discuss-mode` |
| Basics | Max Mode | `/basics/max-mode` |
| Basics | Direct Edit Mode | `/basics/direct-edit` |
| Basics | Using Images and Assets | `/basics/assets` |
| Basics | Version History | `/basics/versions` |
| Basics | Duplicating Apps | `/basics/duplicate` |
| Basics | Backend & APIs | `/basics/backend` |
| Basics | Authentication | `/basics/auth` |
| Basics | Databases | `/basics/databases` |
| Basics | Custom Domains | `/basics/custom-domains` |
| Basics | Custom Knowledge | `/basics/custom-knowledge` |
| Basics | Custom Login Options & Branding | `/basics/custom-login-branding` |
| Integrations | Accepting Payments | `/integrations/accepting-payments` |
| Integrations | Scraping Data | `/integrations/scraping-data` |
| Integrations | Generating Images | `/integrations/generating-images` |
| Integrations | Using Voice AI | `/integrations/using-voice-ai` |
| Account & Billing | Account & Subscriptions | `/billing/account-subscriptions` |
| Account & Billing | Billing | `/billing/billing` |
| Account & Billing | Credit and App Size Limits | `/billing/limits` |
| Guides & Tutorials | From Idea to Live Website | `/guides/idea-to-website` |
| Guides & Tutorials | Prompting Best Practices | `/guides/prompting` |
| Guides & Tutorials | Video Tutorials | `/guides/video-tutorials` |
| Guides & Tutorials | Troubleshooting Errors | `/guides/troubleshooting` |
| Guides & Tutorials | Troubleshooting Login | `/guides/troubleshooting-login` |
| Guides & Tutorials | Blank Page or Missing Images | `/guides/network-blocking` |
| Guides & Tutorials | Remove the Watermark | `/guides/remove-watermark` |
| Community | Community & News | `/community/community` |
| Community | Bugs & Feature requests | `/community/bugs-features` |

### On-page controls

| Control | Where | Opens |
|---|---|---|
| FAQ summary | `/getting-started/faq` | expands that question. One row was opened |
| Expand image | welcome and other pages with figures | enlarges the figure. Not submitted anywhere |
| On this page | right rail | jumps to a heading on the same page |
| Powered by Mintlify | footer | `https://www.mintlify.com/`. Not followed |
| GitHub, LinkedIn | footer | off-site. Not followed |
| Navigation | phone width | the sidebar sheet. Welcome is the current row |

### Signed-in surface

None. The product hosts are the 410 page. Docs stay public. No account was created and no form was submitted.
