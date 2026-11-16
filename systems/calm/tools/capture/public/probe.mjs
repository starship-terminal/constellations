// One-off DOM probe (not part of the pipeline): dumps the header, nav,
// top-bar and card markup of the live pages so selectors can be fixed
// against what the site actually paints today.
import { BASE, launch, patch, closePromo, isChallengeText, UA_DESKTOP } from './lib.mjs';

const { browser } = await launch();
let context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
await patch(context);

const INFO = `(el) => { if (!el) return null; const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return { tag: el.tagName, cls: String(el.className).slice(0, 70), testid: el.getAttribute('data-testid'), href: el.getAttribute('href'), aria: el.getAttribute('aria-label'), text: (el.innerText || '').trim().slice(0, 50), box: (r.width | 0) + 'x' + (r.height | 0) + '@' + (r.x | 0) + ',' + (r.y | 0), vis: cs.visibility, disp: cs.display, op: cs.opacity }; }`;
const VIS = `(el) => { const r = el.getBoundingClientRect(); const cs = getComputedStyle(el); return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && cs.opacity !== '0' && r.left < innerWidth && r.right > 0 && r.top < innerHeight && r.bottom > 0; }`;

async function openOk(url, wait = 11000) {
  for (let attempt = 0; attempt < 8; attempt++) {
    const p = await context.newPage();
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(wait);
    const s = await p.evaluate(() => ({ title: document.title, body: (document.body && document.body.innerText) || '' })).catch(() => null);
    if (s && !isChallengeText(s) && s.body.trim().length >= 40) { await closePromo(p).catch(() => {}); return p; }
    console.log(url, 'blocked', attempt < 2 ? 'retry 90s' : 'fresh context 5min');
    await p.close().catch(() => {});
    if (attempt < 2) await new Promise((r) => setTimeout(r, 90000));
    else {
      await new Promise((r) => setTimeout(r, 300000));
      await context.close().catch(() => {});
      context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
      await patch(context);
    }
  }
  return null;
}

const J = (o) => console.log(JSON.stringify(o, null, 1));

// --- HOME: header Try-Calm tag + login-card close button + signup target ---
{
  const p = await openOk(BASE + '/');
  if (p) {
    console.log('\n======== HOME header ========');
    J(await p.evaluate(`(() => { const info = ${INFO}; const vis = ${VIS};
      return { headerKids: [...document.querySelectorAll('header a, header button')].filter(vis).map(info),
        tryCalm: [...document.querySelectorAll('header a, header button')].filter((el) => /try calm/i.test(el.innerText || '')).map(info) }; })()`));
    const t = p.locator('button[data-testid="desktopnav-login-button"], header button').filter({ hasText: /^\s*Log ?In\s*$/i }).filter({ visible: true }).first();
    if (await t.count()) { await t.click({ timeout: 5000 }).catch(() => t.evaluate((el) => el.click())); await p.waitForTimeout(2000); }
    console.log('======== LOGIN dialog buttons ========');
    J(await p.evaluate(`(() => { const info = ${INFO};
      const d = [...document.querySelectorAll('[role="dialog"], [class*="Modal" i], [class*="Dialog" i]')].pop();
      return { dlg: info(d), buttons: d ? [...d.querySelectorAll('button, a')].map(info) : [] }; })()`));
    await p.keyboard.press('Escape'); await p.waitForTimeout(800);
    const cta = p.locator('header a, header button').filter({ hasText: /try calm/i }).filter({ visible: true }).first();
    const before = p.url();
    if (await cta.count()) { await cta.click({ timeout: 5000 }).catch(() => cta.evaluate((el) => el.click())); await p.waitForTimeout(3000); }
    console.log('Try Calm ->', p.url(), p.url() === before ? '(stayed)' : '(navigated)');
    if (p.url() !== before) {
      console.log('======== SIGNUP landing ========');
      J(await p.evaluate(`(() => { const info = ${INFO}; const vis = ${VIS};
        return { h1: info(document.querySelector('h1, h2')),
          controls: [...document.querySelectorAll('main input, main button, main a, form input, form button, form a, input, button')].filter(vis).slice(0, 12).map(info) }; })()`));
      await p.goBack().catch(() => {});
    }
    await p.close();
  }
}

// --- SLEEP: every "Search"-ish node with real rects ---
{
  const p = await openOk(BASE + '/app/sleep', 12000);
  if (p) {
    console.log('\n======== SLEEP search nodes ========');
    J(await p.evaluate(`(() => { const info = ${INFO}; const vis = ${VIS};
      return { search: [...document.querySelectorAll('button, a, input, [role="search"]')].filter((el) => /search/i.test((el.innerText || '') + ' ' + (el.getAttribute('placeholder') || '') + ' ' + (el.getAttribute('aria-label') || ''))).map(info).filter(Boolean),
        top: [...document.querySelectorAll('button, a')].filter((el) => /log ?in|try calm/i.test(el.innerText || '')).map(info) }; })()`));
    await p.close();
  }
}

// --- MOBILE: opened menu structure at 390 ---
{
  let mctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
  await patch(mctx);
  for (let attempt = 0; attempt < 8; attempt++) {
    const p = await mctx.newPage();
    await p.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
    await p.waitForTimeout(10000);
    const s = await p.evaluate(() => ({ title: document.title, body: (document.body && document.body.innerText) || '' })).catch(() => null);
    if (s && !isChallengeText(s) && s.body.trim().length >= 40) {
      await closePromo(p).catch(() => {});
      const menu = p.locator('button[aria-label*="menu" i]').filter({ visible: true }).first();
      if (await menu.count()) { await menu.click({ timeout: 5000 }).catch(() => menu.evaluate((el) => el.click())); await p.waitForTimeout(1800); }
      console.log('\n======== MOBILE menu open ========');
      J(await p.evaluate(`(() => { const info = ${INFO}; const vis = ${VIS};
        return { header: info(document.querySelector('header')),
          headerKids: [...document.querySelectorAll('header *')].filter((el) => el.children.length === 0 || /^(A|BUTTON|NAV)$/.test(el.tagName)).filter(vis).slice(0, 25).map(info),
          overlays: [...document.querySelectorAll('[role="dialog"], [class*="Menu" i], [class*="Drawer" i], [class*="Overlay" i], nav')].map(info).filter(Boolean).slice(0, 15) }; })()`));
      await p.close();
      break;
    }
    console.log('mobile blocked', attempt < 2 ? 'retry 90s' : 'fresh 5min');
    await p.close().catch(() => {});
    if (attempt < 2) await new Promise((r) => setTimeout(r, 90000));
    else {
      await new Promise((r) => setTimeout(r, 300000));
      await mctx.close().catch(() => {});
      mctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_DESKTOP, locale: 'en-US' });
      await patch(mctx);
    }
  }
  await mctx.close();
}

await context.close();
await browser.close();
