// The Model provider form's rules, kept apart from Settings.tsx so they can
// be tested without React. Run with `pnpm test`.

/** The form. `api_key` is only ever what the user has just typed: the server
    never sends a key back, so a saved key shows as the source badge instead. */
export interface ProviderForm {
  api: string;
  base_url: string;
  api_key: string;
  key_header: string;
  model: string;
  name: string;
  models_url: string;
}

export const EMPTY_FORM: ProviderForm = { api: "anthropic", base_url: "", api_key: "", key_header: "", model: "", name: "", models_url: "" };

/** `form` with one field changed. The form has no models URL field: the one
    a saved provider came with (the docs page's Gemini template sets one)
    belongs to that provider's endpoint, so changing the API or base URL
    drops it rather than sending it, unseen, with a different endpoint, where
    the server would refuse the mismatched origins. */
export function withField(form: ProviderForm, k: keyof ProviderForm, value: string): ProviderForm {
  const next = { ...form, [k]: value };
  if ((k === "api" || k === "base_url") && value !== form[k]) next.models_url = "";
  return next;
}

export const sameForm = (a: ProviderForm, b: ProviderForm): boolean =>
  (Object.keys(EMPTY_FORM) as (keyof ProviderForm)[]).every((k) => a[k] === b[k]);

/** The form after a successful save of `sent`: the key field empties (the
    server has the key and never returns it) only while the form still holds
    exactly what was sent. A reply that lands after the reader changed
    anything leaves their edits, the newer key included, as they are.
    `settled` says whether the form now matches the server (so later state
    replies may refill it). */
export function afterSave(current: ProviderForm, sent: ProviderForm): { form: ProviderForm; settled: boolean } {
  if (!sameForm(current, sent)) return { form: current, settled: false };
  return { form: { ...current, api_key: "" }, settled: true };
}

/** Numbers each request so only the newest one's reply is used: a reply
    from an older request that lands late is ignored. */
export function latestOnly(): { begin(): number; isLatest(n: number): boolean } {
  let last = 0;
  return {
    begin: () => ++last,
    isLatest: (n) => n === last,
  };
}
