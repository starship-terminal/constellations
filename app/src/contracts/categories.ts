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
  commerce: "Marketplace",
  entertainment: [
    "Entertainment",
    "Video Streaming",
    "Music Streaming",
    "Magazines & Newspapers",
  ],
  media: [
    "Entertainment",
    "Video Streaming",
    "Music Streaming",
    "Magazines & Newspapers",
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
};
const categorySlug = (value: string) =>
  value
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, "-")
    .replace(/^-|-$/g, "");
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
