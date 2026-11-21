# Lyft public site tree

Mapped from https://www.lyft.com/ on 2026-11-21, signed out, before the screenshot pass. The request returned 200. The page title was "Ride or drive with Lyft". This is a live rider and driver marketing site, not a parked domain.

There is no theme switch. `color-scheme` on the root was `normal`. No email was typed. No phone number was typed. No password was typed. No form was submitted. No identity provider was clicked. No ride was requested. No checkout was started.

The header "Sign up" control is an app deep link (`lyft.sng.link`). It was not opened. The header "Get a ride" control is the same kind of app deep link. It was not opened.

## Consent banner

A banner sits over the page. It is not a page.

| Control | What it does | Stop? |
|---|---|---|
| Privacy Policy | Opens https://www.lyft.com/privacy in a new tab | |
| close banner | Dismisses the tracking notice | Not clicked. The banner was hidden in screenshots so it would not cover the page |

The help center shows the same notice as a corner toast, plus a region dialog. Both were hidden for the help screenshot. "Select region" was not pressed.

## Header

The wordmark and six items sit in the top bar. Rider, Driver, and Business are links, not flyouts. Hovering Driver did not open a menu.

| Control | Opens | Stop? |
|---|---|---|
| Lyft (wordmark) | `/` | |
| Get a ride | App deep link on `lyft.sng.link` | Stop. Not opened |
| Rider | `/rider` | |
| Driver | `/driver` | |
| Business | `/business` | |
| Log in | `/login`, which redirects to `https://account.lyft.com/auth` | Stop. Empty phone wall only |
| Sign up | App deep link on `lyft.sng.link` | Stop. Not opened |
| EN | Language control. The click did not open a menu on this visit | |

On a 390-wide viewport the nav collapses. "Open mobile navigation menu" opens a drawer. "Close mobile navigation menu" closes it.

## Mobile drawer

| Control | Opens | Stop? |
|---|---|---|
| Log in | `https://www.lyft.com/login` | Stop |
| Rider | Section label in the drawer. The rider links sit under it | |
| Cities | `/rider/cities` | |
| Business rides | `/rider/business` | |
| Help | `https://www.lyft.com/click/pax-help-center` | |
| Sign up to ride | App deep link | Stop. Not opened |
| Driver | Section label | |
| Earnings | `/driver/pay` | |
| Cities | `/driver/cities` | |
| Help | `https://www.lyft.com/click/dax-help-center` | |
| Apply to drive | `/drive-with-lyft` | Stop at the empty phone field |
| Business | `/business` | |
| Log in | `/login` | Stop |

## Homepage sections

| Control | Opens | Stop? |
|---|---|---|
| Sign up to ride | App deep link | Stop |
| Learn more about earnings | `/driver/earnings` | |
| Learn more about riding with Lyft | `/rider` | |
| Try 1 month free | App deep link to membership sales | Stop |
| Get started today | `/business` | |
| Explore solutions | `/business/solutions` | |
| Learn more (safety) | `/safety` | |
| Community guidelines | `/safety/community-guidelines` | |
| Learn more about our Lyft Up programs | `/lyftup/programs` | |
| Wait & Save, Standard, Priority Pickup, XL | Expand a ride-type card on the same page. Standard shows "Request Standard" | Stop. Request was not clicked |
| Previous slide, Next slide | Move the ride-type carousel | |

## Footer

| Group | Items |
|---|---|
| Driver | Become a Driver (`/drive-with-lyft`), New Driver Guide, Earnings, Cities, Help, Safety, Application Requirements, Express Drive, Bonus, Lyft Rewards, Insurance, Black Car Fleets, Driver Blog, Beta Program |
| Rider | Sign up to ride (`/rider`), Lyft Go, Cities, Help, Safety, Business Profile, Rewards, Events, Airports, Gift Cards, Donate |
| Lyft | Careers, Lyft Up, Business, Healthcare, Bikes, Scooters, Autonomous, Lyft Ads (`https://ads.lyft.com`), Venue Partnerships, Developers, Lyft Blog, Press, Investor Relations (`https://investor.lyft.com`) |
| Apps | Lyft driver app (`/app?type=driver`), Lyft rider app (app deep link, not opened) |
| Social | X, Facebook, Instagram. Off-site. Not opened |
| Legal | Terms, Privacy, Accessibility Statement, Your Privacy Choices |

## Login wall

`/login` redirects to `https://account.lyft.com/auth`. The page title is "Log in". The form is empty.

| Control | What it is | Stop? |
|---|---|---|
| EN | Language chip | Not opened |
| Phone number | Empty text field, placeholder "Phone number" | Focused only. Nothing typed |
| Keep me signed in | Unchecked checkbox | Not changed |
| Continue with Phone | Submit | Not clicked |
| Find your account | Link under the button | Not clicked |

## Driver apply wall

`/drive-with-lyft` stays on `www.lyft.com`. Title: "Drive with Lyft – Become a Driver". The phone field is empty.

| Control | What it is | Stop? |
|---|---|---|
| Mobile Phone Number | Empty field | Nothing typed |
| Submit | Submits the application start | Not clicked |
| Log in | Link for an existing driver | Not clicked |

## Help

`https://help.lyft.com/hc/en-us` returned 200. Title: "Lyft Help".

| Control | Opens | Stop? |
|---|---|---|
| Search keywords or questions | Search field. Not submitted | |
| Select region | Region dialog | Not pressed |
| Stay on US site | Dismisses the region dialog | Not pressed. Dialog was hidden for the shot |
| Log in (get help faster) | Signed-in help | Stop. Not clicked |
| Popular articles | Public help articles | Not opened in this pass |
| Driving with Lyft, Riding with Lyft, Applying to drive | Help categories | Not opened in this pass |
