const aliases = new Map<string, string>([
  ["learning", "education"],
  ["fintech", "finance"],
  ["ecommerce", "commerce"],
  ["entertainment", "media"],
]);

/** Share category groups across package browsing and individual captures. */
export function categoryGroup(value: string): string {
  return aliases.get(value) || value;
}

const legacyCategoryLabels: Record<string, string | string[]> = {
  learning: "Education",
  education: "Education",
  fintech: "Finance",
  finance: "Finance",
  ecommerce: "Marketplace",
  "e-commerce": "Marketplace",
  commerce: "Marketplace",
  entertainment: [
    "Entertainment",
    "Video Streaming",
    "Music Streaming",
    "Magazines & Newspapers",
  ],
  // The legacy media bucket also held creator tools and community products.
  media: [
    "Entertainment",
    "Video Streaming",
    "Music Streaming",
    "Magazines & Newspapers",
    "Design & Media Editing",
    "Social Networking",
  ],
  ai: "AI Tool",
  "ai-chat": "AI Tool",
  "ai-agent": "AI Tool",
  "ai-research": ["AI Tool", "Reference", "Inspiration Board"],
  "ai-media": "AI Tool",
  messaging: "Communication Tools",
  devtools: "Development Tools",
  social: "Social Networking",
  design: "Design & Media Editing",
  "design-tool": "Design & Media Editing",
  "design-resource": "Reference",
  "component-library": "Development Tools",
  crypto: "Web3 & Crypto",
  productivity: [
    "Productivity",
    "Development Tools",
    "Project Management",
    "Scheduling Tools",
  ],
  fitness: "Fitness",
  hardware: "Electronic & Devices",
  "food-drink": "Food & Drink",
  browser: "Utility",
  events: "Scheduling Tools",
  "super-app": ["Travel & Booking", "Food Delivery"],
  travel: "Travel & Booking",
  directory: ["Inspiration Board", "Reference"],
};
const categorySlug = (value: string) =>
  value
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, "-")
    .replace(/^-|-$/g, "");
export type CuratedCategory = {
  referenceId: string;
  groupId: string;
  labels: string[];
  reason: string;
};

export type CatalogCategoryRow = {
  slug: string;
  platform?: string;
  category?: string;
};

/** Rows the committed seed must contain for this catalog.

A slug with no seed row is accepted only when `previous` also has no row for
it. That is a package the seed never curated. Dropping a row `previous`
already had is a deleted assignment, and that fails. On a pull request,
`previous` is the base seed. On main, and in the unit test, it is the
committed seed itself, so the check still catches a fixture that deletes a
curated row. A wrong platform group, or a seed row whose package is gone,
still fails. */
export function categorySeedGaps(
  rows: readonly CatalogCategoryRow[],
  committed: readonly CuratedCategory[],
  previous: readonly CuratedCategory[] = committed,
): string[] {
  const byReference = new Map(
    committed.map((entry) => [entry.referenceId, entry]),
  );
  const curated = new Set(previous.map((entry) => entry.referenceId));
  const problems: string[] = [];
  const seen = new Set<string>();
  for (const row of rows) {
    const referenceId = `systems:${row.slug}`;
    if (seen.has(referenceId))
      problems.push(`${row.slug}: duplicate catalog slug`);
    seen.add(referenceId);
    const assignment = byReference.get(referenceId);
    const groupId =
      row.platform === "mobile" ? "ios-categories" : "web-categories";
    if (!assignment) {
      if (curated.has(referenceId)) {
        problems.push(`${row.slug}: curated category row was deleted`);
      }
      continue;
    }
    if (assignment.groupId !== groupId) {
      problems.push(
        `${row.slug}: category group ${assignment.groupId} does not match platform ${row.platform || "web"}`,
      );
    }
  }
  for (const entry of committed) {
    if (!seen.has(entry.referenceId)) {
      problems.push(
        `${entry.referenceId}: category seed row has no catalog package`,
      );
    }
  }
  return problems;
}

/** The category filter for references that carry no category term. */
export const UNCATEGORISED = "uncategorised";

/** Old deep links remain usable; new links carry namespaced database term IDs. */
export function matchesCategory(
  item: {
    category: string;
    categoryIds?: string[];
    categories?: { id: string; label: string }[];
  },
  query: string,
): boolean {
  if (!query) return true;
  if (query === UNCATEGORISED) return !item.categoryIds?.length;
  const labels =
    (Object.hasOwn(legacyCategoryLabels, query)
      ? legacyCategoryLabels[query]
      : undefined) ||
    query.split(":").at(-1) ||
    query;
  const targets = (Array.isArray(labels) ? labels : [labels]).map(categorySlug);
  if (item.categoryIds !== undefined)
    return item.categoryIds.some((id) =>
      targets.includes(categorySlug(id.split(":").at(-1) || id)),
    );
  if (categoryGroup(item.category) === categoryGroup(query)) return true;
  // An item with only a catalog category (a package the seed never curated)
  // also matches the one term its old link names. Switching platform
  // rewrites such a link, `finance` say, to that term's ID. A link naming
  // several labels stays a link, so it never needs this.
  const own = Object.hasOwn(legacyCategoryLabels, item.category)
    ? legacyCategoryLabels[item.category]
    : undefined;
  return (
    query.includes(":") &&
    typeof own === "string" &&
    targets.includes(categorySlug(own))
  );
}
