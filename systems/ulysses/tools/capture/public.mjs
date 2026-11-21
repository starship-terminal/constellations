// Captures the public Ulysses marketing site (https://ulysses.app) into RAW.
// PRODUCT (adapt): Ulysses public marketing site. Login and signup are photographed empty and not entered.
// ADAPTED_FOR names this product so the kit guard does not treat the file as the Gauth example.
const ADAPTED_FOR = "Ulysses";
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

const PW = process.env.PLAYWRIGHT || "/Users/kaichen/.design-systems/pw/node_modules/playwright/index.mjs";
const require = createRequire(PW);
const { chromium } = require(PW);

const RAW = process.env.RAW || path.join(os.homedir(), ".design-systems", "ulysses", "raw-shots");
fs.mkdirSync(RAW, { recursive: true });

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

async function hideCookies(page) {
  await page.evaluate(() => {
    const styleId = "capture-hide-consent";
    if (!document.getElementById(styleId)) {
      const style = document.createElement("style");
      style.id = styleId;
      style.textContent = [
        "#onetrust-consent-sdk, #onetrust-banner-sdk, .onetrust-pc-dark-filter,",
        "#ot-sdk-btn-floating, .ot-sdk-container,",
        "iframe[src*='onetrust'], iframe[src*='cookie'], iframe[title*='cookie' i],",
        "iframe[title*='privacy' i], iframe[id*='sp_message'], #sp_message_container,",
        "[class*='cookie-banner'], [id*='cookie-banner']",
        "{ display: none !important; visibility: hidden !important; pointer-events: none !important; }",
      ].join(" ");
      document.documentElement.appendChild(style);
    }
  }).catch(() => {});
}

async function settle(page) {
  await page.waitForLoadState("domcontentloaded").catch(() => {});
  await wait(page, 1200);
  await hideCookies(page);
  await wait(page, 300);
}

class Shooter {
  constructor(page, prefix, vw, vh, dpr) {
    this.p = page;
    this.prefix = prefix;
    this.vw = vw;
    this.dpr = dpr;
    this.requested = { viewport: { width: vw, height: vh }, deviceScaleFactor: dpr };
  }
  async view(name, sourceUrl) {
    const file = path.join(RAW, `${this.prefix}-${name}.png`);
    this.requested.sanitizedSourceUrl = cleanUrl(sourceUrl || this.p.url());
    await screenshotWithMetadata(this.p, { path: file }, this.requested);
    log("  shot", `${this.prefix}-${name}`);
  }
}

async function measure(page, outName) {
  const data = await page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      return {
        text: (el.innerText || "").replace(/\s+/g, " ").trim().slice(0, 120),
        color: s.color,
        backgroundColor: s.backgroundColor,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        letterSpacing: s.letterSpacing,
        borderRadius: s.borderRadius,
        padding: s.padding,
        border: s.border,
      };
    };
    const vars = [];
    for (const sheet of document.styleSheets) {
      let rules;
      try { rules = sheet.cssRules; } catch { continue; }
      if (!rules) continue;
      for (const r of rules) {
        if (!r.selectorText || (r.selectorText !== ":root" && r.selectorText !== "html") || !r.style) continue;
        for (const p of r.style) {
          if (p.startsWith("--")) vars.push([p, r.style.getPropertyValue(p).trim()]);
        }
      }
    }
    const get = [...document.querySelectorAll("a")].find((a) => (a.innerText || "").trim() === "Get Ulysses");
    const nav = document.querySelector("nav");
    const footer = document.querySelector("footer");
    const email = document.querySelector("input[type=email], input[name*='email']");
    const pass = document.querySelector("input[type=password]");
    const submit = document.querySelector("input[type=submit], button[type=submit]");
    return {
      url: location.origin + location.pathname,
      title: document.title,
      colorScheme: getComputedStyle(document.documentElement).colorScheme,
      body: pick(document.body),
      h1: pick(document.querySelector("h1")),
      h2: pick(document.querySelector("h2")),
      get: pick(get),
      nav: pick(nav),
      footer: footer ? { backgroundColor: getComputedStyle(footer).backgroundColor, color: getComputedStyle(footer).color } : null,
      email: pick(email),
      password: pick(pass),
      submit: pick(submit),
      vars,
      viewport: { innerWidth, innerHeight, devicePixelRatio },
    };
  });
  const file = path.join(RAW, outName);
  fs.writeFileSync(file, JSON.stringify(data, null, 2) + "\n");
  log("  measure", outName);
  return data;
}

async function openPage(browser, url, vw, vh, dpr) {
  const context = await browser.newContext({
    viewport: { width: vw, height: vh },
    deviceScaleFactor: dpr,
    colorScheme: "light",
  });
  const page = await context.newPage();
  await page.goto(url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await settle(page);
  return { context, page };
}

const PAGES = [
  ["home", "https://ulysses.app/en/"],
  ["pricing", "https://ulysses.app/en/pricing/"],
  ["students", "https://ulysses.app/en/students/"],
  ["releases", "https://ulysses.app/en/releases/"],
  ["people", "https://ulysses.app/people/"],
  ["jobs", "https://ulysses.app/jobs/"],
  ["press", "https://ulysses.app/press/"],
  ["privacy", "https://ulysses.app/privacy-policy/web/"],
  ["imprint", "https://ulysses.app/imprint/"],
  ["newsletter", "https://ulysses.app/newsletter/"],
  ["beta", "https://ulysses.app/en/beta/"],
  ["affiliate", "https://ulysses.app/en/affiliate/"],
  ["contact", "https://ulysses.app/contact/"],
  ["notfound", "https://ulysses.app/this-page-is-missing/"],
];

const browser = await chromium.launch({ headless: true });
try {
  for (const [name, url] of PAGES) {
    log("page", name, url);
    const { context, page } = await openPage(browser, url, 1440, 900, 1);
    const shot = new Shooter(page, name + "-light", 1440, 900, 1);
    await shot.view("default", url);
    if (name === "home" || name === "pricing" || name === "notfound") {
      await measure(page, name + "-computed.json");
    }
    await context.close();
  }

  log("login wall");
  {
    const url = "https://license.ulysses.app/users/sign_in";
    const { context, page } = await openPage(browser, url, 1440, 900, 1);
    const shot = new Shooter(page, "login-light", 1440, 900, 1);
    await shot.view("default", url);
    const data = await measure(page, "login-computed.json");
    fs.writeFileSync(path.join(RAW, "login-probe.json"), JSON.stringify({
      requested: url,
      landed: cleanUrl(page.url()),
      title: data.title,
      emailFilled: false,
      passwordFilled: false,
      submitted: false,
      note: "Photographed empty. Nothing typed. Log In not clicked. Forgot your password not opened. Sign up not followed from this page.",
    }, null, 2) + "\n");
    await context.close();
  }

  log("signup wall");
  {
    const url = "https://license.ulysses.app/checkout";
    const { context, page } = await openPage(browser, url, 1440, 900, 1);
    const shot = new Shooter(page, "signup-light", 1440, 900, 1);
    await shot.view("default", url);
    await measure(page, "signup-computed.json");
    fs.writeFileSync(path.join(RAW, "signup-probe.json"), JSON.stringify({
      requested: "https://license.ulysses.app/",
      landed: cleanUrl(page.url()),
      title: await page.title(),
      typed: false,
      submitted: false,
      checkoutEntered: false,
      note: "Volume licensing root redirects here. Photographed the empty signup form. Nothing typed. Continue to Checkout not clicked. Country select not opened. Terms not checked.",
    }, null, 2) + "\n");
    await context.close();
  }

  log("mobile home");
  {
    const url = "https://ulysses.app/en/";
    const { context, page } = await openPage(browser, url, 390, 844, 2);
    const shot = new Shooter(page, "home-light-390", 390, 844, 2);
    await shot.view("default", url);
    const toggle = page.locator("button[aria-label='Toggle navigation'], button.navbar-toggler").first();
    if (await toggle.count()) {
      await toggle.click();
      await wait(page, 500);
      await shot.view("drawer", url);
    }
    await context.close();
  }

  log("icon");
  {
    const { context, page } = await openPage(browser, "https://ulysses.app/en/", 1440, 900, 1);
    const href = await page.evaluate(() => document.querySelector("link[rel='apple-touch-icon']")?.href || null);
    if (href) {
      const res = await page.request.get(href);
      fs.writeFileSync(path.join(RAW, "apple-touch-icon.png"), await res.body());
      log("  icon", href);
    }
    await context.close();
  }
} finally {
  await browser.close();
}
log("done", RAW);
