export type Source = "systems" | "refero";
export interface LibraryItem {
  id: string;
  source: Source;
  slug: string;
  name: string;
  description: string;
  platform: string;
  themes: string[];
  tags: string[];
  category: string;
  image: string | null;
  icon: string | null;
  video: string | null;
  evidence: "measured" | "interpreted";
  captured: string | null;
}
export interface ReferenceMedia {
  id: string;
  name: string;
  url: string;
  type: "image" | "video";
  tags: string[];
}
export interface ReferenceValue {
  name: string;
  value: string;
  role?: string;
  evidence?: string;
}
export interface LibraryDetail extends LibraryItem {
  sourceUrl: string | null;
  media: ReferenceMedia[];
  colors: ReferenceValue[];
  typography: ReferenceValue[];
  spacing: ReferenceValue[];
  radii: ReferenceValue[];
  descriptionLong: string;
  guidelines: string[];
  exports: Record<string, string>;
  related: LibraryItem[];
}
export interface LibraryQuery {
  query?: string;
  source?: Source;
  platform?: string;
  theme?: string;
  limit?: number;
  offset?: number;
}
