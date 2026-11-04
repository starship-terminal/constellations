import type { LibraryItem } from "@/contracts/library";
import type { TaxonomyGroup } from "@/contracts/taxonomy";
import { matchesCategory } from "@/contracts/categories";

export function pickerGroups(
  groups: readonly TaxonomyGroup[],
  platform: string,
) {
  const prefix = platform === "mobile" ? "ios-" : "web-";
  return groups.filter(
    (group) => group.kind === "taxonomy" && group.id.startsWith(prefix),
  );
}
export function groupCaption(groupId: string) {
  if (groupId.endsWith("categories")) return "Category";
  if (groupId.endsWith("flows")) return "Flow";
  if (groupId.endsWith("ui-elements")) return "UI Element";
  if (groupId.endsWith("ux-patterns")) return "UX Pattern";
  if (groupId.endsWith("fonts")) return "Font";
  return groupId === "ios-screen-types" ? "Screen Type" : "Page Type";
}
export function legacyCategoryLabels(
  groups: readonly TaxonomyGroup[],
  query: string,
) {
  if (!query) return "";
  return (
    [
      ...new Set(
        groups
          .filter((group) => group.id.endsWith("categories"))
          .flatMap((group) => group.terms)
          .filter((term) =>
            matchesCategory({ category: "", categoryIds: [term.id] }, query),
          )
          .map((term) => term.label),
      ),
    ].join(", ") || query
  );
}
/** Gallery suggestions cover every platform; screen search defaults to web. */
export function productSearchPlatform(params: Pick<URLSearchParams, "get">) {
  return (
    params.get("platform") || (params.get("view") === "screens" ? "web" : "")
  );
}
export function selectProductSearch(
  params: URLSearchParams,
  item: Pick<LibraryItem, "id" | "platform">,
) {
  const next = new URLSearchParams(params);
  if (!next.getAll("referenceId").includes(item.id))
    next.append("referenceId", item.id);
  if (!next.get("platform")) next.set("platform", item.platform);
  return next;
}
/** Keep filters with the same recorded meaning when changing platform. */
export function platformSearch(
  params: URLSearchParams,
  platform: string,
  groups: readonly TaxonomyGroup[],
  items: readonly LibraryItem[],
) {
  const next = new URLSearchParams(params);
  platform ? next.set("platform", platform) : next.delete("platform");
  const destinations = pickerGroups(groups, platform);
  const terms = params.getAll("term");
  next.delete("term");
  for (const id of terms) {
    const source = groups.find((group) =>
      group.terms.some((term) => term.id === id),
    );
    const term = source?.terms.find((term) => term.id === id);
    const kind = source?.id.replace(/^(web|ios)-/, "");
    const destination = destinations.find(
      (group) =>
        group.id.replace(/^(web|ios)-/, "") === kind ||
        (kind === "page-types" && group.id === "ios-screen-types") ||
        (kind === "screen-types" && group.id === "web-page-types"),
    );
    const match = destination?.terms.find(
      (candidate) => candidate.label === term?.label,
    );
    if (match && !next.getAll("term").includes(match.id))
      next.append("term", match.id);
  }
  const category = params.get("category");
  if (category) {
    const match = destinations
      .filter((group) => group.id.endsWith("categories"))
      .flatMap((group) => group.terms)
      .filter((term) =>
        matchesCategory({ category: "", categoryIds: [term.id] }, category),
      );
    // A legacy alias can mean several alternatives. Keep that OR category
    // filter instead of turning its labels into an AND term selection.
    if (match.length === 1) next.set("category", match[0].id);
    else if (!match.length) next.delete("category");
  }
  next.delete("referenceId");
  for (const id of params.getAll("referenceId")) {
    const item = items.find((candidate) => candidate.id === id);
    if (!platform || item?.platform === platform)
      next.append("referenceId", id);
  }
  next.delete("screen");
  next.delete("offset");
  return next;
}
