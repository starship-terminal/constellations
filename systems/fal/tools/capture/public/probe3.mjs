import { BASE, UA_MOBILE, launch, patch, open } from './lib.mjs';
const dump = (el) => {
  const r = el.getBoundingClientRect();
  const cls = String(el.className).split(' ').slice(0, 5).join(' ');
  return `${el.tagName.toLowerCase()}.${cls} ${r.width|0}x${r.height|0}@${r.x|0},${r.y|0} text=${JSON.stringify((el.innerText||'').slice(0,40))}`;
};
const { browser } = await launch();
const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, colorScheme: 'dark' });
await patch(ctx);
const page = await ctx.newPage();
await open(page, BASE + '/explore', { wait: 9000 });
await page.waitForTimeout(2500);
const ham = page.locator('button[aria-label*="navigation" i]').first();
await ham.click({ timeout: 5000, force: true }).catch(async () => { await ham.tap({ timeout: 4000 }).catch(()=>{}); });
await page.waitForTimeout(2000);
const nav = await page.evaluate((dumpSrc) => {
  const dump = eval(`(${dumpSrc})`);
  const drawers = [...document.querySelectorAll('[class*="vaul" i], [data-vaul-drawer-direction], [role="dialog"]')].map(dump);
  const drawer = document.querySelector('[data-vaul-drawer-direction]');
  const items = drawer ? [...drawer.querySelectorAll('*')].filter((e) => /^(Documentation|Pricing|Enterprise|Products|Model|Community|Blog|Status|Explore|Log-in|Sign-up|Menu|Browse)/.test((e.innerText||'').trim()) && e.children.length < 4).slice(0, 30).map((e) => dump(e) + ' tag=' + e.tagName + ' role=' + e.getAttribute('role')) : ['none'];
  return { drawers, items };
}, dump.toString());
console.log(JSON.stringify(nav, null, 1));
await ctx.close(); await browser.close();
