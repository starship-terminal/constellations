// Measure public RevenueCat components. Hover uses the pointer. Focus uses Tab
// or focus(). Pressed is forced through CSS.forcePseudoState. No form is submitted.
//
//   PLAYWRIGHT=... node tools/capture/public/measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { chromium, UA, BASE, hideConsent, styleOf, RAW, CROPS } from './lib.mjs';

const OUT = path.join(RAW, 'components-computed.json');
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 2,
  userAgent: UA,
  locale: 'en-US',
});
const page = await ctx.newPage();
const cdp = await ctx.newCDPSession(page);

const shots = [];
async function crop(locator, name) {
  const box = await locator.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return null;
  const pad = 8;
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(box.width + pad * 2, 1440 - Math.max(0, box.x - pad)),
    height: Math.min(box.height + pad * 2, 900 - Math.max(0, box.y - pad)),
  };
  const file = path.join(CROPS, name + '.png');
  await locator.page().screenshot({ path: file, clip });
  return { file: 'components/crops/' + name + '.png', clip };
}

async function forceActive(locator, on) {
  const handle = await locator.elementHandle();
  if (!handle) return 'no-handle';
  await cdp.send('CSS.enable');
  await page.evaluate((node) => node.setAttribute('data-rc-press', '1'), handle);
  const doc = await cdp.send('DOM.getDocument');
  const q = await cdp.send('DOM.querySelector', { nodeId: doc.root.nodeId, selector: '[data-rc-press="1"]' });
  if (!q.nodeId) return 'no-node';
  await cdp.send('CSS.forcePseudoState', { nodeId: q.nodeId, forcedPseudoClasses: on ? ['active'] : [] });
  if (!on) await page.evaluate(() => document.querySelector('[data-rc-press]')?.removeAttribute('data-rc-press'));
  return 'ok';
}

async function read(locator, label, { hover = false, focus = false, press = false, cropName = null } = {}) {
  const count = await locator.count();
  if (!count) return { label, missing: true };
  const el = locator.first();
  await el.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(180);
  if (hover) {
    await el.hover().catch(() => {});
    await page.waitForTimeout(220);
  }
  if (focus) {
    await el.focus().catch(() => {});
    await page.waitForTimeout(180);
  }
  let pressVia = null;
  if (press) {
    try { pressVia = await forceActive(el, true); }
    catch (e) { pressVia = 'failed: ' + String(e.message || e).slice(0, 120); }
    await page.waitForTimeout(60);
  }
  const style = await styleOf(el);
  let shot = null;
  if (cropName) shot = await crop(el, cropName).catch((e) => ({ error: String(e.message || e).slice(0, 120) }));
  if (press) await forceActive(el, false).catch(() => {});
  return { label, pressVia, ...style, crop: shot };
}

const findings = { capturedAt: new Date().toISOString().slice(0, 10), viewport: { width: 1440, height: 900, dpr: 2 }, pages: {} };

async function go(pth) {
  console.log('measure', pth);
  await page.goto(BASE + pth, { waitUntil: 'domcontentloaded', timeout: 45000 });
  await page.waitForTimeout(1600);
  await hideConsent(page);
}

await go('/');
const home = {};
home.signup = await read(page.getByRole('link', { name: 'Sign up' }).first(), 'signup-link', { cropName: 'nav-signup-default' });
home.signupHover = await read(page.getByRole('link', { name: 'Sign up' }).first(), 'signup-link-hover', { hover: true, cropName: 'nav-signup-hover' });
home.signupFocus = await read(page.getByRole('link', { name: 'Sign up' }).first(), 'signup-link-focus', { focus: true, cropName: 'nav-signup-focus' });
home.signupPressed = await read(page.getByRole('link', { name: 'Sign up' }).first(), 'signup-link-pressed', { press: true, cropName: 'nav-signup-pressed' });
home.contact = await read(page.getByRole('link', { name: 'Contact sales' }).first(), 'contact-sales', { cropName: 'nav-contact-default' });
home.contactHover = await read(page.getByRole('link', { name: 'Contact sales' }).first(), 'contact-sales-hover', { hover: true, cropName: 'nav-contact-hover' });
home.login = await read(page.getByRole('link', { name: 'Log in' }).first(), 'login-link', { cropName: 'nav-login-default' });
home.loginHover = await read(page.getByRole('link', { name: 'Log in' }).first(), 'login-link-hover', { hover: true, cropName: 'nav-login-hover' });
home.heroCta = await read(page.getByRole('link', { name: 'Start for free' }).first(), 'hero-cta', { cropName: 'hero-cta-default' });
home.heroCtaHover = await read(page.getByRole('link', { name: 'Start for free' }).first(), 'hero-cta-hover', { hover: true, cropName: 'hero-cta-hover' });
home.email = await read(page.locator('input[placeholder*="email" i], input[type="email"]').first(), 'hero-email', { cropName: 'hero-email-default' });
home.emailFocus = await read(page.locator('input[placeholder*="email" i], input[type="email"]').first(), 'hero-email-focus', { focus: true, cropName: 'hero-email-focus' });
home.navTrigger = await read(page.getByRole('button', { name: 'Solutions', exact: true }).first(), 'nav-trigger', { cropName: 'nav-trigger-default' });
home.navTriggerHover = await read(page.getByRole('button', { name: 'Solutions', exact: true }).first(), 'nav-trigger-hover', { hover: true, cropName: 'nav-trigger-hover' });
home.h1 = await read(page.locator('h1').first(), 'home-h1', { cropName: 'home-title-default' });
home.body = await page.evaluate(() => {
  const cs = getComputedStyle(document.body);
  return { backgroundColor: cs.backgroundColor, color: cs.color, fontFamily: cs.fontFamily, fontSize: cs.fontSize, lineHeight: cs.lineHeight };
});
findings.pages.home = home;

await go('/pricing');
const pricing = {};
pricing.h1 = await read(page.locator('h1').first(), 'pricing-h1', { cropName: 'pricing-title-default' });
pricing.tab = await read(page.getByRole('button', { name: 'Growth Tools', exact: true }).first(), 'pricing-tab', { cropName: 'pricing-tab-default' });
pricing.tabHover = await read(page.getByRole('button', { name: 'All features', exact: true }).first(), 'pricing-tab-hover', { hover: true, cropName: 'pricing-tab-hover' });
// click FAQs to reveal an accordion, then measure one row without submitting
const faq = page.getByRole('button', { name: 'FAQs', exact: true }).first();
if (await faq.count()) {
  await faq.click().catch(() => {});
  await page.waitForTimeout(500);
  pricing.faqTab = await read(faq, 'pricing-faq-tab', { cropName: 'pricing-tab-selected' });
}
const acc = page.locator('button').filter({ hasText: /\?$/ }).first();
pricing.accordion = await read(acc, 'faq-accordion', { cropName: 'faq-row-default' });
if (await acc.count()) {
  await acc.click().catch(() => {});
  await page.waitForTimeout(400);
  pricing.accordionOpen = await read(acc, 'faq-accordion-open', { cropName: 'faq-row-open' });
}
findings.pages.pricing = pricing;

await go('/docs');
const docs = {};
docs.search = await read(page.getByRole('button', { name: /Search/ }).first(), 'docs-search', { cropName: 'docs-search-default' });
docs.theme = await read(page.getByRole('button', { name: /dark and light/i }).first(), 'docs-theme-toggle', { cropName: 'docs-theme-toggle-default' });
docs.h1 = await read(page.locator('h1').first(), 'docs-h1', { cropName: 'docs-title-default' });
const themeBtn = page.getByRole('button', { name: /dark and light/i }).first();
if (await themeBtn.count()) {
  await themeBtn.click().catch(() => {});
  await page.waitForTimeout(600);
  docs.darkBody = await page.evaluate(() => {
    const cs = getComputedStyle(document.body);
    const root = getComputedStyle(document.documentElement);
    return {
      backgroundColor: cs.backgroundColor,
      color: cs.color,
      scheme: root.colorScheme,
      className: document.documentElement.className.slice(0, 200),
      dataTheme: document.documentElement.getAttribute('data-theme'),
    };
  });
  docs.h1Dark = await read(page.locator('h1').first(), 'docs-h1-dark', { cropName: 'docs-title-dark' });
}
findings.pages.docs = docs;

await go('/talk-to-sales');
const sales = {};
sales.h1 = await read(page.locator('h1').first(), 'sales-h1', { cropName: 'sales-title-default' });
sales.field = await read(page.locator('input[placeholder="First Name"], input[name="input_1"]').first(), 'sales-field', { cropName: 'sales-field-default' });
sales.fieldFocus = await read(page.locator('input[placeholder="First Name"], input[name="input_1"]').first(), 'sales-field-focus', { focus: true, cropName: 'sales-field-focus' });
sales.submit = await read(page.getByRole('button', { name: /Contact us/i }).first(), 'sales-submit', { cropName: 'sales-submit-default' });
sales.submitHover = await read(page.getByRole('button', { name: /Contact us/i }).first(), 'sales-submit-hover', { hover: true, cropName: 'sales-submit-hover' });
findings.pages.sales = sales;

await go('/changelog');
const log = {};
log.chip = await read(page.getByRole('button', { name: 'All', exact: true }).first(), 'changelog-chip', { cropName: 'changelog-chip-default' });
log.chipHover = await read(page.getByRole('button', { name: 'SDK', exact: true }).first(), 'changelog-chip-hover', { hover: true, cropName: 'changelog-chip-hover' });
const sdk = page.getByRole('button', { name: 'SDK', exact: true }).first();
if (await sdk.count()) {
  await sdk.click().catch(() => {});
  await page.waitForTimeout(400);
  log.chipSelected = await read(sdk, 'changelog-chip-selected', { cropName: 'changelog-chip-selected' });
}
findings.pages.changelog = log;

fs.writeFileSync(OUT, JSON.stringify(findings, null, 2));
console.log('wrote', OUT);
await browser.close();
