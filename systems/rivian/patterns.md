# Rivian patterns

Public marketing on rivian.com. Signed out. No vehicle was configured, reserved, or booked. No account was created.

## Shell

A 56px white header, radius 12px, with a 0.5px stone border and `--shadow-nav` (`0 2px 8px rgba(0,0,0,.15)`). Wordmark at the left. Center links: Vehicles, Charging, Technology, Discover, Gear Shop. Demo drive is the yellow pill at the right, then chat and account icons.

![Home](screenshots/home-light-default.png)

At 390px the center links collapse to a menu icon. The wordmark and chat stay. The yellow Demo drive pill is not in the phone header.

![Home, 390](screenshots/home-light-mobile.png)

## Home

A full-bleed photograph. White type sits on the image. The measured h1 "Find your Rivian" is 72px / 600. The visible hero line in the viewport shot is "R2 is the 2027 MotorTrend SUV of the Year", 56px / 600, white. Two pills sit on the photo: white Design yours and an outlined Book a drive. A yellow chat button sits at the bottom right of every page. It was not opened.

## Vehicles menu

Vehicles opens a panel over the hero. Three cards name R1S, R1T, and R2 with a starting price, a black Design yours pill, and an underlined Explore link. A text list to the right covers compare, demo drive, trade-in, offers, inventory, pre-owned, purchasing, financing, insurance, R3, and fleet. None of those links were followed into a builder or a checkout.

![Vehicles](screenshots/home-light-menu.png)

## R2

The R2 page opens on a grey field with a large photograph in a pill mask, black "R" and "2", and three controls: black Reserve, yellow Design yours, and a pause icon. Reserve points at `/configurations/reserve/r2`. Design yours points at `/configurations/builder/r2`. Neither was opened. Further down, Standard, Premium, and Performance are pills. The footer is black.

![R2](screenshots/r2-light-default.png)

## Charging

The first paint is a loader: a 96px headline, "Charging is easier than you think", and a green bolt on a grey track. Route fields and an email field exist in the DOM below that paint. No address was typed and no email was submitted.

![Charging](screenshots/charging-light-default.png)

## Support

A photograph with a white 88px / 500 headline, "Welcome to Support Center", and a white search field, "How can we help?". No search was run.

![Support](screenshots/support-light-default.png)

## Legal

General Terms is a grey page, black headline, underlined section links. No form.

![General Terms](screenshots/legal-light-default.png)

## Sign in

A split page: a photograph on the left, a white form on the right. Email, password, a remember checkbox, and a black Sign in pill. The page says it is protected by reCAPTCHA Enterprise. Nothing was typed. Sign in was not clicked. No account was created.

![Sign in](screenshots/login-light-default.png)
