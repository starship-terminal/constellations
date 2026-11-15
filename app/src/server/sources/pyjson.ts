// Python's json module is the reference for every tool result the library
// layer prints (server/library.py), and it keeps the difference between the
// integer 1 and the float 1.0 that JSON.parse erases. parseJson marks the
// floats whose JavaScript text would differ from Python's, and pyJsonStringify
// prints them the way json.dumps does, so a token file's `1.0` stays `1.0`.

/** A JSON float whose Python text differs from what JavaScript prints. */
export class PyFloat {
  constructor(readonly value: number) {}
  /** Plain JSON.stringify (the database, the UI) still sees the number. */
  toJSON(): number {
    return this.value;
  }
  /** Python's str(float), which is also how json.dumps writes it. */
  toString(): string {
    return pyFloatRepr(this.value);
  }
  valueOf(): number {
    return this.value;
  }
}

/** The number a value stands for when it is a JSON number or a PyFloat. */
export function numberOf(value: unknown): number | null {
  if (typeof value === "number") return value;
  return value instanceof PyFloat ? value.value : null;
}

/** Python's repr(float): shortest round trip, exponent below 1e-4 and from 1e16. */
export function pyFloatRepr(n: number): string {
  if (Number.isNaN(n)) return "NaN";
  if (!Number.isFinite(n)) return n < 0 ? "-Infinity" : "Infinity";
  if (n === 0) return Object.is(n, -0) ? "-0.0" : "0.0";
  const [mantissa, exponent] = Math.abs(n).toExponential().split("e");
  const digits = mantissa.replace(".", ""),
    exp = Number(exponent),
    sign = n < 0 ? "-" : "";
  if (exp < -4 || exp >= 16) {
    const lead = digits.length > 1 ? `${digits[0]}.${digits.slice(1)}` : digits;
    return `${sign}${lead}e${exp < 0 ? "-" : "+"}${String(Math.abs(exp)).padStart(2, "0")}`;
  }
  if (exp < 0) return `${sign}0.${"0".repeat(-exp - 1)}${digits}`;
  if (digits.length <= exp + 1)
    return `${sign}${digits.padEnd(exp + 1, "0")}.0`;
  return `${sign}${digits.slice(0, exp + 1)}.${digits.slice(exp + 1)}`;
}

/**
 * JSON.parse that keeps floats written as floats. Only a number whose
 * JavaScript text would differ from Python's is wrapped (1.0, 0.0, 1e-05,
 * 1e16); every other number stays a number. Needs the source text a reviver
 * gets from Node 22.
 */
export function parseJson(text: string): unknown {
  return JSON.parse(
    text,
    function (_key, value, context?: { source?: string }) {
      if (typeof value !== "number" || !context?.source) return value;
      if (!/[.eE]/.test(context.source)) return value;
      const size = Math.abs(value);
      if (
        Number.isInteger(value) ||
        (size !== 0 && (size < 1e-4 || size >= 1e16))
      )
        return new PyFloat(value);
      return value;
    },
  );
}

/** json.dumps(value, ensure_ascii=False, separators=(",", ":")). */
export function pyJsonStringify(value: unknown): string {
  return write(value) ?? "null";
}
function write(value: unknown): string | undefined {
  if (value instanceof PyFloat) return pyFloatRepr(value.value);
  if (value && typeof value === "object" && "toJSON" in value)
    value = (value as { toJSON(): unknown }).toJSON();
  if (Array.isArray(value))
    return `[${value.map((v) => write(v) ?? "null").join(",")}]`;
  if (value && typeof value === "object") {
    const parts: string[] = [];
    for (const [key, v] of Object.entries(value)) {
      const text = write(v);
      if (text !== undefined) parts.push(`${JSON.stringify(key)}:${text}`);
    }
    return `{${parts.join(",")}}`;
  }
  return JSON.stringify(value);
}
