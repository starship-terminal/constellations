// Second measurement pass: pricing cards, hero email, focus ring, badge, navbar.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execFileSync } from 'node:child_process';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const PYTHON = process.env.PYTHON || 'python3';
const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
const RAW = path.join(PKG, 'raw');
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const log = (...a) => console.log(...a);
function quantize(file) {
  execFileSync(PYTHON, ['-c', 'import sys\nfrom PIL import Image\nf=sys.argv[1]\nim=Image.open(f).convert("RGB")\nif im.width*im.height>1200000: im=im.resize((im.width//2, im.height//2), Image.LANCZOS)\nim.quantize(256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(f, optimize=True)', file]);
}
const reader = () => (el) => {
  const props = ['paddingTop','paddingRight','paddingBottom','paddingLeft','gap','borderTopWidth','borderTopStyle','borderTopColor','borderTopLeftRadius','backgroundColor','boxShadow','outlineWidth','outlineStyle','outlineColor','outlineOffset','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','color','textTransform'];
  const cs = getComputedStyle(el);
  const r = el.getBoundingClientRect();
  const style = {};
  for (const p of props) style[p] = cs[p];
  return {
    tag: el.tagName.toLowerCase(),
    classes: [...el.classList].slice(0, 5).join(' '),
    text: (el.innerText || el.getAttribute('placeholder') || '').trim().replace(/\s+/g, ' ').slice(0, 80),
    rect: { w: +r.width.toFixed(1), h: +r.height.toFixed(1) },
    style,
  };
};
const browser = await chromium.launch({ headless: true });
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2, userAgent: UA, locale: 'en-US' });
const page = await ctx.newPage();
const read = reader();
const extra = {};
async function crop(loc, name) {
  const file = path.join(CROPS, name + '.png');
  await loc.evaluate((el) => el.scrollIntoView({ block: 'center' }));
  await page.waitForTimeout(200);
  const box = await loc.boundingBox();
  const vp = page.viewportSize();
  const pad = 14;
  await page.screenshot({ path: file, clip: {
    x: Math.max(0, box.x - pad), y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  }, animations: 'disabled' });
  quantize(file);
}
async function grab(key, loc, name) {
  const el = loc.first();
  if (!(await el.count())) { log('miss', key); return; }
  extra[key] = await el.evaluate(read);
  try { await crop(el, name); extra[key].crop = 'components/crops/' + name + '.png'; } catch (e) { extra[key].cropError = String(e.message).slice(0, 80); }
  log(key, extra[key].rect, extra[key].style.backgroundColor, extra[key].style.color, extra[key].style.fontSize, extra[key].style.borderTopLeftRadius, extra[key].text.slice(0, 40));
}
await page.goto('https://www.mural.co/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await page.addStyleTag({ content: '[class*=pendo-],#onetrust-consent-sdk{display:none!important}' });
await grab('navbar', page.locator('.navbar_v2_component, .w-nav').first(), 'navbar-default');
await grab('hero-email', page.locator('input[type=email], input[placeholder*="email" i]').first(), 'hero-email-default');
const started = page.locator('a,button').filter({ hasText: 'Get started free' }).first();
await grab('button-jade', started, 'button-jade-default');
await started.hover().catch(() => {});
await page.waitForTimeout(400);
await grab('button-jade-hover', started, 'button-jade-hover');
// focus the hero email via keyboard
const email = page.locator('input[placeholder*="email" i]').first();
await email.focus();
await page.keyboard.press('Shift+Tab');
await page.keyboard.press('Tab');
await page.waitForTimeout(250);
await grab('hero-email-focus', email, 'hero-email-focus');
const focusDump = await email.evaluate((el) => {
  const cs = getComputedStyle(el);
  return { outline: cs.outline, shadow: cs.boxShadow, border: cs.borderTopWidth + ' ' + cs.borderTopColor, ring: cs.getPropertyValue('--tw-ring-color') };
});
log('hero focus', focusDump);

await page.goto('https://www.mural.co/pricing', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
await page.addStyleTag({ content: '[class*=pendo-],#onetrust-consent-sdk,[class*=qualified],[id*=qualified]{display:none!important}' });
await grab('plan-free', page.locator('.pricing-card_component').nth(0), 'plan-free-default');
await grab('plan-business', page.locator('.pricing-card_component').nth(2), 'plan-business-default');
await grab('badge', page.locator('text=MOST POPULAR').first(), 'badge-popular');
const price = page.locator('.pricing-card_component').nth(2).locator('[class*=price], [class*=value]').first();
await grab('price-figure', page.locator('.pricing-card_value-wrapper').nth(2), 'price-figure');
// hide chat widget more aggressively and reshoot pricing viewport
await page.evaluate(() => {
  document.querySelectorAll('iframe, [class*=qualified], [id*=qualified], [class*=chat]').forEach((n) => {
    if (n.getBoundingClientRect().width < 500) n.style.setProperty('display', 'none', 'important');
  });
});
await page.evaluate(() => scrollTo(0, 520));
await page.waitForTimeout(400);
await page.screenshot({ path: '/tmp/mural-look/pricing-cards.png', animations: 'disabled' });

await page.goto('https://app.mural.co/signin', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2000);
const field = page.locator('#work-email-input');
await field.focus();
await page.keyboard.down('Shift');
await page.keyboard.press('Tab');
await page.keyboard.up('Shift');
await page.keyboard.press('Tab');
await page.waitForTimeout(300);
const ring = await field.evaluate((el) => {
  const cs = getComputedStyle(el);
  let n = el, chain = [];
  for (let i = 0; i < 4 && n; i++, n = n.parentElement) {
    const c = getComputedStyle(n);
    chain.push({ tag: n.tagName, cls: (n.className||'').toString().slice(0,60), outline: c.outline, shadow: c.boxShadow, border: c.borderTopWidth+' '+c.borderTopColor, radius: c.borderTopLeftRadius });
  }
  return { active: document.activeElement === el, outline: cs.outline, shadow: cs.boxShadow, border: cs.border, chain };
});
log('signin focus', JSON.stringify(ring));
await grab('field-focus', field, 'text-field-focus-visible');
const pageBg = await page.evaluate(() => {
  const b = getComputedStyle(document.body);
  const main = document.querySelector('main, [class*=login], [class*=auth], form');
  let card = document.querySelector('form')?.parentElement;
  const chain = [];
  for (let n = document.querySelector('h1'), i = 0; n && i < 6; n = n.parentElement, i++) {
    const c = getComputedStyle(n);
    chain.push({ tag: n.tagName, cls: (n.className||'').toString().slice(0,50), bg: c.backgroundColor, w: n.getBoundingClientRect().width });
  }
  return { body: b.backgroundColor, html: getComputedStyle(document.documentElement).backgroundColor, chain };
});
log('auth bg', JSON.stringify(pageBg));
fs.writeFileSync(path.join(RAW, 'components-extra.json'), JSON.stringify({ extra, ring, pageBg }, null, 1));
await browser.close();
log('done');
