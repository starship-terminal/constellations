# Screenshots

No PNG was saved.

`preview_snapshot` on the attached tab returned: "The browser is not producing
screenshot frames." The page itself had loaded (`document.readyState` was
`complete`, no Cloudflare challenge). Values in `raw/computed.json` were read
with `preview_evaluate` from that same tab. Inventing a screenshot would
misreport the capture, so this folder stays empty of images.
