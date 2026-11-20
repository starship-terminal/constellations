# Patterns

How the public Teams marketing pages are put together. Every screenshot is a signed-out page. The product UI (chat, meetings, calling) sits behind a Microsoft account and is not in this package.

## Shell

A 54px white universal header (`header.uhf-header`) carries the Microsoft wordmark, a Teams product switcher, and the links Products, Plans and pricing, Features, Solutions, Resources, Support. On the right: a filled "Try for free", an outlined "Download Teams", and an outlined "Sign in". See [home-light-default.png](screenshots/home-light-default.png).

Under the header, a 40px Ignite announcement ("Innovation unlocked at Microsoft Ignite: Nov 17-20, 2026") sits on a dark band. It is live site content from the capture day.

At 390px the header collapses to the wordmark and a "Teams" menu. The hero stacks, and "Download now" becomes a full-width pill. See [mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

## Hero

The home hero is a pale blue wash (`#f4fafd` / `#dceef8` declared stops) with a 62px heading, a 16px lede, and one purple "Download now". A product illustration occupies the right half. A jump-link row (Featured news, Solutions, Products and services, Customer stories, Get started) plus "See plans and pricing" sits on the next band.

## Ask Microsoft

Below the jump links, an "Ask Microsoft" block pairs a "Feedback" pill with a 64px question field and suggestion chips ("What are the key benefits of Teams?", "Get a custom quote"). A floating "Ask Microsoft" launcher stays at the bottom right of every page. These are marketing assistants, not the Teams chat client.

## Pricing

[pricing-light-default.png](screenshots/pricing-light-default.png) centres a 62px heading over a pill switcher (Business selected, Individuals, Enterprise) and a second pill row (Business plans, Teams Phone add-on, Teams Rooms add-on). Plan cards below the fold use "Buy now" (`a.btn.btn--sm`, 36px, same purple) and an outlined "Try for free". Buy now was not clicked.

## Download and free

[download-light-default.png](screenshots/download-light-default.png) leads with "Download Microsoft Teams for Mac" and a purple download button. [free-light-default.png](screenshots/free-light-default.png) leads with "Connect with anyone in Teams for free" and a stock photo of a meeting. That photo is a marketing image, not a signed-in capture.

## Footer

The Microsoft footer is `#f2f2f2` with `#616161` text at 11px. It is the shared microsoft.com footer, not Teams product chrome.
