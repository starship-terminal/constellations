import { BASE, UA, UA_MOBILE, launch, patch, open } from './lib.mjs';

const dump = (el) => {
  const r = el.getBoundingClientRect();
  const cs = getComputedStyle(el);
  const cls = String(el.className).split(' ').slice(0, 6).join(' ');
  return `${el.tagName.toLowerCase()}.${cls} ${r.width | 0}x${r.height | 0}@${r.x | 0},${r.y | 0} ` +
    `vis=${cs.visibility} disp=${cs.display} text=${JSON.stringify((el.innerText || el.textContent || '').slice(0, 60))}`;
};

const which = (arg) => {
  const label = arg.startsWith('--docs') ? 'docs' : arg.startsWith('--mobile') ? 'mobile' : 'app';
  const h1 = arg.includes('h1') || arg === '--docs' || arg === '--mobile';
  return { label, h1 };
};

const mode = process.argv[2] || '--docs';
const { browser, context } = await launch();

if (mode.startsWith('--docs')) {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, colorScheme: 'light' });
  await patch(ctx);
  const page = await ctx.newPage();
  await open(page, BASE + '/docs/documentation', { wait: 9000 });
  await page.waitForTimeout(3000);
  const info = await page.evaluate((dumpSrc) => {
    const dump = eval(`(${dumpSrc})`);
    const out = {};
    out.h1s = [...document.querySelectorAll('h1')].map(dump);
    out.ps = [...document.querySelectorAll('main p, article p, .prose p, [class*="prose" i] p')].slice(0, 8).map(dump);
    out.cards = [...document.querySelectorAll('a')].filter((a) => /call 1,000|deploy your own|start with a model/i.test(a.innerText || '')).map(dump);
    out.codeGroups = [...document.querySelectorAll('.code-group, [class*="code" i]')].filter((e) => e.getBoundingClientRect().width > 50).slice(0, 10).map(dump);
    out.mains = [...document.querySelectorAll('main, article, [role="main"], #nd-page, [class*="prose" i]')].slice(0, 8).map(dump);
    out.htmlClass = document.documentElement.className;
    out.bodyText = (document.body.innerText || '').slice(0, 300);
    return out;
  }, dump.toString());
  console.log(JSON.stringify(info, null, 1));
  await ctx.close();
} else if (mode.startsWith('--mobile')) {
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, colorScheme: 'dark' });
  await patch(ctx);
  const page = await ctx.newPage();
  await open(page, BASE + '/explore', { wait: 9000 });
  await page.waitForTimeout(3000);
  const info = await page.evaluate((dumpSrc) => {
    const dump = eval(`(${dumpSrc})`);
    const out = {};
    out.headers = [...document.querySelectorAll('header')].map(dump);
    out.navBtns = [...document.querySelectorAll('button[aria-label]')].filter((b) => /nav|menu/i.test(b.getAttribute('aria-label'))).map((b) => dump(b) + ' aria=' + b.getAttribute('aria-label'));
    out.cards = [...document.querySelectorAll('a.page-model-card')].slice(0, 3).map(dump);
    out.anyCards = [...document.querySelectorAll('a[href^="/models/"]')].slice(0, 5).map(dump);
    out.search = [...document.querySelectorAll('input')].slice(0, 5).map((i) => dump(i) + ' ph=' + (i.placeholder || '') + ' aria=' + (i.getAttribute('aria-label') || ''));
    out.bodyText = (document.body.innerText || '').slice(0, 300);
    return out;
  }, dump.toString());
  console.log(JSON.stringify(info, null, 1));
  // open the nav and dump the drawer
  const ham = page.locator('button[aria-label*="navigation" i], button[aria-label*="menu" i]').first();
  if (await ham.count()) {
    await ham.tap({ timeout: 4000 }).catch(() => ham.click({ timeout: 4000, force: true }).catch(() => {}));
    await page.waitForTimeout(1200);
    const nav = await page.evaluate((dumpSrc) => {
      const dump = eval(`(${dumpSrc})`);
      return {
        dialogs: [...document.querySelectorAll('[role="dialog"], [data-state="open"], [class*="drawer" i], [class*="sheet" i], [class*="dialog" i]')].slice(0, 8).map(dump),
        links: [...document.querySelectorAll('a')].filter((a) => /pricing|documentation|explore|models|login/i.test(a.innerText || '') && a.getBoundingClientRect().width > 0).slice(0, 15).map((a) => dump(a) + ' href=' + a.getAttribute('href')),
      };
    }, dump.toString());
    console.log('OPENED ' + JSON.stringify(nav, null, 1));
  }
  await ctx.close();
}
await browser.close();
