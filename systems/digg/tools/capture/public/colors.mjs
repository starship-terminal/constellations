// Resolve Digg semantic colours to sRGB hex via a probe element. Writes scratch JSON.
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'digg', 'readings');
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, locale: 'en-US' });
const page = await context.newPage();
await page.goto('https://digg.com/', { waitUntil: 'domcontentloaded', timeout: 60000 });
await page.waitForTimeout(1200);
await page.addStyleTag({ content: 'section.cookie-notice{display:none!important}' });

const names = ['background','foreground','card','card-foreground','popover','popover-foreground','primary','primary-foreground','secondary','secondary-foreground','muted','muted-foreground','accent','accent-foreground','destructive','destructive-foreground','border','input','ring','sidebar','sidebar-foreground','sidebar-primary','sidebar-accent','sidebar-border','success','success-foreground','brand-text'];

async function sample(label) {
  return page.evaluate((names) => {
    const probe = document.createElement('div');
    probe.style.cssText = 'position:absolute;left:-9999px;top:0';
    document.body.appendChild(probe);
    const canvas = document.createElement('canvas');
    const ctx = canvas.getContext('2d', { willReadFrequently: true });
    const toHex = (css) => {
      ctx.clearRect(0, 0, 1, 1);
      ctx.fillStyle = '#000';
      ctx.fillStyle = css;
      const serialized = ctx.fillStyle;
      ctx.fillRect(0, 0, 1, 1);
      const [r, g, b, a] = ctx.getImageData(0, 0, 1, 1).data;
      const hex = '#' + [r, g, b].map((n) => n.toString(16).padStart(2, '0')).join('');
      return { css, serialized, hex, alpha: a / 255 };
    };
    const out = {};
    for (const n of names) {
      probe.style.backgroundColor = `var(--${n})`;
      const css = getComputedStyle(probe).backgroundColor;
      out[n] = toHex(css);
    }
    probe.remove();
    return { className: document.documentElement.className, colorScheme: getComputedStyle(document.documentElement).colorScheme, out };
  }, names);
}

const light = await sample('light');
// cycle to dark
for (let i = 0; i < 4; i++) {
  const cls = await page.evaluate(() => document.documentElement.className);
  if (/\bdark\b/.test(cls.split(' '))) break;
  await page.locator('button[aria-label*="Switch theme"]').click();
  await page.waitForTimeout(400);
}
const dark = await sample('dark');
fs.writeFileSync(path.join(RAW, 'colors-computed.json'), JSON.stringify({ light, dark }, null, 2));
console.log('light class', light.className.split(' ').slice(-2));
console.log('dark class', dark.className.split(' ').slice(-2));
for (const n of names) {
  console.log(n.padEnd(24), light.out[n].hex, light.out[n].alpha, '|', dark.out[n].hex, dark.out[n].alpha);
}
await browser.close();
