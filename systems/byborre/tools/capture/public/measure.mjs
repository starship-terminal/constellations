// Measures byborre.com public controls. Nothing is typed or submitted.
// Login fields are measured empty. PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { BASE, chromium, patch, UA, UA_MOBILE, closePromo, styleOf, crop, centre, RAW, clearChallenge } from './lib.mjs';

fs.mkdirSync(RAW, { recursive: true });
const OUT = path.join(RAW, 'components-computed.json');
const out = { _meta: { product: 'byborre.com', captured: '2026-11-21', route: 'public-web' }, components: {} };
const log = (...a) => console.log(...a);

async function open(browser, url, mobile = false) {
  const ctx = await browser.newContext(mobile
    ? { viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, userAgent: UA_MOBILE, isMobile: true, hasTouch: true, locale: 'en-US' }
    : { viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, userAgent: UA, locale: 'en-US' });
  await patch(ctx);
  const page = await ctx.newPage();
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1600);
  if (!(await clearChallenge(page))) log('  challenge?', url);
  await closePromo(page);
  await page.addStyleTag({ content: '*{caret-color:transparent!important}' }).catch(() => {});
  return { page, ctx };
}

async function measure(page, key, state, loc, meta) {
  const c = (out.components[key] ??= { ...meta, states: {} });
  Object.assign(c, meta);
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) {
    c.states[state] = { error: 'missing' };
    log('  ! missing', key, state);
    return;
  }
  try {
    await centre(target);
    const s = await styleOf(target);
    let file;
    try { file = await crop(page, target, `${key}-${state}`, 6); } catch (e) { s.cropError = String(e.message).slice(0, 140); }
    c.states[state] = { ...s, crop: file };
    log('  ', key, state, s.rect && (s.rect.w + 'x' + s.rect.h));
  } catch (e) {
    c.states[state] = { error: String(e.message).slice(0, 180) };
    log('  !', key, state, String(e.message).split('\n')[0]);
  }
}

async function states(page, key, loc, meta) {
  await measure(page, key, 'default', loc, meta);
  const target = loc.filter({ visible: true }).first();
  if (!(await target.count())) return;
  try {
    await target.hover({ timeout: 3000 });
    await page.waitForTimeout(250);
    await measure(page, key, 'hover', loc, meta);
  } catch { /* hover optional */ }
  try {
    await target.focus();
    await page.waitForTimeout(200);
    await measure(page, key, 'focus-visible', loc, meta);
  } catch { /* not focusable */ }
}

const browser = await chromium.launch({ headless: true });

{
  const { page, ctx } = await open(browser, BASE + '/');
  await states(page, 'nav-link', page.getByRole('link', { name: 'Textile Room' }).first(), { title: 'Header nav link', group: 'link', page: 'home' });
  await states(page, 'nav-menu', page.getByRole('button', { name: 'Collaborations' }).first(), { title: 'Header menu button', group: 'button', page: 'home' });
  await states(page, 'hero-cta', page.getByRole('link', { name: 'Explore samples' }).first(), { title: 'Hero button', group: 'button', page: 'home' });
  await states(page, 'cart-button', page.getByRole('button', { name: 'Cart' }).first(), { title: 'Cart icon button', group: 'icon-button', page: 'home' });
  await states(page, 'account-button', page.locator('header button:visible').last(), { title: 'Account icon button', group: 'icon-button', page: 'home' });
  await states(page, 'footer-link', page.getByRole('link', { name: 'Team' }).first(), { title: 'Footer link', group: 'link', page: 'home' });
  await page.getByRole('button', { name: 'Cart' }).first().click();
  await page.waitForTimeout(500);
  await measure(page, 'cart-panel', 'default', page.locator('text=Your cart is empty').locator('xpath=ancestor::div[contains(@class,"rounded")]').first(), { title: 'Empty cart drawer', group: 'dialog', page: 'home' });
  await measure(page, 'cart-close', 'default', page.getByRole('button', { name: 'Close', exact: true }), { title: 'Cart close', group: 'button', page: 'home' });
  await page.keyboard.press('Escape');
  await page.locator('header button:visible').last().click();
  await page.waitForTimeout(700);
  await measure(page, 'login-title', 'default', page.getByText('Log in to continue', { exact: true }), { title: 'Login heading', group: 'dialog', page: 'login' });
  await measure(page, 'login-email', 'default', page.locator('input[name="email"]'), { title: 'Login email field', group: 'text-field', page: 'login' });
  await page.locator('input[name="email"]').focus();
  await page.waitForTimeout(200);
  await measure(page, 'login-email', 'focused', page.locator('input[name="email"]'), { title: 'Login email field', group: 'text-field', page: 'login' });
  await measure(page, 'login-password', 'default', page.locator('input[name="password"]'), { title: 'Login password field', group: 'text-field', page: 'login' });
  await measure(page, 'login-submit', 'default', page.getByRole('button', { name: 'Login' }), { title: 'Login submit', group: 'button', page: 'login' });
  await measure(page, 'login-signup', 'default', page.getByRole('button', { name: 'Sign up', exact: true }), { title: 'Sign up switch', group: 'button', page: 'login' });
  await ctx.close();
}

{
  const { page, ctx } = await open(browser, BASE + '/collection');
  await states(page, 'page-title', page.getByRole('heading', { name: 'Textile Room' }), { title: 'Page title', group: 'type', page: 'collection' });
  await states(page, 'filter-button', page.getByRole('button', { name: 'Pattern' }).first(), { title: 'Pattern filter', group: 'button', page: 'collection' });
  await states(page, 'color-swatch', page.locator('input[name^="color-select"]').nth(1), { title: 'Color filter swatch', group: 'checkbox', page: 'collection' });
  await measure(page, 'textile-card', 'default', page.locator('a[href*="/collection/blink"]').first(), { title: 'Textile card', group: 'card', page: 'collection' });
  await page.locator('a[href*="/collection/blink"]').first().hover().catch(() => {});
  await page.waitForTimeout(300);
  await measure(page, 'textile-card', 'hover', page.locator('a[href*="/collection/blink"]').first(), { title: 'Textile card', group: 'card', page: 'collection' });
  await ctx.close();
}

{
  const { page, ctx } = await open(browser, BASE + '/collection/blink?color=orange&shade=balance');
  await measure(page, 'product-title', 'default', page.getByRole('heading', { name: 'Blink' }).first(), { title: 'Textile name', group: 'type', page: 'textile' });
  await states(page, 'order-sample', page.getByRole('button', { name: 'Order sample' }).first(), { title: 'Order sample bar', group: 'button', page: 'textile' });
  await states(page, 'tone-card', page.getByText('BALANCE', { exact: true }).first(), { title: 'Tone card', group: 'radio', page: 'textile' });
  await states(page, 'accordion', page.getByRole('button', { name: 'Material' }).first(), { title: 'Detail accordion', group: 'button', page: 'textile' });
  await measure(page, 'badge', 'default', page.getByText('Collaboration', { exact: true }).first(), { title: 'Collaboration badge', group: 'badge', page: 'textile' });
  await ctx.close();
}

{
  const { page, ctx } = await open(browser, BASE + '/contact');
  await measure(page, 'field', 'default', page.locator('input[name="firstname"]'), { title: 'Contact text field', group: 'text-field', page: 'contact' });
  await page.locator('input[name="firstname"]').focus();
  await measure(page, 'field', 'focused', page.locator('input[name="firstname"]'), { title: 'Contact text field', group: 'text-field', page: 'contact' });
  await measure(page, 'select', 'default', page.locator('select[name="inquiry"]'), { title: 'Contact select', group: 'select', page: 'contact' });
  await measure(page, 'textarea', 'default', page.locator('textarea[name="project_description"]'), { title: 'Contact textarea', group: 'text-area', page: 'contact' });
  await measure(page, 'submit', 'default', page.getByRole('button', { name: 'Submit' }), { title: 'Contact submit', group: 'button', page: 'contact' });
  await ctx.close();
}

{
  const { page, ctx } = await open(browser, BASE + '/', true);
  await page.getByRole('button', { name: 'Open menu' }).click();
  await page.waitForTimeout(500);
  await measure(page, 'm-menu-button', 'default', page.getByRole('button', { name: 'Close menu' }), { title: 'Mobile close', group: 'icon-button', page: 'mobile-home' });
  await measure(page, 'm-nav-item', 'default', page.getByRole('link', { name: 'Textile Room' }).first(), { title: 'Mobile nav item', group: 'link', page: 'mobile-home' });
  await measure(page, 'm-login', 'default', page.getByRole('button', { name: 'Login/Sign-up' }), { title: 'Mobile login row', group: 'button', page: 'mobile-home' });
  await ctx.close();
}

fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');
log('wrote', OUT, Object.keys(out.components).length, 'components');
await browser.close();
