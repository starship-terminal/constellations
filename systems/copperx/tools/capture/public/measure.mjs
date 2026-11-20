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

// Merge into the committed file, so a run that throws part-way keeps every earlier reading.
// Components no spec measured this run are pruned only when the whole run finished.
const earlier = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : { components: {} };
const today = new Date().toLocaleDateString('en-CA');
const out = {
  _meta: {
    product: 'Copperx',
    source: 'https://copperx.io',
    // The file's date moves only when a run finishes; each component carries the date it was read (run).
    captured: earlier._meta?.captured || today,
    route: 'public',
    note: 'Signed-out marketing only. Account dialog photographed and closed. No field filled, no consent clicked.',
  },
  components: { ...(earlier.components || {}) },
};
const seen = new Set();
let finished = false;

// Undo every state before the next: clear the forced pseudo-classes, drop focus, move the pointer off.
async function reset(page, cdp, nodeId) {
  if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: [] }).catch(() => {});
  await page.evaluate(() => {
    document.querySelectorAll('[data-m-force]').forEach((n) => n.removeAttribute('data-m-force'));
    if (document.activeElement && document.activeElement !== document.body) document.activeElement.blur();
  });
  await page.mouse.move(2, 2).catch(() => {});
  await page.waitForTimeout(350);
}

async function states(page, cdp, key, locator, list) {
  const loc = locator.first();
  seen.add(key);
  const rec = (out.components[key] = { states: {}, run: today });
  if (!(await loc.count())) {
    rec.missing = true;
    log('  ! missing', key);
    return;
  }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  for (const st of list) {
    let nodeId = null;
    let via = 'at rest';
    try {
      if (st === 'hover') {
        via = 'mouse hover';
        await loc.hover({ timeout: 4000 });
        await page.waitForTimeout(350);
      } else if (st === 'focus-visible') {
        // Keyboard modality: focus the element, step back and Tab onto it again.
        via = 'Shift+Tab, Tab';
        await loc.focus();
        await page.keyboard.press('Shift+Tab');
        await page.keyboard.press('Tab');
        await page.waitForTimeout(200);
        if (!(await loc.evaluate((el) => el.matches(':focus-visible')))) {
          rec.states[st] = { skipped: true, via: 'focus failed' };
          log('  ', key, st, 'focus failed');
          continue;
        }
      } else if (st === 'pressed') {
        via = 'CDP forcePseudoState :active:hover';
        await loc.evaluate((el) => el.setAttribute('data-m-force', '1'));
        const { root } = await cdp.send('DOM.getDocument', { depth: 0 });
        ({ nodeId } = await cdp.send('DOM.querySelector', { nodeId: root.nodeId, selector: '[data-m-force]' }));
        if (nodeId) await cdp.send('CSS.forcePseudoState', { nodeId, forcedPseudoClasses: ['active', 'hover'] });
        await page.waitForTimeout(250);
      }
      const s = await styleOf(loc);
      let file;
      try { file = await crop(page, loc, `${key}-${st}`); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
      rec.states[st] = { ...s, crop: file, via };
      log('  ', key, st, s.rect.w + 'x' + s.rect.h, s.style.backgroundColor, s.style.color);
    } catch (e) {
      // First line only: a Playwright call log carries ANSI escapes and markup.
      rec.states[st] = { error: String(e.message).split('\n')[0].replace(/\x1b\[[0-9;]*m/g, '').slice(0, 180) };
      log('  !', key, st, String(e.message).split('\n')[0].slice(0, 100));
    } finally {
      await reset(page, cdp, nodeId);
    }
  }
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
page.setDefaultTimeout(8000);
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
    if (!d) return { missing: true };
    const links = [...d.querySelectorAll('a')].map((a) => ({ text: (a.innerText || '').trim().slice(0, 60), host: new URL(a.href).host }));
    const card = d.querySelector('a');
    const cs = card ? getComputedStyle(card) : null;
    return { links, cardBg: cs && cs.backgroundColor, cardRadius: cs && cs.borderRadius };
  });
  if (out.components['account-choice']) out.components['account-choice'].dialog = dialogMeta;
  await page.keyboard.press('Escape');
  await page.waitForTimeout(300);

  // Header
  if (await page.locator('header').count()) {
    const header = await styleOf(page.locator('header').first());
    out.components.header = { states: { default: header }, run: today };
    log('  header', header.rect.h, header.style.backgroundColor);
  } else {
    out.components.header = { missing: true, states: {}, run: today };
  }
  seen.add('header');

  await open(page, BASE + '/pricing');
  await states(page, cdp, 'pricing-title', page.locator('h1').first(), ['default']);

  await open(page, BASE + '/credit-cards');
  await states(page, cdp, 'cards-title', page.locator('h1').first(), ['default']);
  finished = true;
  out._meta.captured = today;
} finally {
  if (!finished) out._meta.unfinished = today;
  else delete out._meta.unfinished;
  if (finished) for (const k of Object.keys(out.components)) if (!seen.has(k)) delete out.components[k];
  fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
  await browser.close();
}
log('wrote', OUT);
