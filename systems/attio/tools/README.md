# Supported Attio tools

- `build_tokens.py` reads the frozen scoped JSON measurements and generates tokens. Text comes from visible label nodes; geometry and chrome come from containers.
- `build_style_guide.py` renders those tokens.
- `build_images.py [source-directory]` verifies all accepted originals against their recorded SHA-256, decoded format and dimensions before writing screenshots or crops. Without an argument it rebuilds crops from the packaged screenshots. A changed original requires a new capture and explicit review/manifest update, not bypassing validation.
- `read-scoped.js` is a read-only browser function expression. Pass its text to the supported in-app browser `tab.playwright.evaluate` API while the intended Attio view is visibly loaded. Save the returned measurements outside git with the screenshot and decoded-image metadata. It does not navigate, authenticate, change settings or export page copies. Recheck frozen element indices and labels before adapting the token builder to a new capture.

There is no unattended recapture command. The unused starter-kit routes were removed because they target other products and were not used for this capture. Keep sign-in, account settings and capture acceptance under the library's documented workflow.
