// Captures the public Notion Calendar marketing site.
// PRODUCT (adapt): Notion Calendar public marketing site at www.notion.com/product/calendar.
// Login and signup are photographed empty and not entered. Identity providers are not clicked.
// ADAPTED_FOR names this product so the kit guard does not treat the file as the Gauth example.
const ADAPTED_FOR = "Notion Calendar";
if (!ADAPTED_FOR && !process.env.KIT_EXAMPLE) {
  console.error("public.mjs is not adapted");
  process.exit(2);
}

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { createRequire } from "node:module";
import { screenshotWithMetadata } from "./screenshot.mjs";

const PW = process.env.PLAYWRIGHT || "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs";
const require = createRequire(PW);
const { chromium } = require(PW);

const RAW = process.env.RAW || path.join(os.homedir(), ".design-systems", "notion-calendar", "raw-shots");
const PKG = path.resolve(new URL(".", import.meta.url).pathname, "../..");
fs.mkdirSync(RAW, { recursive: true });
fs.mkdirSync(path.join(PKG, "raw"), { recursive: true });

const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

function cleanUrl(url) {
  try {
    const u = new URL(url);
    u.search = "";
    u.hash = "";
    return u.origin + u.pathname;
  } catch {
    return null;
  }
}

async function hideBanners(page) {
  await page.addStyleTag({
    content: `#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter { display: none !important; }`,
  }).catch(() => {});
}

async function settle(page) {
  await page.waitForLoadState("domcontentloaded").catch(() => {});
  await wait(page, 1200);
  await hideBanners(page);
  await wait(page, 400);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page;
    this.prefix = prefix;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name, source) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    const src = source || cleanUrl(this.p.url());
    await screenshotWithMetadata(this.p, { path: file }, { ...this.requested, sanitizedSourceUrl: src });
    log("  shot", `${this.prefix}-${name}`, cleanUrl(this.p.url()));
  }
  async full(name, source) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    const src = source || cleanUrl(this.p.url());
    await screenshotWithMetadata(this.p, { path: file, fullPage: true }, { ...this.requested, sanitizedSourceUrl: src });
    log("  full", `${this.prefix}-${name}`);
  }
}

async function measure(page) {
  return page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const body = getComputedStyle(document.body);
    const names = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      if (!rules) continue;
      for (const rule of rules) {
        if (!rule.style) continue;
        for (const name of rule.style) {
          if (name.startsWith("--")) names.push(name);
        }
      }
    }
    const unique = [...new Set(names)].slice(0, 400);
    const vars = {};
    for (const name of unique) {
      const v = root.getPropertyValue(name).trim();
      if (v) vars[name] = v.slice(0, 180);
    }
    const h1 = document.querySelector("h1");
    const h1s = h1 ? getComputedStyle(h1) : null;
    const btn = [...document.querySelectorAll("a, button")].find((el) => /Get Notion Calendar free|Continue/.test(el.innerText || ""));
    const bs = btn ? getComputedStyle(btn) : null;
    return {
      url: location.origin + location.pathname,
      title: document.title,
      innerWidth: innerWidth,
      innerHeight: innerHeight,
      devicePixelRatio: devicePixelRatio,
      colorScheme: root.colorScheme,
      themeClass: document.documentElement.className.slice(0, 80),
      body: {
        backgroundColor: body.backgroundColor,
        color: body.color,
        fontFamily: body.fontFamily,
        fontSize: body.fontSize,
      },
      h1: h1s ? {
        fontFamily: h1s.fontFamily,
        fontSize: h1s.fontSize,
        fontWeight: h1s.fontWeight,
        lineHeight: h1s.lineHeight,
        color: h1s.color,
        letterSpacing: h1s.letterSpacing,
      } : null,
      primary: bs ? {
        text: (btn.innerText || "").trim().slice(0, 40),
        backgroundColor: bs.backgroundColor,
        color: bs.color,
        borderRadius: bs.borderRadius,
        fontSize: bs.fontSize,
        fontWeight: bs.fontWeight,
        padding: bs.padding,
        height: bs.height,
      } : null,
      varCount: unique.length,
      vars,
    };
  });
}

async function shotPage(browser, url, name, viewport) {
  const context = await browser.newContext({
    viewport: { width: viewport.w, height: viewport.h },
    deviceScaleFactor: 1,
    colorScheme: "light",
    reducedMotion: "reduce",
  });
  const page = await context.newPage();
  const shooter = new Shooter(page, name, viewport.w, viewport.h, 1);
  let landed = null;
  try {
    const resp = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await settle(page);
    landed = { requested: url, final: cleanUrl(page.url()), status: resp ? resp.status() : null, title: await page.title() };
    await shooter.view("light-default", url);
  } catch (err) {
    landed = { requested: url, error: String(err).slice(0, 240) };
    log("  fail", name, landed.error);
  }
  await context.close();
  return landed;
}

async function main() {
  const browser = await chromium.launch({ headless: true });
  const notes = { captured: new Date().toISOString(), pages: [], walls: [] };

  const desktop = { w: 1440, h: 900 };
  const phone = { w: 390, h: 844 };

  const pages = [
    ["https://www.notion.com/product/calendar", "home"],
    ["https://www.notion.com/download", "download"],
    ["https://www.notion.com/pricing", "pricing"],
    ["https://www.notion.com/product/calendar/download", "calendar-download-alias"],
    ["https://www.notion.com/help/category/notion-calendar", "help-calendar"],
    ["https://www.notion.com/contact-sales", "contact-sales"],
  ];

  for (const [url, name] of pages) {
    log("page", name);
    notes.pages.push(await shotPage(browser, url, name, desktop));
  }

  log("phone home");
  notes.pages.push({ ...(await shotPage(browser, "https://www.notion.com/product/calendar", "home-mobile", phone)), width: 390 });

  // Phone drawer
  {
    const context = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, reducedMotion: "reduce" });
    const page = await context.newPage();
    const shooter = new Shooter(page, "home-mobile", 390, 844, 1);
    await page.goto("https://www.notion.com/product/calendar", { waitUntil: "domcontentloaded", timeout: 45000 });
    await settle(page);
    const btn = page.getByRole("button", { name: /open navigation/i });
    if (await btn.count()) {
      await btn.click();
      await wait(page, 500);
      await shooter.view("menu", "https://www.notion.com/product/calendar");
      notes.phoneDrawer = true;
    }
    await context.close();
  }

  // Desktop resources menu
  {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, reducedMotion: "reduce" });
    const page = await context.newPage();
    const shooter = new Shooter(page, "site-tree", 1440, 900, 1);
    await page.goto("https://www.notion.com/product/calendar", { waitUntil: "domcontentloaded", timeout: 45000 });
    await settle(page);
    await page.getByRole("button", { name: /^Resources$/ }).click();
    await wait(page, 400);
    await shooter.view("desktop-menu-resources", "https://www.notion.com/product/calendar");
    await page.keyboard.press("Escape");
    await context.close();
  }

  // Auth walls. Photograph empty. Do not type. Do not click providers.
  const walls = [
    ["https://www.notion.com/login/calendar", "login"],
    ["https://www.notion.com/signup/calendar", "signup"],
  ];
  for (const [url, name] of walls) {
    log("wall", name);
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, reducedMotion: "reduce" });
    const page = await context.newPage();
    const shooter = new Shooter(page, name, 1440, 900, 1);
    await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
    await page.waitForSelector("h1", { timeout: 20000 }).catch(() => {});
    await wait(page, 1500);
    const probe = await page.evaluate(() => ({
      final: location.origin + location.pathname,
      title: document.title,
      h: [...document.querySelectorAll("h1,h2")].map((el) => el.innerText.trim()).slice(0, 4),
      buttons: [...document.querySelectorAll("button")].map((el) => (el.innerText || el.getAttribute("aria-label") || "").trim()).filter(Boolean).slice(0, 12),
      inputs: [...document.querySelectorAll("input")].map((el) => ({ type: el.type, placeholder: el.placeholder || "", filled: (el.value || "").length > 0 })),
    }));
    notes.walls.push({ requested: url, ...probe });
    await shooter.view("light-default", url);
    await context.close();
  }

  // Measure homepage tokens
  {
    const context = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
    const page = await context.newPage();
    await page.goto("https://www.notion.com/product/calendar", { waitUntil: "domcontentloaded", timeout: 45000 });
    await settle(page);
    const measured = await measure(page);
    fs.writeFileSync(path.join(PKG, "raw", "css-vars.json"), JSON.stringify(measured, null, 2) + "\n");
    log("vars", measured.varCount, "h1", measured.h1 && measured.h1.fontSize);
    await context.close();
  }

  fs.writeFileSync(path.join(PKG, "raw", "probe.json"), JSON.stringify(notes, null, 2) + "\n");
  await browser.close();
  log("done");
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
