# Literal.club patterns

How the public signed-out pages fit together. Screenshots are 256-colour. Take colours from [tokens.json](tokens.json).

## App shell

The header is a full-width bar, 80px tall on desktop and 60px on the phone. The wordmark sits on the left with a hairline on its right edge (`light.ui.outline`). Explore, Sign in, and Join stay in the bar at 390px. There is no hamburger. Search is a wide field on desktop and a compact field on the phone.

Join is the green fill (`light.accent.primary` `#278458` in light, `dark.accent.primary` `#33bb7a` in dark). Sign in is discreet text. See [home-light-default](screenshots/home-light-default.png) and [mobile-home-light-default](screenshots/mobile-home-light-default.png).

The footer repeats Press, Legal, Privacy, Terms, the social marks, Become a supporter, Guides, API, Contact, the iPhone app, and Changelog. See [home-light-full](screenshots/home-light-full.png).

## Home

A serif hero, "Discover, organise & discuss books", sits in Libre Baskerville at 40px (`core.typography.hero`). Under it, Join for free uses the same green as the header Join. The App Store badge is a black chip. Book rows and reader rows follow. See [home-light-default](screenshots/home-light-default.png) and [home-dark-default](screenshots/home-dark-default.png).

Search focus paints the field without submitting. See [home-light-search-focused](screenshots/home-light-search-focused.png).

## Explore and a book

Explore is a grid of book cards. A card is about 467 x 284 in the desktop measure. See [explore-light-default](screenshots/explore-light-default.png).

A public book page leads with the serif title (`core.typography.book-title`), a black Want to read control, and the description. Show more expands the blurb in place. Like and Comment sit on a review and were not activated. See [book-light-default](screenshots/book-light-default.png) and [book-light-show-more](screenshots/book-light-show-more.png).

## A public profile

A profile that loads signed out shows the avatar (130px, radius 40%), the name, a green Follow button, and Books, Reviews, and Goals tabs. Follow was not activated. See [profile-light-default](screenshots/profile-light-default.png).

## Sign in and register

The card is a left-aligned serif heading ("Sign in", 24px), an email field, a password field, Forgot password?, a green submit, Sign in with Apple, and a sign-up link. Nothing was typed and nothing was submitted. Register is the same card with Join copy. See [signin-light-default](screenshots/signin-light-default.png) and [register-light-default](screenshots/register-light-default.png).

## Marketing pages

Press, legal, privacy, terms, supporter, guides, developers, contact, the iPhone app, changelog, the tracker pitch, the club pitch, about, and the Goodreads import pitch are public. The developers page is a long document. Import offers Start importing and Create a free account. Those were not followed. See [developers-light-default](screenshots/developers-light-default.png) and [import-light-default](screenshots/import-light-default.png).

## Dark

The same pages resolve `:root.dark` when the browser prefers dark. Text becomes `#f9f9f9`, the page becomes near-black, and the green becomes `#33bb7a` with black label text. Hover, active, and disabled greens are not redeclared in the dark block, so they stay the light values. See [home-dark-default](screenshots/home-dark-default.png) and [signin-dark-default](screenshots/signin-dark-default.png).

## Not on this surface

The library, writing a review, clubs, goals, messages, and the account after sign-in need an account. Checkout on the supporter page was not followed. Search results were not loaded, because that would submit the search form.
