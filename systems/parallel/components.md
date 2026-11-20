# Components

Public controls on www.useparallel.com, captured 2026-11-21, signed out. Values are token names where a token exists. A state that was not read is Not captured.

## Button

The header Sign up and the employer Start Free are pill buttons. The login wall's Sign in is a black pill. See [login-wall-light-default](screenshots/login-wall-light-default.png) and [home-light-default](screenshots/home-light-default.png).

| State | Evidence |
|---|---|
| default | captured, screenshots |
| hover | Not captured as a separate reading |
| focus-visible | forced in [raw/components-computed.json](raw/components-computed.json); crop in [components/crops/](components/crops) |
| pressed | Not captured |
| disabled, loading | not present |

## Link

Footer links (Explore Jobs, Platform, Manifesto, Terms) and in-page text links. See any full-page marketing shot.

## Text field

Home "Search roles" and the job-search field "Search by role, skill, or company". Placeholder text only. Not submitted. See [search-light-default](screenshots/search-light-default.png).

## Menu

Explore opens a four-item menu: Explore Paths, Explore Jobs, AI Training, Take Workform. See [home-light-explore-menu](screenshots/home-light-explore-menu.png). The employer header opens Overview, Platform, Recruiting, Studio. See [employers-light-overview-menu](screenshots/employers-light-overview-menu.png). Phone uses Open menu. See [mobile-home-light-menu-open](screenshots/mobile-home-light-menu-open.png).

## Tabs

Talent and Employers in the header. Jobs and Companies on the search page.

## Dialog

`/login` is a centered card: email, password, Sign in, or LinkedIn. `/signup` is LinkedIn only. Both are walls. Not filled. See [login-wall-light-default](screenshots/login-wall-light-default.png) and [signup-wall-light-default](screenshots/signup-wall-light-default.png).

## Card and list row

Job cards on the search page: logo, company, title, location, salary chip, type chip, save heart. See [search-light-default](screenshots/search-light-default.png).

## Accordion

Employer FAQ. One item opened. See [employers-light-faq-open](screenshots/employers-light-faq-open.png).

## Switch and select

Search has a Remote Only switch and Location, Salary, Job Type, and Sort menus. Visible in [search-light-default](screenshots/search-light-default.png). Their open panels are in [search-light-filters](screenshots/search-light-filters.png).

## Not present on the public pages

Checkbox, radio, tooltip, toast, data table, and a dedicated badge component were not found. Avatar-like marks are company logos on job cards, not a user avatar component.

## Gaps

- Signed-in Hire, candidate matches, messages, and profile were not reached.
- Hover and pressed were not tokenised.
- Radii and motion durations were not declared as custom properties, so they stay Not captured rather than estimated from screenshots.
