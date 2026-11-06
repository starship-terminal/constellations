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
  categoryIds?: string[];
  categories?: { id: string; label: string }[];
  image: string | null;
  imageFallback?: string | null;
  videoFallback?: string | null;
  iconFallback?: string | null;
  icon: string | null;
  video: string | null;
  evidence: "measured" | "interpreted";
  captured: string | null;
  productType?: string | null;
  designStyle?: string | null;
  industry?: string | null;
  sourceUrl?: string | null;
  fonts?: string[];
  previewFrames?: string[];
}
export interface ReferenceMedia {
  id: string;
  name: string;
  url: string;
  type: "image" | "video";
  tags: string[];
  kind?:
    | "screenshot"
    | "crop"
    | "icon"
    | "board"
    | "shot"
    | "poster"
    | "video"
    | "detail"
    | "detail_poster"
    | "favicon";
  path?: string;
  group?: string;
  thumbnail?: string | null;
  poster?: string | null;
  fallback?: string | null;
}
export interface PackageDocument {
  path: string;
  name: string;
  group: string;
  size: number;
  url: string;
}
export interface PackageDocumentContent extends PackageDocument {
  text: string;
  format: "markdown" | "json" | "html" | "text";
}
export interface MeasuredPackageDetail {
  screenshots: ReferenceMedia[];
  crops: ReferenceMedia[];
  icons: ReferenceMedia[];
  boards: ReferenceMedia[];
  iconTotal: number;
  documents: PackageDocument[];
  readme: string;
  readmePath: string;
  styleGuide: string | null;
  capture: Record<string, unknown> | null;
  widths: string[];
  access: string;
  notes: string;
  tokenTheme: string;
  swatches: Record<
    string,
    { role: string; token: string; value: string | null }[]
  >;
  fonts: { token: string; family: string; stack: string }[];
  typeStyles: {
    name: string;
    family?: string;
    size?: string;
    weight?: number;
    lineHeight?: string | number;
    letterSpacing?: string;
  }[];
  spacing: { name: string; value: string }[];
  radii: { name: string; value: string }[];
  shadows: { token: string; css: string }[];
  omitted: Record<string, string>;
  layoutGaps: Record<string, string>;
}
export interface InterpretedStyleDetail {
  designSystem: Record<string, unknown>;
  pageUrl: string | null;
  sourceUrl: string | null;
  productType: string | null;
  designStyle: string | null;
  industry: string | null;
  tags: string[];
  theme: string | null;
  similar: { slug: string | null; name: string | null; why: string | null }[];
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
  measured?: MeasuredPackageDetail;
  interpreted?: InterpretedStyleDetail;
}
export interface LibraryQuery {
  query?: string;
  source?: Source;
  platform?: string;
  theme?: string;
  category?: string;
  productType?: string;
  designStyle?: string;
  industry?: string;
  tag?: string;
  limit?: number;
  offset?: number;
}
