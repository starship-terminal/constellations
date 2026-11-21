# Todoist public site tree

Mapped from https://www.todoist.com/ on 2026-11-21 in headless Chromium, signed out. `robots.txt` allows `/` and disallows `/app/`, `/auth/`, `/api/`, `/contact`, and `/upgrade`. The sitemap is https://www.todoist.com/sitemap.xml. This file records the shared chrome, the homepage controls, and one page of each public template that the chrome opens. A control that opens a login or signup wall is recorded and that branch stops.

The marketing host and the app host are different systems. Marketing lives on www.todoist.com. Login and signup live on app.todoist.com.

## Header

Present on every marketing page. At 1440 the links sit in the bar. At 390 they move into a menu button.

| Control | Opens |
|---|---|
| todoist wordmark | https://www.todoist.com/ |
| Individual | https://www.todoist.com/features |
| Business | https://www.todoist.com/teamwork |
| Integrations & AI | Menu, stays on the page. See Integrations & AI. |
| Resources | Menu, stays on the page. See Resources. |
| Pricing | https://www.todoist.com/pricing |
| Log in | https://app.todoist.com/auth/login . Empty email and password wall. Branch stops. See [login-review.json](login-review.json). |
| Start for free | https://app.todoist.com/auth/signup . Empty signup wall. Branch stops. |
| Menu button (390) | Overlay with Individual, Business, Integrations & AI, Resources, Pricing, Log in, Start for free. Close returns to the page. |

## Integrations & AI

Opened from the header control. The panel stays on the page.

| Label | Opens |
|---|---|
| AI tools | https://www.todoist.com/todoist-assist |
| AI agents | https://www.todoist.com/integrations/ai-agents |
| Integrations | https://www.todoist.com/integrations |
| API | https://developer.todoist.com/ |

## Resources

Opened from the header control. The panel stays on the page.

| Label | Opens |
|---|---|
| Download apps | https://www.todoist.com/downloads (redirects to /downloads/mac on desktop) |
| Templates | https://www.todoist.com/templates |
| Teams Toolkit | https://www.todoist.com/toolkit |
| Customer stories | https://www.todoist.com/customers |
| Help center | https://www.todoist.com/help |
| Security & trust | https://trustcenter.todoist.net/ |
| Productivity methods + quiz | https://www.todoist.com/productivity-methods |
| Inspiration Hub | https://www.todoist.com/inspiration |

## Homepage controls

| Control | Opens |
|---|---|
| Start for free (hero and later sections) | https://app.todoist.com/auth/signup . Branch stops. |
| Integration chips (Claude, ChatGPT, Google Calendar, Microsoft Teams, Zapier, Chrome & Gmail, Slack, n8n, Outlook Mail) | A public integration page under https://www.todoist.com/integrations/apps/ |
| Explore all integrations | https://www.todoist.com/integrations |
| API, Read the API docs | https://developer.todoist.com/ |
| CLI, Install the CLI | https://www.todoist.com/cli |
| MCP server, Set up the MCP server | https://developer.todoist.com/api/v1/ |
| Learn about AI in Todoist | https://www.todoist.com/ai-tools |
| For your team, Explore Todoist for Business | https://www.todoist.com/teamwork |
| For your life, Explore Todoist for Personal | https://www.todoist.com/features |
| Customer story cards, Read story | A public story under https://www.todoist.com/inspiration/ or https://www.todoist.com/customers |
| Download apps | https://www.todoist.com/downloads |
| Read our story | https://www.todoist.com/about-us |
| See pricing | https://www.todoist.com/pricing |

No message was typed. No video was played.

## Footer

Shared on marketing pages.

| Column | Control | Opens |
|---|---|---|
| Product | Download apps | https://www.todoist.com/downloads |
| Product | Pricing | https://www.todoist.com/pricing |
| Product | Templates | https://www.todoist.com/templates |
| Product | Teams Toolkit | https://www.todoist.com/toolkit |
| Product | Help center | https://www.todoist.com/help |
| Product | Compare | https://www.todoist.com/compare |
| Product | Import from Microsoft To Do | https://www.todoist.com/importer/microsoft-todo |
| Product | For individuals | https://www.todoist.com/features |
| Product | For businesses | https://www.todoist.com/teamwork |
| Teams | Real estate, Agencies, Law firms, For founders | https://www.todoist.com/teams/realtors-3, /teams/agencies-3, /teams/legal-3, /teams/owners-3 |
| Integrations | AI tools | https://www.todoist.com/todoist-assist |
| Integrations | AI agents | https://www.todoist.com/integrations/ai-agents |
| Integrations | Integrations | https://www.todoist.com/integrations |
| Integrations | Developer API | https://developer.todoist.com/ |
| Integrations | Status | https://status.todoist.net/ |
| Learn | Productivity quiz | https://www.todoist.com/productivity-methods |
| Learn | Customer stories | https://www.todoist.com/customers |
| Learn | Inspiration Hub | https://www.todoist.com/inspiration |
| Learn | Task management, Time management, Habit forming | https://www.todoist.com/task-management, /time-management, /habit-forming |
| Company | About us | https://www.todoist.com/about-us |
| Company | Careers | https://www.todoist.com/careers |
| Company | Press | https://www.todoist.com/press |
| Company | Channel partners | https://www.todoist.com/channelpartners |
| Social | YouTube, LinkedIn, Instagram, Reddit | External profiles. Not followed. |
| Legal | Security | https://www.todoist.com/security |
| Legal | Trust center | https://trustcenter.todoist.net/ |
| Legal | Privacy | https://www.todoist.com/privacy |
| Legal | Terms | https://www.todoist.com/terms-of-service |
| Legal | Cookie preferences, Your Privacy Choices | Stay on the page. Not clicked. The cookie overlay was hidden, not answered. |

## Page templates

Each row is one template the chrome opens. Collection items (one integration, one story, one template) use the same chrome.

| Template | URL | Controls beyond the chrome |
|---|---|---|
| Home | https://www.todoist.com/ | See Homepage controls. |
| Individual | https://www.todoist.com/features | Feature sections. Start for free stops at signup. |
| Business | https://www.todoist.com/teamwork | Play (in-page video, not played). FAQ expand. Start for free stops at signup. |
| Pricing | https://www.todoist.com/pricing | Monthly / Yearly stay on the page. Prices in opens a currency menu, not followed. Beginner "Get started" and Pro and Business "Start for free" stop at signup. FAQ expand stays on the page. |
| Integrations | https://www.todoist.com/integrations | Search field. No query was typed. App cards open a public integration page. |
| Templates | https://www.todoist.com/templates | Horizontal scroll buttons stay on the page. A template card is a public page. Use template was not followed past the card. |
| Downloads | https://www.todoist.com/downloads | Redirects to /downloads/mac. Platform links stay on the downloads template. |
| Help | https://www.todoist.com/help | Search field. No query was typed. |
| Inspiration | https://www.todoist.com/inspiration | Article cards stay public. |
| Customers | https://www.todoist.com/customers | Watch story and Read story stay public. Not played. |
| Compare | https://www.todoist.com/compare | Play (not played). FAQ expand. |
| AI tools | https://www.todoist.com/ai-tools | Play (not played). FAQ expand. |
| CLI | https://www.todoist.com/cli | Copy buttons. Nothing was copied. |
| About | https://www.todoist.com/about-us | Play video (not played). Previous and Next stay on the page. |
| Careers | https://www.todoist.com/careers | Job links stay on the careers host. No application was opened. |
| Security | https://www.todoist.com/security | Policy page. No form. |

## Auth walls

| Control | Landed URL | Stop |
|---|---|---|
| Log in | https://app.todoist.com/auth/login | Empty wall. Email and password are visible. Google, Facebook, and Apple are offered and were not clicked. Log in was not clicked. |
| Start for free, Get started | https://app.todoist.com/auth/signup | Empty wall. Email and password are visible. Google, Facebook, and Apple are offered and were not clicked. Sign up with Email was not clicked. |
| Forgot your password? | Not opened. | The login wall already shows the link. The branch stops on the wall. |
| Sign up, from the login wall | Not opened. | Same signup URL as Start for free. |
| Go to login, from the signup wall | Not opened. | Same login URL as Log in. |
