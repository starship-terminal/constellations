// Screenshot a snapshot written by unsnap.py: node render.mjs <dir> <label> [full] [light]
// 'full' unrolls the fixed layout and its inner scroller so the whole page is captured.
// Linear copies keep the theme they were taken in (the palette is a script-generated constructed
// stylesheet), so each copy renders once, as captured; there is no 'light' flag.
import fs from 'fs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const [,, dir, label, ...flags] = process.argv;
const meta = JSON.parse(fs.readFileSync(`${dir}/${label}.json`));
// PRODUCT (adapt): Linear has no in-copy theme switch.
const light = false;
const out = label;
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2, colorScheme: /-light(?=-|$)/.test(label) ? 'light' : 'dark' });
const { routeCdn } = await import('./lib.mjs');
await routeCdn(ctx);
const p = await ctx.newPage();
await p.goto('file://' + dir + '/' + label + '.html', { waitUntil: 'load', timeout: 60000 });
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
await p.screenshot({ path: `${dir}/${out}.png` });
if (flags.includes('full')) { await p.evaluate(() => { scrollTo(0, 0); const sc = [...document.querySelectorAll('*')].filter(e => /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20); for (const e of sc) { let n = e; while (n && n !== document.documentElement) { n.style.setProperty('height', 'auto', 'important'); n.style.setProperty('max-height', 'none', 'important'); n.style.setProperty('overflow', 'visible', 'important'); if (getComputedStyle(n).position === 'fixed') n.style.setProperty('position', 'relative', 'important'); n = n.parentElement; } } }); await p.waitForTimeout(500); await p.screenshot({ path: `${dir}/${out}-full.png`, fullPage: true }); }
await b.close(); console.log('rendered', out);
