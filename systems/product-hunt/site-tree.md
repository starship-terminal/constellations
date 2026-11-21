# Product Hunt public site tree

Mapped from https://www.producthunt.com/ on 2026-11-21, signed out, in headed Chromium at 1440×900. The painted theme stays light. `colorScheme` computed to `normal`. Sign in opens an empty OAuth wall on `/login`. Nothing was typed. No identity provider was clicked. No form was submitted. No captcha was solved. No vote, follow, comment, or share was clicked. A control that opens that wall is recorded and that branch stops.

`login-extracted` stays `not-started`.

## Shell

The public pages share one header. Desktop items with a chevron open a hover menu. MCP, Advertise, and the logo are links. The phone width (390) replaces the centre links with an "Open menu" button.

| Control | Opens | Stop? |
|---|---|---|
| Logo | `/` | |
| Search field | Search dialog, empty, no query typed | |
| Best Products | Hover menu, and `/categories` on click | |
| Launches | Hover menu, and today's leaderboard on click | |
| Community | Hover menu, and no page of its own | |
| MCP | `/mcp/install` | |
| Advertise | `/sponsor` | |
| Subscribe | `/newsletters` | |
| Sign in | `/login` OAuth wall | yes, signup wall |
| MCP banner "See more" | `/mcp/install` | |
| MCP banner dismiss | Hides the banner | local, not clicked |
| Footer category links | `/categories/<slug>` | |
| Footer "See All Categories" | `/categories` | |

## Best Products menu

Hover on Best Products. Moving away closes it. [screenshots/nav-best-products-menu.png](screenshots/nav-best-products-menu.png)

| Item | Opens |
|---|---|
| Orbit Awards | public awards page (promo row) |
| AI Workflow Automation | `/categories/ai-workflow-automation` |
| AI Dictation Apps | `/categories/ai-dictation-apps` |
| Trending Categories | `/categories` |
| Engineering & Development | `/categories/engineering-development` |
| LLMs | `/categories/llms` |
| Productivity | `/categories/productivity` |
| Marketing & Sales | `/categories/marketing-sales` |
| Design & Creative | `/categories/design-creative` |
| Social & Community | `/categories/social-community` |
| Finance | `/categories/finance` |
| AI Agents | `/categories/ai-agents` |
| Other Categories | `/categories` |
| Vibe Coding Tools | `/categories/vibe-coding` |
| AI notetakers | `/categories/ai-meeting-notetakers` |
| Code Review Tools | `/categories/code-review-tools` |
| No-code Platforms | `/categories/no-code-platforms` |
| Figma Plugins | `/categories/figma-plugins` |
| Static site generators | `/categories/static-site-generators` |

## Launches menu

[screenshots/nav-launches-menu.png](screenshots/nav-launches-menu.png)

| Item | Opens |
|---|---|
| Launch archive | `/leaderboard/daily/2026/11/21` |
| Launch Guide | `/en/collections/19793093-launch-guide` |

## Community menu

[screenshots/nav-community-menu.png](screenshots/nav-community-menu.png)

| Item | Opens |
|---|---|
| Forums | `/forums` |
| Events | `/producthunt` |
| Kitty Points Leaderboard | `/kitty-points` |
| Streaks | `/visit-streaks` |
| Newsletter | `/newsletters` |
| Stories | `/stories` |
| Changelog | `/changes` |

Discuss and Read are labels, not links.

## Search dialog

Click the header search field. Escape or the close button closes it. No query was typed. [screenshots/search-light-empty.png](screenshots/search-light-empty.png)

| Item | Opens |
|---|---|
| Popular launch tags | `/topics/<slug>` |
| View All Launch tags | topics index |
| Product category links | `/categories/<slug>` |
| View All Product categories | `/categories` |

## Homepage

`/`. Ranked list: Today, Yesterday, Last Week, Last Month. Each row links to `/products/<slug>`. Topic chips link to `/topics/<slug>`. The comment and vote squares were not clicked. [screenshots/home-light-default.png](screenshots/home-light-default.png)

## Footer

[screenshots/footer-light-default.png](screenshots/footer-light-default.png)

| Item | Opens |
|---|---|
| Category columns | `/categories/<slug>` |
| Trending products | `/products/<slug>` |
| Top reviewed | `/products/<slug>/reviews` |
| Top forum threads | `/p/<forum>/<thread>` |
| Newsletter, Apps, About | `/newsletters`, `/apps`, `/about` |
| FAQ | `https://help.producthunt.com/` |
| Terms, Privacy | `/legal` |
| Privacy Choices | `/privacy/do-not-sell` |
| Advertise | `/sponsor` |
| llms.txt | `/llms.txt` |
| MCP Server | `/mcp/install` |
| Contact | `mailto:hello@producthunt.com` |
| X, LinkedIn | external profiles |

## Phone menu

At 390, "Open menu" opens a drawer. Best Products is expanded. Launches and Community are collapsed rows. [screenshots/mobile-home-light-menu.png](screenshots/mobile-home-light-menu.png)

| Item | Opens |
|---|---|
| Close | Closes the drawer |
| Subscribe | `/newsletters` |
| Sign in | `/login` | yes, signup wall |
| Search | Search field, not submitted |
| Orbit Awards, Categories | same targets as the desktop menu |
| Launches, Community | Expand the same menus |
| MCP | `/mcp/install` |

## Pages opened

| Page | URL | Shot |
|---|---|---|
| Home | `/` | [screenshots/home-light-default.png](screenshots/home-light-default.png) |
| Product | `/products/alter-contacts-ai-client-relationships` | [screenshots/product-light-default.png](screenshots/product-light-default.png) |
| Categories | `/categories` | [screenshots/categories-light-default.png](screenshots/categories-light-default.png) |
| Topic | `/topics/artificial-intelligence` | [screenshots/topic-light-default.png](screenshots/topic-light-default.png) |
| Leaderboard | `/leaderboard/daily/2026/11/21` | [screenshots/leaderboard-light-default.png](screenshots/leaderboard-light-default.png) |
| Forums | `/forums` | [screenshots/forums-light-default.png](screenshots/forums-light-default.png) |
| Newsletters | `/newsletters` | [screenshots/newsletters-light-default.png](screenshots/newsletters-light-default.png) |
| About | `/about` | [screenshots/about-light-default.png](screenshots/about-light-default.png) |
| Apps | `/apps` | [screenshots/apps-light-default.png](screenshots/apps-light-default.png) |
| MCP | `/mcp/install` | [screenshots/mcp-light-default.png](screenshots/mcp-light-default.png) |
| Stories | `/stories` | [screenshots/stories-light-default.png](screenshots/stories-light-default.png) |
| Missing page | `/products/this-product-does-not-exist-constellations` | [screenshots/error-light-default.png](screenshots/error-light-default.png) |
| Login wall | `/login` | [screenshots/login-light-default.png](screenshots/login-light-default.png) |
| Phone home | `/` at 390 | [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png) |
| Phone product | `/products/alter-contacts-ai-client-relationships` at 390 | [screenshots/mobile-product-light-default.png](screenshots/mobile-product-light-default.png) |

`/signup` returns the same 404 card as a missing product. There is no separate signup URL. The login wall's heading is "Sign up on Product Hunt". It has six identity buttons and no email field. That is where capture stopped.

Events (`/producthunt`), Kitty Points, and Streaks are public links in the Community menu. They were not opened. Start new thread, Follow, Add to collection, Share, and Upvote stay on the signed-out side of the wall and were not clicked.
