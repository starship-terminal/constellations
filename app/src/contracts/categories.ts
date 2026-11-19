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

/** The seed row a new catalog slug gets until someone curates its labels.

An add-only capture pull request cannot rewrite the committed seed for the
merge commit. The check derives this row from the catalog category and
accepts it beside the committed seed. A hand-edited label, or a missing row
for a package that was already on the base, still fails. */
export function derivedCategoryAssignment(
  row: CatalogCategoryRow,
): CuratedCategory {
  const platform = row.platform === "mobile" ? "mobile" : "web";
  const category = row.category || "";
  return {
    referenceId: `systems:${row.slug}`,
    groupId: platform === "mobile" ? "ios-categories" : "web-categories",
    labels: [],
    reason: category
      ? `Derived from catalog.json category ${category} until this package is curated.`
      : "Derived from catalog.json until this package is curated.",
  };
}

/** Slugs this catalog adds when every shared row is unchanged.

Null when a shared row was edited or removed, or when nothing was added.
The category check uses this so an add-only capture can keep the committed
seed. An edited existing row cannot. */
export function addedCatalogSlugs(
  rows: readonly CatalogCategoryRow[],
  baseRows: readonly CatalogCategoryRow[],
): Set<string> | null {
  const base = new Map(baseRows.map((row) => [row.slug, row]));
  const head = new Map(rows.map((row) => [row.slug, row]));
  if (base.size === 0 || head.size <= base.size) return null;
  for (const slug of base.keys()) {
    if (!head.has(slug)) return null;
  }
  for (const [slug, row] of base) {
    const current = head.get(slug);
    if (!current || JSON.stringify(current) !== JSON.stringify(row))
      return null;
  }
  return new Set([...head.keys()].filter((slug) => !base.has(slug)));
}

/** Rows the committed seed must contain for this catalog.

`baseSlugs` is the catalog on the pull request base. A slug in `rows` that
is not in `baseSlugs` may use the derived assignment when the committed seed
has no row yet. Every base slug must still match the committed seed exactly.
Returns the problems, empty when the seed covers the catalog. */
export function categorySeedGaps(
  rows: readonly CatalogCategoryRow[],
  committed: readonly CuratedCategory[],
  baseSlugs?: ReadonlySet<string>,
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
    if (!assignment) {
      if (baseSlugs && !baseSlugs.has(row.slug)) continue;
      problems.push(`${row.slug}: missing from the category seed`);
      continue;
    }
    if (assignment.groupId !== groupId) {
      problems.push(
        `${row.slug}: category group ${assignment.groupId} does not match platform ${row.platform || "web"}`,
      );
    }
    if (baseSlugs && !baseSlugs.has(row.slug)) {
      const derived = derivedCategoryAssignment(row);
      if (
        assignment.reason !== derived.reason ||
        assignment.groupId !== derived.groupId ||
        assignment.labels.length !== derived.labels.length
      ) {
        problems.push(`${row.slug}: added category seed row was hand-edited`);
      }
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
