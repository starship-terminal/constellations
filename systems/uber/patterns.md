# Patterns

## Marketing header

Every captured desktop page opens with a 64px black bar. The wordmark sits left. Product pills (Ride, Earn, Travel, Business, Uber Eats, About) sit beside it. The right cluster is language, Help, Log in (dark pill), and Sign up (white pill).

Shown in [screenshots/ride-light-default.png](screenshots/ride-light-default.png), [screenshots/about-light-default.png](screenshots/about-light-default.png), [screenshots/business-light-default.png](screenshots/business-light-default.png), and [screenshots/drive-light-default.png](screenshots/drive-light-default.png).

## Ride request

The ride page is a two-column hero. Left: a 52px "Request a ride" headline, two grey location fields, date and time, and a black "See prices" button. Right: a map. A pale promo strip (`#eff4fe`) sits under the hero and links toward signup. The strip was not followed into a phone or payment form.

Shown in [screenshots/ride-light-default.png](screenshots/ride-light-default.png).

## Signup wall

`https://auth.uber.com/v2/` asks "What's your phone number or email?" then Continue, or Continue with Google, or Continue with Apple. Continue is the disabled fill until a value is present. The page says a verification code may arrive by text or WhatsApp. Nothing was typed. No screenshot: the preview browser was not producing screenshot frames, and a new headless session was not opened against the login page.

## Not-found

`/us/en/` and `/us/en/earn/` returned a 404 in this capture. The US earn URL renders the designed not-found page: 52px headline, black "Go to Uber's homepage" button, same black header. Shown in [screenshots/not-found-light-default.png](screenshots/not-found-light-default.png). A bare `https://www.uber.com/` redirect from this network landed on `/sg/en/` and 404ed. The US ride URL is the working home.
