# fal.ai public site tree

Mapped signed out on 2026-11-21 from [https://fal.ai/](https://fal.ai/) in headless Chromium. A control that opens a login wall is recorded and that branch stops. OAuth providers were not clicked. Forms were not submitted.

## Header (desktop)

| Control | Opens |
|---|---|
| Logo "fal home" | Page `/` |
| Products (dropdown, hover) | Menu, not a page. Items below. |
| Products → Model APIs | Page `/explore` |
| Products → Serverless | Page `/serverless` |
| Products → Compute | Page `/docs/documentation/compute` |
| Docs | Page `/docs/documentation` |
| Pricing | Page `/pricing` |
| Enterprise | Page `/enterprise-hub` |
| Resources (dropdown, hover) | Menu. Items below. |
| Resources → Blog | Page `/blog` |
| Resources → Learn | Page `/learn` |
| Resources → Events | Page `/events` |
| Resources → Grants | Page `/grants` |
| Resources → Careers | Page `/careers` |
| Resources → GenMedia Report v2 | Page `/gen-media-report-volume-2` |
| Contact Sales | Page `/contact-sales` (sales form, not submitted) |
| Get Started | Login wall. Header href is `/dashboard`, which redirects to `/login?returnTo=%2Fdashboard`. Stopped. |

## Home body

| Control | Opens |
|---|---|
| Get Started (hero) | Login wall `/dashboard` → `/login?returnTo=%2Fdashboard`. Stopped. |
| Contact Sales (hero) | Page `/contact-sales` |
| Explore fal Worlds | Page `/worlds` |
| Model APIs tab | In-page pane `#w-tabs-0-data-w-pane-0`. Does not navigate. |
| Serverless tab | In-page pane `#w-tabs-0-data-w-pane-1` |
| Compute tab | In-page pane `#w-tabs-0-data-w-pane-2` |
| Explore Models / Explore all models | Page `/explore` |
| Featured model cards (H3 Max, Seedance 2.5, Meshy 7.1, Flux 3, GPT Image, MiniMax H3) | Page under `/models/<vendor>/<model>/<task>` |
| Private Deployments | Page `/docs/documentation/serverless` |
| See Documentation | Page `/docs/documentation` |
| See Pricing | Page `/pricing` |
| Learn More | Page `/enterprise-hub` |
| Copy to clipboard (code sample) | Copies sample code. No navigation. |
| Named model landing links (Seedream 5.0, GPT Image 2.6, Krea 3, and the rest in the footer lists) | Marketing page at `/<model-slug>` or `/models/...` |
| Workflows | Login wall `/login?returnTo=%2Fworkflows`. Stopped. |
| Training | Page `/models/fal-ai/flux-lora-fast-training` |

## Footer

| Control | Opens |
|---|---|
| Status | External [https://status.fal.ai/](https://status.fal.ai/) |
| Documentation | Page `/docs/documentation` |
| Pricing | Page `/pricing` |
| Serverless | Page `/serverless` |
| Enterprise | Page `/enterprise-hub` |
| Genmedia CLI | External [https://genmedia.sh/](https://genmedia.sh/) |
| Events | Page `/events` |
| Verify fal-Generated Content | Page `/verify`. Its Get Started is a login wall. |
| Report Content | Page `/report-content` (report form, not submitted) |
| Gen Media Report 2026 | Page `/gen-media-report-volume-2` (download form, not submitted) |
| Trust & Safety | Page `/legal/trust-and-safety` |
| Careers | Page `/careers`. Job rows open external Ashby listings. |
| Blog | Page `/blog` |
| Grants | Page `/grants` |
| Legal | Page `/legal` |
| Your Privacy Choices | In-page hash `#your-privacy-choices`. It is a footer link, not a consent accept. The DataGrail consent dialog (`aside.dg-consent-banner`) is separate and was hidden, not accepted. |
| Plugins | Page `/plugins` |
| MCP | Page `/mcp` |
| Learn | Page `/learn` |
| Get in touch | mailto link to the public support address (not opened; address not copied here) |
| Image / video / lab / playground / tool lists | Pages under `/explore/...`, `/tools/...`, `/<model-slug>`, `/agent`, `/sandbox` |
| Discord, Github, Reddit, X, LinkedIn, YouTube, Instagram, TikTok | External. Github is `https://github.com/fal-ai`, not an OAuth button. |
| Terms of Service | Page `/legal/terms-of-service` |
| Privacy Policy | Page `/legal/privacy-policy` |

## Docs shell (`/docs` redirects to `/docs/documentation`)

| Control | Opens |
|---|---|
| Documentation, Examples, Model API Reference, SDK Reference, Inference API, Platform API, Changelog | Docs pages under `/docs/...` |
| Sidebar links (Status, Community, Blog, Overview, Why fal, Quick Start, Accounts and Identity, Teams, Get Your API Key, Key-based, MCP, genmedia, Resources, Model APIs) | Docs pages. Get Your API Key and Key-based are documentation, not the key dashboard. |
| Accounts that need a session (API key dashboard, apps dashboard) | Login wall `/dashboard` or `/dashboard/keys`. Stopped. |
| Open search | In-page search field ("Search or ask a question"). Not submitted. |
| Switch to system / light / dark theme | Local theme on the docs shell. Dark was opened and photographed. |
| Ask Assistant | Assistant panel on the docs page. No message was sent. |
| Contact Sales | Page `/contact-sales` |
| Login | Login wall `/login`. Stopped. |

## Explore (`/explore`)

| Control | Opens |
|---|---|
| Search models | Search field. A visible input is `readonly` and `aria-hidden`; typing was not forced. |
| Category and lab links | Pages under `/explore/<slug>` (image, video, audio, 3d, labs, trending, vendor labs). |
| Model cards | Page `/models/...` |
| Try it now | Model playground page when public; some try actions are login walls and those branches stop. |
| Log-in / Sign-up | Login wall `/login?returnTo=%2Fexplore`. Stopped. |
| Pagination (Previous, Next, page numbers) | Same explore list, another page of results. |
| Theme controls | Present on the docs shell. Explore's `<html>` class included `light` on this capture. |

## Login wall (`/login`)

Reached from Get Started, `/dashboard`, `/signup` (404 page then Get Started), Workflows, and every `returnTo` link. There is no separate signup URL: `/signup` is a 404.

| Control | Opens |
|---|---|
| Continue with GitHub | `/api/auth/v2/connect/github`. Not clicked. |
| Continue with Google | `/api/auth/v2/connect/google`. Not clicked. |
| Continue with Microsoft | `/api/auth/v2/connect/microsoft`. Not clicked. |
| Use SSO | A button. Not clicked. No email field is visible before it. |
| Home, Docs, Blog, Pricing, Enterprise | Public pages. |
| Terms of Service, Privacy Policy | Legal pages. |
| Contact support | mailto link. Not opened. |

No email field, password field, or code field is on the wall.
