// Screenshot an Electron desktop app's window and dump its CSS variables, live, over the
// app's remote-debugging port. The owner launches the app with the switch and signs in there:
//
//   osascript -e 'tell application "Linear" to quit'
//   open -a Linear --args --remote-debugging-port=9333
//   PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
//     node tools/kit/capture/electron/shot.mjs <out-dir> <name> [url-prefix] [--hover=<selector>]
//
// Writes <out-dir>/<name>.png at the window's own size and pixel ratio, and <out-dir>/<name>.vars.json
// (every custom property declared on :root, html or body, with its value as computed now, plus the
// theme class). A url() in a value is recorded as url(…) and a bare URL keeps no query.
// --hover forces :hover on the first match through CDP, so no pointer moves.
// Read-only: it never clicks or navigates.
// Quit the app and open it normally afterwards; an open port lets any local process drive it.
import { screenshotWithMetadata } from '../screenshot.mjs';
import { safeUrl } from '../safe-url.mjs';
import { noQuery, scrubQueries } from '../no-query.mjs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const [out, name, prefix = 'https://'] = process.argv.slice(2).filter(a => !a.startsWith('--'));
const hover = process.argv.find(a => a.startsWith('--hover='))?.slice(8);
const port = process.env.PORT || '9333';
if (!out || !name) { console.error('usage: shot.mjs <out-dir> <name> [url-prefix] [--hover=<selector>]'); process.exit(2); }

const browser = await pw.chromium.connectOverCDP(`http://127.0.0.1:${port}`);
const page = browser.contexts().flatMap(c => c.pages()).find(p => p.url().startsWith(prefix));
if (!page) { console.error(`no page starting with ${noQuery(prefix)}`); process.exit(1); }   // logs are committed: no query in them
let cdp, nodeId;
if (hover) {
  cdp = await page.context().newCDPSession(page);
  await cdp.send('DOM.enable'); await cdp.send('CSS.enable');
  const { root } = await cdp.send('DOM.getDocument');
  ({ nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: hover }));
  if (!nodeId) { console.error(`no element matches ${noQuery(hover)}`); process.exit(1); }
  await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['hover'] });
  await page.waitForTimeout(300);
}
await screenshotWithMetadata(page, { path: `${out}/${name}.png` });
const vars = await page.evaluate(() => {
  // Names come from the rules; values from the computed style, so only the rules that apply now
  // (the theme the screenshot shows) decide them.
  const names = new Set();
  for (const s of document.styleSheets) {
    let rules; try { rules = s.cssRules; } catch { continue; }
    for (const r of rules) if (r.selectorText && /^(:root|html|body)/.test(r.selectorText))
      for (const p of r.style) if (p.startsWith('--')) names.add(p);
  }
  // A custom property can hold a url() or a bare URL with a signed or per-account query (an
  // avatar, a token-bearing asset), so every value goes through noUrl here and noQuery (no-query.mjs) below.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const html = getComputedStyle(document.documentElement), body = getComputedStyle(document.body);
  // body's value wins whenever body declares one, a blank override included; trimmed only after
  const read = (n) => { const b = noUrl(body.getPropertyValue(n)); return (b !== '' ? b : noUrl(html.getPropertyValue(n))).trim(); };
  const v = {};
  for (const n of [...names].sort()) v[n] = read(n);
  return { url: location.href, themeClass: document.documentElement.className, dpr: devicePixelRatio,
           size: [innerWidth, innerHeight], vars: v };
});
if (hover) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] });
const { writeFileSync } = await import('node:fs');
vars.url = safeUrl(vars.url);
vars.vars = scrubQueries(vars.vars);   // a bare, scheme-relative or relative URL in a value keeps no query
writeFileSync(`${out}/${name}.vars.json`, JSON.stringify(vars, null, 1) + '\n');
console.log(`${out}/${name}.png`, Object.keys(vars.vars).length, 'variables');
await browser.close().catch(() => {});
