# Opsgenie

Public marketing capture, 2026-11-22. Values below are the declared colours in the public light stylesheet linked from the Opsgenie migration page. Take them from [tokens.json](tokens.json). This file was written by hand because catalog.json was left alone, so `make design-md` was not run.

## Colors

| Role | Value | Source |
|---|---|---|
| page | #ffffff | `--ds-surface` |
| hero text | #292a2e | measured migration h1 |
| text | #292a2e | `--ds-text` |
| muted | #505258 | `--ds-text-subtle` |
| disabled | #080f214a | `--ds-text-disabled` |
| accent | #1868db | `--ds-background-brand-bold` |
| accent hover | #1558bc | `--ds-background-brand-bold-hovered` |
| accent pressed | #144794 | `--ds-background-brand-bold-pressed` |
| accent text | #ffffff | `--ds-text-inverse` |
| link | #1868db | `--ds-link` |
| border | #0b120e24 | `--ds-border` |
| focus | #4688ec | `--ds-border-focused` |
| danger | #c9372c | `--ds-background-danger-bold` |
| warning | #fbc828 | `--ds-background-warning-bold` |
| success | #5b7f24 | `--ds-background-success-bold` |

## Type

The migration h1 is Charlie Display, 48px, weight 800, line height 56px. Plan your migration is Charlie Text, 20px, weight 500. Declared AtlasKit heading roles use Atlassian Sans. Both families are proprietary and are not in this package.
