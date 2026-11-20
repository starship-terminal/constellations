/** Home browse rows. These are filename/tag searches over captured media, not
 * inferred annotations, so a word under two rows of the same media kind would
 * show the same captures twice. */
export const browseSections = [
  {
    title: "Page Types",
    kind: "screenshot",
    choices: [
      "Dashboard",
      "Home",
      "Settings",
      "Profile",
      "Search",
      "Onboarding",
    ],
  },
  {
    title: "UX Patterns",
    kind: "screenshot",
    choices: ["Filter", "Empty", "Navigation"],
  },
  {
    title: "UI Elements",
    kind: "crop",
    choices: ["Button", "Dialog", "Menu", "Table", "Navigation", "Card"],
  },
] as const;
export type BrowseSection = (typeof browseSections)[number];

/** Eight captures, at most two per product, rotated across products by the
 * server before it repeats one. */
export function browseParams(
  section: BrowseSection,
  choice: string,
  platform?: string,
): URLSearchParams {
  const params = new URLSearchParams({
    q: choice,
    kind: section.kind,
    scope: "media",
    limit: "8",
    perProduct: "2",
  });
  if (platform) params.set("platform", platform);
  return params;
}
