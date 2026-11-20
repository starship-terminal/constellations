// Captures Scale's public pages into RAW (full-colour PNGs). quantize.py turns them into screenshots/.
//
//   RAW=~/.design-systems/scale/raw-shots PLAYWRIGHT=... node public.mjs [name,name]
//
// Names are {page}-light-{state}.png. Phone shots get a mobile- prefix.
// Desktop is 1440x900 at 1x. Phone is 390x844 at 2x. Nothing is submitted.
// OneTrust is hidden, never clicked. Login and signup branches stop at the wall.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, hideConsent } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'scale', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function lazyScroll(p) {
  let last = 0;
  for (let i = 0; i < 24; i++) {
    const h = await p.evaluate(() => document.documentElement.scrollHeight);
    if (h === last && i > 2) break;
    last = h;
    const y = Math.min(i * 700, h);
    await p.evaluate((yy) => scrollTo(0, yy), y);
    await wait(p, 180);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name, source) {
    const file = `${RAW}/${this.prefix}-${name}.png`;
    await screenshotWithMetadata(this.p, { path: file }, { ...this.requested, sanitizedSourceUrl: source || null });
    this.count++;
    log('  shot', this.prefix, name);
  }
  async full(name = 'full', source) {
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
    if (H > MAXH) log(`  ! ${name}: page is ${H}px tall, capturing first ${hCap}px only`);
    const req = { ...this.requested, sanitizedSourceUrl: source || null };
    if (hCap <= chunk) await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, req);
    else for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
      await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, req);
    }
    this.count++;
    log('  shot', this.prefix, name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 300);
  }
}

const step = async (label, fn) => {
  try { await fn(); }
  catch (e) { log('  FAILED', label, String(e.message || e).split('\n')[0]); }
};

async function clickNamed(p, name) {
  await p.evaluate((name) => {
    document.getElementById('onetrust-consent-sdk')?.remove();
    const nodes = [...document.querySelectorAll('button, [role="tab"], a')];
    const el = nodes.find((n) => ((n.innerText || n.getAttribute('aria-label') || '').replace(/\s+/g, ' ').trim()) === name);
    if (!el) throw new Error('missing control ' + name);
    el.click();
  }, name);
}

const PAGES = {
  home: { path: '/', run: async (p, S, mob) => {
    await S.view('default', BASE + '/');
    if (!mob) {
      await step('products-menu', async () => {
        await clickNamed(p, 'Products');
        await wait(p, 500);
        await S.view('products-menu', BASE + '/');
        await p.keyboard.press('Escape');
        await wait(p, 200);
      });
      await step('solutions-menu', async () => {
        await clickNamed(p, 'Solutions');
        await wait(p, 400);
        await S.view('solutions-menu', BASE + '/');
        await p.keyboard.press('Escape');
      });
      await step('research-menu', async () => {
        await clickNamed(p, 'Research');
        await wait(p, 400);
        await S.view('research-menu', BASE + '/');
        await p.keyboard.press('Escape');
      });
      await step('resources-menu', async () => {
        await clickNamed(p, 'Resources');
        await wait(p, 400);
        await S.view('resources-menu', BASE + '/');
        await p.keyboard.press('Escape');
      });
      await step('get-started-focus', async () => {
        await p.locator('a[href="/demo"]').first().focus();
        await wait(p, 250);
        await S.view('get-started-focus', BASE + '/');
      });
    } else {
      await step('menu-open', async () => {
        await clickNamed(p, 'Open menu');
        await wait(p, 600);
        await S.view('menu-open', BASE + '/');
        await step('products-group', async () => {
          await clickNamed(p, 'Products');
          await wait(p, 400);
          await S.view('menu-products', BASE + '/');
        });
      });
    }
    await S.full('full', BASE + '/');
  } },
  'data-engine': { path: '/data-engine' },
  'genai-data': { path: '/generative-ai-data-engine' },
  'physical-ai': { path: '/physical-ai' },
  government: { path: '/public-sector-data-engine' },
  automotive: { path: '/automotive', run: async (p, S) => {
    await S.view('default', BASE + '/automotive');
    await step('image-tab', async () => {
      await clickNamed(p, 'Image');
      await wait(p, 500);
      await S.view('image-tab', BASE + '/automotive');
    });
    await S.full('full', BASE + '/automotive');
  } },
  rl: { path: '/rlenvironments' },
  'off-the-shelf': { path: '/off-the-shelf-data', run: async (p, S) => {
    await S.view('default', BASE + '/off-the-shelf-data');
    await step('field-focus', async () => {
      const field = p.locator('input[name="firstname"]');
      if (await field.count()) {
        await field.first().scrollIntoViewIfNeeded();
        await field.first().focus();
        await wait(p, 300);
        await S.view('field-focus', BASE + '/off-the-shelf-data');
        // Type nothing that is personal. A single letter shows the filled state, then clear it.
        await field.first().fill('A');
        await wait(p, 200);
        await S.view('field-filled', BASE + '/off-the-shelf-data');
        await field.first().fill('');
      }
    });
  } },
  experts: { path: '/experts', run: async (p, S) => {
    await S.view('default', BASE + '/experts');
    await step('finance', async () => {
      await clickNamed(p, 'Finance');
      await wait(p, 400);
      await S.view('finance', BASE + '/experts');
    });
    await S.full('full', BASE + '/experts');
  } },
  portfolio: { path: '/genai-portfolio', run: async (p, S) => {
    await S.view('default', BASE + '/genai-portfolio');
    await step('faq', async () => {
      await clickNamed(p, 'Is there any vendor lock-in?');
      await wait(p, 400);
      await S.view('faq-open', BASE + '/genai-portfolio');
    });
  } },
  donovan: { path: '/donovan', run: async (p, S) => {
    await S.view('default', BASE + '/donovan');
    await step('tab', async () => {
      await clickNamed(p, 'Agentic RAG');
      await wait(p, 500);
      await S.view('agentic-rag', BASE + '/donovan');
    });
    await S.full('full', BASE + '/donovan');
  } },
  'eval-models': { path: '/evaluation/model-developers' },
  'eval-public': { path: '/evaluation/public-sector' },
  'eval-enterprise': { path: '/evaluation/enterprise' },
  enterprise: { path: '/enterprise' },
  'public-sector': { path: '/public-sector' },
  'global-public': { path: '/global-public-sector' },
  insurance: { path: '/enterprise/insurance' },
  healthcare: { path: '/enterprise/healthcare', run: async (p, S) => {
    await S.view('default', BASE + '/enterprise/healthcare');
    await step('tab', async () => {
      await clickNamed(p, 'Scheduling Intelligence');
      await wait(p, 400);
      await S.view('scheduling', BASE + '/enterprise/healthcare');
    });
  } },
  'national-security': { path: '/public-sector/national-security' },
  demo: { path: '/demo', run: async (p, S) => {
    await S.view('default', BASE + '/demo');
    await S.full('full', BASE + '/demo');
    // Form is visible and not submitted. Focus one empty field.
    await step('focus', async () => {
      const field = p.locator('input[name="company"]');
      if (await field.count()) {
        await field.first().focus();
        await wait(p, 250);
        await S.view('company-focus', BASE + '/demo');
      }
    });
  } },
  about: { path: '/about' },
  security: { path: '/security' },
  guides: { path: '/guides' },
  'guide-cv': { path: '/guides/computer-vision' },
  careers: { path: '/careers' },
  blog: { path: '/blog', run: async (p, S, mob) => {
    await S.view('default', BASE + '/blog');
    if (!mob) {
      await step('search', async () => {
        await clickNamed(p, 'SEARCH... ⌘K');
        await wait(p, 600);
        await S.view('search-open', BASE + '/blog');
        await p.keyboard.press('Escape');
      });
    }
    await S.full('full', BASE + '/blog');
  } },
  'blog-post': { path: '/blog/arabic-first-ai' },
  events: { path: '/events' },
  docs: { path: '/docs', run: async (p, S, mob) => {
    await S.view('default', BASE + '/docs');
    if (!mob) {
      await step('theme', async () => {
        await clickNamed(p, 'Change theme preference');
        await wait(p, 400);
        await S.view('theme-menu', BASE + '/docs');
        await p.keyboard.press('Escape');
      });
    }
  } },
  partnership: { path: '/partnership' },
  'data-partnership': { path: '/data-partnership', run: async (p, S) => {
    await S.view('default', BASE + '/data-partnership');
    await step('faq', async () => {
      await clickNamed(p, 'Why are AI companies interested in my data?');
      await wait(p, 400);
      await S.view('faq-open', BASE + '/data-partnership');
    });
  } },
  customer: { path: '/customers/time' },
  terms: { path: '/legal/terms' },
  privacy: { path: '/legal/privacy' },
  cookies: { path: '/legal/cookie' },
  login: { url: 'https://dashboard.scale.com/login', run: async (p, S) => {
    // Wall only. Do not type, do not click Google or GitHub, do not submit.
    await S.view('wall', 'https://dashboard.scale.com/login');
  } },
};

const EXTERNAL = {
  labs: { url: 'https://labs.scale.com/' },
  'labs-papers': { url: 'https://labs.scale.com/papers' },
  'labs-leaderboard': { url: 'https://labs.scale.com/leaderboard' },
  'labs-blog': { url: 'https://labs.scale.com/blog' },
  brand: { url: 'https://brand.scale.com/' },
};

const desktopKeys = [...Object.keys(PAGES), ...Object.keys(EXTERNAL)];
const mobileKeys = ['home', 'data-engine', 'enterprise', 'demo', 'blog', 'docs', 'about', 'careers', 'login', 'labs'];

const browser = await chromium.launch({ headless: true });
let total = 0;

async function runOne(key, mob) {
  const name = (mob ? 'mobile-' : '') + key;
  if (pageArg.length && !pageArg.includes(name) && !pageArg.includes(key)) return;
  const spec = PAGES[key] || EXTERNAL[key];
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
  await ctx.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
  });
  const p = await ctx.newPage();
  const url = spec.url || (BASE + spec.path);
  const source = url.split('?')[0];
  log(name, source);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, spec.wait || 2200);
    await hideConsent(p);
    if (spec.run) await spec.run(p, S, mob);
    else {
      await S.view('default', source);
      if (!mob) await S.full('full', source);
    }
  } catch (e) {
    log('  PAGE FAILED', name, String(e.message || e).split('\n')[0]);
  }
  total += S.count;
  await ctx.close();
}

for (const key of desktopKeys) await runOne(key, false);
for (const key of mobileKeys) await runOne(key, true);
log('done', total, 'screenshots ->', RAW);
await browser.close();
