"use client";

// Theme and sidebar prefs. The DOM (html[data-theme], html[data-nav], set
// before paint by layout.tsx's inline script) is the source of truth; every
// writer goes through here so readers (Rail, Settings) hear about changes,
// including ones made in another tab.
import { useEffect, useState } from "react";

/** The chosen theme; "system" follows prefers-color-scheme and is stored as no value. */
export type Theme = "system" | "light" | "dark";
export interface Prefs {
  theme: Theme;
  /** The theme on screen (html[data-theme]), whatever was chosen. */
  resolved: "light" | "dark";
  collapsed: boolean;
}

const EVENT = "ds-prefs";
// What the server renders; the first effect replaces it with the DOM's value.
const SERVER: Prefs = { theme: "system", resolved: "dark", collapsed: false };

const asTheme = (v: string | null): Theme => (v === "light" || v === "dark" ? v : "system");

// This tab's choice, kept in memory so it holds when storage is blocked or
// full (the save is best-effort); null until this tab chooses or hears one.
let choice: Theme | null = null;

const stored = (): Theme => {
  if (choice) return choice;
  try {
    return asTheme(localStorage.getItem("ds-theme"));
  } catch {
    return "system";
  }
};

const systemTheme = (): "light" | "dark" => (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");

const read = (): Prefs => {
  const d = document.documentElement.dataset;
  return { theme: stored(), resolved: d.theme === "light" ? "light" : "dark", collapsed: d.nav === "collapsed" };
};

const applyNav = (c: boolean) => {
  const root = document.documentElement;
  if (c) root.dataset.nav = "collapsed";
  else delete root.dataset.nav;
};

export function setTheme(t: Theme) {
  choice = t;
  document.documentElement.dataset.theme = t === "system" ? systemTheme() : t;
  try {
    if (t === "system") localStorage.removeItem("ds-theme");
    else localStorage.setItem("ds-theme", t);
  } catch {}
  window.dispatchEvent(new Event(EVENT));
}

/** Apply the stored theme and sidebar fold when the document has none yet.
    layout.tsx's inline script does this before paint; it does not run when
    Next falls back to client rendering the root layout (a notFound() from a
    dynamic route does), and React never executes a script it renders itself.
    A no-op when the script already ran. */
export function bootPrefs() {
  const d = document.documentElement;
  if (!d.dataset.theme) d.dataset.theme = stored() === "system" ? systemTheme() : stored();
  try {
    if (localStorage.getItem("ds-nav") === "collapsed") d.dataset.nav = "collapsed";
  } catch {}
}

export function setCollapsed(c: boolean) {
  applyNav(c);
  try {
    if (c) localStorage.setItem("ds-nav", "collapsed");
    else localStorage.removeItem("ds-nav");
  } catch {}
  window.dispatchEvent(new Event(EVENT));
}

export function usePrefs(): Prefs {
  const [prefs, setPrefs] = useState<Prefs>(SERVER);
  useEffect(() => {
    const sync = () => setPrefs(read());
    // Another tab changed a pref: apply it to this document too.
    const onStorage = (e: StorageEvent) => {
      if (e.key === "ds-theme") {
        choice = asTheme(e.newValue);
        document.documentElement.dataset.theme = choice === "system" ? systemTheme() : choice;
      }
      else if (e.key === "ds-nav") applyNav(e.newValue === "collapsed");
      else return;
      sync();
    };
    // The OS switched light/dark: follow it while the choice is System.
    const media = matchMedia("(prefers-color-scheme: dark)");
    const onMedia = () => {
      if (stored() !== "system") return;
      document.documentElement.dataset.theme = systemTheme();
      sync();
    };
    sync();
    window.addEventListener(EVENT, sync);
    window.addEventListener("storage", onStorage);
    media.addEventListener("change", onMedia);
    return () => {
      window.removeEventListener(EVENT, sync);
      window.removeEventListener("storage", onStorage);
      media.removeEventListener("change", onMedia);
    };
  }, []);
  return prefs;
}
