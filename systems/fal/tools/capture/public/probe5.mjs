import { BASE, UA, launch, patch, open } from './lib.mjs';
const { browser } = await launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'light' });
await patch(ctx);
const p = await ctx.newPage();
await open(p, BASE + '/docs/documentation', { wait: 9000 });
await p.waitForTimeout(2500);
const h1 = p.locator('h1');
console.log('all h1 count', await h1.count());
const hv = h1.filter({ visible: true });
console.log('visible h1 count', await hv.count());
console.log('hasText+visible count', await h1.filter({ hasText: /build with fal|documentation/i }).filter({ visible: true }).count());
for (let i = 0; i < await h1.count(); i++) {
  const r = await h1.nth(i).evaluate((e) => { const b = e.getBoundingClientRect(); const cs = getComputedStyle(e); let anc = e.parentElement; const chain = []; while (anc && chain.length < 5) { chain.push(anc.tagName + '.' + String(anc.className).slice(0,40) + ':' + getComputedStyle(anc).display + ':' + getComputedStyle(anc).visibility); anc = anc.parentElement; } return { w: b.width, h: b.height, t: e.innerText.slice(0,30), vis: cs.visibility, disp: cs.display, chain }; });
  console.log(i, JSON.stringify(r));
}
// same for 'Next page' buttons and pricing table check
const ctx2 = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'dark' });
await patch(ctx2);
const p2 = await ctx2.newPage();
await open(p2, BASE + '/explore', { wait: 9000 });
await p2.waitForTimeout(2500);
const nb = p2.locator('button[aria-label="Next page"]');
console.log('next all', await nb.count(), 'vis', await nb.filter({ visible: true }).count());
const tr = p2.locator('a.page-model-card span.truncate');
console.log('truncate vis', await tr.filter({ visible: true }).count());
await ctx2.close();
const ctx3 = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'light' });
await patch(ctx3);
const p3 = await ctx3.newPage();
await open(p3, BASE + '/pricing', { wait: 9000 });
await p3.waitForTimeout(2500);
const tb = await p3.evaluate(() => [...document.querySelectorAll('table, [role="table"], [class*="table" i]')].slice(0,8).map((e) => { const r = e.getBoundingClientRect(); return `${e.tagName}.${String(e.className).slice(0,50)} ${r.width|0}x${r.height|0}@${r.x|0},${r.y|0}`; }));
console.log('pricing tables', JSON.stringify(tb));
await ctx3.close(); await browser.close();
