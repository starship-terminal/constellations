// Measures Typeform's public components without signing in or submitting.
//
//   PLAYWRIGHT=... node tools/capture/public/measure.mjs
//
// Writes raw/components-computed.json and crops under components/crops/.
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';
import { launch, hideConsent, hoverMenu, dismissAnnouncement, BASE, RAW, CROPS, PROPS } from './lib.mjs';

const PYTHON = process.env.PYTHON || 'python3';
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(CROPS, { recursive: true });

const out = { _meta: { source: 'https://www.typeform.com/ public, signed out, 2026-11-21', viewport: '1440x900', theme: 'light' }, components: {} };

function save() {
  fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
}

async function read(page, handle, states) {
  return page.evaluate((el, { props, states }) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const base = {};
    for (const p of props) base[p] = cs[p];
    base.rect = { x: r.x, y: r.y, w: r.width, h: r.height };
    base.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    base.tag = el.tagName.toLowerCase();
    return { default: base, states };
  }, { props: PROPS, states }).catch(() => null);
}

async function crop(page, handle, name) {
  const box = await handle.boundingBox();
  if (!box || box.width < 2 || box.height < 2) return;
  const pad = 8;
  const vp = page.viewportSize();
  const clip = {
    x: Math.max(0, box.x - pad),
    y: Math.max(0, box.y - pad),
    width: Math.min(vp.width - Math.max(0, box.x - pad), box.width + pad * 2),
    height: Math.min(vp.height - Math.max(0, box.y - pad), box.height + pad * 2),
  };
  if (clip.width < 2 || clip.height < 2) return;
  const file = path.join(CROPS, name + '.png');
  await page.screenshot({ path: file, clip });
  execFileSync(PYTHON, ['-c', `
from PIL import Image
im = Image.open(${JSON.stringify(file)}).convert('RGB')
im.quantize(colors=256, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(${JSON.stringify(file)}, optimize=True)
`]);
}

async function statesOf(page, handle, name) {
  const reading = { name };
  await handle.scrollIntoViewIfNeeded().catch(() => {});
  await page.waitForTimeout(200);
  const box = await handle.boundingBox();
  if (!box) { reading.miss = true; return reading; }
  reading.default = await handle.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = {};
    for (const p of props) o[p] = cs[p];
    o.rect = { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) };
    o.text = (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return o;
  }, PROPS);
  await crop(page, handle, name + '-default');
  const cx = box.x + Math.min(box.width / 2, 40);
  const cy = box.y + Math.min(box.height / 2, 16);
  await page.mouse.move(cx, cy);
  await page.waitForTimeout(250);
  reading.hover = await handle.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const o = {};
    for (const p of props) o[p] = cs[p];
    return o;
  }, PROPS);
  await crop(page, handle, name + '-hover');
  await handle.focus().catch(() => {});
  await page.keyboard.press('Shift+Tab').catch(() => {});
  await page.keyboard.press('Tab').catch(() => {});
  await page.waitForTimeout(150);
  reading.focus = await handle.evaluate((el, props) => {
    const cs = getComputedStyle(el);
    const active = document.activeElement === el || el.contains(document.activeElement);
    const o = { active };
    for (const p of props) o[p] = cs[p];
    return o;
  }, PROPS);
  if (reading.focus.active) await crop(page, handle, name + '-focus-visible');
  await page.mouse.move(8, 8);
  return reading;
}

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(3500);
await hideConsent(page);
await dismissAnnouncement(page);

const specs = [
  ['button-primary', 'a.button, a.btn, a[class*="button"]'],
  ['nav-link', 'a.nav_link, [aria-label="open products dropdown menu"]'],
  ['header', 'header, .nav_component, .navbar'],
];

// Prefer role-based finds that survive Webflow class hashes.
async function first(sel) {
  const loc = page.locator(sel).first();
  if (await loc.count() && await loc.isVisible().catch(() => false)) return loc;
  return null;
}

const finds = [
  ['button-primary', async () => first('a:has-text("Sign up")')],
  ['button-secondary', async () => first('a:has-text("Contact sales")')],
  ['link-login', async () => first('a:has-text("Log in")')],
  ['nav-platform', async () => first('[aria-label="open products dropdown menu"]')],
  ['header', async () => first('header, .navbar, .nav_component')],
  ['hero-heading', async () => first('h1, h2')],
  ['announcement', async () => first('[class*="announcement"], [class*="banner"]')],
];

for (const [name, fn] of finds) {
  const loc = await fn();
  if (!loc) { out.components[name] = { miss: true }; console.log('miss', name); continue; }
  out.components[name] = await statesOf(page, loc, name);
  console.log('measured', name, out.components[name].default && out.components[name].default.backgroundColor, out.components[name].default && out.components[name].default.fontSize);
}
save();

// pricing page buttons and cards
await page.goto(BASE + '/pricing', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(3000);
await hideConsent(page);
await dismissAnnouncement(page);
const priceFinds = [
  ['billing-yearly', async () => first('button:has-text("Yearly")')],
  ['billing-monthly', async () => first('button:has-text("Monthly")')],
  ['plan-card', async () => first('[class*="pricing_card"], [class*="plan-card"], [class*="price-card"]')],
];
for (const [name, fn] of priceFinds) {
  const loc = await fn();
  if (!loc) { out.components[name] = { miss: true, page: 'pricing' }; console.log('miss', name); continue; }
  out.components[name] = await statesOf(page, loc, name);
  out.components[name].page = 'pricing';
  console.log('measured', name);
}
save();

// menu
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(2500);
await hideConsent(page);
await dismissAnnouncement(page);
if (await hoverMenu(page, 'open products dropdown menu')) {
  const menu = page.locator('#w-dropdown-list-0, .nav_dropdown-wrapper.w--open').first();
  if (await menu.count()) {
    out.components['nav-menu'] = await statesOf(page, menu, 'nav-menu');
    const item = page.locator('#w-dropdown-list-0 a').first();
    if (await item.count()) out.components['nav-menu-item'] = await statesOf(page, item, 'nav-menu-item');
  }
}
save();

// template preview dialog
await page.goto(BASE + '/templates/nps-survey-template', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(3000);
await hideConsent(page);
const preview = page.locator('[aria-label="open template preview"]').first();
if (await preview.count()) {
  await preview.click();
  await page.waitForTimeout(800);
  const dialog = page.locator('[role="dialog"], [class*="modal"]').first();
  if (await dialog.count() && await dialog.isVisible().catch(() => false)) {
    out.components['template-dialog'] = await statesOf(page, dialog, 'template-dialog');
  }
}
save();
console.log('components', Object.keys(out.components).length);
await browser.close();
