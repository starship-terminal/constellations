// Screenshot a snapshot written by unsnap.py: node render.mjs <dir> <label> [full] [scroll=<px|max>]
// 'full' also takes a whole-page shot. Duolingo copies keep the theme they were taken in (the
// palette triplets sit in <html style>, and the account theme follows the system colour scheme,
// so the light and dark copies were taken by switching the browser's colour scheme, not the
// account), so each copy renders once, as captured.
import fs from 'fs';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const { routeCdn, FONTS } = await import('./lib.mjs');
const [,, dir, label, ...flags] = process.argv;
const meta = JSON.parse(fs.readFileSync(`${dir}/${label}.json`));
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2, colorScheme: /-light(?=-|$)/.test(label) ? 'light' : 'dark' });
await routeCdn(ctx);
const p = await ctx.newPage();
await p.goto('file://' + dir + '/' + label + '.html', { waitUntil: 'load', timeout: 60000 });
await p.addStyleTag({ content: FONTS });
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(2000);
if (meta.scrollY) await p.evaluate(y => scrollTo(0, y), meta.scrollY);
const scrollFlag = flags.find(f => f.startsWith('scroll='));
await p.evaluate(({ flag }) => {
  const marked = document.querySelectorAll('[data-snap-scroll]');
  if (marked.length && !flag) {
    marked.forEach((n) => { const [t, l] = n.getAttribute('data-snap-scroll').split(',').map(Number); n.scrollTop = t; n.scrollLeft = l; });
  } else if (flag) {
    const all = [...document.querySelectorAll('*')].filter(e => /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20);
    const sc = all.sort((a, b) => b.scrollHeight - a.scrollHeight)[0];
    if (sc) sc.scrollTop = flag === 'max' ? sc.scrollHeight : Number(flag);
  }
}, { flag: scrollFlag && scrollFlag.slice(7) });
await p.waitForTimeout(500);
await p.screenshot({ path: `${dir}/${label}.png` });
if (flags.includes('full')) { await p.screenshot({ path: `${dir}/${label}-full.png`, fullPage: true }); }
await b.close(); console.log('rendered', label);
