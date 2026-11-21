// Captures the public Dia marketing site (https://www.diabrowser.com) into RAW.
// PRODUCT (adapt): Dia browser marketing site. Login and signup walls are photographed empty and not entered.
// ADAPTED_FOR names this product so the kit guard does not treat the file as the Gauth example.
const ADAPTED_FOR = "Dia";
if (!ADAPTED_FOR && !process.env.KIT_EXAMPLE) {
  console.error("public.mjs is not adapted");
  process.exit(2);
}

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { createRequire } from "node:module";
import { screenshotWithMetadata } from "./screenshot.mjs";
import { scrubConsole } from "./no-query.mjs";

scrubConsole();

const pwPath = process.env.PLAYWRIGHT || "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs";
const require = createRequire(pwPath);
const { chromium } = require(pwPath);

const RAW = process.env.RAW || path.join(os.homedir(), ".design-systems", "dia", "raw-shots");
fs.mkdirSync(RAW, { recursive: true });

const BASE = "https://www.diabrowser.com";
const log = (...a) => console.log(...a);
const wait = (p, ms) => p.waitForTimeout(ms);

const WANT = new Set((process.argv[2] || "home,pages,auth,mobile,measure").split(",").filter(Boolean));

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

async function settle(page) {
  await page.waitForLoadState("domcontentloaded").catch(() => {});
  await wait(page, 1400);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log("  shot", `${this.prefix}-${name}`);
  }
  async full(name = "full") {
    const p = this.p;
    const H0 = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const steps = Math.min(8, Math.ceil(H0 / 800));
    for (let i = 0; i < steps; i++) {
      await p.evaluate((y) => scrollTo(0, y), i * 800);
      await wait(p, 120);
    }
    await p.evaluate(() => scrollTo(0, 0));
    await wait(p, 400);
    const H = await p.evaluate(() => Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0));
    const chunk = Math.floor(8000 / this.dpr);
    const MAXH = 2 * chunk;
    const hCap = Math.min(H, MAXH);
    const f = path.join(RAW, `${this.prefix}-${name}`);
    if (H > MAXH) log(`  ! ${name}: page is ${H}px, capturing first ${hCap}px`);
    if (hCap <= chunk) {
      await screenshotWithMetadata(p, { path: `${f}.png`, fullPage: true }, this.requested);
    } else {
      await screenshotWithMetadata(p, {
        path: `${f}.png`,
        fullPage: true,
        clip: { x: 0, y: 0, width: this.vw, height: hCap },
      }, this.requested);
    }
    log("  shot", `${this.prefix}-${name}`, "H=" + H);
    await p.evaluate(() => scrollTo(0, 0));
  }
}

async function measure(page, outName) {
  const data = await page.evaluate(() => {
    const root = getComputedStyle(document.documentElement);
    const names = new Set();
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      const walk = (list) => {
        if (!list) return;
        for (const r of list) {
          if (r.style) for (const prop of r.style) if (prop.startsWith("--")) names.add(prop);
          if (r.cssRules) walk(r.cssRules);
        }
      };
      walk(rules);
    }
    const vars = {};
    for (const n of [...names].sort()) vars[n] = root.getPropertyValue(n).trim();
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute("aria-label") || "").replace(/\s+/g, " ").trim().slice(0, 90),
        bg: s.backgroundColor, color: s.color, font: s.fontFamily, size: s.fontSize,
        weight: s.fontWeight, radius: s.borderRadius, pad: s.padding, border: s.border,
        lh: s.lineHeight, ls: s.letterSpacing, h: Math.round(r.height), w: Math.round(r.width),
        shadow: s.boxShadow,
      };
    };
    const buttons = [...document.querySelectorAll("button, a")].slice(0, 30).map(pick).filter(Boolean);
    const h1 = document.querySelector("h1");
    const inputs = [...document.querySelectorAll("input, textarea")].map((el) => ({
      type: el.type, name: el.name, placeholder: el.placeholder, valueLen: (el.value || "").length,
    }));
    return {
      href: location.href.split("?")[0].split("#")[0],
      title: document.title,
      innerWidth: window.innerWidth,
      innerHeight: window.innerHeight,
      dpr: window.devicePixelRatio,
      colorScheme: root.colorScheme,
      body: {
        bg: getComputedStyle(document.body).backgroundColor,
        color: getComputedStyle(document.body).color,
        font: getComputedStyle(document.body).fontFamily,
        size: getComputedStyle(document.body).fontSize,
      },
      h1: pick(h1),
      buttons,
      inputs,
      varCount: Object.keys(vars).length,
      vars,
      links: [...document.querySelectorAll("a")].map((a) => ({
        text: (a.innerText || "").replace(/\s+/g, " ").trim().slice(0, 60),
        href: a.getAttribute("href"),
      })).filter((x) => x.href).slice(0, 80),
    };
  });
  const file = path.join(RAW, outName);
  fs.writeFileSync(file, JSON.stringify(data, null, 2));
  log("  measured", outName, "vars", data.varCount, "title", data.title);
  return data;
}

async function goto(page, url) {
  const res = await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await settle(page);
  const final = cleanUrl(page.url());
  const title = await page.title();
  const status = res ? res.status() : null;
  const body = await page.evaluate(() => (document.body?.innerText || "").slice(0, 500));
  const wall = /just a moment|verify you are human|cf-challenge|are you a robot/i.test(body) && body.length < 900;
  log("  open", final, status, title.slice(0, 80), wall ? "WALL" : "");
  return { final, title, status, wall, body: body.slice(0, 220) };
}

const desktopPages = [
  ["home", "/"],
  ["whats-new", "/release-notes/latest"],
  ["apps", "/apps"],
  ["security", "/security"],
  ["download", "/download"],
  ["download-thanks", "/download/thanks"],
  ["windows", "/windows"],
  ["help", "/help"],
  ["privacy", "/privacy"],
  ["terms", "/termsofuse"],
  ["changelog", "/changelog"],
  ["forwork", "/forwork"],
  ["pro", "/pro"],
  ["skills", "/skills"],
  ["earlybirds", "/earlybirds"],
  ["students", "/students"],
  ["notfound", "/this-page-does-not-exist-capture-2026"],
];

const authUrls = [
  ["login", "https://www.diabrowser.com/login"],
  ["signup", "https://www.diabrowser.com/signup"],
  ["auth", "https://auth.diabrowser.com/"],
  ["auth-login", "https://auth.diabrowser.com/login"],
  ["auth-signup", "https://auth.diabrowser.com/signup"],
  ["auth-sign-in", "https://auth.diabrowser.com/sign-in"],
  ["auth-sign-up", "https://auth.diabrowser.com/sign-up"],
];

async function desktop(browser) {
  const context = await browser.newContext({
    viewport: { width: 1440, height: 900 },
    deviceScaleFactor: 1,
    reducedMotion: "reduce",
  });
  const page = await context.newPage();
  page.setDefaultTimeout(20000);
  if (WANT.has("home") || WANT.has("measure") || WANT.has("pages")) {
    await goto(page, BASE + "/");
    const s = new Shooter(page, "home-light", 1440, 900, 1);
    if (WANT.has("home") || WANT.has("pages")) {
      await s.view("default");
      await s.full("full");
    }
    if (WANT.has("measure")) await measure(page, "home-measure.json");
    // Open the mobile-only menu if a desktop control exists. Record whatever appears.
    const opened = await page.evaluate(() => {
      const btn = [...document.querySelectorAll("button")].find((b) => /menu/i.test(b.getAttribute("aria-label") || ""));
      if (!btn) return null;
      const box = btn.getBoundingClientRect();
      if (box.width < 2) return { skipped: "hidden", label: btn.getAttribute("aria-label") };
      btn.click();
      return { clicked: btn.getAttribute("aria-label"), w: Math.round(box.width) };
    });
    log("  menu probe", JSON.stringify(opened));
    if (opened && opened.clicked) {
      await wait(page, 500);
      await s.view("menu");
      await page.keyboard.press("Escape").catch(() => {});
    }
  }
  if (WANT.has("pages")) {
    for (const [slug, route] of desktopPages) {
      if (slug === "home") continue;
      const info = await goto(page, BASE + route);
      fs.writeFileSync(path.join(RAW, `${slug}-open.json`), JSON.stringify(info, null, 2));
      if (info.wall) {
        log("  skip shot, challenge", slug);
        continue;
      }
      const s = new Shooter(page, `${slug}-light`, 1440, 900, 1);
      await s.view("default");
      if (["whats-new", "apps", "security", "download", "help", "notfound"].includes(slug)) {
        await s.full("full").catch((e) => log("  full fail", slug, e.message));
      }
    }
  }
  if (WANT.has("auth")) {
    for (const [slug, url] of authUrls) {
      let info;
      try {
        info = await goto(page, url);
      } catch (err) {
        log("  auth fail", slug, err.message.split("\n")[0]);
        fs.writeFileSync(path.join(RAW, `${slug}-probe.json`), JSON.stringify({ url, error: err.message.split("\n")[0] }, null, 2));
        continue;
      }
      const inputs = await page.evaluate(() => [...document.querySelectorAll("input, textarea, button, a")].slice(0, 30).map((el) => ({
        tag: el.tagName,
        type: el.type || null,
        text: (el.innerText || el.getAttribute("aria-label") || el.placeholder || "").replace(/\s+/g, " ").trim().slice(0, 60),
        valueLen: (el.value || "").length,
      })));
      const probe = { ...info, inputs, filled: inputs.some((i) => i.valueLen > 0) };
      fs.writeFileSync(path.join(RAW, `${slug}-probe.json`), JSON.stringify(probe, null, 2));
      if (info.wall) continue;
      const looksAuth = /sign in|log in|sign up|create account|continue with|email|password/i.test(info.body + " " + info.title);
      if (looksAuth) {
        const s = new Shooter(page, `${slug}-light`, 1440, 900, 1);
        await s.view("default");
      } else {
        log("  not an auth wall", slug, info.final);
      }
    }
  }
  await context.close();
}

async function mobile(browser) {
  const context = await browser.newContext({
    viewport: { width: 390, height: 844 },
    deviceScaleFactor: 2,
    isMobile: true,
    hasTouch: true,
    reducedMotion: "reduce",
  });
  const page = await context.newPage();
  await goto(page, BASE + "/");
  const s = new Shooter(page, "mobile-home-light", 390, 844, 2);
  await s.view("default");
  const opened = await page.evaluate(() => {
    const btn = [...document.querySelectorAll("button")].find((b) => /menu/i.test(b.getAttribute("aria-label") || "") && b.getBoundingClientRect().width > 2);
    if (!btn) return null;
    btn.click();
    return btn.getAttribute("aria-label");
  });
  log("  mobile menu", opened);
  await wait(page, 700);
  if (opened) await s.view("menu");
  await page.keyboard.press("Escape").catch(() => {});
  await wait(page, 300);
  const info = await goto(page, BASE + "/apps");
  fs.writeFileSync(path.join(RAW, "mobile-apps-open.json"), JSON.stringify(info, null, 2));
  const inner = new Shooter(page, "mobile-apps-light", 390, 844, 2);
  await inner.view("default");
  await context.close();
}

const browser = await chromium.launch({ headless: true });
try {
  if (WANT.has("home") || WANT.has("pages") || WANT.has("auth") || WANT.has("measure")) await desktop(browser);
  if (WANT.has("mobile")) await mobile(browser);
} finally {
  await browser.close();
}
log("done", RAW);
