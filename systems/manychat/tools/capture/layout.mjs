// This public capture has no signed-in page copies, so there is no layout.json
// to write. The signed-in kit script is not shipped with this package.
console.error('layout.mjs reads signed-in snapshots. This capture has none, so there is no layout.json to write.');
process.exit(2);
