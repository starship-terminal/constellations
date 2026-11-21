# YouTube public site tree

Mapped from https://www.youtube.com/ on 2026-11-21, signed out, in an incognito tab. The painted theme is dark (`html[dark]`). The region badge on the wordmark is SG. Nothing was typed into a field. No identity provider was clicked. No form was submitted. Like, dislike, subscribe, comment, share-send, and playlist-save were not used. A control that opens a sign-in wall is recorded and that branch stops.

YouTube has no separate signup route on youtube.com. Sign in and Create account both leave for accounts.google.com. Those walls were photographed empty and the branch stopped.

## Shell

The signed-out home is an app shell: a 56px masthead, a collapsed 72px guide, and an empty feed. The feed copy is "Try searching to get started". There is no public video grid until a search or an Explore destination.

| Control | Opens | Stop? |
|---|---|---|
| Guide | Drawer on the same page (see Guide) | |
| YouTube Home | `/` | |
| Search | Combobox. Submitting a query opens `/results` | query not typed in the map pass; one public results page was loaded by URL for capture |
| Search button | Same as submitting the combobox | |
| Search with your voice | Voice dialog: "To search by voice, go to your browser settings and allow access to microphone" | microphone not granted |
| Settings | Masthead menu (see Settings menu) | |
| Sign in | accounts.google.com ServiceLogin, "Sign in to continue to YouTube" | yes, login wall |
| Home | `/` | |
| Shorts | `/shorts/` then a public short (`/shorts/<id>`) | do not like, comment, share, or remix |
| Subscriptions | `/feed/subscriptions` | empty signed-out state; Sign in stops |
| You | `/feed/you` | empty library; Sign in stops |

## Guide

Guide opens a 240px drawer over a scrim. Escape or Guide again closes it. Show more expands Explore. Show less collapses it.

| Item | Opens | Stop? |
|---|---|---|
| Home | `/` | |
| Shorts | `/shorts/` | |
| Subscriptions | `/feed/subscriptions` | Sign in |
| You | `/feed/you` | Sign in |
| History | `/feed/history` | signed-out history wall; Sign in |
| Sign in (drawer prompt) | accounts.google.com | yes, login wall |
| Music | `/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ` | public topic channel |
| Movies | `/feed/storefront` | public storefront |
| Gaming | `/gaming` | public gaming shelf |
| Podcasts | `/podcasts` | public, behind Show more |
| Playables | `/playables` | public, behind Show more |
| Memberships | `/channel_memberships` | public marketing, behind Show more |
| Show more / Show less | Expands or folds Podcasts, Playables, Memberships | local |
| YouTube Premium | `/premium` | public marketing; Try / checkout not started |
| YouTube Music | `https://music.youtube.com/` | other product |
| YouTube Kids | `https://www.youtubekids.com/?source=youtube_web` | other product |
| YouTube Labs | `/labs` | public |
| Report history | `/reporthistory` | not followed into an account |
| About | `https://about.youtube/` | public marketing |
| Press | `https://www.youtube.com/about/press/` | public |
| Copyright | `https://www.youtube.com/about/copyright/` | public |
| Contact us | `/t/contact_us/` | form not submitted |
| Creators | `https://www.youtube.com/creators/` | public |
| Advertise | `https://www.youtube.com/ads/` | public |
| Developers | `https://developers.google.com/youtube` | other host |
| Terms | `/t/terms` | public |
| Privacy | `/t/privacy` | public |
| Policy & Safety | `https://www.youtube.com/about/policies/` | public |
| How YouTube works | `https://www.youtube.com/howyoutubeworks` | public |
| Test new features | `/new` | not opted in |

## Settings menu

The masthead Settings button opens a menu. Appearance was not switched. Location was opened and closed without choosing a country. Display language was opened and closed without choosing a language.

| Item | Opens | Stop? |
|---|---|---|
| Your data in YouTube | `https://myaccount.google.com/.../yourdata/youtube` | yes, Google account |
| Appearance: Device theme | Appearance submenu | not switched |
| Display language | Language list for this browser | not changed |
| Restricted Mode: Off | Restricted Mode submenu | not changed |
| Location | "Choose your location" list | not changed |
| Keyboard shortcuts | Dialog: Playback, General, and related sections | closed |
| Settings | `/account`, which redirects to the Google sign-in wall | yes, login wall |
| Help | YouTube Help | not followed |
| Send feedback | Feedback form | not submitted |

## Search

| Control | Opens | Stop? |
|---|---|---|
| Results page | `/results?search_query=…` | public video rows and an ad |
| Chips | All, Shorts, Unwatched, Videos, Recently uploaded, Live | local filters; not each applied |
| Filters | Dialog: Type, Duration, Upload date, Features, Prioritize | opened and cancelled; Apply not used |
| A video title | `/watch?v=` | public watch page |
| A channel name | `/@` or `/channel/` | public channel |

## Watch page

A public watch page loads signed out (`/watch?v=jNQXAC9IVRw`, "Me at the zoo", channel jawed). The player, title, subscribe, like, dislike, share, save, comments teaser, and related videos are on the page.

| Control | Opens | Stop? |
|---|---|---|
| Play / pause | Player | playback only |
| Like, Dislike | Sign-in prompt | not clicked |
| Subscribe | Sign-in prompt | not clicked |
| Share | Share dialog | not sent |
| Save to playlist | "Want to watch this again later? Sign in to add this video to a playlist." | yes, login wall |
| More actions | Menu: Save, Report | Report not submitted |
| Comments | Comment composer asks to sign in | not typed |
| Channel name | Public channel | |

## Empty signed-out states

| Page | What it shows | Stop? |
|---|---|---|
| `/` | "Try searching to get started" | |
| `/feed/subscriptions` | "Don't miss new videos. Sign in to see updates from your favorite YouTube channels" | Sign in |
| `/feed/you` | "Enjoy your favorite videos. Sign in to access videos that you've liked or saved" | Sign in |
| `/feed/history` | "Keep track of what you watch. Watch history isn't viewable when signed out." | Sign in |
| `/gaming` | A public shelf, plus a "This content isn't available, try again later" row | |

## Premium and about

| Page | What it shows | Stop? |
|---|---|---|
| `/premium` | Public plans (Individual, Family, Student). "Try 1 month" goes to accounts.google.com | checkout not started |
| `https://about.youtube/` | Public about page. Nav: How YouTube Works, Creators, Culture & Trends, Blog | |

## Auth walls

Photographed empty. Next was not clicked. Create account was opened only as a page, and its fields were left empty. Forgot email, identity providers, and Guest mode were not clicked.

| Control | Opens | What it shows |
|---|---|---|
| Sign in (masthead, guide, empty states, `/account`) | accounts.google.com `/v3/signin/identifier` | "Sign in to continue to YouTube". Email or phone, Forgot email, Next, Create account. |
| Create account | accounts.google.com `/lifecycle/steps/signup/name` | "Create a Google Account. Enter your name." First name and Last name empty. Next not clicked. |

## Phone

At 390px the same shell collapses. The guide becomes a bottom or drawer nav. Home and one inner page (a public watch page) were photographed at that width. Login was photographed at that width and left empty.

## Not entered

Signed-in library, subscriptions feed contents, history contents, Studio, purchases, membership checkout, comments, likes, playlists, and any Google account page past the empty identifier or name step. `login-extracted` stays `not-started`.
