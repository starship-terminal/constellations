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

A slug with no seed row is accepted. The seed still has to cover every slug
it does list, with the right platform group, and every seed row still needs
a catalog package. That is the state an add-only capture leaves, and it is
the state main checks after the capture merges. A wrong platform group, or a
seed row whose package is gone, still fails. */
export function categorySeedGaps(
  rows: readonly CatalogCategoryRow[],
  committed: readonly CuratedCategory[],
): string[] {
  const byReference = new Map(
    committed.map((entry) => [entry.referenceId, entry]),
  );
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
    if (!assignment) continue;
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
  return categoryGroup(item.category) === categoryGroup(query);
}
