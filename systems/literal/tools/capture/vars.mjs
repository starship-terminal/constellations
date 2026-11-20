// Harvest literal.club custom properties from the live page.
//
//   PLAYWRIGHT=... CDP=http://127.0.0.1:9339 node tools/capture/vars.mjs
//
// Writes raw/css-vars.json: declared :root / :root.light / :root.dark /
// :root:not(.light) blocks, plus getComputedStyle resolution in light
// (default) and dark (emulateMedia colorScheme dark).
import fs from 'node:fs';
import path from 'node:path';
import { RAW, launchBrowser, newPage, open } from './public/lib.mjs';

const NAMES = [
  '--textPrimary', '--textSecondary', '--textDiscreet', '--textBlack', '--textDisabled', '--textWhite',
  '--uiBase', '--uiInput', '--uiOutline', '--uiBaseLight', '--uiWhite', '--uiBlack', '--uiSecondary',
  '--uiBoxBackground', '--uiHover', '--uiBackdrop', '--uiOverlayBackground',
  '--accentPrimary', '--accentPrimaryHover', '--accentPrimaryActive', '--accentPrimaryDisabled',
  '--accentAlert', '--accentDanger',
  '--sunny', '--barbie', '--grassy', '--mediterranean', '--atlantis', '--miami', '--smokey',
  '--avatarRadius', '--outlineWidth', '--shadowColor',
  '--zIndexContent', '--zIndexDropdown', '--zIndexHeader', '--zIndexModal', '--zIndexDrawer',
];
for (let i = 1; i <= 40; i++) NAMES.push(`--size-${i}`);

const browser = await launchBrowser();
const page = await newPage({ browser, width: 1440, height: 900, colorScheme: 'light' });
await open(page, 'https://literal.club/', { wait: 1200 });

const declared = await page.evaluate(() => {
  // Each page callback runs apart from this module and needs its own copy.
  const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
  const blocks = [];
  const walk = (list) => {
    for (const r of list) {
      try {
        if (r.style && r.selectorText && /:root|html/.test(r.selectorText)) {
          const vars = {};
          for (const n of r.style) if (n.startsWith('--')) vars[n] = noUrl(r.style.getPropertyValue(n).trim());
          if (Object.keys(vars).length) blocks.push({ selector: r.selectorText, vars });
        }
        if (r.cssRules) walk([...r.cssRules]);
      } catch { /* cross-origin */ }
    }
  };
  for (const sheet of [...document.styleSheets]) {
    try { walk([...sheet.cssRules]); } catch { /* cross-origin */ }
  }
  return blocks;
});

async function resolve(colorScheme) {
  await page.emulateMedia({ colorScheme });
  await page.waitForTimeout(400);
  return page.evaluate((names) => {
    const noUrl = (v) => (typeof v === 'string' ? v.replace(/url\((?!\s*['"]?(?:data:|#))\s*(?:"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|(?:[^)\\]|\\.)*)\s*\)/gi, 'url(…)') : v);
    const cs = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const out = {};
    for (const n of names) out[n] = noUrl(cs.getPropertyValue(n).trim());
    return {
      colorScheme: matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light',
      htmlClass: document.documentElement.className,
      matchDark: matchMedia('(prefers-color-scheme: dark)').matches,
      bodyBackground: body.backgroundColor,
      bodyColor: body.color,
      vars: out,
    };
  }, NAMES);
}

const light = await resolve('light');
const dark = await resolve('dark');
fs.mkdirSync(RAW, { recursive: true });
const out = {
  read: new Date().toLocaleDateString('en-CA'),
  url: 'https://literal.club/',
  note: 'Declared on :root, :root.light, :root.dark and :root:not(.light). Dark resolves when prefers-color-scheme is dark; no public theme toggle was found. :root.dark matches :root:not(.light).',
  declared,
  resolved: { light: light.vars, dark: dark.vars },
  surfaces: { light, dark },
};
fs.writeFileSync(path.join(RAW, 'css-vars.json'), JSON.stringify(out, null, 2) + '\n');
console.log('declared blocks', declared.length, 'light accent', light.vars['--accentPrimary'], 'dark accent', dark.vars['--accentPrimary']);
await page.close();
await browser.close();
