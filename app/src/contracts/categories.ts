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

const legacyCategoryLabels: Record<string, string> = {
  learning: "Education",
  education: "Education",
  fintech: "Finance",
  finance: "Finance",
  ecommerce: "Marketplace",
  commerce: "Marketplace",
  entertainment: "Entertainment",
  media: "Entertainment",
  ai: "AI Tool",
  "ai-chat": "AI Tool",
  "ai-agent": "AI Tool",
  "ai-research": "AI Tool",
  "ai-media": "AI Tool",
  messaging: "Communication Tools",
  devtools: "Development Tools",
  social: "Social Networking",
  design: "Design & Media Editing",
  "design-tool": "Design & Media Editing",
  "design-resource": "Reference",
  "component-library": "Development Tools",
  crypto: "Web3 & Crypto",
  productivity: "Productivity",
  fitness: "Fitness",
  hardware: "Electronic & Devices",
  "food-drink": "Food & Drink",
  browser: "Utility",
  events: "Scheduling Tools",
  "super-app": "Travel & Booking",
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
  const target = categorySlug(
    legacyCategoryLabels[query] || query.split(":").at(-1) || query,
  );
  if (item.categoryIds !== undefined)
    return item.categoryIds.some(
      (id) => categorySlug(id.split(":").at(-1) || id) === target,
    );
  return categoryGroup(item.category) === categoryGroup(query);
}
