import type { LibraryItem, ReferenceMedia } from "./library";

export type ScreenKind = "screenshot" | "crop";
/** A captured asset, retaining both its package and original media identity. */
export interface ScreenItem {
  id: string;
  reference: LibraryItem;
  media: ReferenceMedia;
  /** Verified app-owned classifications for this original capture. */
  termIds?: string[];
}
export interface ScreenQuery {
  query?: string;
  scope?: "all" | "media";
  platform?: string;
  category?: string;
  tag?: string;
  theme?: string;
  group?: string;
  kind?: ScreenKind;
  /** Selected packages are combined with OR. */
  referenceIds?: string[];
  /** All selected taxonomy terms must be present on the same capture. */
  termIds?: string[];
  /** Flows require verified ordered sequences, which this corpus lacks. */
  mode?: "screens" | "flows";
  /** Exact original capture identity; ignores pagination when supplied. */
  screenId?: string;
  sort?: "recent" | "name";
  offset?: number;
  limit?: number;
  /**
   * Keep at most this many captures per product and order the rest
   * round-robin across products (first-seen order), so a page of results
   * shows many products. `total` still counts every match; page by
   * `pageable`, which counts the sampled captures.
   */
  perProduct?: number;
}
export interface ScreenFacet {
  value: string;
  count: number;
}
export interface ScreenResponse {
  items: ScreenItem[];
  total: number;
  /** How many captures offset/limit can page through: `total`, or the
   * sampled count when `perProduct` is set. */
  pageable: number;
  /** Actual platform/kind corpus counts, before reference, text or term filters. */
  termCounts: Record<string, number>;
  facets: {
    platforms: ScreenFacet[];
    categories: ScreenFacet[];
    tags: ScreenFacet[];
    groups: ScreenFacet[];
    kinds: ScreenFacet[];
  };
  /** Legacy summary; ordered flows remain unavailable without sequence evidence. */
}
