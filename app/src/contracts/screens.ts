import type { LibraryItem, ReferenceMedia } from "./library";

export type ScreenKind = "screenshot" | "crop";
/** A captured asset, retaining both its package and original media identity. */
export interface ScreenItem {
  id: string;
  reference: LibraryItem;
  media: ReferenceMedia;
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
  referenceId?: string;
  /** Exact original capture identity; ignores pagination when supplied. */
  screenId?: string;
  sort?: "recent" | "name";
  offset?: number;
  limit?: number;
}
export interface ScreenFacet {
  value: string;
  count: number;
}
export interface ScreenResponse {
  items: ScreenItem[];
  total: number;
  facets: {
    platforms: ScreenFacet[];
    categories: ScreenFacet[];
    tags: ScreenFacet[];
    groups: ScreenFacet[];
    kinds: ScreenFacet[];
  };
  /** This corpus does not record Refero's screen classifications or ordered flows. */
  taxonomy: { pageTypes: string[]; uiElements: string[]; uxPatterns: string[] };
}
