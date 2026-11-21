# Coolors patterns

How the public screens combine the components in [components.md](components.md). Signed out. The map of which control opens which page is [site-tree.md](site-tree.md).

## App header

A 60px white bar. The wordmark sits left and links home. Tools opens the mega-menu. Go Pro is a pink text button (the modal was not opened). Sign in opens the access overlay. Sign up was not opened.

## Homepage

A 110px Inter headline, a short subtitle, then Start the Generator (primary) and Explore 10M+ Palettes (gray). Palette art sits to the right. Tool cards and a color-of-the-day card follow. A logo strip sits under the hero.

## Palette generator

Start the Generator opens `/generate`, which redirects to a palette URL. This pass landed on `/4f7cac-c0e0de-162521-3c474b-9eefe5`. Five columns fill the page under a toolbar (View, Export, Save, and icon tools). The hint is "Press the spacebar to generate color palettes!" A tutorial modal ("Let's go!") was closed, not continued. Save and Export were not used.

## Explore

Explore 10M+ Palettes opens `/palettes`, which redirects to `/palettes/trending` ("Trending Color Palettes"). A search field is on the page. Nothing was typed or submitted.

## Contrast checker

`/contrast-checker` redirects to a pair URL. This pass was `/contrast-checker/112a46-acc8e5`. The offline render shows `#FFFFFF` in the inputs because the swatch images did not load. That pair is not the live pair.

## What was not opened

Sign up, Continue with Google, Continue with Apple, Continue with email, Go Pro checkout, Save, Export, the mobile menu, dark theme, and the account wall at `/account/affiliation`.
