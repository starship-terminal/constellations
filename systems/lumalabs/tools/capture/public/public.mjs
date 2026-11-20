// Captures Luma AI's public pages into RAW (full-colour PNGs).
// quantize.py turns them into screenshots/.
//
//   PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Desktop shots are 1440x900 at 1x. Mobile shots are 390x844 at 2x.
// Names are {page}-light-{state}.png. Mobile names get a mobile- prefix.
// Nothing is submitted. Sign-in, Google, Apple, and form fields are not used.
// A control that leaves lumalabs.ai for an account host is recorded and skipped.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { screenshotWithMetadata } from '../screenshot.mjs';

const pw = await import(process.env.PLAYWRIGHT || 'playwright');
const { chromium } = pw.default ?? pw;

const BASE = 'https://lumalabs.ai';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36';
const UA_MOBILE = 'Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.0 Mobile/15E148 Safari/604.1';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'lumalabs', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const PAGES = {
  home: '/',
  app: '/app',
  pricing: '/pricing',
  api: '/api',
  enterprise: '/enterprise',
  mcp: '/mcp',
  news: '/news',
  careers: '/careers',
  ray: '/ray',
  uni1: '/uni-1',
  'learning-center': '/learning-center',
  'create-video': '/create/ai-video-generator',
  'create-image': '/create/ai-video-generator-from-image',
  about: '/about',
  'case-studies': '/case-studies',
  'creative-partner': '/creative-partner-program',
  educator: '/education/educator',
  student: '/education/student',
  'terms': '/legal/terms-of-service',
  privacy: '/legal/privacy-policy',
  cookies: '/legal/cookie-policy',
  subprocessors: '/legal/subprocessors',
  'agents-guide': '/agents-guide',
  changelog: '/changelog',
  'contact-sales': '/contact-sales',
  dreamlab: '/dreamlab/featured',
  'llm-info': '/llm-info',
  'series-b': '/series-b',
  'trend-report': '/the-state-of-ai-2026-annual-trend-report',
  whitepaper: '/whitepaper',
  'uni1-showcase': '/uni-1/showcase',
  photon: '/photon',
  'news-ray32': '/news/introducing-ray-3-2',
  'news-skills': '/news/luma-skills',
  'case-aperture': '/case-studies/aperture',
  'learn-article': '/learning-center/articles/luma-connectors',
};

async function lazyScroll(p) {
  const h = await p.evaluate(() => document.documentElement.scrollHeight);
  const cap = Math.min(h, 6000);
  for (let y = 0; y < cap; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: null };
    this.count = 0;
  }
  async view(name) {
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full') {
    const p = this.p;
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(14000 / this.dpr);
    const f = `${RAW}/${this.prefix}-${name}`;
    for (const old of fs.readdirSync(RAW).filter((n) => n.startsWith(`${path.basename(f)}.part`) || n.startsWith(`${this.prefix}-${name}.part`))) {
      fs.unlinkSync(`${RAW}/${old}`);
    }
    const MAXH = 8 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, {
          path: `${f}.part${i}.png`, fullPage: true,
          clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) },
        }, this.requested);
      }
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

async function hideConsent(p) {
  await p.evaluate(() => {
    for (const el of document.querySelectorAll('[id*="cookie" i],[class*="cookie" i],[id*="consent" i],[class*="consent" i]')) {
      const t = (el.innerText || '').slice(0, 400);
      if (/cookie|consent|privacy preference/i.test(t) && el.getBoundingClientRect().height > 40) {
        el.style.setProperty('display', 'none', 'important');
      }
    }
  }).catch(() => {});
}

async function clickNamed(p, role, name) {
  const loc = p.getByRole(role, { name, exact: false }).first();
  if (!(await loc.count())) return false;
  await loc.click({ timeout: 4000 }).catch(() => {});
  await wait(p, 500);
  return true;
}

const interactions = {
  home: async (p, S, mob) => {
    await S.view('prompt');
    await clickNamed(p, 'button', 'Product Hero Shots');
    await S.view('chip');
    if (mob) {
      const menu = p.getByRole('button', { name: 'Toggle mobile navigation menu' }).first();
      if (await menu.count()) {
        await menu.click().catch(() => {});
        await wait(p, 700);
        await S.view('nav-open');
        await p.keyboard.press('Escape').catch(() => {});
        await wait(p, 300);
      }
    }
  },
  app: async (p, S) => {
    await clickNamed(p, 'button', 'Yearly');
    await S.view('yearly');
    await clickNamed(p, 'button', 'What is Luma Agents?');
    await S.view('faq-open');
  },
  pricing: async (p, S) => {
    await clickNamed(p, 'button', 'Yearly');
    await S.view('yearly');
  },
  api: async (p, S) => {
    await clickNamed(p, 'button', 'Uni-1.1');
    await S.view('uni-tab');
    await clickNamed(p, 'button', 'What key capabilities are available via the API?');
    await S.view('faq-open');
  },
  enterprise: async (p, S) => {
    const sel = p.getByRole('button', { name: 'Select an industry' }).first();
    if (await sel.count()) {
      await sel.click().catch(() => {});
      await wait(p, 500);
      await S.view('select-open');
      await p.keyboard.press('Escape').catch(() => {});
    }
  },
  mcp: async (p, S) => {
    await clickNamed(p, 'button', 'ChatGPT');
    await S.view('chatgpt-tab');
    await clickNamed(p, 'button', '2 Or add Luma AI by hand');
    await S.view('step-open');
  },
  careers: async (p, S) => {
    await clickNamed(p, 'button', 'All departments');
    await S.view('filter-open');
    await p.keyboard.press('Escape').catch(() => {});
  },
  uni1: async (p, S) => {
    await clickNamed(p, 'button', 'Go to slide 3');
    await S.view('slide-3');
  },
  'case-studies': async (p, S) => {
    await clickNamed(p, 'button', 'Agency');
    await S.view('filter-agency');
  },
  photon: async (p, S) => {
    await clickNamed(p, 'button', 'Next');
    await S.view('next');
  },
  'learning-center': async (p, S) => {
    await clickNamed(p, 'button', 'What is Luma Agents?');
    await S.view('faq-open');
  },
};

const browser = await chromium.launch({ headless: true });
let total = 0;
const keys = Object.keys(PAGES);
const runs = [
  ...keys.map((k) => ({ k, mob: false })),
  ...['home', 'pricing', 'app', 'news', 'careers'].map((k) => ({ k, mob: true })),
];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(k)) continue;
  const vw = mob ? 390 : 1440;
  const vh = mob ? 844 : 900;
  const dpr = mob ? 2 : 1;
  const ctx = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    userAgent: mob ? UA_MOBILE : UA,
    isMobile: mob,
    hasTouch: mob,
    locale: 'en-US',
  });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  log('page', name, PAGES[k]);
  try {
    const resp = await p.goto(BASE + PAGES[k], { waitUntil: 'domcontentloaded', timeout: 50000 });
    await wait(p, 2200);
    const host = new URL(p.url()).hostname;
    if (!/lumalabs\.ai$/.test(host)) {
      log('  WALL', p.url().split('?')[0]);
      await ctx.close();
      continue;
    }
    log('  status', resp?.status(), 'host', host);
    await hideConsent(p);
    await S.view('default');
    await S.full();
    if (interactions[k]) await interactions[k](p, S, mob).catch((e) => log('  interact fail', e.message.split('\n')[0]));
  } catch (e) {
    log('  PAGE FAILED', name, e.message.split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}
log('done', total, '->', RAW);
await browser.close();
