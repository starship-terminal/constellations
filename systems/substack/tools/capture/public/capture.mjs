#!/usr/bin/env node
/**
 * Public Substack capture. Does not type, submit, click identity providers,
 * subscribe, or follow a signed-in inbox.
 *
 * PLAYWRIGHT=~/.design-systems/pw/node_modules/playwright/index.mjs \
 *   node systems/substack/tools/capture/public/capture.mjs
 */
import { createRequire } from "node:module";
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const pwPath = process.env.PLAYWRIGHT || path.join(process.env.HOME, ".design-systems/pw/node_modules/playwright/index.js");
const { chromium } = require(pwPath);

const here = path.dirname(fileURLToPath(import.meta.url));
const pkg = path.resolve(here, "../../..");
const shots = path.join(pkg, "screenshots");
const raw = path.join(pkg, "raw");
const outDir = process.env.SHOTS || "/tmp/substack-shots";

const DESKTOP = { width: 1440, height: 900 };
const PHONE = { width: 390, height: 844 };

function hexFrom(color) {
  if (!color) return null;
  const m = color.match(/rgba?\((\d+),\s*(\d+),\s*(\d+)/);
  if (!m) return color;
  const h = (n) => Number(n).toString(16).padStart(2, "0");
  return `#${h(m[1])}${h(m[2])}${h(m[3])}`;
}

async function measure(page) {
  return page.evaluate(() => {
    const pick = (el) => {
      if (!el) return null;
      const s = getComputedStyle(el);
      const r = el.getBoundingClientRect();
      return {
        text: (el.innerText || el.getAttribute("aria-label") || el.placeholder || "").replace(/\s+/g, " ").trim().slice(0, 80),
        backgroundColor: s.backgroundColor,
        color: s.color,
        borderRadius: s.borderRadius,
        border: `${s.borderTopWidth} ${s.borderTopStyle} ${s.borderTopColor}`,
        fontFamily: s.fontFamily,
        fontSize: s.fontSize,
        fontWeight: s.fontWeight,
        lineHeight: s.lineHeight,
        height: Math.round(r.height),
        width: Math.round(r.width),
        padding: s.padding,
        boxShadow: s.boxShadow.slice(0, 220),
        letterSpacing: s.letterSpacing,
      };
    };
    const byText = (sel, re) => [...document.querySelectorAll(sel)].find((el) => re.test((el.innerText || el.getAttribute("aria-label") || "").trim()));
    return {
      url: location.href,
      title: document.title,
      htmlClass: document.documentElement.className,
      viewport: { innerWidth: innerWidth, innerHeight: innerHeight, dpr: devicePixelRatio },
      body: pick(document.body),
      h1: pick(document.querySelector("h1")),
      h2: pick(document.querySelector("h2")),
      dialog: pick(document.querySelector("[role=dialog]")),
      primary: pick(byText("button, a", /^(Continue|Start publishing|Start your Substack|Subscribe)$/)),
      field: pick(document.querySelector("input[type=email], input[placeholder*='email' i], input[placeholder*='Email']")),
      checkbox: pick(document.querySelector("input[type=checkbox]")),
    };
  });
}

async function shoot(page, name) {
  const file = path.join(outDir, `${name}.png`);
  await page.screenshot({ path: file, fullPage: false });
  const box = await page.evaluate(() => ({
    innerWidth: window.innerWidth,
    innerHeight: window.innerHeight,
    dpr: window.devicePixelRatio,
    vv: window.visualViewport && { w: window.visualViewport.width, h: window.visualViewport.height, scale: window.visualViewport.scale },
  }));
  return { file, name, ...box, url: page.url() };
}

async function dismiss(page) {
  await page.keyboard.press("Escape").catch(() => {});
  await page.waitForTimeout(200);
}

async function main() {
  await mkdir(outDir, { recursive: true });
  await mkdir(shots, { recursive: true });
  await mkdir(raw, { recursive: true });
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: DESKTOP,
    deviceScaleFactor: 1,
    colorScheme: "dark",
    locale: "en-US",
  });
  const page = await context.newPage();
  page.setDefaultTimeout(25000);
  const log = [];
  const readings = {};

  async function goto(url) {
    await page.goto(url, { waitUntil: "domcontentloaded" });
    await page.waitForTimeout(1200);
  }

  // Home
  await goto("https://substack.com/");
  readings.home = await measure(page);
  log.push(await shoot(page, "home-dark-default"));

  // Sign-in dialog, empty. Do not type.
  await page.getByRole("button", { name: "Sign in" }).first().click();
  await page.waitForTimeout(600);
  readings.signinDialog = await measure(page);
  log.push(await shoot(page, "home-dark-signin-dialog"));
  await dismiss(page);

  // Category filter, still the public home.
  await goto("https://substack.com/?category=technology");
  await page.waitForTimeout(400);
  log.push(await shoot(page, "home-dark-category-technology"));

  // About, with Resources menu open.
  await goto("https://substack.com/about");
  readings.about = await measure(page);
  log.push(await shoot(page, "about-light-default"));
  await page.getByRole("button", { name: "Resources" }).click();
  await page.waitForTimeout(400);
  log.push(await shoot(page, "about-light-resources-menu"));
  await dismiss(page);
  await page.getByRole("button", { name: "Creators", exact: true }).click();
  await page.waitForTimeout(300);
  log.push(await shoot(page, "about-light-creators-menu"));
  await dismiss(page);

  // App marketing page. Close the download dialog without submitting.
  await goto("https://substack.com/app");
  readings.app = await measure(page);
  log.push(await shoot(page, "app-dark-default"));
  await dismiss(page);
  await page.waitForTimeout(300);
  log.push(await shoot(page, "app-dark-page"));

  // Public post. Close the subscribe prompt. Do not subscribe.
  await goto("https://www.oneusefulthing.org/p/fable-52-and-jagged-agi");
  await page.waitForTimeout(800);
  await dismiss(page);
  await page.waitForTimeout(400);
  readings.post = await measure(page);
  log.push(await shoot(page, "post-light-default"));

  // Explore and a leaderboard.
  await goto("https://substack.com/explore");
  readings.explore = await measure(page);
  log.push(await shoot(page, "explore-dark-default"));
  await goto("https://substack.com/leaderboard/technology/paid");
  log.push(await shoot(page, "leaderboard-dark-default"));

  // Discover page that an unknown path lands on (public, not an error wall).
  await goto("https://substack.com/this-page-does-not-exist-capture-2026");
  readings.discover = await measure(page);
  log.push(await shoot(page, "discover-light-default"));

  // Login wall. Do not type. Do not click Continue.
  await goto("https://substack.com/sign-in");
  readings.login = await measure(page);
  log.push(await shoot(page, "login-dark-default"));

  // Signup wall. Do not type. Do not check the box. Do not click Continue.
  await goto("https://substack.com/onboarding?flow=creator_signup");
  readings.signup = await measure(page);
  log.push(await shoot(page, "signup-dark-default"));

  // Privacy, a public legal page linked from the signup wall.
  await goto("https://substack.com/privacy");
  readings.privacy = await measure(page);
  log.push(await shoot(page, "privacy-light-default"));

  // Phone: homepage and one inner page (about).
  await page.setViewportSize(PHONE);
  await goto("https://substack.com/");
  readings.homePhone = await measure(page);
  log.push(await shoot(page, "mobile-home-dark-default"));
  const menu = page.getByRole("button", { name: /menu|More|Open/i }).first();
  if (await menu.count()) {
    await menu.click().catch(() => {});
    await page.waitForTimeout(400);
    log.push(await shoot(page, "mobile-home-dark-menu"));
  }
  await goto("https://substack.com/about");
  readings.aboutPhone = await measure(page);
  log.push(await shoot(page, "mobile-about-light-default"));

  await writeFile(path.join(raw, "public-readings.json"), JSON.stringify({ date: "2026-11-21", readings, shots: log }, null, 2));
  await writeFile(path.join(outDir, "manifest.json"), JSON.stringify(log, null, 2));
  console.log(JSON.stringify(log.map((s) => s.name), null, 2));
  await browser.close();
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
