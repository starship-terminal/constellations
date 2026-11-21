# Doppler public site tree

Mapped on 2026-11-21, signed out, with Playwright (headless Chromium). Start: [https://www.doppler.com/](https://www.doppler.com/). The marketing host answered 200. No form was filled. No OAuth button was clicked. A control that opens a login, signup, or account wall is recorded and that branch stops.

Sitemap: [https://www.doppler.com/sitemap.xml](https://www.doppler.com/sitemap.xml) points at [https://www.doppler.com/sitemap-0.xml](https://www.doppler.com/sitemap-0.xml), which lists **692** URLs, all on `www.doppler.com`. Docs live on `docs.doppler.com` and are not in that sitemap. They were mapped from the docs sidebar on [https://docs.doppler.com/docs/start](https://docs.doppler.com/docs/start).

Themes observed: the marketing site paints one dark surface (`rgb(28, 22, 36)` page, warm-white type). Emulating `prefers-color-scheme: dark` did not change it, and no theme control was found. Docs paint a light page (`rgb(255, 255, 255)`). No docs theme toggle was found in the header, sidebar, or footer (ReadMe classic chrome: search, sidebar collapse, copy page). Docs theme is recorded as not present on the public docs chrome.

Widths checked: desktop `window.innerWidth` 1440, phone 390.

## Login, signup, and account walls

These URLs were reached or linked. The branch stops. No email, password, or OAuth click.

| Control | Opens | Where it appears |
|---|---|---|
| Sign In | [https://dashboard.doppler.com/login](https://dashboard.doppler.com/login) | Header on every marketing page. Probe: email and password fields, plus Google and GitHub. Not clicked. |
| Start for Free, Sign Up, Start 14 Day Trial | [https://dashboard.doppler.com/register](https://dashboard.doppler.com/register) | Header, hero, menu footers, pricing, blog CTAs |
| Doppler Share | [https://share.doppler.com/](https://share.doppler.com/) | Footer, Product column |
| Import to Doppler | [https://dashboard.doppler.com/workplace/template/import](https://dashboard.doppler.com/workplace/template/import) | Some blog posts |
| workplace Billing page | [https://dashboard.doppler.com/workplace/billing](https://dashboard.doppler.com/workplace/billing) | Blog product-update posts |
| Dashboard home (no path) | [https://dashboard.doppler.com/](https://dashboard.doppler.com/) | Older changelog posts |
| Try Doppler for free, free account | [https://dashboard.doppler.com/login](https://dashboard.doppler.com/login) | Blog bodies |

Docs header **Sign Up** goes to the same register wall. Docs **Support** goes to [https://support.doppler.com/](https://support.doppler.com/). Not entered.

## Global marketing chrome

Present on every `www.doppler.com` page measured at 1440. Header height 72px. At 390 the same links collapse behind **Toggle menu**.

### Header links (always visible at 1440)

| Control | Opens |
|---|---|
| Logo | [/](https://www.doppler.com/) |
| Doppler for Agents | [/agents](https://www.doppler.com/agents) |
| Customers | [/customers](https://www.doppler.com/customers) |
| Pricing | [/pricing](https://www.doppler.com/pricing) |
| Sign In | login wall (table above) |
| Get Demo | [/demo](https://www.doppler.com/demo) |
| Start for Free | register wall |

### Header menus (buttons, `aria-expanded`, desktop)

**Platform** opens a dropdown. Each row is a link:

| Link | Opens |
|---|---|
| Secrets manager | [/platform/secrets-manager](https://www.doppler.com/platform/secrets-manager) |
| Govern access | [/platform/govern](https://www.doppler.com/platform/govern) |
| Develop locally | [/platform/develop](https://www.doppler.com/platform/develop) |
| CICD & production | [/platform/orchestrate](https://www.doppler.com/platform/orchestrate) |
| Compliance | [/platform/compliance](https://www.doppler.com/platform/compliance) |
| Secrets rotation | [/platform/secrets-rotation](https://www.doppler.com/platform/secrets-rotation) |
| Start for Free (menu footer) | register wall |

**Solutions** opens a dropdown:

| Link | Opens |
|---|---|
| On-prem | [/doppler-on-prem](https://www.doppler.com/doppler-on-prem) |
| Single source of truth | [/solutions/use-cases/single-source-of-truth](https://www.doppler.com/solutions/use-cases/single-source-of-truth) |
| Least privilege access | [/solutions/use-cases/least-privilege-access](https://www.doppler.com/solutions/use-cases/least-privilege-access) |
| Leak prevention | [/solutions/use-cases/leak-prevention](https://www.doppler.com/solutions/use-cases/leak-prevention) |
| Breach remediation | [/solutions/use-cases/breach-remediation](https://www.doppler.com/solutions/use-cases/breach-remediation) |
| Secrets sprawl | [/secrets-sprawl](https://www.doppler.com/secrets-sprawl) |
| Start for Free | register wall |

**Resources** opens a dropdown:

| Link | Opens |
|---|---|
| Resources & media | [/resources](https://www.doppler.com/resources) |
| Blog | [/blog](https://www.doppler.com/blog) |
| Careers | [/careers](https://www.doppler.com/careers) |
| Docs | [https://docs.doppler.com/](https://docs.doppler.com/) (redirects to `/docs/start`) |
| Integrations | [/integrations](https://www.doppler.com/integrations) |
| GitHub Actions secrets aren't enough | [/blog/github-actions-secrets-best-practices](https://www.doppler.com/blog/github-actions-secrets-best-practices) |
| How to stop AI coding agents from reaching your production secrets | [/blog/ai-coding-agents-production-secrets](https://www.doppler.com/blog/ai-coding-agents-production-secrets) |
| Explore More | [/blog](https://www.doppler.com/blog) |
| Start for Free | register wall |

**Toggle menu** (phone, `aria-label` "Toggle menu"): opens the same Platform, Solutions, and Resources groups as stacked disclosures, plus the header links. Screenshot: `mobile-home-dark-menu-open`.

Cookie buttons (Cookie Preferences, Do Not Sell or Share My Personal Information, Cookie Settings, Okay) sit in a OneTrust layer. They were hidden, not clicked. They open a consent dialog, not a page.

### Footer (every marketing page)

Product: Customers, Pricing, Changelog ([https://docs.doppler.com/changelog](https://docs.doppler.com/changelog)), Doppler Share (account wall), Universal Import, Security, On-prem.

Resources: Whitepapers ([/resources/whitepapers](https://www.doppler.com/resources/whitepapers)), Guides ([/resources/guides](https://www.doppler.com/resources/guides)), Vault ([/doppler-vs-vault](https://www.doppler.com/doppler-vs-vault)), Akeyless ([/doppler-vs-akeyless](https://www.doppler.com/doppler-vs-akeyless)), Infisical ([/doppler-vs-infisical](https://www.doppler.com/doppler-vs-infisical)), Breach dashboard, Glossary.

Developers: Documentation, API reference ([https://docs.doppler.com/reference](https://docs.doppler.com/reference)), AI coding agents, Bug bounty ([https://hackerone.com/doppler](https://hackerone.com/doppler), external), Compliance request ([https://trust.doppler.com/](https://trust.doppler.com/), external trust center), Status ([https://dopplerstatus.com/](https://dopplerstatus.com/) and [https://www.dopplerstatus.com/](https://www.dopplerstatus.com/), external).

Integrations column: Vercel, Heroku, Github Secrets (docs anchor), AWS Secret Manager, More... (`/integrations`).

Community: Discussions, Need help, Feature requests, Show and tell (all `community.doppler.com`, external).

Company: SecretOps for students, Blog, About, Careers, Resources & media, Events (`/resources#event`), Support ([https://support.doppler.com/](https://support.doppler.com/)), Brand Hub.

Legal: Terms of Service, Privacy notice, Data protection, Sub-Processors, Cookie notice, Website terms. Paths under `/legal/` (full list below).

Icon row: community, GitHub (`github.com/dopplerhq`), LinkedIn, YouTube, Bluesky, Instagram, TikTok. One icon is a `mailto:` link. Not followed. No address was written down.

Status pill in the footer: **All Systems Operational** opens [https://www.dopplerstatus.com/](https://www.dopplerstatus.com/).

## Home page interactions

[https://www.doppler.com/](https://www.doppler.com/)

| Control | Opens |
|---|---|
| Start for Free (hero and closing band) | register wall |
| Get Demo (closing band) | `/demo` |
| Learn More under Native AI integration | [https://docs.doppler.com/docs/mcp](https://docs.doppler.com/docs/mcp) |
| See Pricing / Learn More under pricing claims | `/pricing` |
| Learn More under audit claim | `/platform/compliance` |
| See Integrations | `/integrations` |
| Learn More under SOC 2 | [https://trust.doppler.com/](https://trust.doppler.com/) |
| Learn More under agent-scoped access | [https://docs.doppler.com/docs/service-account-identities](https://docs.doppler.com/docs/service-account-identities) |
| Learn More under secrets sprawl | `/secrets-sprawl` |
| Learn More under dynamic secrets | [https://docs.doppler.com/docs/dynamic-secrets](https://docs.doppler.com/docs/dynamic-secrets) |
| Read More (Ada, Traive, Paradox) | `/case-studies/ada`, `/case-studies/traive`, `/case-studies/paradox` |
| Product demo frame | [https://doppler.navattic.com/bt03ubn](https://doppler.navattic.com/bt03ubn) (external interactive demo, not the dashboard) |

No tabs, search field, or accordion on the home page. Menus are the header dropdowns above.

## Page index (marketing)

Photographed pages are marked. Repeating templates (blog posts, changelog notes, glossary terms, guide chapters, integration detail pages) share one layout. One example of each template was opened. The rest are listed from the sitemap so the tree stays complete.

### Product and company (photographed at 1440 unless noted)

| Path | In-page controls | Phone 390 |
|---|---|---|
| `/` | header menus | yes, plus menu-open |
| `/pricing` | FAQ accordions (see below). Plan CTAs go to the register wall or `/demo` | yes |
| `/agents` | links into docs and agent landing pages | full page |
| `/customers` | industry filter buttons | yes |
| `/integrations` | category filter buttons and a Search field (not submitted) | yes |
| `/blog` | category buttons and a Search field (not submitted) | yes |
| `/resources` | Content Type menu, Search field, pagination | viewport |
| `/demo` | booking form (not filled) and FAQ accordions | yes |
| `/security` | links to trust center and legal | viewport |
| `/about` | links to careers and blog | viewport |
| `/careers` | job links (external board if present; not applied) | viewport |
| `/brand` | Copy hex buttons (copy to clipboard, no navigation) | viewport |
| `/glossary` | A–Z filter buttons and Search | viewport |
| `/breach-dashboard` | year filter buttons | viewport |
| `/platform/secrets-manager` | same marketing shell | viewport |
| `/platform/govern` | same marketing shell | viewport |
| `/doppler-on-prem` | CTA to demo and register wall | viewport |
| `/case-studies/ada` | case-study template | viewport |
| `/legal/privacy` | legal template | viewport |
| `/universal-import` | FAQ accordions | viewport |

### Platform (all six, from the Platform menu and sitemap)

`/platform/secrets-manager`, `/platform/govern`, `/platform/develop`, `/platform/orchestrate`, `/platform/compliance`, `/platform/secrets-rotation`.

Each is a long marketing page in the same shell. CTAs are Start for Free (register wall) and Get Demo (`/demo`).

### Solutions

`/solutions/use-cases/single-source-of-truth`, `/solutions/use-cases/least-privilege-access`, `/solutions/use-cases/leak-prevention`, `/solutions/use-cases/breach-remediation`. Plus `/secrets-sprawl` and `/doppler-on-prem` from the same menu.

### Comparisons (footer)

`/doppler-vs-vault`, `/doppler-vs-akeyless`, `/doppler-vs-infisical`.

### Customers and case studies

`/customers` filter buttons (in-page, no URL change observed): AI, Software development, Marketplace, Agriculture, Insurtech, Health, Biomedical research. Each filters the card grid.

Case studies (same template, one photographed): `/case-studies/ada`, `agentsync`, `becks`, `bodi`, `cci`, `endear`, `hyper`, `mattr`, `paradox`, `retraced`, `traive`, `whatnot`.

### Pricing FAQ (accordion buttons, stay on `/pricing`)

What does Doppler do? How long does it take to learn Doppler? Is Doppler secure? Where's my data stored? How will you charge me? What counts as a user? Can I add an Enterprise feature to my Team subscription? Do you offer a discount for non-profits, students, and educators? Can I deploy Doppler on-premise? Do I need a credit card to sign up? How does Doppler pricing work? How does billing work? Can I cancel at anytime?

Plan buttons: Start 14 Day Trial opens the register wall. Demo buttons open `/demo`.

### Demo (`/demo`)

**Choose a Time** and the form fields (name, email, company size select: Under 100 / 101-1000 / 1001+ employees) were left empty. FAQ accordions stay on the page: Is the Enterprise plan right for me? Do you support on-premises deployments? How does Doppler handle access for AI agents and automated workflows? Can I integrate with my current stack? Is Doppler compliant? Not quite ready for a demo? Need help or support?

### Blog

`/blog` category buttons (in-page filter): ALL, COMPANY, DEVREL, EMPLOYEES, ENGINEERING, PRODUCT, TUTORIALS, SECURITY. Search input placeholder "Search" (not submitted). Pagination: Previous page / next.

299 posts under `/blog/<slug>`. Template: article, author link (`/blog/author/<slug>`), related posts, and a newsletter **Stay up to Date** button. That button was not submitted. Author pages include a newsletter **Submit** button. Not submitted.

### Integrations

`/integrations` category buttons: WEBHOOKS, AUTOMATION & WEBHOOKS, SECRETS ROTATION, DEVELOPER TOOLKIT, DYNAMIC SECRETS, SCIM, KUBERNETES, SYNCS, MONITORING & ALERTS, SAML SSO. Search field not submitted. **Request Integration** stays on the page as a request control. Not submitted.

Detail pages (same template): `/integrations/aws-parameter-store`, `aws-secrets-manager`, `azure-app-service`, `azure-devops`, `azure-key-vault`, `bitbucket`, `buddy`, `circleci`, `cloudflare-workers`, `digitalocean`, `docker`, `docker-compose`, `firebase-functions`, `flyio`, `gcp-cloud-build`, `gcp-secret-manager`, `gitlab`, `heroku`, `kubernetes`, `laravel-forge`, `netlify`, `railway`, `render`, `serverless`, `vercel`.

### Resources

`/resources` **Content Type** opens a menu of the hubs below. Search field not submitted. Pagination present.

Hubs: `/resources/events`, `/resources/guides`, `/resources/infographics`, `/resources/press`, `/resources/podcasts`, `/resources/videos`, `/resources/webinars`, `/resources/whitepapers`, `/resources/research-reports`.

### Glossary

`/glossary` plus 45 term pages `/glossary/<term>`. Index controls: ALL and letter buttons A–Z, plus Search. Letter buttons filter the index in place.

### Changelog mirror

`/changes` on the marketing host redirects to [https://docs.doppler.com/changelog](https://docs.doppler.com/changelog). The sitemap still lists 194 notes at `/changes/<slug>`. Those notes are the same docs changelog entries.

### Guides (51 URLs, chapter templates)

Series indexes and chapters:

- `/guides/aws-guides` and chapters (`aws-cdk-secrets-manager`, `aws-cli-secrets-manager`, `aws-kms-key-rotation`, `aws-secrets-manager-alternatives`, `aws-secrets-manager-kubernetes`, `aws-secrets-manager-vs-kms`, `aws-secrets-manager-vs-parameter-store`, `aws-vault`, `lambda-secrets-manager`, `secrets-manager-aws`, `ssm-parameter-store`, `terraform-aws-secrets-manager`)
- `/guides/cloudflare-workers-doppler` and chapters (`add-secrets-to-doppler`, `clone-starter-project`, `complete`, `create-doppler-project`, `deploy-app-sync-secrets`, `github-actions-cicd`, `intro`, `local-development`, `rotating-secrets`, `team-collaboration`, `troubleshooting`)
- `/guides/managing-secrets-at-scale` and chapters (`automating-secrets-management`, `integrating-secrets-into-cicd-production`, `intro`, `managing-secrets`, `secrets-management`, `teams-managing-secrets`, `whats-next`)
- `/guides/mcp-server-security-risks-attack-scenarios` and chapters (`credential-leakage`, `detecting-mcp-security-incidents`, `exposed-remote-mcp-servers`, `intro`, `malicious-code-and-credential-theft`, `over-privileged-credentials`, `prompt-injection-triggers`)
- `/guides/secrets-management-solutions` and chapters (`cloud-security`, `multi-cloud`, `open-source`, `single-cloud`, `strategy`)
- `/guides/the-pros-and-cons-of-using-gitflow-in-terraform-opentofu-projects` and chapters (`Advantages-of-Using-GitFlow-for-Terraform`, `Best-practices-for-GitFlow-with-Terraform`, `Introduction-to-GitFlow-for-Terraform`)

Chapter pages use the same long-form template as blog posts (header, body, footer). Next-chapter links stay inside the series.

### Legal

`/legal/cookie`, `/legal/dpa`, `/legal/dpa-onprem`, `/legal/privacy`, `/legal/referral-program-terms`, `/legal/sub-processors`, `/legal/terms`, `/legal/website-terms`.

### Other sitemap roots (same marketing shell, not each photographed)

`/advent-of-code-2026`, `/agents-claude-code`, `/agents-codex`, `/agents-cursor`, `/agents-github-copilot`, `/agents-grok-build`, `/agents-hermes`, `/agents-openclaw`, `/agents-opencode`, `/barcade`, `/beyond-the-breach`, `/dzone-the-future-of-secrets-management`, `/future-of-secrets-management`, `/managed-workload-identities`, `/mastering-the-backlog`, `/new-era-of-secrets-management`, `/secrets-management-core-practices`, `/secretsops-for-students`, `/securing-modern-applications`, `/the-future-of-secrets-management-2025`, `/the-roi-of-secrets-management`, `/the-true-cost-of-a-data-breach`, `/whitepaper/ai-infrastructure-mcp-security`, `/why-secrets-management-is-no-longer-a-nice-to-have`.

These are campaign and whitepaper landings. CTAs follow the same rule: Start for Free is the register wall, Get Demo is `/demo`.

### Brand page copy buttons

On `/brand`, each swatch button copies a hex value and does not navigate: Warm Black `#1C1624`, Warm White `#F1F0EC`, Purple `#6B13F5`, Light Purple `#B997FF`, Fluorescent Green `#00F575`, Carmine `#F55C15`, Lilac `#FF9EFA`, Factory Yellow `#FEE442`. **Copy company description** copies text. Not activated (clipboard).

## Docs (`docs.doppler.com`)

[https://docs.doppler.com/](https://docs.doppler.com/) redirects to [https://docs.doppler.com/docs/start](https://docs.doppler.com/docs/start). Light theme. No theme toggle found.

### Docs header

| Control | Opens |
|---|---|
| Documentation | `/docs` (start) |
| API Reference | `/reference` |
| Changelog | `/changelog` |
| Search (aria-label "Search", shortcut shown as ⌘K) | in-page search dialog. Placeholder "Start typing to search…". Tabs inside the dialog: All, Documentation, API Reference, Changelog. Not typed into. Escape closes it. |
| Toggle navigation menu | mobile drawer of the sidebar |
| Hide sidebar navigation | collapses the left nav in place |
| Sign Up | register wall |
| Support | [https://support.doppler.com/](https://support.doppler.com/) |
| Status | status host |
| Community | [https://community.doppler.com/](https://community.doppler.com/) |

### Docs sidebar

Each row is a link. A **Show subpages for …** button expands that group in place (no navigation). Groups observed:

Getting started: Welcome (`/docs/start`), Getting Started, Team Management, CI/CD & Production, Managing Secrets, Secrets Rotation (beginner series slugs under `/docs/secretops-beginners-series-*`).

Development: API Reference (`/reference/api`), Command Line (`/docs/install-cli` and children: CLI Guide, Automatic Restart, TUI, secrets setup/access/setting, injection templates, multiple commands, multiple workplaces, fallback files, CLI behavior, troubleshooting, MCP Server), Editors (VS Code and language notes, PyCharm, WebStorm), SDKs (Node.js, Python, Other), Languages (C#, Ruby), Frameworks (Ecto, PM2, Vite.js, Terraform CDK).

Integrations: Universal Import Guide, Integration Access Scoping, Automated Syncs (AWS, Azure, Bitbucket, CircleCI, Cloudflare Pages, Codefresh, Deno Deploy, DigitalOcean, Fly.io, GCP, GitHub, GitLab, Harness, Hasura, Heroku, Laravel Forge, Netlify, Postman, Railway, Qovery, Render, Supabase, Terraform Cloud, Vercel), DIY Syncs (Lambda, Beanstalk, ECS, BuddyCI, Workers, Cloud 66, Cron, Droplets, Docker, Compose, Direnv, EAS, Firebase, Cloud Build, Gitpod, Jenkins, Vapor, Pipedream, Serverless, Webapp.io), Infrastructure as Code (`/docs/terraform`), Kubernetes and the operator (install, sync, secrets, troubleshooting, uninstall, security, examples, External Secrets Operator), Rotated Secrets (AWS, Azure, Cloudflare, GCP, MongoDB Atlas, OpenAI, SendGrid, Twilio), Dynamic Secrets (AWS IAM, Azure).

Workplace: structure, settings, default environments, domain verification, activity logs (SQS, Datadog, Discord, HTTPS, Teams, Slack, Splunk, Sumo Logic), access logs, EKM (AWS, GCP), limits, high availability, analytics.

Access: SAML SSO (Auth0, Authentik, AWS, Duo, Google, JumpCloud, Entra ID, Okta, OneLogin), SCIM (same vendors), team, groups, custom roles, advanced permissions, service accounts, OIDC identities, MFA.

Projects: create, permissions, tags, webhooks, templates, change requests, configs, branch configs, inheritance, service tokens, trusted IPs, secrets (import, visibility, generation, versioning, search, compare).

Also: Security Fact Sheet, Doppler Share Security, troubleshooting notes, FAQs, SLO.

**Copy Page** and the AI split button sit on the article. Not clicked (they copy page text). **Yes** / **No** ("this page helped me") open a feedback control. Not clicked. An **Ask AI** button sits at the bottom right of the docs page. Not clicked.

Blog SECURITY and integrations KUBERNETES filters were inventoried. A click did not produce a distinct screenshot, so those two filtered states are mapped and not photographed. The customers AI filter is photographed.

### Docs pages photographed

`/docs/start` at 1440 and 390, search open, Command Line subpages expanded. `/changelog` at 1440.

API reference (`/reference`) is a separate docs section with the same search chrome. Not walked page by page. Its index is the sidebar link above.

## External hosts linked from the public tree

Recorded, not crawled past the first hop: `dashboard.doppler.com` (wall), `share.doppler.com` (wall), `trust.doppler.com`, `support.doppler.com`, `community.doppler.com`, `dopplerstatus.com`, `hackerone.com/doppler`, `github.com/dopplerhq`, social profiles, `doppler.navattic.com`.

## What was not captured

Signed-in dashboard, workplace, billing, share links, and any page behind the login wall. Docs theme: no control found. Newsletter and demo forms: not filled. OAuth: not clicked.
