# Patterns

Signed-out Yelp, 2026-11-19. Two screenshots exist. The other pages were measured in the preview tab and have no image, because the pane did not paint and headless Chromium was blocked on them.

## Marketing header

The about page and the homepage share one header. Left: the Yelp wordmark. Centre: a search field (what, where) with a red search button, radius 8px, shadow `0 0 18px rgba(0,0,0,0.16)`. Right: Yelp for Business, Write a Review, Start a Project, a gray Log In pill and a red Sign Up pill. Under that, category links: Restaurants, Home & Garden, Auto Services, Health & Beauty, Travel & Activities, More.

Shown in [about-light-default.png](screenshots/about-light-default.png).

## Search results

`/search?find_desc=coffee&find_loc=San+Francisco%2C+CA` is public while signed out. The header turns white. Sign in replaces the photo-header Log In. The title is Poppins 24px. Filters are pill chips (All, Price, Open Now, Reservations). Each result is a name, a rating made of 20px stars, a review count, a neighbourhood and an open-until line. The footer sits on `#F7F7F7`.

No screenshot. Computed styles are in [raw/components.json](raw/components.json).

## Business page

`/biz/kopê-house-san-francisco` is public. The name is a 48px white heading over a photo. Rating, category and hours sit under it. Write a review is the red pill. See hours is a white outline pill. Add photos, Share and Save are present. None of those was pressed.

## About

A full-bleed photo with a 60px white heading, then a row of illustrated cards (Careers, Newsroom, Investor Relations, Trust & Safety). Screenshot: [about-light-default.png](screenshots/about-light-default.png).

## Missing page

A made-up path returns "Page not found (404)". The heading is Poppins 28px. A search field sits in the header. The illustration is Yelp's artwork and is not redrawn. Screenshot: [notfound-light-default.png](screenshots/notfound-light-default.png).

## Login

`/login` is a separate, older page: gray page `#F5F5F5`, 300px fields, radius 3px, a `#D32323` Log In button, Continue with Apple, and a Sign up link. It asks for email and password. The signup pane also asks for first name, last name, city and ZIP. Nothing was typed or submitted.
