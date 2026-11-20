import type { LibraryItem } from "@/contracts/library";
import { getStore, type ResearchStore } from "@/server/db";
import seed from "@/data/system-categories.json";

// Packages the category seed curated. One of these with no rows was cleared
// in the app; any other package with no rows was simply never curated.
const curated = new Set(seed.map((row) => row.referenceId));

/** Apply app-owned classification without altering captured source evidence. */
export async function withReferenceCategories<T extends LibraryItem>(
  items: T[],
  store?: ResearchStore,
): Promise<T[]> {
  const referenceIds = items
    .filter((item) => item.source === "systems")
    .map((item) => item.id);
  if (referenceIds.length === 0) return items;
  const database = store || (await getStore());
  const assignments = await database.listReferenceCategoryDetails(referenceIds);
  const byReference = new Map<string, { id: string; label: string }[]>();
  for (const assignment of assignments) {
    const values = byReference.get(assignment.referenceId) || [];
    values.push({ id: assignment.termId, label: assignment.label });
    byReference.set(assignment.referenceId, values);
  }
  return items.map((item) => {
    if (item.source !== "systems") return item;
    const categories = byReference.get(item.id);
    // Never curated: keep the catalog category and leave categoryIds unset,
    // so category links match it the legacy way and it lists as uncategorised
    // instead of disappearing from every category.
    if (!categories && !curated.has(item.id)) return item;
    const terms = categories || [];
    return {
      ...item,
      categoryIds: terms.map((term) => term.id),
      categories: terms,
      category: terms[0]?.label || "",
    };
  });
}
