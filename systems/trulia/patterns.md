# Trulia patterns

Signed-out homepage only, https://www.trulia.com/, 2026-11-19. CSS viewport 1169 by 731 at device pixel ratio 2. No screenshots.

## Marketing home

A fixed header sits over the page: wordmark, Buy and Rent navigation, Mortgage, Saved Homes, Saved Searches, and a bordered Sign up or Log in button. Header height is 64px.

The hero is a photograph with a white headline ("Discover a place you'll love to live"), a Buy / Rent / Sold tab group (Buy selected, white chip on the photo), and a 60px search combobox. The search placeholder asks for city, neighborhood, zip, county, or school. Nothing was typed.

Below the hero, a display heading ("Explore homes on Trulia") introduces city cards. Each card is a photo with a white title and "View Homes". Resident quotes sit on those cards. They are published marketing copy, not an account.

A later band, "See how Trulia can help", repeats three primary buttons: Find a home, Find a rental, Learn more. Each is a 42px tarzana-700 pill-less rectangle with 8px radius.

The footer is caption-sized link columns (Popular Searches, Popular Rental Searches, Explore Trulia, For Professionals) plus a 10px legal line. Trulia is named as a trademark of Zillow, Inc.

## What was not opened

Listing results, a listing detail, a neighborhood page, mortgage tools, saved homes, and the sign-in dialog. Navigating to a city page tripped PerimeterX ("Press & Hold to confirm you are a human"). The homepage reload then failed the same way. Those patterns are gaps, recorded in [components.md](components.md).

## Theme and width

The page painted light while `prefers-color-scheme: dark` matched. No theme control was in the header. Phone width (390) was not captured. The measured width is 1169, the preview tab's fill size, not a requested 1440.
