// PRODUCT (Superset): what the theme engine writes. Superset's theme object carries `ui`, which
// applyUIColors() writes as inline custom properties on <html> (overriding the stylesheet's :root
// fallbacks), and `terminal`, handed to xterm.js, which paints on a canvas, so no CSS holds it. The
// renderer mirrors the active theme's terminal colours into localStorage as `theme-terminal`. This
// reads both: the inline declarations as written, and the terminal palette, with the theme's id.
//
//   PORT=9404 node tools/capture/electron/theme.mjs raw/theme.<theme>.json
import { connect, disconnect, writeJson } from './cdp.mjs';
import { WINDOWS } from './product.mjs';

const out = process.argv[2];
if (!out) { console.error('usage: theme.mjs <out.json>'); process.exit(2); }
const { browser, page } = await connect(WINDOWS.main);
const data = await page.evaluate(() => ({
  themeId: localStorage.getItem('theme-id'),
  themeType: localStorage.getItem('theme-type'),
  terminal: JSON.parse(localStorage.getItem('theme-terminal') || '{}'),
  htmlClass: document.documentElement.className,
  inline: Object.fromEntries([...document.documentElement.style].filter(n => n.startsWith('--'))
    .map(n => [n, document.documentElement.style.getPropertyValue(n).trim()])),
}));
writeJson(out, { meta: { read: new Date().toISOString().slice(0, 10), source: "the inline style of <html> and localStorage['theme-terminal'] in the Superset window" }, ...data });
console.log(out, data.themeId, Object.keys(data.inline).length, 'inline properties', Object.keys(data.terminal).length, 'terminal colours');
await disconnect(browser);
