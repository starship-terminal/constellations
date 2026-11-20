// Captures excalidraw.com's public signed-out editor into RAW (full-colour
// PNGs); quantize.py turns them into screenshots/.
//
//   RAW=/some/scratch/dir PLAYWRIGHT=/path/to/playwright/index.mjs node public.mjs [page,page,...]
//
// Names are {page}-{theme}-{state}.png; mobile ones get a `mobile-` prefix.
// excalidraw.com is a single surface: the editor itself is the landing page,
// public and signed out. Desktop shots are 1440x900 at 1x, mobile 390x844 at
// 2x. The app is a fixed-height canvas app — nothing scrolls, so there are no
// `*-full` captures and no truncation. States inside the editor (welcome
// screen, open menus, the properties sidebar, the library panel, the export /
// command-palette / keyboard-shortcuts dialogs, dark theme) are reached by
// local UI presses only: tool buttons, the hamburger, menu items, the theme
// radio and dialog close buttons. Nothing is drawn, opened from disk, saved,
// shared, exported, generated or signed into: Open, Save, Live collaboration,
// Share, Export to Excalidraw+, the AI actions, Reset canvas and every Sign up
// are measured never pressed.
import fs from 'fs';
import os from 'os';
import path from 'path';
import { screenshotWithMetadata } from '../screenshot.mjs';
import { clearChallenge, patch, chromium, UA, UA_MOBILE, BASE, pickTool, openMainMenu, setTheme, closeMenus, closeDialog } from './lib.mjs';

// Full-colour originals stay outside the repo (quantize.py writes screenshots/ from them).
const RAW = process.env.RAW || path.join(os.homedir(), '.design-systems', 'excalidraw', 'raw-shots');
fs.mkdirSync(RAW, { recursive: true });
const pageArg = (process.argv[2] || '').split(',').filter(Boolean);
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);
const step = async (label, fn) => { try { await fn(); } catch (e) { log('  FAILED', label, String(e.message).split('\n')[0]); } };
const clickEl = async (loc, ms = 6000) => { await loc.click({ timeout: ms }).catch(() => loc.evaluate((el) => el.click())); };

class Shooter {
  constructor(p, prefix, vw, vh, dpr, sourceUrl) { this.p = p; this.prefix = prefix; this.vw = vw; this.dpr = dpr; this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, sanitizedSourceUrl: sourceUrl }; this.count = 0; }
  async view(name) { await screenshotWithMetadata(this.p, { path: `${RAW}/${this.prefix}-${name}.png` }, this.requested); this.count++; log('  shot', this.prefix + '-' + name); }
}

// Opens a named item inside the open main menu. Items with a chevron open a
// submenu; leaf items trigger an action (only safe local ones are called).
const menuItem = (p, text) => p.locator('.dropdown-menu.main-menu .dropdown-menu-item, .dropdown-menu.main-menu [class*="dropdown-menu-item"]').filter({ hasText: new RegExp('^' + text) }).first();
const clickMenuItem = async (p, text) => {
  const it = menuItem(p, text);
  if (!(await it.count())) return false;
  await clickEl(it);
  return true;
};

const editor = {
  url: BASE + '/', wait: 9000,
  run: async (p, S) => {
    // 1. first-run state: the welcome screen on the blank canvas
    await S.view('default');
    // 2. the editor chrome: pick Selection, welcome dismisses
    await step('editor', async () => {
      await pickTool(p, 'Selection');
      await S.view('editor');
    });
    // 3. hamburger menu open (also proves the trigger state)
    await step('menu', async () => {
      await openMainMenu(p);
      await S.view('menu');
    });
    // 4. Preferences submenu (hover-to-open chevron item)
    await step('preferences', async () => {
      if (await clickMenuItem(p, 'Preferences')) {
        await wait(p, 1200);
        await S.view('menu-preferences');
      }
    });
    // 5. the canvas-background swatches already sit at the open menu's foot —
    //    `menu` above covers them; a second identical shot would be noise.
    await closeMenus(p);
    // 6. more-tools dropdown (image/frame/embed/laser/AI entries)
    await step('moretools', async () => {
      const t = p.locator('button.App-toolbar__extra-tools-trigger').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await p.waitForSelector('.dropdown-menu', { state: 'visible', timeout: 4000 }).catch(() => {});
      await wait(p, 900);
      await S.view('moretools');
      await p.keyboard.press('Escape');
      await wait(p, 600);
    });
    // 7. zoom footer dropdown (Zen/grid/snapping toggles — measured, not set)
    await step('zoommenu', async () => {
      const t = p.locator('.zoom-button, [class*="zoom"] button').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 900);
      await S.view('zoommenu');
      await p.keyboard.press('Escape');
      await wait(p, 600);
    });
    // 8. the left properties sidebar: select a shape tool to summon it
    await step('sidebar', async () => {
      await pickTool(p, 'Rectangle');
      await p.waitForSelector('.App-menu__left', { state: 'visible', timeout: 5000 }).catch(() => {});
      await wait(p, 900);
      await S.view('sidebar');
    });
    // 9. library panel (the sidebar trigger top-right)
    await step('library', async () => {
      const t = p.locator('button.sidebar-trigger__label-element').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await p.waitForSelector('.sidebar, .library-menu, [class*="library"]', { state: 'visible', timeout: 5000 }).catch(() => {});
      await wait(p, 1200);
      await S.view('library');
      await p.keyboard.press('Escape');
      await wait(p, 600);
      // the trigger toggles; ensure it closed
      if (await p.locator('.sidebar').filter({ visible: true }).count()) await clickEl(t);
      await wait(p, 500);
    });
    // 10. Export image dialog (menu item opens the local dialog; Export is
    //     never pressed)
    await step('export', async () => {
      await openMainMenu(p);
      if (await clickMenuItem(p, 'Export image…|Export image\\.\\.\\.|Export image')) {
        await p.waitForSelector('.Dialog, [role="dialog"]', { state: 'visible', timeout: 6000 }).catch(() => {});
        await wait(p, 1400);
        await S.view('export');
        await closeDialog(p);
      } else await closeMenus(p);
    });
    // 11. keyboard shortcuts dialog — the main menu's Help item opens the
    //     same local sheet as '?' (a plain HelpDialog, not a shortcut press)
    await step('shortcuts', async () => {
      await closeMenus(p);
      const dlg = () => p.locator('.Modal.Dialog.HelpDialog, .HelpDialog').filter({ visible: true }).count();
      if (!(await dlg())) {
        await openMainMenu(p);
        if (await clickMenuItem(p, '^Help')) await wait(p, 1600);
      }
      if (!(await dlg())) {
        // fallback: the bottom-right "?" button opens the same sheet
        const hb = p.locator('button.help-icon, button[aria-label*="help" i]').filter({ visible: true }).first();
        if (await hb.count()) { await clickEl(hb); await wait(p, 1600); }
      }
      if (await dlg()) {
        await S.view('shortcuts');
        await closeDialog(p);
      }
    });
    // 12. command palette (Ctrl+/ — a local launcher dialog)
    await step('cmdk', async () => {
      await p.keyboard.press('Control+/').catch(() => {});
      await p.waitForSelector('.command-palette-dialog, [class*="command-palette"]', { state: 'visible', timeout: 4000 }).catch(() => {});
      await wait(p, 1000);
      if (await p.locator('.command-palette-dialog, [class*="command-palette"]').filter({ visible: true }).count()) {
        await S.view('cmdk');
        await p.keyboard.press('Escape');
        await wait(p, 500);
      }
    });
    // 13. find-on-canvas (Ctrl+F — local search box)
    await step('find', async () => {
      await p.keyboard.press('Control+f').catch(() => {});
      await wait(p, 1000);
      const box = p.locator('[class*="SearchMenu"], [class*="search"], input[placeholder*="Find"]').filter({ visible: true }).first();
      if (await box.count()) {
        await S.view('find');
        await p.keyboard.press('Escape');
        await wait(p, 500);
      }
    });
  },
};

const dark = {
  url: BASE + '/', wait: 9000,
  run: async (p, S) => {
    // no 'default' shot here: before the theme flip the welcome screen is still
    // light, which `editor-light-default` already covers — shooting it under a
    // `*-dark-*` name would mislabel a light capture.
    await step('dark', async () => {
      await pickTool(p, 'Selection');
      await setTheme(p, 'dark');
      await closeMenus(p);
    });
    // step() swallows a failed toggle: check what painted before naming any shot *-dark-*.
    if (!(await p.locator('.excalidraw.theme--dark').count().catch(() => 0))) {
      log('  SKIPPED dark: .excalidraw.theme--dark did not appear after the theme toggle');
      return;
    }
    const D = new Shooter(p, S.prefix.replace(/-light$/, '-dark'), S.vw, S.requested.viewport.height, S.dpr, S.requested.sanitizedSourceUrl);
    await D.view('editor');
    await step('dark-menu', async () => { await openMainMenu(p); await D.view('menu'); await closeMenus(p); });
    await step('dark-sidebar', async () => {
      await pickTool(p, 'Rectangle');
      await p.waitForSelector('.App-menu__left', { state: 'visible', timeout: 5000 }).catch(() => {});
      await wait(p, 800);
      await D.view('sidebar');
    });
    await step('dark-library', async () => {
      const t = p.locator('button.sidebar-trigger__label-element').filter({ visible: true }).first();
      if (!(await t.count())) return;
      await clickEl(t);
      await wait(p, 1200);
      await D.view('library');
      await p.keyboard.press('Escape');
      await wait(p, 500);
    });
    await step('dark-export', async () => {
      await openMainMenu(p);
      if (await clickMenuItem(p, 'Export image')) {
        await p.waitForSelector('.Dialog, [role="dialog"]', { state: 'visible', timeout: 6000 }).catch(() => {});
        await wait(p, 1400);
        await D.view('export');
        await closeDialog(p);
      } else await closeMenus(p);
    });
    await step('dark-welcome', async () => {
      // the theme persists in localStorage: a reload shows the dark welcome
      await p.reload({ waitUntil: 'domcontentloaded' }).catch(() => {});
      await clearChallenge(p);
      await wait(p, 8000);
      await D.view('welcome');
    });
    S.count += D.count;
  },
};

const mobileLight = {
  url: BASE + '/', wait: 9000,
  run: async (p, S) => {
    await S.view('default'); // welcome
    await step('editor', async () => { await pickTool(p, 'Selection'); await S.view('editor'); });
    await step('menu', async () => {
      await openMainMenu(p);
      await S.view('menu');
      await closeMenus(p);
    });
    await step('shape-actions', async () => {
      // selecting a shape tool swaps the bottom bar to compact-shape-actions
      await pickTool(p, 'Rectangle');
      await wait(p, 900);
      await S.view('shape-actions');
    });
  },
};

const specs = { desktop: { light: editor, dark }, mobile: { light: mobileLight } };

const b = await chromium.launch();
let total = 0;
for (const [kind, themes] of Object.entries(specs)) {
  const mob = kind === 'mobile';
  const vw = mob ? 390 : 1440, vh = mob ? 844 : 900, dpr = mob ? 2 : 1;
  for (const [theme, spec] of Object.entries(themes)) {
    const name = `${mob ? 'mobile-' : ''}editor`;
    const arg = `${name}-${theme}`;
    if (pageArg.length && !pageArg.includes(arg) && !pageArg.includes(name)) continue;
    const ctx = await b.newContext({ viewport: { width: vw, height: vh }, deviceScaleFactor: dpr, userAgent: mob ? UA_MOBILE : UA, isMobile: mob, hasTouch: mob, locale: 'en-US' });
    await patch(ctx);
    const p = await ctx.newPage();
    log(arg);
    const S = new Shooter(p, `${name}-${theme}`, vw, vh, dpr, spec.url);
    try {
      await p.goto(spec.url, { waitUntil: 'domcontentloaded', timeout: 90000 }).catch(() => {});
      if (!(await clearChallenge(p))) { log('  BLOCKED challenge', spec.url); await ctx.close(); continue; }
      await wait(p, spec.wait || 8000);
      await spec.run(p, S);
    } catch (e) { log('  PAGE FAILED', arg, e.message.split('\n')[0]); }
    total += S.count;
    await ctx.close();
  }
}
log('done', total, 'screenshots ->', RAW);
await b.close();
