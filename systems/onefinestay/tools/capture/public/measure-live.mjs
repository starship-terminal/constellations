// Read computed styles from the live public homepage. Writes raw/measurements.json.
// No form is filled. Cookie banner is hidden (remove-only) after the page loads
// so header controls can be measured.
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { launch, BASE } from './lib.mjs';

const RAW = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..', 'raw');
fs.mkdirSync(RAW, { recursive: true });

const { browser, context } = await launch({ width: 1440, height: 900 });
const page = await context.newPage();
await page.goto(BASE + '/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(2500);
await page.evaluate(() => {
  const sdk = document.getElementById('onetrust-consent-sdk');
  if (sdk) sdk.style.setProperty('display', 'none', 'important');
});
await page.waitForTimeout(400);

const data = await page.evaluate(() => {
  const pick = (el) => {
    if (!el) return null;
    const cs = getComputedStyle(el);
    const r = el.getBoundingClientRect();
    return {
      tag: el.tagName,
      text: (el.innerText || el.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim().slice(0, 60),
      fontFamily: cs.fontFamily,
      fontSize: cs.fontSize,
      fontWeight: cs.fontWeight,
      lineHeight: cs.lineHeight,
      letterSpacing: cs.letterSpacing,
      color: cs.color,
      backgroundColor: cs.backgroundColor,
      borderTopColor: cs.borderTopColor,
      borderTopWidth: cs.borderTopWidth,
      borderRadius: cs.borderRadius,
      padding: cs.padding,
      height: Math.round(r.height) + 'px',
      boxShadow: cs.boxShadow === 'none' ? 'none' : cs.boxShadow.slice(0, 180),
      textTransform: cs.textTransform,
    };
  };
  const q = (sel) => document.querySelector(sel);
  const byText = (sel, re) => [...document.querySelectorAll(sel)].find((el) => re.test((el.innerText || '').trim()) && el.getBoundingClientRect().height > 0);
  const root = getComputedStyle(document.documentElement);
  const vars = {};
  for (const sheet of document.styleSheets) {
    let rules;
    try { rules = sheet.cssRules; } catch { continue; }
    const walk = (rs) => {
      if (!rs) return;
      for (const rule of rs) {
        if (rule.style) {
          for (const prop of rule.style) {
            if (prop.startsWith('--') && !prop.startsWith('--tw-')) vars[prop] = rule.style.getPropertyValue(prop).trim().slice(0, 120);
          }
        }
        if (rule.cssRules) walk(rule.cssRules);
      }
    };
    walk(rules);
  }
  const resolved = {};
  for (const name of Object.keys(vars)) resolved[name] = root.getPropertyValue(name).trim().slice(0, 120);
  return {
    title: document.title,
    viewport: { innerWidth, innerHeight, devicePixelRatio },
    colorScheme: root.colorScheme,
    background: root.backgroundColor,
    vars,
    resolved,
    elements: {
      body: pick(document.body),
      inquire: pick(q('a[aria-label="Inquire Now"]')),
      destinations: pick(q('a[aria-label="Destinations"]')),
      logo: pick(q('a[aria-label="onefinestay homepage"]')),
      h2: pick(document.querySelector('h2')),
      paragraph: pick(document.querySelector('main p, #main p, p')),
      dates: pick(byText('button, div, span', /^Dates$/)),
    },
  };
});

// Hover the Inquire button and read it again.
await page.locator('a[aria-label="Inquire Now"]').first().hover();
await page.waitForTimeout(400);
data.elements.inquireHover = await page.evaluate(() => {
  const el = document.querySelector('a[aria-label="Inquire Now"]');
  const cs = getComputedStyle(el);
  return { color: cs.color, backgroundColor: cs.backgroundColor, borderTopColor: cs.borderTopColor };
});
await page.locator('a[aria-label="Inquire Now"]').first().focus();
await page.waitForTimeout(200);
data.elements.inquireFocus = await page.evaluate(() => {
  const el = document.querySelector('a[aria-label="Inquire Now"]');
  const cs = getComputedStyle(el);
  return { outline: cs.outline, outlineColor: cs.outlineColor, boxShadow: cs.boxShadow.slice(0, 180), color: cs.color, backgroundColor: cs.backgroundColor };
});

fs.writeFileSync(path.join(RAW, 'measurements.json'), JSON.stringify(data, null, 2));
const brand = Object.keys(data.vars).filter((k) => /brand|color|font|radius|shadow/.test(k));
console.log('vars', Object.keys(data.vars).length, 'brandish', brand.length);
console.log(JSON.stringify({ elements: data.elements, colorScheme: data.colorScheme, viewport: data.viewport }, null, 2));
console.log('sample vars', brand.slice(0, 40).map((k) => k + '=' + data.resolved[k]).join('\n'));
await browser.close();
