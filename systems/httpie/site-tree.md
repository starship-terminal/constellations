# HTTPie site tree

Mapped on 2026-11-21 from [https://httpie.io/](https://httpie.io/) with headless Chromium. The crawl followed public links on `httpie.io` only. It stopped at 80 pages with 310 still queued, almost all blog posts and docs leaves. The control map below is the full first-level tree, not that truncated crawl.

No signed-in surface was reached. [https://httpie.io/login](https://httpie.io/login), `/signin`, `/sign-in` and `/account` are the site's own 404 ("The requested page doesn't exist. Take me home"). [https://httpie.io/app](https://httpie.io/app) opens the API client in an Incognito space with no account form.

## Theme

The marketing shell paints dark by default (`html.dark`, body `rgb(30, 25, 25)`, text `rgb(245, 245, 240)`). A footer control labelled LIGHT MODE / AUTO / DARK MODE switches the class. AUTO follows `prefers-color-scheme`. `<meta name="theme-color" content="#F5F5F0">` is the light paper, with no dark media variant.

## Home controls

| Control | Opens |
|---|---|
| Wordmark | [/](https://httpie.io/) |
| Desktop | [/desktop](https://httpie.io/desktop) |
| Terminal | [/cli](https://httpie.io/cli) |
| AI | [/ai](https://httpie.io/ai) |
| Docs | [/docs](https://httpie.io/docs) |
| Jobs (badge 5) | [/jobs](https://httpie.io/jobs) |
| Blog | [/blog](https://httpie.io/blog) |
| Twitter | https://twitter.com/httpie (external) |
| GitHub | https://github.com/httpie (external) |
| Discord | [/discord](https://httpie.io/discord) (Discord invite widget, not an HTTPie page) |
| Go to App | [/app](https://httpie.io/app) |
| Changelog card / Read blog post | [/blog/changelog-0027](https://httpie.io/blog/changelog-0027) |
| Public beta chip | [/blog/changelog-0017](https://httpie.io/blog/changelog-0017) |
| Learn more (Web & Desktop) | [/desktop](https://httpie.io/desktop) |
| Get the Mac App / Download | [/download](https://httpie.io/download) |
| Learn more (Terminal) | [/cli](https://httpie.io/cli) |
| About | [/about](https://httpie.io/about) |
| Terms & Conditions | [/terms](https://httpie.io/terms) |
| Privacy Policy | [/privacy](https://httpie.io/privacy) |
| LIGHT MODE / AUTO / DARK MODE | local theme class on the same page |
| Share on Twitter, Follow, Star on GitHub, DEV, Reddit | external |

## Product pages

| Page | What it is |
|---|---|
| [/desktop](https://httpie.io/desktop) | Web and Desktop marketing |
| [/cli](https://httpie.io/cli) | Terminal marketing. Links into CLI docs and [/cli/run](https://httpie.io/cli/run) |
| [/cli/run](https://httpie.io/cli/run) | Public terminal demo |
| [/ai](https://httpie.io/ai) | HTTPie AI marketing |
| [/download](https://httpie.io/download) | Desktop download (macOS, Windows, Linux) |
| [/app](https://httpie.io/app) | Public web client, Incognito space |

## Docs hub

[/docs](https://httpie.io/docs) links to two books:

- [/docs/desktop](https://httpie.io/docs/desktop): 156 unique section URLs (getting started, requests, GraphQL, import/export, spaces, variables, account, settings, theme, shortcuts, AI). Account and log-in are documentation pages, not a sign-in form.
- [/docs/cli](https://httpie.io/docs/cli): latest is 3.2.4. The sidebar also lists version URLs (`/docs/cli/3.2.4` and older) and one page per CLI topic.

## Blog and jobs

[/blog](https://httpie.io/blog) lists changelog posts (`/blog/changelog-0001` through `changelog-0027`) and essays (`/blog/ai`, `/blog/stardust`, `/blog/httpie-3.2.0`, and others). [/jobs](https://httpie.io/jobs) lists five Ashby-hosted roles at `/jobs/<uuid>`. Those role pages are white Ashby embeds, not the marketing shell. Apply links leave for `jobs.ashbyhq.com`.

## Stopped, not captured as product UI

| URL | What it showed |
|---|---|
| [/login](https://httpie.io/login), `/signin`, `/sign-in`, `/account` | Site 404. Not a login wall. |
| [/discord](https://httpie.io/discord) | Discord invite. Asks for a display name and date of birth. Not filled. |
| [/survey](https://httpie.io/survey) | Mailchimp survey. Not filled. |
| External hosts | GitHub, Twitter, Reddit, Product Hunt, Ashby, brew.sh, pypi.org |

## App controls (incognito, no account form)

| Control | Interaction |
|---|---|
| Incognito space | Labels the unsigned space. Not a sign-in form. |
| Collection | Sidebar section |
| Collapse | Folds the sidebar |
| Drafts | Draft list |
| Import… | Import dialog. Not submitted. |
| Close tab | Closes the request tab |
| Environments | Environment switcher |
| GET | Method menu |
| Send | Would send the sample `GET httpie.io/hello`. Not pressed. |
| Params, Headers, Auth, Body | Request editor tabs. Auth opens a local type menu (None, Basic auth, Bearer token, API key). No credentials entered. |
| Request, Response | Pane tabs. Response stayed at "Not sent". |
| Try it out / Close / Read announcement | HTTPie AI promo. Try it out was not pressed. Close dismisses the promo. |
