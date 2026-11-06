// Screenshot a snapshot written by unsnap.py: node render.mjs <dir> <label> [full]
// 'full' unrolls the fixed layout and its inner scroller so the whole page is captured.
import fs from 'fs';
import path from 'path';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const [,, dirArg, label, ...flags] = process.argv;
const dir = path.resolve(dirArg);   // a relative <dir> would make a broken file:// URL
const meta = JSON.parse(fs.readFileSync(`${dir}/${label}.json`));
const b = await chromium.launch();
const ctx = await b.newContext({ viewport: { width: meta.w, height: meta.h }, deviceScaleFactor: 2 });
// Offline like measure.mjs: only Google Fonts and the app's own static images load; every other
// request, a navigation or anything signed in, is aborted.
await ctx.route('**/*', (route) => {
  const req = route.request();
  const u = req.url();
  if (u.startsWith('file:') || u.startsWith('data:')) return route.continue();
  if (req.isNavigationRequest()) return route.abort();
  if (/^https:\/\/fonts\.(googleapis|gstatic)\.com\//.test(u)) return route.continue();
  if (req.resourceType() === 'image' && /^https:\/\/app\.researchrabbit\.ai\/assets\//.test(u)) return route.continue();
  return route.abort();
});
const p = await ctx.newPage();
await p.goto('file://' + dir + '/' + label + '.html', { waitUntil: 'load', timeout: 60000 });
await p.waitForTimeout(2500);
if (meta.scrollY) await p.evaluate(y => scrollTo(0, y), meta.scrollY);
await p.waitForTimeout(500);
await p.screenshot({ path: `${dir}/${label}.png` });
if (flags.includes('full')) { await p.evaluate(() => { scrollTo(0, 0); const sc = [...document.querySelectorAll('*')].filter(e => /(auto|scroll)/.test(getComputedStyle(e).overflowY) && e.scrollHeight > e.clientHeight + 20); for (const e of sc) { let n = e; while (n && n !== document.documentElement) { n.style.setProperty('height', 'auto', 'important'); n.style.setProperty('max-height', 'none', 'important'); n.style.setProperty('overflow', 'visible', 'important'); if (getComputedStyle(n).position === 'fixed') n.style.setProperty('position', 'relative', 'important'); n = n.parentElement; } } }); await p.waitForTimeout(500); await p.screenshot({ path: `${dir}/${label}-full.png`, fullPage: true }); }
await b.close(); console.log('rendered', label);
