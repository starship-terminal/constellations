// Measures tilda.cc public components. Nothing is submitted.
//
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, launch, open, closePromo, styleOf, crop, RAW } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { read: '2026-11-21', viewport: '1440x900', tool: 'tools/capture/public/measure.mjs' }, components: {} };
const log = (...a) => console.log(...a);

async function record(page, key, state, locator, note) {
  const loc = locator.first();
  if (!(await loc.count())) {
    log('  missing', key, state);
    return;
  }
  try {
    const style = await styleOf(loc);
    const c = (out.components[key] ??= { states: {}, page: page.url().replace(/\?.*$/, '') });
    c.states[state] = { ...style, note };
    await crop(page, loc, `${key}-${state}`);
    log('  ok', key, state, style.rect && style.rect.w);
  } catch (e) {
    log('  fail', key, state, e.message.split('\n')[0]);
  }
}

async function states(page, key, locator) {
  const loc = locator.first();
  await record(page, key, 'default', loc);
  await loc.hover().catch(() => {});
  await page.waitForTimeout(280);
  await record(page, key, 'hover', loc);
  await loc.focus().catch(() => {});
  await page.waitForTimeout(200);
  await record(page, key, 'focus-visible', loc);
  await page.mouse.move(2, 2);
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);
await cdp.send('DOM.enable');
await cdp.send('CSS.enable');

await open(page, BASE + '/', { wait: 2000 });
await closePromo(page);

await states(page, 'nav-link', page.locator('#t-header a').filter({ hasText: /^PRICING$/ }));
await states(page, 'login-link', page.locator('a.t934__enter'));
await states(page, 'signup-link', page.locator('a.t934__reg'));
await record(page, 'header', 'default', page.locator('#t-header'));
await record(page, 'wordmark', 'default', page.locator('#t-header a').filter({ hasText: /Tilda Publishing/ }).first());

const more = page.locator('.tmain-submenu__hooklink').first();
await states(page, 'more-trigger', more);
await more.click();
await page.waitForTimeout(500);
await record(page, 'more-menu', 'default', page.locator('.tmain-submenu__container'));
await states(page, 'menu-link', page.locator('.tmain-submenu__link').filter({ hasText: 'Templates' }));
await page.locator('.tmain-submenu__close').first().click().catch(() => {});
await page.waitForTimeout(300);

const cta = page.locator('a.t-btn').filter({ hasText: /Create a website for free/ }).first();
await cta.scrollIntoViewIfNeeded().catch(() => {});
await states(page, 'hero-cta', cta);

const h1 = page.locator('h1, .t-title, .tn-atom').filter({ hasText: /Create beautiful websites/ }).first();
await record(page, 'hero-title', 'default', h1);

// pricing
await open(page, BASE + '/pricing/', { wait: 2000 });
await record(page, 'pricing-title', 'default', page.locator('h1').first());
const plan = page.locator('.t-btn, a').filter({ hasText: /Choose|Get started|Start|Buy|Select/i }).first();
if (await plan.count()) await states(page, 'plan-cta', plan);
const select = page.locator('select').first();
if (await select.count()) {
  await record(page, 'currency-select', 'default', select);
  await select.focus().catch(() => {});
  await record(page, 'currency-select', 'focus-visible', select);
}

// templates radios
await open(page, BASE + '/tpls/', { wait: 2000 });
const radio = page.locator('input[type="radio"]').first();
if (await radio.count()) {
  const label = radio.locator('xpath=ancestor::label[1]');
  const target = (await label.count()) ? label : radio;
  await record(page, 'template-radio', 'default', target);
}
await record(page, 'template-title', 'default', page.locator('h1').first());

// faq field: type a public question, do not submit
await open(page, BASE + '/en/answers/', { wait: 2000 });
const search = page.locator('#t-searcher');
if (await search.count()) {
  await record(page, 'faq-search', 'default', search);
  await search.click();
  await record(page, 'faq-search', 'focused', search);
  await search.fill('domain');
  await page.waitForTimeout(300);
  await record(page, 'faq-search', 'filled', search);
  await search.fill('');
}
const faqBtn = page.locator('button, a, .t-answers__category').filter({ hasText: /^Domains$/ }).first();
if (await faqBtn.count()) {
  await faqBtn.click().catch(() => {});
  await page.waitForTimeout(500);
  await record(page, 'faq-category', 'selected', faqBtn);
}

// login wall: measure fields, do not type, do not submit
await open(page, BASE + '/login/', { wait: 1800 });
await record(page, 'login-email', 'default', page.locator('#email'));
await page.locator('#email').focus().catch(() => {});
await record(page, 'login-email', 'focused', page.locator('#email'));
await record(page, 'login-password', 'default', page.locator('#password'));
await record(page, 'login-submit', 'default', page.locator('button.ts-btn').first());
await states(page, 'login-submit', page.locator('button.ts-btn').first());

// registration wall: measure empty fields only
await open(page, BASE + '/registration/', { wait: 1800 });
await record(page, 'signup-name', 'default', page.locator('#name'));
await record(page, 'signup-email', 'default', page.locator('#email'));
await record(page, 'signup-password', 'default', page.locator('#password'));
await record(page, 'signup-submit', 'default', page.locator('button.ts-btn').first());

// colors swatch
await open(page, BASE + '/colors/', { wait: 1500 });
const swatch = page.locator('div, span, a').filter({ hasText: /^#5199ff$/ }).first();
if (await swatch.count()) await record(page, 'color-swatch', 'default', swatch);

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('components', Object.keys(out.components).length);
await browser.close();
