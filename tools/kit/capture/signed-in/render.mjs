// Screenshot a snapshot written by unsnap.py: node render.mjs <dir> <label> [full] [light]
// 'full' unrolls the fixed layout and its inner scroller so the whole page is captured.
// 'light' removes the `dark` class from <html> before the screenshot and writes
// <label-with-dark-swapped-for-light>.png: Manus paints its light palette from :root and its dark
// one from `.dark`, with every component colour a var() of those, so the same static copy
// renders both themes and no account setting is touched.
// Every request goes through lib.mjs's routeCdn: the product's asset host is served from the local
// cache beside the copies, and anything else (the product itself, trackers) is aborted, as in measure.mjs.
// PRODUCT (adapt): name the product here once every part marked PRODUCT (adapt) is rewritten
// for it. While this is null the script stops: the kit's copy is Manus and Claude's example and would
// read or write Manus and Claude's values. KIT_EXAMPLE=1 runs the example as it is.
const ADAPTED_FOR = null;
if (!ADAPTED_FOR && !process.env.KIT_EXAMPLE) {
  console.error('render.mjs is the kit\'s Manus and Claude example, not adapted: rewrite the parts marked PRODUCT (adapt), then set ADAPTED_FOR');
  process.exit(2);
}
import fs from 'fs';
import path from 'path';
import { pathToFileURL } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
const [,, dirArg, label, ...flags] = process.argv;
if (!dirArg || !label) { console.error('usage: render.mjs <dir> <label> [full] [light] [scroll=<px>|max|auto]'); process.exit(2); }
// scroll= takes a pixel offset, max or auto; anything else (a selector:px pair) became Number('...'),
// NaN, and the scroller silently stayed at 0
const badScroll = flags.find((f) => f.startsWith('scroll=') && !/^scroll=(?:\d+(?:\.\d+)?|max|auto)$/.test(f));
if (badScroll) { console.error(`render.mjs: ${badScroll}: scroll= takes a pixel offset, max or auto`); process.exit(2); }
const dir = path.resolve(dirArg);               // a relative <dir> made a broken file:// URL
process.env.SNAPS ??= dir;                       // lib.mjs keys its CDN cache off SNAPS
const { chromium, routeCdn, setLight } = await import('./lib.mjs');
const meta = JSON.parse(fs.readFileSync(path.join(dir, `${label}.json`)));
// PRODUCT (adapt): the light switch is lib.mjs's setLight, which measure.mjs uses too, so a light
// render and a light reading of one copy are the same page.
const light = flags.includes('light');
if (light && !/-dark(?=-|$)/.test(label)) {
  console.error(`render.mjs: 'light' needs a copy taken in dark (a label containing -dark), got ${label}`);
  process.exit(1);
}
const out = light ? label.replace(/-dark(?=-|$)/, '-light') : label;
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2, colorScheme: light || !/-dark(?=-|$)/.test(label) ? 'light' : 'dark' });
await routeCdn(ctx);
const p = await ctx.newPage();
await p.goto(pathToFileURL(path.join(dir, label + '.html')).href, { waitUntil: 'load', timeout: 60000 });
// ChatGPT paints dark from a `dark` class on <html> (and on each message's markdown body), Claude from data-mode="dark" on <html> and on
// every design-system root (`.cds-root`, portals included); both paint light
// when that is taken away, so one copy renders both themes and no account setting changes.
if (light) await setLight(p);
await p.waitForTimeout(2500);
if (meta.scrollY) await p.evaluate(y => scrollTo(0, y), meta.scrollY);
// Restore inner scrollers: from the data-snap-scroll marks snapshot.js leaves on scrolled elements
// (or meta.scrolls for an older copy) unless a flag is given, else from a
// `scroll=<top>` flag (`scroll=max` for the bottom) applied to the tallest scroller outside <nav>.
const scrollFlag = flags.find(f => f.startsWith('scroll='));
await p.evaluate(({ scrolls, flag }) => {
  const marked = document.querySelectorAll('[data-snap-scroll]');
  if (marked.length && !flag) {
    marked.forEach((n) => { const [t, l] = n.getAttribute('data-snap-scroll').split(',').map(Number); n.scrollTop = t; n.scrollLeft = l; });
  } else if (scrolls && scrolls.length && !flag) {
    for (const s of scrolls) { let n = document.documentElement; for (const i of s.path) n = n && n.children[i]; if (n) { n.scrollTop = s.top; n.scrollLeft = s.left; } }
  } else if (flag) {
    const all = [...document.querySelectorAll('*')].filter(e => !e.closest('nav') && /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20);
    const sc = all.find(e => e.querySelector('.group\\/turn')) || all.sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
    // `scroll=auto` scrolls to the first turn the virtualised list had rendered at snapshot time.
    const turn = sc && sc.querySelector('.group\\/turn');
    if (sc && flag === 'auto' && turn) sc.scrollTop = turn.getBoundingClientRect().top - sc.getBoundingClientRect().top - 16;
    else if (sc) sc.scrollTop = flag === 'max' ? sc.scrollHeight : Number(flag);
  }
}, { scrolls: meta.scrolls, flag: scrollFlag && scrollFlag.slice(7) });
await p.waitForTimeout(500);
const requested = { viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2 };
await screenshotWithMetadata(p, { path: `${dir}/${out}.png` }, requested);
if (flags.includes('full')) { await p.evaluate(() => { scrollTo(0, 0); const sc = [...document.querySelectorAll('*')].filter(e => /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20); for (const e of sc) { let n = e; while (n && n !== document.documentElement) { n.style.setProperty('height', 'auto', 'important'); n.style.setProperty('max-height', 'none', 'important'); n.style.setProperty('overflow', 'visible', 'important'); if (getComputedStyle(n).position === 'fixed') n.style.setProperty('position', 'relative', 'important'); n = n.parentElement; } } }); await p.waitForTimeout(500); await screenshotWithMetadata(p, { path: `${dir}/${out}-full.png`, fullPage: true }, requested); }
await b.close(); console.log('rendered', out);
