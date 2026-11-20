// Measures Overflow's public components. Nothing is submitted or signed into.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, hideCookies, styleOf, crop, RAW } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);

const { browser, context } = await launch({ width: 1440, height: 900 });
const cdpBrowser = context;
const components = {};

async function measure(page, cdp, name, locator, states = ['default']) {
  const count = await locator.count();
  if (!count) {
    components[name] = { missing: true, states: {} };
    log('miss', name);
    return;
  }
  const loc = locator.first();
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(250);
  const entry = { missing: false, states: {} };
  const box = await loc.boundingBox();
  if (!box) { components[name] = { missing: true, states: {} }; log('offscreen', name); return; }
  if (states.includes('default')) {
    entry.states.default = await styleOf(loc);
    await crop(page, loc, `${name}-default`);
  }
  if (states.includes('hover')) {
    await page.mouse.move(box.x + Math.min(box.width / 2, 40), box.y + Math.min(box.height / 2, 16));
    await page.waitForTimeout(350);
    entry.states.hover = await styleOf(loc);
    await crop(page, loc, `${name}-hover`);
    await page.mouse.move(2, 2);
    await page.waitForTimeout(150);
  }
  if (states.includes('focus-visible')) {
    await loc.focus().catch(() => {});
    await page.keyboard.press('Shift+Tab').catch(() => {});
    await page.keyboard.press('Tab').catch(() => {});
    await page.waitForTimeout(200);
    const focused = await loc.evaluate((el) => document.activeElement === el || el.contains(document.activeElement));
    entry.states['focus-visible'] = { ...(await styleOf(loc)), via: focused ? 'Tab' : 'focus failed' };
    if (focused) await crop(page, loc, `${name}-focus-visible`);
    await page.evaluate(() => document.activeElement && document.activeElement.blur());
  }
  if (states.includes('pressed')) {
    try {
      const handle = await loc.elementHandle();
      if (handle) {
        await cdp.send('CSS.enable');
        const { nodeId } = await cdp.send('DOM.describeNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => ({ nodeId: null }));
        // Force :active through the Playwright locator's bounding box hover+CDP if available.
        await page.evaluate((el) => el.setAttribute('data-capture-press', '1'), await loc.elementHandle());
      }
    } catch { /* pressed recorded from CDP below */ }
    try {
      await cdp.send('DOM.enable');
      await cdp.send('CSS.enable');
      const objectId = (await loc.elementHandle())._remoteObject ? undefined : undefined;
      const eh = await loc.elementHandle();
      const remote = await eh.evaluateHandle((el) => el);
      // Use CSS.forcePseudoState via DOM.querySelector on a marked node.
      await loc.evaluate((el) => el.setAttribute('data-capture-target', '1'));
      const doc = await cdp.send('DOM.getDocument');
      const found = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '[data-capture-target="1"]' });
      if (found.nodeId) {
        await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: ['hover', 'active'] });
        await page.waitForTimeout(120);
        entry.states.pressed = { ...(await styleOf(loc)), via: 'CDP forcePseudoState active' };
        await crop(page, loc, `${name}-pressed`);
        await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: [] });
      }
      await loc.evaluate((el) => el.removeAttribute('data-capture-target'));
    } catch (e) {
      entry.states.pressed = { via: 'pressed failed: ' + String(e.message).split('\n')[0] };
    }
  }
  components[name] = entry;
  log('ok', name, Object.keys(entry.states).join(','));
}

async function on(path, fn) {
  const page = await context.newPage();
  const cdp = await context.newCDPSession(page);
  await cdp.send('DOM.enable');
  await cdp.send('CSS.enable');
  log('open', path);
  await open(page, BASE + path, { wait: 2000 });
  await hideCookies(page);
  await fn(page, cdp);
  await page.close();
}

const interactive = ['default', 'hover', 'focus-visible', 'pressed'];

await on('/', async (page, cdp) => {
  await measure(page, cdp, 'hero-title', page.locator('h1').first(), ['default']);
  await measure(page, cdp, 'hero-cta', page.getByRole('link', { name: /Download - free trial/i }), interactive);
  await measure(page, cdp, 'nav-cta', page.getByRole('link', { name: 'Download for free' }).first(), interactive);
  await measure(page, cdp, 'nav-link', page.locator('header a.nav-link, .navbar a.nav-link').filter({ hasText: 'Examples' }).first(), interactive);
  await measure(page, cdp, 'nav-signin', page.getByRole('link', { name: /^Sign In$/i }).first(), interactive);
  await measure(page, cdp, 'product-trigger', page.locator('a[href="#product-collapse"]').first(), interactive);
  await page.locator('a[href="#product-collapse"]').first().click().catch(() => {});
  await page.waitForTimeout(500);
  await measure(page, cdp, 'product-menu', page.locator('#product-collapse').first(), ['default']);
  await measure(page, cdp, 'menu-link', page.locator('#product-collapse a').filter({ hasText: 'Features' }).first(), interactive);
  await measure(page, cdp, 'logo', page.locator('a.header-logo, .navbar-brand, header a[href="/"]').first(), ['default']);
  await measure(page, cdp, 'demo-link', page.getByText('Watch product demo').first(), interactive);
});

await on('/pricing/', async (page, cdp) => {
  await measure(page, cdp, 'pricing-h1', page.locator('h1').first(), ['default']);
  await measure(page, cdp, 'plan-card', page.locator('.pricing-card, .plan-card, .price-card, [class*="pricing"][class*="card"], .card').first(), ['default']);
  await measure(page, cdp, 'plan-cta', page.locator('a.btn, button.btn').filter({ hasText: /start|trial|get|choose|buy|contact/i }).first(), interactive);
  const opener = page.locator('.accordion__opener').first();
  await measure(page, cdp, 'faq-item', opener, interactive);
  await opener.click().catch(() => {});
  await page.waitForTimeout(400);
  await measure(page, cdp, 'faq-open', page.locator('.accordion__item').first(), ['default']);
});

await on('/download/', async (page, cdp) => {
  await measure(page, cdp, 'download-mac', page.getByRole('link', { name: /Download for Mac/i }).or(page.getByRole('button', { name: /Download for Mac/i })).first(), interactive);
  await measure(page, cdp, 'download-h1', page.locator('h1').first(), ['default']);
});

await on('/features/', async (page, cdp) => {
  await measure(page, cdp, 'section-h2', page.locator('h2').first(), ['default']);
  await measure(page, cdp, 'feature-card', page.locator('a[href="#feature_sync"], .feature-card, [class*="feature"]').first(), ['default']);
});

await on('/blog/', async (page, cdp) => {
  await measure(page, cdp, 'blog-card', page.locator('article a, .blog-card a, a[href*="/blog/"]').nth(2), ['default', 'hover']);
});

await on('/integrations/', async (page, cdp) => {
  await measure(page, cdp, 'integration-card', page.locator('a[href*="support.overflow"], .integration, [class*="integration"]').first(), ['default']);
});

// Phone menu button. A fresh mobile context.
await context.close();
const mob = await launch({ mobile: true });
const mp = await mob.context.newPage();
const mcdp = await mob.context.newCDPSession(mp);
await mcdp.send('DOM.enable');
await mcdp.send('CSS.enable');
await open(mp, BASE + '/', { wait: 2000 });
await hideCookies(mp);
await measure(mp, mcdp, 'm-menu-button', mp.locator('button.navbar-toggler').first(), interactive);
await mp.locator('button.navbar-toggler').first().click().catch(() => {});
await mp.waitForTimeout(600);
await measure(mp, mcdp, 'm-nav-item', mp.locator('.navbar-collapse a, #headerNav a, .navbar-nav a').filter({ hasText: 'Examples' }).first(), ['default']);
await crop(mp, mp.locator('header, .navbar, nav').first(), 'm-header-default').catch(() => {});
await mob.browser.close();
await browser.close();

const out = {
  readAt: new Date().toLocaleDateString('en-CA'),
  source: 'Computed styles on overflow.io public pages, desktop 1440x900 and phone 390x844. Cookie bar hidden, never accepted. No form submitted.',
  components,
};
fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
console.log('wrote', OUT, 'components', Object.keys(components).length);
