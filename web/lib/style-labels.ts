// Small display helpers shared by the gallery, home page and chat cards.
type Swatches = Record<string, { role: string; value: string | null }[]>;

/** A package's card tint: its first accent/primary/brand/face colour. */
export const tintOf = (swatches: Swatches): string =>
  Object.values(swatches)
    .flat()
    .find((x) => /accent|primary|brand|face/i.test(x.role))?.value || "";

/** A theme id as a short label ("light-mobile" -> "mobile"). */
export const themeLabel = (t: string): string =>
  t.replace("-experimental", " (exp.)").replace("light-mobile", "mobile").replace("light-high-contrast", "high contrast");
