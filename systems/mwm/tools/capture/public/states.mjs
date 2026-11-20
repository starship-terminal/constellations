// Component states and a settled home shot. Nothing is submitted.
//   PLAYWRIGHT=... node states.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const { chromium } = await import(process.env.PLAYWRIGHT);
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'mwm', 'raw-shots');
const KEEP = path.join(PKG, 'raw');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(PKG, 'components', 'crops'), { recursive: true });

function styleOf(el) {
  const s = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  return {
    tag: el.tagName,
    cls: (el.className || '').toString().slice(0, 100),
    text: (el.innerText || el.getAttribute('placeholder') || el.getAttribute('aria-label') || '').toString().trim().replace(/\s+/g, ' ').slice(0, 60),
    bg: s.backgroundColor, color: s.color, font: s.fontFamily.split(',')[0],
    fs: s.fontSize, fw: s.fontWeight, lh: s.lineHeight, ls: s.letterSpacing,
    rad: s.borderRadius, pad: s.padding, gap: s.columnGap,
    border: s.borderTopWidth + ' ' + s.borderTopStyle + ' ' + s.borderTopColor,
    shadow: s.boxShadow === 'none' ? '' : s.boxShadow.slice(0, 120),
    outline: s.outlineStyle === 'none' ? '' : s.outline,
    h: Math.round(r.height), w: Math.round(r.width),
  };
}

const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const browser = await chromium.launch({ headless: true });
const out = { components: {}, viewport: { width: 1440, height: 900, dpr: 1 } };

async function shot(page, name) {
  await screenshotWithMetadata(page, { path: path.join(RAW, name + '.png') }, {
    viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1,
    sanitizedSourceUrl: page.url().split('?')[0],
  });
}
async function crop(page, locator, file) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad),
    width: Math.min(1440 - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(900 - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  const dest = path.join(PKG, 'components', 'crops', file);
  await page.screenshot({ path: dest, clip });
  return { file, box };
}

const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, locale: 'en-US' });
const page = await ctx.newPage();
page.setDefaultTimeout(8000);

async function open(url) {
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1200);
}

// Home, after the typewriter has had time to finish a cycle.
await open('https://mwm.ai/');
await page.waitForTimeout(6000);
await shot(page, 'home-dark-default');
log('home settled', await page.evaluate(() => (document.querySelector('h1') || {}).innerText));

const homeSpecs = {
  'nav-item': page.locator('.mwm-product-nav-item').nth(2),
  'button-secondary': page.locator('.mwm-product-login').first(),
  'button-primary': page.locator('.mwm-product-start').first(),
  'prompt': page.locator('.mwm-prompt').first(),
  'text-field': page.locator('textarea').first(),
  'chip': page.locator('.mwm-select-pill, .mwm-tool-pill').first(),
  'icon-button': page.locator('.mwm-icon-button').first(),
};
out.components.home = {};
for (const [key, loc] of Object.entries(homeSpecs)) {
  const states = {};
  try {
    states.default = await loc.evaluate(styleOf);
    await crop(page, loc, key + '-default.png');
    await loc.hover();
    await page.waitForTimeout(400);
    states.hover = await loc.evaluate(styleOf);
    await crop(page, loc, key + '-hover.png');
    await page.mouse.move(2, 2);
    await loc.focus();
    await page.keyboard.press('Shift+Tab');
    await page.keyboard.press('Tab');
    await page.waitForTimeout(250);
    states['focus-visible'] = await loc.evaluate(styleOf);
  } catch (e) { states.error = String(e.message).split('\n')[0]; }
  out.components.home[key] = states;
  log('home', key, states.error || (states.default && states.default.fs) || 'no-default');
}

// Products menu.
try {
  await page.locator('.mwm-product-nav-chevron').first().click();
  await page.waitForTimeout(600);
  await shot(page, 'home-dark-products-menu');
  const item = page.locator('.mwm-product-mega a, [class*=mega] a').first();
  out.components.home.menu = { default: await item.evaluate(styleOf).catch((e) => ({ error: e.message })) };
  await crop(page, page.locator('[class*=mega]').first(), 'menu-default.png');
  log('menu open');
} catch (e) { log('menu FAIL', e.message.split('\n')[0]); }

// Pricing plan card and FAQ.
await open('https://mwm.ai/pricing');
await page.waitForTimeout(800);
const price = page.locator('.mwm-plan-price').first();
const popular = page.locator('.mwm-plan-popular').first();
const cta = page.getByRole('link', { name: 'Get MWM AI Pro' }).first();
const faq = page.locator('.mwm-pricing-faq-trigger').first();
out.components.pricing = {};
for (const [key, loc] of Object.entries({ 'plan-price': price, badge: popular, 'plan-cta': cta, 'faq-trigger': faq })) {
  try {
    await loc.scrollIntoViewIfNeeded();
    const states = { default: await loc.evaluate(styleOf) };
    await crop(page, loc, key + '-default.png');
    await loc.hover();
    await page.waitForTimeout(350);
    states.hover = await loc.evaluate(styleOf);
    out.components.pricing[key] = states;
    log('pricing', key);
  } catch (e) { out.components.pricing[key] = { error: e.message.split('\n')[0] }; log('pricing FAIL', key); }
}
try {
  await faq.click();
  await page.waitForTimeout(400);
  out.components.pricing['faq-open'] = await page.locator('.mwm-pricing-faq-trigger').first().evaluate(styleOf);
  await shot(page, 'pricing-dark-faq-open');
  log('faq open');
} catch (e) { log('faq FAIL', e.message.split('\n')[0]); }

// Console sign-in: open the email form, focus the field, type then clear. Never submit.
await open('https://console.mwm.ai/');
await page.waitForTimeout(800);
try {
  await page.locator('button.signin-switch-link').click();
  await page.waitForTimeout(500);
  const email = page.locator('input[type=email]');
  out.components.console = { email: { default: await email.evaluate(styleOf) } };
  await email.click();
  await page.waitForTimeout(250);
  out.components.console.email.focused = await email.evaluate(styleOf);
  await email.fill('measure@example.com');
  await page.waitForTimeout(200);
  out.components.console.email.filled = await email.evaluate(styleOf);
  await email.fill('');
  const submit = page.locator('button.signin-submit');
  out.components.console.submit = { default: await submit.evaluate(styleOf) };
  await submit.hover();
  await page.waitForTimeout(300);
  out.components.console.submit.hover = await submit.evaluate(styleOf);
  await crop(page, page.locator('form, .signin-card, main').first(), 'console-form-default.png');
  await shot(page, 'console-sign-in-dark-email');
  log('console email form measured, cleared, not submitted');
} catch (e) { log('console FAIL', e.message.split('\n')[0]); out.components.console = { error: e.message.split('\n')[0] }; }

// Create sign-in button states. Never click a provider.
await open('https://create.mwm.ai/');
await page.waitForTimeout(800);
try {
  const btn = page.locator('.signin-btn').first();
  out.components.create = { 'provider-button': { default: await btn.evaluate(styleOf) } };
  await btn.hover();
  await page.waitForTimeout(300);
  out.components.create['provider-button'].hover = await btn.evaluate(styleOf);
  await crop(page, btn, 'create-provider-default.png');
  log('create button');
} catch (e) { log('create FAIL', e.message.split('\n')[0]); }

await ctx.close();
await browser.close();
fs.writeFileSync(path.join(KEEP, 'components.json'), JSON.stringify(out, null, 1) + '\n');
log('wrote components.json');
