import type { LibraryItem } from "@/contracts/library";
import { getStore, type ResearchStore } from "@/server/db";

/** Apply app-owned classification without altering captured source evidence. */
export async function withReferenceCategories<T extends LibraryItem>(
  items: T[],
  store?: ResearchStore,
): Promise<T[]> {
  const database = store || (await getStore());
  const [groups, assignments] = await Promise.all([
    database.listTaxonomyGroups(),
    database.listReferenceCategories(),
  ]);
  const terms = new Map(
    groups
      .filter(
        (group) =>
          group.id === "web-categories" || group.id === "ios-categories",
      )
      .flatMap((group) => group.terms.map((term) => [term.id, term] as const)),
  );
  const byReference = new Map<string, { id: string; label: string }[]>();
  for (const assignment of assignments) {
    const term = terms.get(assignment.termId);
    if (!term) continue;
    const values = byReference.get(assignment.referenceId) || [];
    values.push({ id: term.id, label: term.label });
    byReference.set(assignment.referenceId, values);
  }
  return items.map((item) => {
    if (item.source !== "systems") return item;
    const categories = byReference.get(item.id) || [];
    return {
      ...item,
      categoryIds: categories.map((term) => term.id),
      categories,
      category: categories[0]?.label || "",
    };
  });
}
