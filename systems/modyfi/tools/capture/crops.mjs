// Element crops from the archived homepage, read before any hover.
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const CROPS = path.join(PKG, 'components', 'crops');
fs.mkdirSync(CROPS, { recursive: true });
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const browser = await chromium.launch();
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 2 });
const page = await context.newPage();
await page.goto('https://web.archive.org/web/20250219221151/https://www.modyfi.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
await page.waitForTimeout(4000);
await page.evaluate(() => {
  document.querySelectorAll('#wm-ipp-base, #wm-ipp, [id^="wm-ipp"]').forEach((x) => x.style.setProperty('display', 'none', 'important'));
});
const shots = {
  'nav-default': '.rl_navbar2_component',
  'nav-link-default': 'a.rl_navbar2_link',
  'signup-button-default': 'a.rl_navbar2_button.w-button:not(.loginbutton)',
  'login-button-default': 'a.rl_navbar2_button.loginbutton.w-button',
  'hero-title-default': 'h1',
  'hero-body-default': 'p.rl-text-style-medium-8',
  'cta-button-default': 'a.rl-button',
  'section-title-default': 'h2',
};
const measured = {};
for (const [name, sel] of Object.entries(shots)) {
  const el = page.locator(sel).first();
  if (!(await el.count())) { console.log('missing', name); continue; }
  const box = await el.boundingBox();
  const style = await el.evaluate((node) => {
    const s = getComputedStyle(node);
    return {
      color: s.color, backgroundColor: s.backgroundColor, borderTopColor: s.borderTopColor,
      borderTopWidth: s.borderTopWidth, borderRadius: s.borderRadius, fontFamily: s.fontFamily,
      fontSize: s.fontSize, fontWeight: s.fontWeight, lineHeight: s.lineHeight, letterSpacing: s.letterSpacing,
      paddingTop: s.paddingTop, paddingLeft: s.paddingLeft, text: (node.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 80),
    };
  });
  measured[name] = style;
  await el.screenshot({ path: path.join(CROPS, name + '.png') });
  console.log('crop', name, box && Math.round(box.width), style.backgroundColor, style.color);
}
const signup = page.locator('a.rl_navbar2_button.w-button:not(.loginbutton)').first();
await signup.hover();
await page.waitForTimeout(400);
const hover = await signup.evaluate((node) => {
  const s = getComputedStyle(node);
  return { color: s.color, backgroundColor: s.backgroundColor, borderTopColor: s.borderTopColor, borderRadius: s.borderRadius };
});
measured['signup-button-hover'] = hover;
await signup.screenshot({ path: path.join(CROPS, 'signup-button-hover.png') });
console.log('hover', hover);
fs.writeFileSync(path.join(PKG, 'raw', 'crops-measured.json'), JSON.stringify(measured, null, 2) + '\n');
await browser.close();
