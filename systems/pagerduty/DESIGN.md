# PagerDuty

Public marketing capture, 2026-11-22. Values below were read from the homepage with `getComputedStyle`. Take them from [tokens.json](tokens.json). This file was written by hand because catalog.json was left alone, so `make design-md` was not run.

## Colors

| Role | Value | Source |
|---|---|---|
| page | #fafafa | `--background`, body background |
| text | #1d1d1d | `--foreground`, body colour |
| text strong | #171717 | `--color-text-primary-light` |
| muted surface | #f5f5f5 | `--color-gray-100` |
| border | #e5e5e5 | `--color-gray-200` |
| hero | #0a0a0a | `--color-gray-950`. The homepage hero is a dark green photograph, not this flat colour |
| accent | #048a24 | `--color-green-600`. Start for Free computed `rgb(4, 138, 36)` |
| accent pressed | #005a24 | `--color-green-dark`. Declared. Not photographed |
| accent wash | #e6f3ea | `--color-green-xlight` |
| accent text | #ffffff | Start for Free text |
| link | #048a24 | Header Products label and green text links |
| focus | not captured | Not measured |

## Typography

The homepage h1 is plainFont, 60px, weight 300, line-height 75px, white on the hero. Body is plainFont, 16px, `#1d1d1d`. plainFont is proprietary and is not in this package.

## Do and don't

See [README.md](README.md). One green pill. Log In is an outlined pill. The hero is a dark campaign, not a product screenshot.
