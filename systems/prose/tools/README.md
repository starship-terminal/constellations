# Tools

This folder began as a copy of the shared capture kit, and this file was the kit's guide. That
guide described routes and builders written for other products, which this package never used.

Any file here that is still an unchanged copy of a kit example records that other product, not
this one, and was never adapted: for example a `capture/signed-in/` route written for Claude, a
`build_components_md.py` written for ChatGPT, a `build_components_md.public.py` or
`capture/public/` route written for Gauth, or a `native/` builder written for Grok Bot. The 2026-11
audit deletes the unused copies in separate changes, so some may still be here. Do not run one
against this product before adapting it.

The package's own builders and tests are the files its [README](../README.md) names in its rebuild
steps; that README also says how the values were read. The kit and its guide live at
[tools/kit/](../../../tools/kit/README.md) in the repository root.
