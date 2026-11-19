// Measures Copperx marketing controls without signing in or submitting anything.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and components/crops/{name}-{state}.png.
// Log in opens the account-choice dialog and is closed. dashboard.copperx.io and
// payout.copperx.io are never opened. The contact page is a Google Form iframe
// and is not filled.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, styleOf, crop, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const out = {
  _meta: {
    product: 'Copperx',
    source: 'https://copperx.io',
    captured: '2026-11-18',
    route: 'public',
    note: 'Signed-out marketing only. Account dialog photographed and closed. No field filled, no consent clicked.',
  },
  components: {},
};

async function states(page, cdp, key, locator, list) {
  const loc = locator.first();
  const rec = (out.components[key] ??= { states: {} });
  if (!(await loc.count())) {
    rec.missing = true;
    log('  ! missing', key);
    return;
  }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  for (const st of list) {
    try {
      if (st === 'hover') {
        await loc.hover({ timeout: 4000 });
        await page.waitForTimeout(350);
      } else if (st === 'focus-visible') {
        await loc.focus();
        await page.keyboard.down('Shift');
        await loc.focus();
        await page.keyboard.up('Shift');
        await page.waitForTimeout(200);
      } else if (st === 'pressed') {
        await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
        const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
        const { nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' });
        if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
        await page.waitForTimeout(250);
      }
      const s = await styleOf(loc);
      let file;
      try { file = await crop(page, loc, `${key}-${st}`); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
      rec.states[st] = { ...s, crop: file };
      log('  ', key, st, s.rect.w + 'x' + s.rect.h, s.style.backgroundColor, s.style.color);
      if (st === 'pressed') {
        await page.evaluate(() => document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force')));
      }
    } catch (e) {
      rec.states[st] = { error: String(e.message).slice(0, 180) };
      log('  !', key, st, String(e.message).slice(0, 100));
    }
  }
  await page.mouse.move(2, 2).catch(() => {});
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

try {
  await open(page, BASE + '/');
  await states(page, cdp, 'login-button', page.locator('button.btn-light').filter({ hasText: 'Log in' }), ['default', 'hover', 'focus-visible', 'pressed']);
  await states(page, cdp, 'primary-button', page.locator('button.btn-dark').filter({ hasText: 'Get Started' }), ['default', 'hover', 'focus-visible', 'pressed']);
  await states(page, cdp, 'sales-button', page.locator('a.btn-light').filter({ hasText: 'Contact Sales' }), ['default', 'hover']);
  await states(page, cdp, 'hero-title', page.locator('h1').first(), ['default']);
  await states(page, cdp, 'nav-link', page.locator('a.text-indigo-400, a[class*="text-indigo"]').first(), ['default', 'hover']);

  // Account dialog. Links are not followed.
  await page.locator('button.btn-light').filter({ hasText: 'Log in' }).first().click();
  await page.waitForTimeout(700);
  const panel = page.locator('a[href*="dashboard.copperx.io"]').first();
  await states(page, cdp, 'account-choice', panel, ['default']);
  const dialogMeta = await page.evaluate(() => {
    const d = document.querySelector('[role="dialog"]');
    const links = [...d.querySelectorAll('a')].map((a) => ({ text: (a.innerText || '').trim().slice(0, 60), host: new URL(a.href).host }));
    const card = d.querySelector('a');
    const cs = card ? getComputedStyle(card) : null;
    return { links, cardBg: cs && cs.backgroundColor, cardRadius: cs && cs.borderRadius };
  });
  out.components['account-choice'].dialog = dialogMeta;
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  // Header
  const header = await styleOf(page.locator('header').first());
  out.components.header = { states: { default: header } };
  log('  header', header.rect.h, header.style.backgroundColor);

  await open(page, BASE + '/pricing');
  await states(page, cdp, 'pricing-title', page.locator('h1').first(), ['default']);

  await open(page, BASE + '/credit-cards');
  await states(page, cdp, 'cards-title', page.locator('h1').first(), ['default']);
} finally {
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
  await browser.close();
}
log('wrote', OUT);
