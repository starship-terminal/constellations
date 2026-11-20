// Measures OneSoil's public marketing controls. Nothing is submitted.
//
//   PLAYWRIGHT=... node measure.mjs
//
// Writes raw/components-computed.json and components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, styleOf, crop, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'OneSoil', captured: '2026-11-21', route: 'public marketing, signed out' }, components: {} };
const log = (...a) => console.log(...a);

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

async function open(url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1500);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
}

async function record(name, state, locator, note) {
  const loc = locator.first();
  if (!(await loc.count())) {
    log('  missing', name, state);
    return;
  }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const style = await styleOf(loc);
  out.components[name] ??= { note, states: {} };
  out.components[name].states[state] = style;
  await crop(page, loc, `${name}-${state}`).catch((e) => log('  crop fail', name, state, String(e.message || e).split('\n')[0]));
  log('  ', name, state);
}

async function force(locator, pseudo) {
  const el = locator.first();
  await cdp.send('CSS.enable');
  const node = await el.evaluateHandle((n) => n);
  const { nodeId } = await cdp.send('DOM.describeNode', { objectId: node._objectId || (await node.evaluate((n) => n)) }).catch(() => ({}));
  // Use DOM.getDocument + query via backend id from the element.
  const described = await cdp.send('DOM.describeNode', { objectId: (await page.evaluateHandle((el) => el, await el.elementHandle()))._remoteObject?.objectId }).catch(() => null);
  return described;
}

async function pressState(locator) {
  const handle = await locator.first().elementHandle();
  if (!handle) return;
  const { objectId } = handle._objectId ? { objectId: handle._objectId } : {};
  // Playwright ElementHandle exposes the remote object through CDP via DOM.requestNode.
  try {
    const remote = await handle.evaluateHandle((el) => el);
    const obj = remote._objectId || null;
  } catch {}
  const node = await cdp.send('DOM.requestNode', { objectId: handle._objectId }).catch(async () => {
    // ElementHandle in this Playwright build stores the object id differently.
    return null;
  });
  return node;
}

async function withPseudo(locator, pseudo, fn) {
  const handle = await locator.first().elementHandle();
  if (!handle) return;
  const objectId = handle._objectId || handle._guid && null;
  // Playwright 1.40+ ElementHandle has no public objectId. Use CSS.forcePseudoState via DOM.getNodeForLocation after bounding box is unreliable.
  // Fallback: evaluate a class is not the product's state. Use the CDP session attached to the page and DOM.querySelector on a marked attribute.
  await locator.first().evaluate((el) => el.setAttribute('data-capture', '1'));
  const doc = await cdp.send('DOM.getDocument');
  const found = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '[data-capture="1"]' });
  await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: pseudo });
  await page.waitForTimeout(200);
  await fn();
  await cdp.send('CSS.forcePseudoState', { nodeId: found.nodeId, forcedPseudoClasses: [] }).catch(() => {});
  await locator.first().evaluate((el) => el.removeAttribute('data-capture')).catch(() => {});
}

async function hover(locator) {
  await locator.first().hover();
  await page.waitForTimeout(350);
}

await open(BASE + '/en');
const demo = page.locator('header').getByRole('link', { name: 'Schedule a demo' });
const free = page.locator('header').getByRole('link', { name: 'Try Free' });
const products = page.locator('header').getByRole('button', { name: 'Products', exact: true });
await record('button-primary', 'default', demo, 'Header Schedule a demo, near-black pill');
await hover(demo);
await record('button-primary', 'hover', demo, 'Header Schedule a demo hovered');
await page.mouse.move(4, 4);
await demo.first().focus();
await page.waitForTimeout(200);
await record('button-primary', 'focus-visible', demo, 'Header Schedule a demo keyboard focus');
await withPseudo(demo, ['active', 'hover'], async () => record('button-primary', 'pressed', demo, 'forced :active:hover via CDP'));
await page.evaluate(() => document.activeElement && document.activeElement.blur());

await record('button-accent', 'default', free, 'Header Try Free, green pill. Following it opens the app sign-in wall, so it was not clicked.');
await hover(free);
await record('button-accent', 'hover', free, 'Try Free hovered');
await page.mouse.move(4, 4);
await withPseudo(free, ['active', 'hover'], async () => record('button-accent', 'pressed', free, 'forced :active:hover via CDP'));

await record('nav-button', 'default', products, 'Header Products trigger');
await products.click();
await page.waitForTimeout(500);
await record('nav-button', 'selected', products, 'Products trigger while its panel is open');
const card = page.locator('a[href="/en/platform"]').filter({ hasText: 'OneSoil Platform' }).first();
await record('menu-card', 'default', card, 'Products panel card');
await hover(card);
await record('menu-card', 'hover', card, 'Products panel card hovered');
await page.keyboard.press('Escape');
await page.waitForTimeout(300);

const lang = page.locator('header').getByRole('button', { name: 'EN', exact: true });
await lang.click();
await page.waitForTimeout(400);
const en = page.locator('a[href="/en"]').filter({ hasText: 'English' }).first();
await record('menu-item', 'default', en, 'Language row');
await page.keyboard.press('Escape');

await page.evaluate(() => scrollTo(0, 520));
await page.waitForTimeout(300);
const audience = page.locator('a[href="/en/solutions/farmers"]').filter({ hasText: 'For those who grow' }).first();
await record('audience-card', 'default', audience, 'Home audience card');

const chat = page.locator('button').filter({ has: page.locator('svg') }).last();
// The green chat bubble is a fixed button. Select by position instead of guessing the widget vendor.
const bubble = page.locator('body > div button, button').filter({ hasText: '' });
await page.evaluate(() => scrollTo(0, 0));

// h1 type
const h1 = page.locator('h1').first();
await record('display', 'default', h1, 'Home display heading');
const accent = page.locator('h1 span, h1 em, h1 strong').first();
if (await accent.count()) await record('display-accent', 'default', accent, 'Green words inside the home heading');

await open(BASE + '/en/contact-us');
const field = page.locator('input[name="name"]');
await record('text-field', 'default', field, 'Contact name field, empty, not submitted');
await field.click();
await page.waitForTimeout(200);
await record('text-field', 'focus', field, 'Contact name field focused, nothing typed');
const area = page.locator('textarea[name="message"]');
await record('text-area', 'default', area, 'Contact message, empty');
const select = page.locator('select[name="country"]');
await record('select', 'default', select, 'Country select, not opened, not chosen');
const submit = page.getByRole('button', { name: 'Submit' });
await record('button-submit', 'default', submit, 'Submit, not clicked');
await hover(submit);
await record('button-submit', 'hover', submit, 'Submit hovered, not clicked');
const check = page.locator('input[name="consent"]');
await record('checkbox', 'default', check, 'Consent checkbox, not toggled');

await open(BASE + '/en/contact-us?form=schedule_demo');
const chip = page.getByRole('radio', { name: 'Agronomist' });
await record('chip', 'default', chip, 'Demo role chip');
await chip.first().scrollIntoViewIfNeeded();
await chip.first().click();
await page.waitForTimeout(250);
await record('chip', 'selected', chip, 'Agronomist chip after a click. The form was not submitted.');

await open(BASE + '/en/platform');
const dl = page.getByRole('button', { name: /^Download$/ });
await record('button-secondary', 'default', dl, 'Download button on platform');
await dl.click();
await page.waitForTimeout(400);
await record('dialog', 'open', page.getByRole('button', { name: 'Close' }), 'Close control of the Download popover');
const store = page.getByRole('link', { name: /App Store/ });
await record('store-link', 'default', store, 'App Store link inside Download popover. Not followed.');
await page.getByRole('button', { name: 'Close' }).click().catch(() => {});
const faq = page.getByRole('button', { name: /Do I need to upload/i });
await record('accordion', 'default', faq, 'FAQ collapsed');
await faq.click();
await page.waitForTimeout(300);
await record('accordion', 'expanded', faq, 'FAQ expanded');

await open(BASE + '/en/resources');
const cat = page.locator('a[href="/en/resources/category/learn"]').first();
await record('card', 'default', cat, 'Resources category card');
await hover(cat);
await record('card', 'hover', cat, 'Resources category card hovered');

await open('https://help.onesoil.ai/en/');
const search = page.locator('input[type="search"], input[placeholder*="Search" i], input[type="text"]').first();
if (await search.count()) await record('search-field', 'default', search, 'Help center search, not typed into');

// Theme probe: does prefers-color-scheme dark change painted colours?
const darkCtx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  colorScheme: 'dark',
  locale: 'en-US',
});
const dp = await darkCtx.newPage();
await dp.goto(BASE + '/en', { waitUntil: 'domcontentloaded' });
await dp.waitForTimeout(1200);
out._meta.darkProbe = await dp.evaluate(() => {
  const h1 = document.querySelector('h1');
  const body = document.body;
  const btn = [...document.querySelectorAll('a')].find((a) => /Schedule a demo/.test(a.innerText || ''));
  const cs = (el) => el ? { color: getComputedStyle(el).color, bg: getComputedStyle(el).backgroundColor } : null;
  return {
    prefers: matchMedia('(prefers-color-scheme: dark)').matches,
    body: cs(body),
    h1: cs(h1),
    cta: cs(btn),
    themeToggle: [...document.querySelectorAll('button, a')].some((el) => /dark mode|light mode|theme/i.test((el.innerText || '') + (el.getAttribute('aria-label') || ''))),
  };
});
await darkCtx.close();

// Foundations from computed styles on home.
await open(BASE + '/en');
out._meta.foundations = await page.evaluate(() => {
  const pick = (el) => {
    if (!el) return null;
    const s = getComputedStyle(el);
    return {
      color: s.color, bg: s.backgroundColor, font: s.fontFamily, size: s.fontSize, weight: s.fontWeight,
      line: s.lineHeight, radius: s.borderRadius, shadow: s.boxShadow, pad: s.padding, border: s.border,
      transition: s.transitionDuration + ' ' + s.transitionTimingFunction,
    };
  };
  const a = [...document.querySelectorAll('header a')];
  const demo = a.find((el) => /Schedule a demo/.test(el.innerText || ''));
  const free = a.find((el) => /Try Free/.test(el.innerText || ''));
  const link = [...document.querySelectorAll('a')].find((el) => el.getAttribute('href') === '/en/platform');
  return {
    body: pick(document.body),
    h1: pick(document.querySelector('h1')),
    header: pick(document.querySelector('header')),
    demo: pick(demo),
    free: pick(free),
    link: pick(link),
    vars: [...document.styleSheets].slice(0, 8).map((sheet) => {
      try { return sheet.href || 'inline'; } catch { return 'blocked'; }
    }),
  };
});

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, 'components', Object.keys(out.components).length);
await browser.close();
