import { describe, expect, it } from "vitest";
import {
  THEME_OPTIONS,
  themeInitScript,
  themeStorageChanged,
} from "@/components/appearance";

// Evaluates the inline script the root layout runs before first paint.
function run(stored: string | null, prefersDark = false, throws = false) {
  const root = { dataset: {} as Record<string, string> };
  const env = {
    document: { documentElement: root },
    localStorage: {
      getItem: () => {
        if (throws) throw new Error("blocked");
        return stored;
      },
    },
    matchMedia: () => ({ matches: prefersDark }),
  };
  new Function("document", "localStorage", "matchMedia", themeInitScript)(
    env.document,
    env.localStorage,
    env.matchMedia,
  );
  return root.dataset.theme;
}

describe("themeInitScript", () => {
  it("applies the stored theme before hydration", () => {
    expect(run("light")).toBe("light");
    expect(run("dark")).toBe("dark");
  });
  it("resolves system against the OS preference", () => {
    expect(run("system", false)).toBe("light");
    expect(run("system", true)).toBe("dark");
  });
  it("falls back to dark for a missing, unknown or unreadable value", () => {
    expect(run(null)).toBe("dark");
    expect(run("sepia")).toBe("dark");
    expect(run("light", false, true)).toBe("dark");
  });
});

describe("themeStorageChanged", () => {
  it("reacts to the theme key and a cleared store, not to other keys", () => {
    expect(themeStorageChanged("studio-theme")).toBe(true);
    expect(themeStorageChanged(null)).toBe(true);
    expect(themeStorageChanged("ds-icon")).toBe(false);
  });
});

describe("THEME_OPTIONS", () => {
  it("lists System, Dark, Light in that order", () => {
    expect(THEME_OPTIONS.map((o) => o.label)).toEqual([
      "System",
      "Dark",
      "Light",
    ]);
  });
});
