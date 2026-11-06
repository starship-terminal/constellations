// Screenshot a snapshot written by unsnap.py: node render.mjs <dir> <label> [full] [light]
// 'full' unrolls the fixed layout and its inner scroller so the whole page is captured.
// 'light' removes the `dark` class from <html> before the screenshot and writes
// <label-with-dark-swapped-for-light>.png: Manus paints its light palette from :root and its dark
// one from `.dark`, with every component colour a var() of those, so the same static copy
// renders both themes and no account setting is touched.
import fs from 'fs';
import path from 'path';
const [,, dirArg, label, ...flags] = process.argv;
const dir = path.resolve(dirArg); // file:// needs an absolute path, so a relative <dir> is resolved first
// lib.mjs keys its CDN cache off SNAPS (default <SNAPS>/../cdn-cache), so point it at this snapshot dir.
process.env.SNAPS ??= dir;
const { chromium, newContext } = await import('./lib.mjs');
const meta = JSON.parse(fs.readFileSync(`${dir}/${label}.json`));
const light = flags.includes('light');
const out = light ? label.replace(/-dark(?=-|$)/, '-light') : label;
const b = await chromium.launch();
// The same context measure.mjs uses: CDN responses served from the local cache, anything else (manus.im
// favicons, canonical links) aborted, so a flaky stylesheet fetch cannot leave the screenshot unstyled.
const ctx = await newContext(b, meta, light);
const p = await ctx.newPage();
for (let attempt = 0; ; attempt++) {
  await p.goto('file://' + dir + '/' + label + '.html', { waitUntil: 'load', timeout: 60000 });
  await p.waitForTimeout(2500);
  // Manus's shell is a 100vh flex box: a document taller than twice the viewport usually means a sheet did
  // not apply, so reload (as lib.mjs's openSnap does). A page that is long by design is still rendered.
  if (await p.evaluate(() => document.documentElement.scrollHeight <= innerHeight * 2 && document.styleSheets.length >= 10)) break;
  if (attempt === 2) { console.error(`warning: ${label} may not have come up styled; check the PNG`); break; }
}
if (light) { await p.evaluate(() => document.documentElement.classList.remove('dark')); await p.waitForTimeout(600); }
if (meta.scrollY) await p.evaluate(y => scrollTo(0, y), meta.scrollY);
// Restore inner scrollers: from meta.scrolls when the snapshot recorded them, else from a
// `scroll=<top>` flag (`scroll=max` for the bottom) applied to the tallest scroller outside <nav>.
const scrollFlag = flags.find(f => f.startsWith('scroll='));
await p.evaluate(({ scrolls, flag }) => {
  if (scrolls && scrolls.length) {
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
await p.screenshot({ path: `${dir}/${out}.png` });
if (flags.includes('full')) { await p.evaluate(() => { scrollTo(0, 0); const sc = [...document.querySelectorAll('*')].filter(e => /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20); for (const e of sc) { let n = e; while (n && n !== document.documentElement) { n.style.setProperty('height', 'auto', 'important'); n.style.setProperty('max-height', 'none', 'important'); n.style.setProperty('overflow', 'visible', 'important'); if (getComputedStyle(n).position === 'fixed') n.style.setProperty('position', 'relative', 'important'); n = n.parentElement; } } }); await p.waitForTimeout(500); await p.screenshot({ path: `${dir}/${out}-full.png`, fullPage: true }); }
await b.close(); console.log('rendered', out);
