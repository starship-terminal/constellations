import { BASE, UA, UA_MOBILE, launch, patch, open } from './lib.mjs';

const dump = (el) => {
  const r = el.getBoundingClientRect();
  const cs = getComputedStyle(el);
  const cls = String(el.className).split(' ').slice(0, 6).join(' ');
  return `${el.tagName.toLowerCase()}.${cls} ${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0} ` +
    `vis=${cs.visibility} disp=${cs.display} text=${JSON.stringify((el.innerText || el.textContent || '').slice(0, 70))}`;
};

const { browser } = await launch();
const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, colorScheme: 'dark' });
await patch(ctx);
const page = await ctx.newPage();
await open(page, BASE + '/explore', { wait: 9000 });
await page.waitForTimeout(2500);
const ham = page.locator('button[aria-label*="navigation" i]').first();
await ham.tap({ timeout: 4000 }).catch(() => ham.click({ timeout: 4000, force: true }).catch(() => {}));
await page.waitForTimeout(1500);
const nav = await page.evaluate((dumpSrc) => {
  const dump = eval(`(${dumpSrc})`);
  const drawer = [...document.querySelectorAll('div')].find((d) => /vaul-drawer|drawer-content/.test(String(d.className)) && d.getBoundingClientRect().top > 500);
  const items = drawer ? [...drawer.querySelectorAll('a, button, [role="link"], li')].slice(0, 25).map(dump) : ['no drawer'];
  return { drawer: drawer ? dump(drawer) : 'none', items };
}, dump.toString());
console.log(JSON.stringify(nav, null, 1));
await ctx.close();

const ctx2 = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'light' });
await patch(ctx2);
const p2 = await ctx2.newPage();
await open(p2, BASE + '/docs/documentation', { wait: 9000 });
await p2.waitForTimeout(2500);
const docs = await p2.evaluate((dumpSrc) => {
  const dump = eval(`(${dumpSrc})`);
  const cols = document.querySelector('.columns');
  return {
    colKids: cols ? [...cols.children].map(dump) : ['no .columns'],
    colKidKids: cols ? [...cols.children[0]?.querySelectorAll('*') || []].slice(0, 10).map(dump) : [],
    sideLinks: [...document.querySelectorAll('a')].filter((a) => /start with a model/i.test(a.innerText || '')).map((a) => dump(a) + ' up=' + String(a.parentElement?.className || '').slice(0, 60)),
  };
}, dump.toString());
console.log('DOCS ' + JSON.stringify(docs, null, 1));
await ctx2.close();

// sandbox anchor on the model page
const ctx3 = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'dark' });
await patch(ctx3);
const p3 = await ctx3.newPage();
await open(p3, BASE + '/models/krea/v3/text-to-image', { wait: 9000 });
await p3.waitForTimeout(2500);
const sb = await p3.evaluate((dumpSrc) => {
  const dump = eval(`(${dumpSrc})`);
  return [...document.querySelectorAll('a[href*="/sandbox"], [class*="sandbox" i]')].map(dump);
}, dump.toString());
console.log('SB ' + JSON.stringify(sb, null, 1));
await ctx3.close();
await browser.close();
