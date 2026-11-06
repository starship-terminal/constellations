"use client";

// Theme and sidebar prefs. The DOM (html[data-theme], html[data-nav], set
// before paint by layout.tsx's inline script) is the source of truth; every
// writer goes through here so readers (Rail, Settings) hear about changes,
// including ones made in another tab.
import { useEffect, useState } from "react";

export type Theme = "light" | "dark";
export interface Prefs {
  theme: Theme;
  collapsed: boolean;
}

const EVENT = "ds-prefs";
// What the server renders; the first effect replaces it with the DOM's value.
const SERVER: Prefs = { theme: "dark", collapsed: false };

const read = (): Prefs => {
  const d = document.documentElement.dataset;
  return { theme: d.theme === "light" ? "light" : "dark", collapsed: d.nav === "collapsed" };
};

const applyNav = (c: boolean) => {
  const root = document.documentElement;
  if (c) root.dataset.nav = "collapsed";
  else delete root.dataset.nav;
};

export function setTheme(t: Theme) {
  document.documentElement.dataset.theme = t;
  try {
    localStorage.setItem("ds-theme", t);
  } catch {}
  window.dispatchEvent(new Event(EVENT));
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
      if (e.key === "ds-theme" && (e.newValue === "light" || e.newValue === "dark"))
        document.documentElement.dataset.theme = e.newValue;
      else if (e.key === "ds-nav") applyNav(e.newValue === "collapsed");
      else return;
      sync();
    };
    sync();
    window.addEventListener(EVENT, sync);
    window.addEventListener("storage", onStorage);
    return () => {
      window.removeEventListener(EVENT, sync);
      window.removeEventListener("storage", onStorage);
    };
  }, []);
  return prefs;
}
