import { closePromo, clearChallenge, patch, chromium, UA, UA_MOBILE, BASE } from './lib.mjs';
const b = await chromium.launch();
for (const mob of [false, true]) {
  const ctx = await b.newContext(mob
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
  if (!(await clearChallenge(p))) { console.log('BLOCKED', mob); await ctx.close(); continue; }
  await p.waitForTimeout(9000);
  await closePromo(p);
  const els = await p.evaluate((mob) => {
    const out = [];
    const xmax = mob ? 330 : 1330;
    document.querySelectorAll('*').forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.height > 0 && r.height < 64 && r.top >= 0 && r.top < 80 && r.left >= xmax && r.width < 60) {
        const cs = getComputedStyle(el);
        if (cs.pointerEvents !== 'none') out.push({ tag: el.tagName, cls: (el.className.baseVal ?? el.className + '').slice(0, 70), txt: (el.innerText || '').trim().slice(0, 20), x: Math.round(r.left), w: Math.round(r.width), cur: cs.cursor });
      }
    });
    return out.slice(0, 25);
  }, mob);
  console.log('=== ' + (mob ? 'mobile' : 'desktop'));
  for (const e of els) console.log(' ', JSON.stringify(e));
  await ctx.close();
}
await b.close();
