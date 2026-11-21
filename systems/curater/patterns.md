# Patterns

## App shell

Desktop keeps a fixed icon rail. The logo links to `/`. Home, Feed, and Taste Profile are links. Notifications, Profile, Create, and Settings are buttons. Settings sits at the bottom of the rail.

Phone drops the rail. The header holds the logo, Feed, Taste Profile, Search, and Menu.

See [screenshots/home-light-default.png](screenshots/home-light-default.png) and [screenshots/mobile-home-light-default.png](screenshots/mobile-home-light-default.png).

## Home digest

`/` and `/home` are the same trending digest: a title, a subtitle, the Google pill, then stacked curation summaries. Each summary links to a curation and a curator.

## Feed

`/feed` is a masonry of public curations. Featured and For You switch the list in place. More filters by subscription, contributor, or category. Search expands a field and does not navigate. Log in or sign up goes to `/auth/login`.

A category item sets `?categoryId=`. Contributors sets `?authors=contributors`. A tag chip sets `?tag=`.

## Login wall

The wall has two shapes.

The dialog stays on the current URL. It is what Notifications, Profile, Create, and Add to my taste open. It offers only Continue with Google.

The page is `/auth/login`. `/signin`, `/auth/callback`, and `/onboarding` redirect there. The page is a split: a sample curation on the left, "Sign in to Curater" and Continue with Google on the right. Privacy and Terms sit under the button.

See [screenshots/login-light-default.png](screenshots/login-light-default.png) and [screenshots/home-light-signin-dialog.png](screenshots/home-light-signin-dialog.png).

## Legal and about

Privacy, Terms, and About are long text pages inside the same shell. About links to the public curator profile and to an external social profile. The extension page explains the Chrome save flow and links to `/extension/chrome`, which leaves the site for the Chrome Web Store. That store button was not clicked.

## Profile and collection

A public handle such as `/glauber` is a curator page: a role chip, a TasteScope line, counts, and a grid. A collection such as `/collection/visual-identity` is a themed grid. Both are readable signed out.

## Taste

`/taste` redirects to `/taste/soon`. The page says TasteScope is active for curators and full access is coming soon. No form is on the page.
