# Endless public site tree

Captured 2026-11-21, signed out, from [https://endless.io](https://endless.io). That host redirects to [https://endless.app/](https://endless.app/). The machine-readable copy is [raw/site-tree.json](raw/site-tree.json).

English pages only. Locale mirrors (`/es`, `/pt`, `/de`, `/fr`) and per-country radar leaves are branches, not each opened. Cookie banners were hidden. No form was submitted.

## Shell

The marketing header is on every marketing page.

| Control | Opens |
|---|---|
| Endless home, Product | [https://endless.app/](https://endless.app/) |
| Models | [https://endless.app/models](https://endless.app/models) |
| Industries (hover) | Menu: Media and news, Agencies and studios, Brands and marketing, Education |
| Industries (click) | [https://endless.app/industries](https://endless.app/industries) |
| Pricing | [https://endless.app/pricing](https://endless.app/pricing) |
| Blog | [https://endless.app/blog](https://endless.app/blog) |
| Sign in | Stop. See Auth. |
| Sign up for free | Stop. Same sign-in surface. Not clicked through. |
| Menu (390 wide) | Bottom sheet with the same links, Industries expanded |

Footer theme button cycles three labels: "Theme: system. Switch to light", "Theme: light. Switch to dark", "Theme: dark. Switch to system". Light paints a `#fcfcfc` page. Dark paints a black page.

Footer also links Product, model groups, Industries, Company (About, Blog, Comparisons, Brand kit, Contact), Legal, Tools, language mirrors, and country radar indexes. Cookie settings was not clicked.

## Pages opened

| Path | What it is |
|---|---|
| `/` | Home. Composer, model chip, prompt chips, product demo. |
| `/pricing` | Monthly / Annual toggle, plan cards, credit estimator. Get started is a sign-up stop. |
| `/models` | Model index with Chat, Image, Video, Audio, 3D filters and a search field. |
| `/model-index` | Model index article. |
| `/models/chat`, `/models/image`, `/models/video`, `/models/audio`, `/models/3d` | Category indexes. |
| `/models/<slug>` | One model page. Footer and indexes link the rest. Several slugs were opened. |
| `/industries` and `/industries/media`, `/agencies`, `/brands`, `/education` | Industry landings. |
| `/blog` | Filters: All, Guides, Customer stories. Cards link posts. |
| `/compare` | Comparison index. |
| `/integrations` | Integration index. `/integrations/notion` was opened as a sample. |
| `/mcp` | MCP setup. Client links go to docs. Installer deep links are recorded without their query strings. |
| `/about`, `/contact`, `/brand` | Company pages. Contact has a form. It was not submitted. |
| `/legal` and the five legal articles | Privacy, terms, business terms, professional services, subprocessors. |
| `/tools` and many `/tools/<slug>` pages | Tool landings. They share one template. |
| `/skills` and `/skills/copywriting` | Skills index and one skill. |
| `/radar` and `/radar/trends/united-states` | Radar index and one country sample. |
| `/status` and `/status/is-chatgpt-down` | Public status pages. |
| `/docs`, `/docs/api`, `/docs/get-started/what-is-endless`, `/docs/get-started/quickstart` | Docs shell. Sidebar sections expand in place. |
| `/sign-in` | Auth boundary. Photographed. Not submitted. |

## Home interactions

| Control | Result |
|---|---|
| Industries hover | Menu of four industry links. Screenshot `home-light-industries-menu`. |
| Select model (GPT-6.1 Terra) | Dialog: "Unlock more features" and Sign up free. Does not list models while signed out. |
| Add to prompt | Same gate dialog. |
| Create | Does not navigate and does not start a generation while signed out. |
| Prompt chips (Account analysis, Launch post, Product video) | Fill the composer. Not submitted. |
| Composer focus | Focuses the textarea. Nothing typed. |

## Auth stop

[https://endless.app/login](https://endless.app/login) redirects to [https://endless.app/sign-in](https://endless.app/sign-in). The page shows Google, Microsoft, an email field, a password field, Continue, and Use passkey instead. Apple was not in the rendered control list on this capture.

No email, password, code, or identity provider was used. Signed-in paths named in robots.txt were not opened: `/boards`, `/backpack`, `/iterate`, `/monitoring`, `/chat`, `/settings`, `/auth`.

On this capture, [https://endless.io/login](https://endless.io/login) redirected to the public homepage, not to the form.

## Not fully walked

Locale mirrors. The remaining tool, model, blog, comparison, skill, and integration leaves, which share the templates above. Docs articles beyond the four opened. Per-country radar leaves, listed in the JSON under `footerCountryBranches`.
