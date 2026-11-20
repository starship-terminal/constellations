import { BASE, UA, launch, patch, open } from './lib.mjs';
const dump = (el) => {
  const r = el.getBoundingClientRect();
  const cls = String(el.className).split(' ').slice(0, 6).join(' ');
  return `${el.tagName.toLowerCase()}.${cls} ${r.width|0}x${r.height|0}@${r.x|0},${r.y|0} text=${JSON.stringify((el.innerText||'').slice(0,60))}`;
};
const { browser } = await launch();
// PRICING (marketing, light)
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'light' });
await patch(ctx);
const p = await ctx.newPage();
await open(p, BASE + '/pricing', { wait: 9000 });
await p.waitForTimeout(2500);
const pr = await p.evaluate((dumpSrc) => {
  const dump = eval(`(${dumpSrc})`);
  return {
    switches: [...document.querySelectorAll('[role="switch"], input[type="checkbox"], button[class*="toggle" i], [class*="switch" i]')].slice(0,10).map(dump),
    periodTexts: [...document.querySelectorAll('button, a, label, [role="tab"], [role="radio"], [class*="radio" i] label')].filter((e)=>/monthly|annual|yearly|usage.?based|per.?month|billing/i.test(e.innerText||'')).slice(0,15).map(dump),
    planHeads: [...document.querySelectorAll('h1,h2,h3,h4')].slice(0,20).map(dump),
    priceRows: [...document.querySelectorAll('[class*="price" i], [class*="plan" i]')].filter((e)=>e.getBoundingClientRect().width>150 && e.getBoundingClientRect().height>50).slice(0,15).map(dump),
  };
}, dump.toString());
console.log('PRICING ' + JSON.stringify(pr, null, 1));
await ctx.close();
// EXPLORE internals (dark)
const ctx2 = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'dark' });
await patch(ctx2);
const p2 = await ctx2.newPage();
await open(p2, BASE + '/explore', { wait: 9000 });
await p2.waitForTimeout(2500);
const ex = await p2.evaluate((dumpSrc) => {
  const dump = eval(`(${dumpSrc})`);
  const card = document.querySelector('a.page-model-card');
  return {
    cardTree: card ? [...card.querySelectorAll('*')].slice(0, 20).map(dump) : ['no card'],
    pagers: [...document.querySelectorAll('[class*="pag" i], [role="navigation"], nav')].slice(0,12).map(dump),
    nexts: [...document.querySelectorAll('a, button')].filter((e)=>/next|previous|prev|page|more|load/i.test(e.innerText||e.getAttribute('aria-label')||'')).slice(0,15).map((e)=>dump(e)+' aria='+(e.getAttribute('aria-label')||'')+' href='+(e.getAttribute('href')||'')),
  };
}, dump.toString());
console.log('EXPLORE ' + JSON.stringify(ex, null, 1));
await ctx2.close();
await browser.close();
