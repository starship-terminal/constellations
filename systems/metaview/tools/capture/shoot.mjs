// One-shot public capture for Metaview. Writes full-colour PNGs to RAW.
// PLAYWRIGHT=... node shoot.mjs
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from './screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT);
const { chromium } = pw.default ?? pw;
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'metaview', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });

const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const desktop = [
  ['home', 'https://www.metaview.ai/'],
  ['pricing', 'https://www.metaview.ai/pricing'],
  ['demo', 'https://www.metaview.ai/demo'],
  ['fillmore', 'https://www.metaview.ai/fillmore'],
  ['sourcing', 'https://www.metaview.ai/sourcing'],
  ['screening', 'https://www.metaview.ai/screening'],
  ['notes', 'https://www.metaview.ai/interview-notes'],
  ['reports', 'https://www.metaview.ai/reports'],
  ['about', 'https://www.metaview.ai/about'],
  ['integrations', 'https://www.metaview.ai/integrations'],
  ['privacy', 'https://www.metaview.ai/privacy'],
  ['careers', 'https://www.metaview.ai/careers'],
  ['resources', 'https://www.metaview.ai/resources'],
  ['desktop', 'https://www.metaview.ai/desktop'],
];
const mobile = [
  ['home', 'https://www.metaview.ai/'],
  ['pricing', 'https://www.metaview.ai/pricing'],
  ['signin', 'https://app.metaview.ai/auth/sign-in'],
];
const auth = [
  ['signin', 'https://app.metaview.ai/auth/sign-in'],
  ['signup', 'https://app.metaview.ai/auth/sign-up'],
];

const only = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);

async function shot(page, file, requested) {
  await screenshotWithMetadata(page, { path: file }, requested);
  log('  shot', path.basename(file));
}

async function full(page, prefix, vw, dpr, requested) {
  const H = await page.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body ? document.body.scrollHeight : 0));
  const chunk = Math.floor(14000 / dpr);
  const MAXH = 8 * chunk;
  const hCap = Math.min(H, MAXH);
  const f = `${prefix}-full`;
  if (H > MAXH) log(`  ! page is ${H}px, capturing first ${hCap}px`);
  if (hCap <= chunk) {
    await screenshotWithMetadata(page, { path: f + '.png', fullPage: true }, requested);
  } else {
    for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(page, {
        path: `${f}.part${i}.png`, fullPage: true,
        clip: { x: 0, y, width: vw, height: Math.min(chunk, hCap - y) },
      }, requested);
    }
  }
  log('  full H=' + H);
}

const browser = await chromium.launch({ headless: true });

async function runSet(list, { mob, prefix }) {
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  for (const [name, url] of list) {
    const key = prefix + name;
    if (only.length && !only.includes(key) && !only.includes(name)) continue;
    log(key, url);
    const ctx = await browser.newContext({
      viewport: { width: vw, height: vh },
      deviceScaleFactor: dpr,
      userAgent: mob ? UA_MOBILE : UA,
      isMobile: mob,
      hasTouch: mob,
      locale: 'en-US',
    });
    const page = await ctx.newPage();
    const requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: url.split('?')[0] };
    try {
      const res = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      const status = res ? res.status() : 0;
      const title = await page.title();
      log('  status', status, 'title', title.slice(0, 80));
      const body = await page.evaluate(() => (document.body && document.body.innerText || '').slice(0, 180));
      if (/just a moment|cloudflare|cf-challenge|attention required/i.test(title + ' ' + body)) {
        log('  BLOCKED cloudflare, stopping this launch');
        await ctx.close();
        continue;
      }
      await page.waitForTimeout(2500);
      await shot(page, `${RAW}/${key}-light-default.png`, requested);
      await full(page, `${RAW}/${key}-light`, vw, dpr, requested);
    } catch (e) {
      log('  FAILED', e.message.split('\n')[0]);
    }
    await ctx.close();
  }
}

await runSet(desktop, { mob: false, prefix: '' });
await runSet(mobile, { mob: true, prefix: 'mobile-' });
await runSet(auth, { mob: false, prefix: 'auth-' });
await browser.close();
log('done', RAW);
