// Token files arrive as DTCG ($value) or legacy Tokens Studio (value) trees.
// Resolution mirrors tools/catalog.py's Resolver, which `catalog.py export`
// and every generated export use, so the app shows the values the library
// publishes: an alias is a whole-string `{path}`, looked up in the token's own
// set, then an optional theme set, then `core`, then from the root. Text that
// merely contains braces is a literal, never substituted.
import { PyFloat, numberOf } from "./pyjson";
type Raw = Record<string, any>;
export type TokenLeaf = {
  name: string;
  value: unknown;
  type?: string;
  description?: string;
  extensions: Raw | null;
};

// A group may legitimately contain a token named "value". Legacy Tokens
// Studio tokens use an unprefixed value field, so distinguish their payload
// from a nested token tree before treating the enclosing object as a leaf.
function containsToken(node: unknown): boolean {
  if (!node || typeof node !== "object" || Array.isArray(node)) return false;
  if (node instanceof PyFloat) return false;
  const obj = node as Raw;
  if (Object.hasOwn(obj, "$value")) return true;
  if (
    Object.hasOwn(obj, "value") &&
    (typeof obj.type === "string" ||
      !obj.value ||
      typeof obj.value !== "object" ||
      obj.value instanceof PyFloat ||
      Array.isArray(obj.value))
  )
    return true;
  return Object.values(obj).some(containsToken);
}
export function tokenLeaves(
  node: unknown,
  prefix = "",
  out: TokenLeaf[] = [],
): TokenLeaf[] {
  if (!node || typeof node !== "object" || Array.isArray(node)) return out;
  const obj = node as Raw;
  const dtcg = Object.hasOwn(obj, "$value");
  const legacy =
    Object.hasOwn(obj, "value") &&
    (typeof obj.type === "string" || !containsToken(obj.value));
  if (dtcg || legacy)
    out.push({
      name: prefix,
      value: dtcg ? obj.$value : obj.value,
      type: obj.$type ?? obj.type,
      description: obj.$description ?? obj.description,
      extensions: obj.$extensions ?? null,
    });
  else
    for (const [key, value] of Object.entries(obj))
      if (!key.startsWith("$"))
        tokenLeaves(value, prefix ? `${prefix}.${key}` : key, out);
  return out;
}

/** Marks a value whose alias, anywhere inside it, points at nothing. */
export const UNRESOLVED: unique symbol = Symbol("unresolved");
export type Resolved = unknown | typeof UNRESOLVED;
export function hasUnresolved(value: Resolved): boolean {
  if (value === UNRESOLVED) return true;
  if (Array.isArray(value)) return value.some(hasUnresolved);
  if (value && typeof value === "object" && !(value instanceof PyFloat))
    return Object.values(value).some(hasUnresolved);
  return false;
}

export function tokenResolver(leaves: TokenLeaf[]) {
  const flat = new Map(leaves.map((leaf) => [leaf.name, leaf.value]));
  const final = (path: string, theme?: string, depth = 0): Resolved =>
    flat.has(path)
      ? deep(flat.get(path), path.split(".")[0], theme, depth)
      : UNRESOLVED;
  const deep = (
    value: unknown,
    set: string,
    theme: string | undefined,
    depth: number,
  ): Resolved => {
    if (depth > 12) return UNRESOLVED;
    if (typeof value === "string") {
      const match = /^\{([^}]+)\}$/.exec(value.trim());
      if (!match) return value;
      const ref = match[1];
      const sets = [set, ...(theme && theme !== set ? [theme] : []), "core"];
      const target = [...sets.map((s) => `${s}.${ref}`), ref].find((name) =>
        flat.has(name),
      );
      return target ? final(target, theme, depth + 1) : UNRESOLVED;
    }
    if (Array.isArray(value))
      return value.map((v) => deep(v, set, theme, depth));
    if (value && typeof value === "object" && !(value instanceof PyFloat))
      return Object.fromEntries(
        Object.entries(value).map(([key, v]) => [
          key,
          deep(v, set, theme, depth),
        ]),
      );
    return value;
  };
  return { final };
}

/** Python's round(): halves go to the even neighbour (76.5 -> 76), where
 * Math.round always goes up. catalog.py's _hex uses it. */
export function pyRound(value: number): number {
  const floor = Math.floor(value);
  const rest = value - floor;
  if (rest !== 0.5) return Math.round(value);
  return floor % 2 === 0 ? floor : floor + 1;
}
/** DTCG 2025 colour objects carry components, not a string. */
export function tokenHex(value: unknown): string | null {
  if (!value || typeof value !== "object" || Array.isArray(value)) return null;
  if (value instanceof PyFloat) return null;
  const color = value as Raw;
  if (!Array.isArray(color.components)) return null;
  if (typeof color.hex === "string" && color.hex) return color.hex;
  const hex = (n: number) =>
    pyRound(Number(n) * 255)
      .toString(16)
      .padStart(2, "0");
  const alpha = numberOf(color.alpha) ?? 1;
  return (
    "#" +
    color.components.slice(0, 3).map(hex).join("") +
    (alpha === 1 ? "" : hex(alpha))
  );
}
/** Replace every DTCG colour object inside a resolved value with its hex. */
export function colorsAsHex(value: unknown): unknown {
  const hex = tokenHex(value);
  if (hex) return hex;
  if (Array.isArray(value)) return value.map(colorsAsHex);
  if (value && typeof value === "object" && !(value instanceof PyFloat))
    return Object.fromEntries(
      Object.entries(value).map(([key, v]) => [key, colorsAsHex(v)]),
    );
  return value;
}
