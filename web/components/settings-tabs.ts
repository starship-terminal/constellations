// The Settings page's sections, one tab each, and the two rules the tab list
// follows: which tab a URL hash opens, and where an arrow key moves.
// Kept out of Settings.tsx so the node test runner can load it.

// The id is the panel's id and the URL hash, so /settings#model-provider (the
// chat's setup link) opens that tab; the aliases keep the hashes of the older
// one-page layout working.
export const TABS = [
  { id: "model-provider", label: "Model provider", aliases: [] },
  { id: "appearance", label: "Appearance", aliases: ["preferences"] },
  { id: "agents", label: "For agents", aliases: ["for-agents"] },
  { id: "saved-media", label: "Saved media", aliases: [] },
  { id: "data", label: "Data", aliases: [] },
] as const;

export type TabId = (typeof TABS)[number]["id"];

/** The tab a URL hash names, or null for none or an unknown one. */
export function tabFromHash(hash: string): TabId | null {
  let h = hash.replace(/^#/, "");
  try {
    h = decodeURIComponent(h);
  } catch {
    return null;
  }
  const t = TABS.find((x) => x.id === h || (x.aliases as readonly string[]).includes(h));
  return t ? t.id : null;
}

/** The tab a key moves to from `current`, or null for a key the list ignores.
    Both arrow pairs work, since the list is vertical at desktop width and a
    row on a phone; it wraps at either end. */
export function tabForKey(current: TabId, key: string): TabId | null {
  const i = TABS.findIndex((x) => x.id === current);
  const n = TABS.length;
  const next =
    key === "ArrowDown" || key === "ArrowRight"
      ? (i + 1) % n
      : key === "ArrowUp" || key === "ArrowLeft"
        ? (i - 1 + n) % n
        : key === "Home"
          ? 0
          : key === "End"
            ? n - 1
            : -1;
  return next < 0 ? null : TABS[next].id;
}
