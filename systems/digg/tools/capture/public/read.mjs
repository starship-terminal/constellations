// Read Digg's public signed-out design system. Writes JSON under RAW (scratch),
// never into the package. Hides the cookie notice. Does not click identity
// providers, submit forms, or type credentials.
//
//   PLAYWRIGHT=... node read.mjs
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'digg', 'readings');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';

const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
});
const page = await context.newPage();
page.setDefaultTimeout(20000);

async function hideConsent(p) {
  await p.addStyleTag({ content: 'section.cookie-notice, .cookie-notice { display: none !important; visibility: hidden !important; pointer-events: none !important; }' }).catch(() => {});
}

async function open(url) {
  const resp = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(1600);
  await hideConsent(page);
  return resp && resp.status();
}

function dumpVars() {
  return page.evaluate(() => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\([^)]*\)/gi, 'url(…)') : v);
    const rules = [];
    const blocked = [];
    const fonts = [];
    const walk = (list, ctx, href) => {
      for (const r of list) {
        if (r.type === CSSRule.STYLE_RULE) {
          const props = {};
          for (let i = 0; i < r.style.length; i++) {
            const name = r.style[i];
            if (name.startsWith('--')) props[name] = noUrl(r.style.getPropertyValue(name).trim());
          }
          if (Object.keys(props).length) rules.push({ selector: r.selectorText, context: ctx, href: href || '', properties: props });
        } else if (r.cssRules) {
          const next = r.conditionText ? ctx.concat(r.cssText.slice(0, r.cssText.indexOf('{')).trim()) : ctx;
          walk(r.cssRules, next, href);
        }
        if (r.type === CSSRule.FONT_FACE_RULE) {
          fonts.push({ family: r.style.getPropertyValue('font-family'), weight: r.style.getPropertyValue('font-weight'), style: r.style.getPropertyValue('font-style'), href: href || '' });
        }
      }
    };
    for (const sheet of document.styleSheets) {
      try { walk(sheet.cssRules, [], sheet.href || ''); }
      catch (e) { blocked.push(sheet.href || 'inline'); }
    }
    const root = getComputedStyle(document.documentElement);
    const names = new Set();
    for (const rule of rules) for (const n of Object.keys(rule.properties)) names.add(n);
    const resolved = {};
    for (const n of names) resolved[n] = noUrl(root.getPropertyValue(n).trim());
    return {
      htmlClass: document.documentElement.className,
      colorScheme: root.colorScheme,
      rules,
      fonts,
      blocked,
      resolved,
    };
  });
}

await open('https://digg.com/');
const light = await dumpVars();
fs.writeFileSync(path.join(RAW, 'vars-light.json'), JSON.stringify(light));
console.log('light rules', light.rules.length, 'names', Object.keys(light.resolved).length, 'blocked', light.blocked.length, 'class', light.htmlClass.slice(0, 80));

// Cycle theme until html has dark (Light -> Dark -> System). Stop after 4 clicks.
let dark = null;
for (let i = 0; i < 4; i++) {
  const cls = await page.evaluate(() => document.documentElement.className);
  if (/\bdark\b/.test(cls)) { dark = await dumpVars(); break; }
  await page.locator('button[aria-label*="Switch theme"]').click();
  await page.waitForTimeout(500);
}
if (!dark) {
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.waitForTimeout(400);
  // click until dark or give up
  for (let i = 0; i < 3; i++) {
    const cls = await page.evaluate(() => document.documentElement.className);
    if (/\bdark\b/.test(cls)) break;
    await page.locator('button[aria-label*="Switch theme"]').click();
    await page.waitForTimeout(400);
  }
  dark = await dumpVars();
}
fs.writeFileSync(path.join(RAW, 'vars-dark.json'), JSON.stringify(dark));
console.log('dark class', dark.htmlClass.slice(0, 120), 'scheme', dark.colorScheme, 'names', Object.keys(dark.resolved).length);

// Tailwind theme keys of interest
const interesting = Object.keys(light.resolved).filter((n) => /color|font|radius|shadow|spacing|ease|duration|ring|sidebar|background|foreground|primary|destructive|muted|accent|border|card|popover/.test(n)).sort();
fs.writeFileSync(path.join(RAW, 'var-names.json'), JSON.stringify(interesting, null, 2));
console.log('interesting', interesting.length);
console.log(interesting.slice(0, 80).join('\n'));

const samples = ['--background', '--foreground', '--primary', '--primary-foreground', '--secondary', '--muted', '--muted-foreground', '--accent', '--border', '--ring', '--card', '--popover', '--destructive', '--sidebar', '--radius', '--font-sans'];
for (const n of samples) console.log('L', n, light.resolved[n], '| D', dark.resolved[n]);

await browser.close();
console.log('wrote', RAW);
