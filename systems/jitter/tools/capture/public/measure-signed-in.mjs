// Measure signed-in Jitter controls. Nothing billed, exported, invited, or shared.
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { BASE, chromium, UA, closePromo, styleOf, crop, centre, RAW, patch } from './lib.mjs';

const OUT = process.env.OUT_JSON || path.join(RAW, 'components-computed.json');
const PROFILE = process.env.PROFILE || path.join(os.homedir(), '.design-systems', 'jitter', 'chrome-profile');
fs.mkdirSync(RAW, { recursive: true });
const out = fs.existsSync(OUT) ? JSON.parse(fs.readFileSync(OUT, 'utf8')) : {};
out._meta ??= { product: 'jitter', captured: '2026-11-18', route: 'signed-in-web' };
out._meta.signedIn = '2026-11-18';
out.components ??= {};
const log = (...a) => console.log(new Date().toISOString().slice(11, 19), ...a);
const save = () => fs.writeFileSync(OUT, JSON.stringify(out, null, 1) + '\n');

const ctx = await chromium.launchPersistentContext(PROFILE, {
  headless: true,
  viewport: { width: 1440, height: 900 },
  deviceScaleFactor: 1,
  userAgent: UA,
  locale: 'en-US',
  args: [] /* no AutomationControlled flag: removed in the 2026-11 audit (D7) */,
});
await patch(ctx);
const page = ctx.pages()[0] || await ctx.newPage();
page.setDefaultTimeout(12000);
let current = 'files';

async function reset() {
  await page.evaluate(() => document.activeElement && document.activeElement.blur && document.activeElement.blur()).catch(() => {});
  await page.mouse.move(1430, 8);
  await page.waitForTimeout(150);
}

async function measure(key, state, loc, opts = {}) {
  const c = out.components[key];
  try {
    const s = await styleOf(loc);
    let file;
    if (opts.crop !== false) {
      try { file = await crop(page, loc, `${key}-${state}`, opts.pad ?? 10); }
      catch (e) { s.cropError = String(e.message || e).slice(0, 140); }
    }
    c.states[state] = { ...s, crop: file, via: opts.via };
    log('  ', key, state, `${s.rect.w}x${s.rect.h}`, s.face?.backgroundColor || s.style.backgroundColor);
  } catch (e) {
    c.states[state] = { error: String(e.message || e).slice(0, 200) };
    log('  !', key, state, String(e.message).slice(0, 140));
  }
}

async function S(key, loc, list, meta = {}, opts = {}) {
  const prev = out.components[key];
  out.components[key] = {
    page: current, url: page.url().replace(/\?.*$/, ''),
    title: meta.title, group: meta.group, desc: meta.desc,
    states: { ...(prev && prev.states || {}) },
  };
  if (!(await loc.count().catch(() => 0))) {
    out.components[key].missing = true;
    log('  ! missing', key);
    save();
    return;
  }
  const el = loc.first();
  for (const st of list) {
    try {
      if (!opts.noReset) await reset();
      if (!opts.noScroll) await centre(el).catch(() => {});
      let via = 'at rest';
      if (st === 'hover') {
        await el.hover({ timeout: 4000 }).catch(() => el.hover({ force: true }));
        await page.waitForTimeout(300);
        via = 'mouse hover';
      } else if (st === 'focused') {
        await el.click({ timeout: 3000 }).catch(() => el.evaluate((n) => n.focus()));
        via = 'clicked; nothing submitted';
      }
      await measure(key, st, el, { ...opts, via });
    } catch (e) {
      out.components[key].states[st] = { error: String(e.message || e).slice(0, 200) };
      log('  !', key, st, String(e.message).slice(0, 120));
    }
  }
  await reset();
  save();
}

const q = (sel) => page.locator(sel);

await page.goto(BASE + '/files/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2200);
await closePromo(page);
current = 'files';
await S('files-create', page.getByText('Create new file', { exact: true }), ['default', 'hover'], { group: 'Files', title: 'Create new file', desc: 'Violet CTA on Drafts. Not clicked in this measure pass.' });
await S('files-figma', page.getByText('Import from Figma', { exact: true }), ['default', 'hover'], { group: 'Files', title: 'Import from Figma', desc: 'Blue CTA on Drafts. Not followed.' });
await S('files-search', page.getByPlaceholder(/search/i).first(), ['default', 'focused'], { group: 'Files', title: 'Files search', desc: 'Sidebar search. Focused, not typed.' });
await S('files-avatar', q('a[href="/account/"]').first(), ['default'], { group: 'Files', title: 'Account avatar', desc: 'Header avatar linking to /account/.' });
await S('files-upgrade', page.getByText('Upgrade your plan', { exact: true }).first(), ['default'], { group: 'Files', title: 'Upgrade your plan', desc: 'Sidebar billing link. Measured at rest, never followed.' });

current = 'account';
await page.goto(BASE + '/account/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(2000);
await closePromo(page);
await S('account-name', q('input[type="text"], input[name="name"], input[name="username"]').first(), ['default'], { group: 'Account', title: 'Account name field', desc: 'Name field on /account/. Not edited in this pass.' });

current = 'editor';
await page.goto(BASE + '/files/', { waitUntil: 'domcontentloaded', timeout: 45000 });
await page.waitForTimeout(1800);
const fileCard = page.getByText('New file', { exact: true }).first();
if (await fileCard.count()) {
  await fileCard.click();
  await page.waitForTimeout(3500);
}
await closePromo(page);
await S('editor-share', page.getByText('Share', { exact: true }).first(), ['default'], { group: 'Editor', title: 'Share', desc: 'Editor header Share. Not clicked.' });
await S('editor-export', page.getByText('Export', { exact: true }).first(), ['default'], { group: 'Editor', title: 'Export', desc: 'Editor header Export. Not clicked; paid export was not opened.' });
await S('editor-design', page.getByText('Design', { exact: true }).first(), ['default'], { group: 'Editor', title: 'Design tab', desc: 'Selected Design mode in the editor inspector.' });
await S('editor-animate', page.getByText('Animate', { exact: true }).first(), ['default'], { group: 'Editor', title: 'Animate tab', desc: 'Animate mode control. Not switched in this measure pass.' });
await S('editor-upgrade', page.getByText('Upgrade now', { exact: true }).first(), ['default'], { group: 'Editor', title: 'Upgrade now', desc: 'Editor toolbar upgrade chip. Not clicked.' });

save();
await ctx.close();
log('wrote', OUT);
