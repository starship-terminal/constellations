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
