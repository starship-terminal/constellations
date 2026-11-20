# LinkedIn patterns

How the components in [components.md](components.md) combine on the public signed-out pages. Every value is in [tokens.json](tokens.json). Crops are in [components/crops/](components/crops). Page captures are in [screenshots/](screenshots).

## The guest nav

The home, company, and profile pages share an 80px white header (`core.size.nav`). The wordmark sits at the left in `#0a66c2`. Five icon links (Top Content, People, Learning, Jobs, Games) sit in the middle at about 64-80px wide and 52px tall, in `rgba(0, 0, 0, 0.6)`. A hairline divider separates them from two pills: Sign in, a transparent 48px pill with a 1px brand ring, and Join now, a filled `#0a66c2` 48px pill with a white label and a 24px radius. Both are sign-in destinations. At 390px the same pills wrap under the wordmark.

See [home-light-default](screenshots/home-light-default.png) and [nav-join](components/crops/nav-join-default.png).

## The guest home

The hero is a white band. The heading "Welcome to your professional community" is 48px, weight 400, `rgba(0, 0, 0, 0.9)`, wrapping to about 572 x 120. Under it: a filled Continue with Google pill, an outline Sign in with email pill, a legal line, and a Join now text link. An illustration sits to the right.

Below that, a `#f3f2f0` canvas band holds "Explore top LinkedIn content" and topic chips (Career, Productivity, Finance) at 32px on the page and, when the measure pass centred one, a 48px pill. A later band, "Find the right job or internship for you", repeats the chip shape for job categories.

The footer is a thin legal strip: LinkedIn Corporation, User Agreement, Privacy Policy, and the rest, about 50px tall.

## Jobs search

`/jobs/search/` with the public tracking parameter stays on the results page. Without it, the same path bounced to the guest home on this capture. The viewport opens on filter chips (Date posted, Company, Easy Apply, Under 10 applicants), a results heading ("11,000+ Designer Jobs in United States" at 24px), a list of job cards about 504 x 133, and a detail pane with a 48px Apply pill and a Save outline pill. Apply was measured, never followed. The keyword field was not painted in the results header this pass.

See [jobs-light-default](screenshots/jobs-light-default.png) and [apply-cta](components/crops/apply-cta-default.png).

## Company page

`/company/linkedin` loads signed out. The top card shows the name at 36px, the industry, Sunnyvale, CA, a follower count, a 48px See jobs pill, and a 48px Follow pill. Follow is a sign-in destination. Tabs (Overview, Jobs, Life, About us) sit under the card. The About us tab did not measure as a 32-64px control this pass, so it is not in the component list.

See [company-light-default](screenshots/company-light-default.png).

## Public profile

`/in/reidhoffman` loads signed out as a published profile. The name is 36px. The headline wraps under it. A 128px avatar sits beside the name. Join to view profile is a 48px brand pill. Message is a 48px outline pill. Both are sign-in destinations and were not followed.

See [profile-light-default](screenshots/profile-light-default.png).

## Sign-in wall

`/login` is a centred card on white: a Sign in heading, Continue with Google, Sign in with Apple, an email field and a password field at 400 x 48, and a 400 x 48 brand submit pill. The page itself checked "Keep me signed in". Nothing was typed or submitted.

See [signin-light-default](screenshots/signin-light-default.png).

## Mobile

At 390px the guest home wraps Sign in and Join now onto a second row. The heading wraps to about 358px wide. The jobs search keeps the filter chips and the two-pane results, squeezed. The company page keeps the name and the two pills.

See [mobile-home-light-default](screenshots/mobile-home-light-default.png).
