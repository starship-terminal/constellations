// Measure public Typefully controls. No form is submitted. SSO is not clicked.
//   PLAYWRIGHT=... node measure.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const REF = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = path.join(REF, 'raw');
fs.mkdirSync(RAW, { recursive: true });

const PROPS = ['display','position','width','height','paddingTop','paddingRight','paddingBottom','paddingLeft','gap','borderTopWidth','borderTopStyle','borderTopColor','borderTopLeftRadius','borderTopRightRadius','borderBottomRightRadius','borderBottomLeftRadius','backgroundColor','backgroundImage','color','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','boxShadow','outlineWidth','outlineStyle','outlineColor','outlineOffset','opacity','cursor','transitionDuration','transitionTimingFunction'];

function pick(style) {
  const o = {};
  for (const k of PROPS) o[k] = style[k];
  return o;
}

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, userAgent: UA, locale: 'en-US', colorScheme: 'light' });
const page = await context.newPage();
const cdp = await context.newCDPSession(page);

async function styleOf(locator) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  return page.evaluate((el) => {
    const props = ['display','position','width','height','paddingTop','paddingRight','paddingBottom','paddingLeft','gap','borderTopWidth','borderTopStyle','borderTopColor','borderTopLeftRadius','borderTopRightRadius','borderBottomRightRadius','borderBottomLeftRadius','backgroundColor','backgroundImage','color','fontFamily','fontSize','fontWeight','lineHeight','letterSpacing','boxShadow','outlineWidth','outlineStyle','outlineColor','outlineOffset','opacity','cursor','transitionDuration','transitionTimingFunction'];
    const s = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    const o = { rect: { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height) } };
    for (const k of props) o[k] = s[k];
    const vars = {};
    for (const name of ['--color-typ-accent','--color-typ-c1','--color-typ-c2','--color-typ-bg0','--color-typ-bg1','--accent']) {
      vars[name] = getComputedStyle(el).getPropertyValue(name).trim() || getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    }
    o.vars = vars;
    o.text = (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80);
    return o;
  }, handle);
}

async function force(locator, states) {
  const handle = await locator.elementHandle();
  if (!handle) return null;
  await cdp.send('CSS.enable');
  const { nodeId } = await cdp.send('DOM.requestNode', { objectId: (await handle.evaluateHandle((el) => el))._objectId ? undefined : undefined }).catch(() => ({ nodeId: null }));
  // Use element hover/focus instead of nodeId gymnastics when possible.
  return null;
}

const out = { readAt: new Date().toISOString().slice(0, 10), page: 'https://typefully.com/pricing', components: {} };

await page.goto('https://typefully.com/pricing', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);

const specs = [
  ['button-primary', page.getByRole('button', { name: 'Get started' }).nth(2)],
  ['button-secondary', page.getByRole('button', { name: 'Get started' }).first()],
  ['link-nav', page.getByRole('link', { name: 'Pricing', exact: true }).first()],
  ['link-cta', page.getByRole('link', { name: 'Try Typefully now' }).first()],
  ['heading', page.getByRole('heading', { name: 'Pricing' }).first()],
];

for (const [name, loc] of specs) {
  if (!(await loc.count())) { out.components[name] = { missing: true }; continue; }
  await loc.scrollIntoViewIfNeeded().catch(() => {});
  const base = await styleOf(loc);
  out.components[name] = { default: base };
  await loc.hover().catch(() => {});
  await page.waitForTimeout(250);
  out.components[name].hover = await styleOf(loc);
  await loc.focus().catch(() => {});
  await page.waitForTimeout(150);
  out.components[name].focus = await styleOf(loc);
  console.log(name, base && base.rect, base && base.backgroundColor, base && base.color, base && base.fontSize);
}

// login dialog button on home
await page.goto('https://typefully.com/', { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(1200);
const login = page.getByRole('button', { name: 'Log in', exact: true }).first();
await login.click();
await page.waitForTimeout(700);
const google = page.getByRole('button', { name: 'Google', exact: true }).last();
out.components['button-auth'] = { default: await styleOf(google) };
const email = page.getByRole('button', { name: 'Email', exact: true }).last();
out.components['button-auth-email'] = { default: await styleOf(email) };
await email.click();
await page.waitForTimeout(400);
const field = page.locator('input[type="email"]').first();
out.components['text-field'] = { default: await styleOf(field) };
if (await field.count()) {
  await field.focus();
  out.components['text-field'].focus = await styleOf(field);
}
console.log('auth', JSON.stringify(out.components['button-auth'], null, 0).slice(0, 300));

// docs search
await page.goto('https://typefully.com/docs/api', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1500);
const searchBtn = page.getByRole('button', { name: /Open Search/i }).first();
if (await searchBtn.count()) {
  out.components['button-docs-search'] = { default: await styleOf(searchBtn) };
  await searchBtn.click();
  await page.waitForTimeout(500);
  const input = page.locator('input[placeholder="Search..."]').first();
  out.components['text-field-search'] = { default: await styleOf(input) };
}

fs.writeFileSync(path.join(RAW, 'components-computed.json'), JSON.stringify(out, null, 1) + '\n');
console.log('wrote components', Object.keys(out.components));
await browser.close();
