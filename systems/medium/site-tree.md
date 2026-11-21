# Medium public site tree

Walked signed out on 2026-11-21 from [https://medium.com/](https://medium.com/) (HTTP 200). Desktop viewport 1440. Phone viewport 390. No cookie banner was on the homepage. No page-level theme switch was found. `prefers-color-scheme` and `html[data-color-scheme]` pick light or dark. Query strings are stripped. Source and redirect parameters are not recorded.

Opened means the control was used and the result was photographed or the destination loaded. Linked means the href was read and the page was not opened in this pass. Stopped means the control leads to a login, signup, subscribe, or identity-provider wall and the branch ended there.

## Header, desktop

The wordmark links to `/`.

| Control | Opens |
|---|---|
| Our story | `/about` |
| Membership | `/membership` |
| Write | `/m/signin` with a register operation. Signup wall. Stopped. |
| Sign in | `/m/signin` with a login operation. Login wall. Stopped. |
| Get started (link) | `/m/signin` with a register operation. Signup wall. Stopped. |

## Homepage body

URL stays `/` unless noted.

| Control | Result |
|---|---|
| Get started (button) | Dialog on `/`, titled "Join Medium." Signup wall. Close dismisses it. Not submitted. Not photographed. |
| Start reading (button, two copies) | The same Join Medium dialog on `/`. Signup wall. Not submitted. |

No homepage search. No locale switch. No overflow menu. No theme switch.

## Footer, desktop

| Control | Opens |
|---|---|
| Help | `https://help.medium.com/hc/en-us` |
| Status | `https://status.medium.com` |
| About | `/about` |
| Careers | `/jobs-at-medium/work-at-medium-959d1a85284e` |
| Press | mailto. Not sent. The address is not recorded. |
| Blog | `https://blog.medium.com/` |
| Store | `/store`, which redirects to `https://www.bonfire.com/store/medium/` (HTTP 200, a third-party shop). Linked, not photographed. |
| Privacy | `https://policy.medium.com/medium-privacy-policy-f03bf92035c9` |
| Rules | `https://policy.medium.com/medium-rules-30e5502c4eb4` |
| Terms | `https://policy.medium.com/medium-terms-of-service-9db0094a1e0f` |
| Text to speech | `https://speechify.com/medium` |

## Header, phone (390)

The same destinations sit in the page. Our story, Membership, Write, and Sign in are in the document. The painted header shows the wordmark and Get started. Start reading stays in the hero. The footer collapses to About, Help, Terms, and Privacy. No hamburger was found. Dark phone is [home-dark-phone](screenshots/home-dark-phone.png).

## Membership

`/membership` loaded HTTP 200. Header: wordmark to `/`, Sign in to `/m/signin` (wall, stopped), Sign up to `/m/signin` (wall, stopped).

| Control | Opens |
|---|---|
| Get started | `/plans` |
| View plans | `/plans` |
| Member-only story | A story on the same host. One card was not opened, because the byline is a member account. |
| Select | A plan checkout. Subscribe wall. Not pressed. |

Footer adds Teams, which links to `/business`.

## About

`/about` loaded HTTP 200. Header: Sign in and Sign up, both to `/m/signin`. Walls. Stopped.

| Control | Opens |
|---|---|
| Medium members | `/membership` |
| start reading, Start reading | `/m/signin`. Wall. Stopped. |
| write your story, Start writing | `/new-story`. That route asks for an account. Not opened. |
| Become a member | `/membership` |

## Plans

`/plans` loaded HTTP 200. Title "Join a community of readers, writers, and thinkers." Monthly and annual prices are shown. Select is on each plan. Not pressed. No checkout was started.

## Sign-in wall

`/m/signin` loaded HTTP 200. Empty card. Photographed, then the branch stopped.

| Control | Result |
|---|---|
| Sign in with email | Reveals an email field. Not typed. Not submitted. |
| Create one | Switches the card toward register. Signup wall. Not submitted. |
| Remember me | A checkbox. Not changed. |
| Forgot email or trouble signing in? Get help | `https://help.medium.com/hc/en-us/requests/new`. A request form. Not opened. |
| Terms of Service, Privacy Policy | policy.medium.com. Linked. |

No Google, Apple, or other identity provider was on this card. None was clicked.

## Blog

`https://blog.medium.com/` loaded HTTP 200 and stayed on medium.com `/blog`. Public publication shell.

| Control | Opens |
|---|---|
| Get app | A store listing. Not opened. |
| Write, Sign up, Sign in | `/m/signin`. Walls. Stopped. |
| Search | `/search`. Public. Opened empty. Not typed. |
| Product News, Latest | `/blog/all` |
| Newsletter, Subscribe | `https://blog.medium.com/newsletter`. Subscribe wall. Not opened. |
| Follow, user options menu | Account actions. Not used. |

## Help

`https://help.medium.com/hc/en-us` loaded HTTP 200. Search field was left empty. Not submitted. Category links stay on the help center. Not followed past the home.

## Careers

The public staff story at `/jobs-at-medium/work-at-medium-959d1a85284e` loaded HTTP 200. Write, Sign up, Sign in, and Follow go to `/m/signin`. Walls. Stopped. "View all open positions" links to a Greenhouse board. Not opened. No application was started.

## Not offered on the public homepage

No settings area. No create or editor surface. Write, Get started, and Start reading all stop at the join dialog or `/m/signin`.
