// Captures The Org's public pages. Login, signup, contact, and person pages
// are never opened for a screenshot. Forms are never filled or submitted.
//
//   PLAYWRIGHT=... node public.mjs [page,page,...]
//
// Desktop 1440x900 at 1x. Phone 390x844 at 2x. Names are {page}-light-{state}.png.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { fileURLToPath } from 'url';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { chromium, UA, UA_MOBILE, BASE, patch, closePromo, clearChallenge, hasPrivateContact, isAuthWall } from './lib.mjs';

const PKG = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..', '..');
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'the-org', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

async function guard(p) {
  if (await isAuthWall(p)) return 'auth-wall';
  if (!(await clearChallenge(p, { tries: 3, step: 600 }))) return 'challenge';
  if (await hasPrivateContact(p)) return 'private-contact';
  return null;
}

async function lazyScroll(p) {
  const h = await p.evaluate(() => Math.min(document.documentElement.scrollHeight, 7200));
  for (let y = 0; y < h; y += 700) {
    await p.evaluate((y) => scrollTo(0, y), y);
    await wait(p, 120);
  }
  await p.evaluate(() => scrollTo(0, 0));
  await wait(p, 400);
}

class Shooter {
  constructor(p, prefix, vw, vh, dpr) {
    this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
    this.count = 0;
  }
  async view(name) {
    await closePromo(this.p);
    const blocked = await guard(this.p);
    if (blocked) { log('  skip shot', name, blocked); return; }
    await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested);
    this.count++;
    log('  shot', name);
  }
  async full(name = 'full') {
    const p = this.p;
    await closePromo(p);
    const blocked = await guard(p);
    if (blocked) { log('  skip full', blocked); return; }
    await lazyScroll(p);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body.scrollHeight));
    const chunk = Math.floor(8000 / this.dpr);
    const MAXH = 4 * chunk;
    const hCap = Math.min(H, MAXH);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    const f = `${RAW}/${this.prefix}-${name}`;
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: f + '.png', fullPage: true }, this.requested);
    } else {
      for (let i = 0, y = 0; y < hCap; i++, y += chunk) {
        await screenshotWithMetadata(p, { path: `${f}.part${i}.png`, fullPage: true, clip: { x: 0, y, width: this.vw, height: Math.min(chunk, hCap - y) } }, this.requested);
      }
    }
    this.count++;
    log('  shot', name, 'H=' + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function openMenu(p, label) {
  const btn = p.getByRole('button', { name: label, exact: true }).first();
  await btn.click();
  await wait(p, 500);
}

async function openPhoneMenu(p) {
  // The 32px header button has no accessible name. Click the visible header button.
  const clicked = await p.evaluate(() => {
    const buttons = [...document.querySelectorAll('header button, nav button')];
    const vis = buttons.find((b) => {
      const r = b.getBoundingClientRect();
      return r.width > 0 && r.height > 0 && r.width < 48;
    });
    if (!vis) return false;
    vis.click();
    return true;
  });
  if (!clicked) throw new Error('no phone menu button');
  await wait(p, 600);
}

const desktop = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await S.full();
    await openMenu(p, 'Platform');
    await S.view('platform-menu');
    await p.keyboard.press('Escape');
    await wait(p, 300);
    await openMenu(p, 'Enrich');
    await S.view('enrich-menu');
    await p.keyboard.press('Escape');
  } },
  pricing: { path: '/pricing', run: async (p, S) => {
    await S.view('default');
    const monthly = p.getByText('Monthly', { exact: true }).first();
    await monthly.click({ timeout: 8000 });
    await wait(p, 400);
    await S.view('monthly');
    await S.full();
  } },
  'learn-more': { path: '/learn-more', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'for-companies': { path: '/for-companies', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'for-candidates': { path: '/for-candidates', run: async (p, S) => { await S.view('default'); } },
  'for-professionals': { path: '/for-professionals', run: async (p, S) => { await S.view('default'); } },
  'browser-extension': { path: '/browser-extension', run: async (p, S) => { await S.view('default'); } },
  'crm-enrichment': { path: '/crm-enrichment', run: async (p, S) => { await S.view('default'); } },
  'mcp-connectors': { path: '/mcp-connectors', run: async (p, S) => { await S.view('default'); } },
  'developer-portal': { path: '/developer-portal', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); await S.full(); } },
  trust: { path: '/trust', run: async (p, S) => { await S.view('default'); } },
  solutions: { path: '/solutions', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'employer-branding': { path: '/employer-branding', run: async (p, S) => { await S.view('default'); } },
  'professional-networking': { path: '/professional-networking', run: async (p, S) => { await S.view('default'); } },
  'job-discovery': { path: '/job-discovery', run: async (p, S) => { await S.view('default'); } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'explore-industries': { path: '/explore/industries', run: async (p, S) => {
    await S.view('default');
    const field = p.locator('input[name="Industries search"], input[placeholder*="search" i]').first();
    if (await field.count()) {
      await field.focus();
      await wait(p, 300);
      await S.view('search-focused');
    }
  } },
  'explore-countries': { path: '/explore/countries', run: async (p, S) => { await S.view('default'); } },
  'explore-ranges': { path: '/explore/employee-ranges', run: async (p, S) => { await S.view('default'); } },
  'explore-it': { path: '/explore/industries/information-technology', run: async (p, S) => { await S.view('default'); } },
  'explore-us': { path: '/explore/countries/united-states', run: async (p, S) => { await S.view('default'); } },
  companies: { path: '/companies', run: async (p, S) => { await S.view('default'); } },
  'companies-a': { path: '/companies/a-1', run: async (p, S) => { await S.view('default'); } },
  'people-directory': { path: '/people-directory', run: async (p, S) => { await S.view('default'); } },
  iterate: { path: '/iterate', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'iterate-moves': { path: '/iterate/categories/executive-moves', run: async (p, S) => { await S.view('default'); } },
  article: { path: '/iterate/executive-moves-you-should-know-about-february-18-2026', run: async (p, S) => { await S.view('default'); await S.full(); } },
  'org-five-blocks': { path: '/org/five-blocks', run: async (p, S) => {
    await S.view('default');
    const teams = p.getByRole('button', { name: 'Teams', exact: true }).first();
    if (await teams.count()) { await teams.click(); await wait(p, 500); await S.view('teams'); }
    const offices = p.getByRole('button', { name: 'Offices', exact: true }).first();
    if (await offices.count()) {
      await offices.click();
      await wait(p, 500);
      if (await hasPrivateContact(p)) log('  skip offices shot: private contact');
      else await S.view('offices');
    }
    const chart = p.getByRole('button', { name: 'Org chart', exact: true }).first();
    if (await chart.count()) { await chart.click(); await wait(p, 400); }
    await S.full();
  } },
  'org-google': { path: '/org/google', run: async (p, S) => { await S.view('default'); } },
  terms: { path: '/terms', run: async (p, S) => { await S.view('default'); } },
  privacy: { path: '/privacy', run: async (p, S) => { await S.view('default'); } },
};

const mobile = {
  home: { path: '/', run: async (p, S) => {
    await S.view('default');
    await openPhoneMenu(p);
    await S.view('menu');
    await S.full();
  } },
  pricing: { path: '/pricing', run: async (p, S) => { await S.view('default'); await S.full(); } },
  explore: { path: '/explore', run: async (p, S) => { await S.view('default'); } },
  'org-five-blocks': { path: '/org/five-blocks', run: async (p, S) => { await S.view('default'); await S.full(); } },
  iterate: { path: '/iterate', run: async (p, S) => { await S.view('default'); } },
  about: { path: '/about', run: async (p, S) => { await S.view('default'); } },
  companies: { path: '/companies', run: async (p, S) => { await S.view('default'); } },
};

const b = await chromium.launch();
let total = 0;
const runs = [...Object.keys(desktop).map((k) => ({ k, mob: false })), ...Object.keys(mobile).map((k) => ({ k, mob: true }))];
for (const { k, mob } of runs) {
  const name = (mob ? 'mobile-' : '') + k;
  if (pageArg.length && !pageArg.includes(name)) continue;
  const spec = (mob ? mobile : desktop)[k];
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
  await patch(ctx);
  const p = await ctx.newPage();
  log(name, spec.path);
  const S = new Shooter(p, `${name}-light`, vw, vh, dpr);
  try {
    await p.goto(BASE + spec.path, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await wait(p, 1800);
    const blocked = await guard(p);
    if (blocked) { log('  SKIP PAGE', blocked); await ctx.close(); continue; }
    await spec.run(p, S);
  } catch (e) { log('  PAGE FAILED', name, e.message.split('\n')[0]); }
  total += S.count;
  await ctx.close();
}
log('done', total, 'screenshots ->', RAW);
await b.close();
